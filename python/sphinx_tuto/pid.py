#!/usr/bin/env python

from __future__ import print_function, division

""" Implementation of a simple PID controller """

import os

__copyright__ = "Copyright (c) 2019, New York University and Max Planck Gesellschaft."
__license__ = "BSD-3-Clause"

class DefaultConfiguration:
    """ PID configuration
    
    Configuration object with default values for kp, kd and ki
    can be used as input argument to create an instance of PID
    @see PID
    """
    
    #: proportional gain
    kp=1
    #: derivative gain
    kd=1
    #: integral gain
    ki=1

#: 
class RosConfiguration:
    """ ROS param configuration
    
    This contains the name of the ros parameter server keys for the PID gains.
    """
    #: key for reading kp gain
    ROSPARAM_KP = "kp"
    #: key for reading kd gain
    ROSPARAM_KD = "kd"
    #: key for reading ki gain
    ROSPARAM_KI = "ki"


class ConfigFileConfiguration:
    """ Path to default configuration file, relative to the pid package """
    #: relative path to the default configuration fole
    relative_path = os.path.join("..", "..", "config", "test_pid_gains.yaml")


class PID:
    """
    Simple 1D PID controller
    """

    def __init__(self,configuration):
        """
        :param configuration: Any object with "kp", "kd" and "ki" attributes (as float)
        """
        #: The PID gains.
        self._configuration = configuration
        #: The integral term.
        self._integral = 0

    def get_gains(self):
        """ Get the gains in a dictionary. keys: "kp", "kd" and "ki"
        :returns: Dict -- The PID gains.
        """
        return {"kp":self._configuration.kp,"kd":self._configuration.kp,"ki":self._configuration.ki}

    def reset_integral(self):
        """
        Reset integral part of the PID to 0.0
        """
        self._integral = 0.0

    def compute(self,position,velocity,position_target,delta_time):
        """ Compute the force related to the pid controller.
        This function is not stateless, as it performs integration.
        Call reset_integral() to reset the integral part.

        :param position: Float -- current position
        :param velocity: Float -- current velocity
        :param position_target: Float -- target position
        :param delta_time: Float -- time passed since last measurement.
                                    Used for integral computation
        :returns: Float -- computed force
        """
        position_error = position_target - position
        self._integral += delta_time * position_error
        return (position_error * self._configuration.kp - velocity * 
                self._configuration.kd + self._integral *
                self._configuration.ki)

    def __str__(self):
        """ Convert the object into a string """
        return "PID controller: kp:"+str(self._configuration.kp)+" kd:"+str(self._configuration.kd)+" ki:"+str(self._configuration.ki)


def _read_yaml_config_file(file_path):
    """ Convenience function for reading pid configuration from yaml file
    :param file_path: str -- Path relative to the execution path or global path.
    """

    # importing yaml and reading yaml file
    import yaml
    with open(file_path,"r") as f:
        config_dict = yaml.load(f)
    # checking the yaml file had the excepted entries
    expected_attributes = ["kp","kd","ki"]
    for attribute in expected_attributes:
        if not attribute in config_dict.keys():
            raise Exception("Configuration file "+str(file_path)+" is expected to have the "+str(attribute)+" entry")
    # creating a config object with correct attributes
    class config(object): pass
    c = config();
    for attribute in expected_attributes:
        try : 
            setattr(config,attribute,float(config_dict[attribute]))
        except Exception as e: 
            raise Exception("failed to convert "+attribute+"("+str(config_dict[attribute])+") to float (file: "+str(file_path)+")")
    # constructing and returning controller
    return PID(config)


def get_default_pid():
    """ Factory for default PID controller.
    See PID and see DefaultConfiguration.

    :returns: PID -- a new PID controller based on the DefaultConfiguration.
    """
    return PID(DefaultConfiguration)


def get_ros_params_pid(verbose=True):
    """ Get a PID controller paramterized through ROS params
    
    Assumes roscore is running and suitable parameters have been written in the
    server.
    :param verbose: Bool -- True: prints (stdout) the ros parameters it reads.
    :returns: PID based on gains read from the ROS parameter server. 
    """
    # importing ros and checking roscore is running
    import rospy
    if rospy.is_shutdown():
        raise Exception("failed to read ros parameters: ros is shutdown")
    # placeholder for the config
    class config:
        kp=None
        kd=None
        ki=None
    # reading the gains from ros parameter server
    parameters = [RosConfiguration.ROSPARAM_KP,RosConfiguration.ROSPARAM_KD,RosConfiguration.ROSPARAM_KI]
    gains = ["kp","kd","ki"]
    # if requested, printing the parameters it is about to read
    if verbose:
        print("reading ros parameters: "+", ".join(parameters))
    for parameter,gain in zip(parameters,gains):
        if not rospy.has_param(parameter):
            raise Exception("ros parameter server does not have the requested parameter: "+str(parameter)+" (current parameters: "+", ".join(rospy.get_param_names())+")")
        try:
            value = rospy.get_param(parameter)
            setattr(config,gain,value)
        except Exception as e:
            raise Exception("failed to read ros parameter "+str(parameter)+": "+str(e))
    # constructing and returning controller    
    return PID(config)

def get_config_file_pid(config_file_path=None,verbose=True):
    """

    :param config_file_path: Path to configuration file relative to the script
                             where this function is defined is specified in the
                             ConfigFileConfiguration object. If None, uses
                             default config file (in config folder), else used
                             specified path
    :param verbose: If True, prints path to config file used to standard output
    :returns: PID based on gains read from default configuration file 
    """
    if config_file_path is None:
        # getting abs path to this script
        abs_path_script = os.path.realpath(__file__)
        # getting name of this file
        script = os.path.basename(abs_path_script)
        # getting abs path of folder in which this script is
        abs_path =  abs_path_script[:-len(script)]
        # getting abs path to config file
        abs_path_config = os.path.abspath(abs_path+os.sep+ConfigFileConfiguration.relative_path)
    else : abs_path_config = config_file_path
    # checking file exists
    if not os.path.isfile(abs_path_config):
        raise Exception("failed to find configuration file: "+str(abs_path_config))
    # printing path to config file if asked
    if verbose:
        print("reading pid gains from: ",os.path.abspath(abs_path_config))
    # constructing and returning the controller
    return _read_yaml_config_file(abs_path_config)
