#pragma once


#include "tuto_sphinx_doxygen/gains_configuration.hpp"
#include "yaml-cpp/yaml.h"


namespace tuto_sphinx_doxygen {

  
  /*! @brief Reading configuration from yaml file. */
  class File_configuration : public Gains_configuration {
    
  public:
    
    /**
     * Returns error encountered when reading configuration
     * @param yaml_file absolute path to configuration yaml file. 
     *        The file is expected to have parameters "kp", "kd" and "ki"
     * @see has_error()
     */
    File_configuration(std::string yaml_file);

    /** @copydoc Gains_configuration::get_kp() */
    double get_kp() const;

    /** @copydoc Gains_configuration::get_kd() */
    double get_kd() const;

    /** @copydoc Gains_configuration::get_ki() */
    double get_ki() const;

    /** @copydoc Gains_configuration::has_error() */
    bool has_error() const;

    /** @copydoc Gains_configuration::get_error() */
    std::string get_error() const;
    
  private:
    /** @brief  Proportinal gain. */
    double kp_;
    /** @brief  Derivative gain. */
    double kd_;
    /** @brief  Integral gain. */
    double ki_;
    /** @brief  Internal error message. */
    std::string error_message_;
    /** @brief  True if an error occured. */
    bool error_;
    
  };

}
