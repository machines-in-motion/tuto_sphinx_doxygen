"""shinx_tuto

This python pacakge is a small example on how to document a C++/python package
using shpinx/doxygen/breath/exhale all together.

"""


class PID(object):
    """ Dummy class that contains some documentation """
    
    #: Proportional gain.
    kp = 1.0

    def __init__(self):
        #: Derivative gain.
        self.kd = 0.0

    def compute(self, x, dx, x_ref, dx_ref):
        """ Computes the control.

        :param x: The current pose
        :type x: Float
        :param dx: The current speed
        :type dx: Float
        :param x_ref: The reference pose
        :type x_ref: Float
        :param dx_ref: The reference speed.
        :type dx_ref: Float
        :return: The control
        :rtype: Float
        """

        return self.kp * (x_ref - x) + self.kd * (dx_ref - dx)