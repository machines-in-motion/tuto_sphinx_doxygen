#pragma once

#include "tuto_sphinx_doxygen/gains_configuration.hpp"


#define DEFAULT_KP 1.0
#define DEFAULT_KD 1.0
#define DEFAULT_KI 1.0


namespace tuto_sphinx_doxygen {

  /** @brief Default configuration for the kp, kd, ki paramters.
   * 
   * This class initialize the PID gains as follow:
   *  - kp = DEFAULT_KP,
   *  - kd = DEFAULT_KD
   *  - ki = DEFAULT_KI
   */
  class Default_configuration : public Gains_configuration {
    
  public:
    /** @brief Here we use the default destructor. */
    ~Default_configuration(){}
    
    /**
     * @brief Always returns DEFAULT_KP.
     * 
     * @return double DEFAULT_KP
     */
    double get_kp() const;
    
    /**
     * @brief Always returns DEFAULT_KD.
     * 
     * @return double DEFAULT_KD
     */
    double get_kd() const;
    
    /**
     * @brief Always returns DEFAULT_KI.
     * 
     * @return double DEFAULT_KI
     */
    double get_ki() const;
    
    /**
     * @brief Always returns false.
     * 
     * @return true Never
     * @return false Always
     */
    bool has_error() const;
    
    /**
     * @brief Always returns "no error".
     * 
     * @return std::string "no error"
     */
    std::string get_error() const;
    
  };



};
