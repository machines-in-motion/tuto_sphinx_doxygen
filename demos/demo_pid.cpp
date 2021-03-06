/**
 * @file demo_pid.cpp
 * @author Vincent Berenz
 * license License BSD-3-Clause
 * @copyright Copyright (c) 2019, New York University and Max Planck Gesellshaft.
 * @date 2019-05-22
 * 
 * @brief example of a simple demo suitable for continuous integration
 * @see https://git-amd.tuebingen.mpg.de/amd-clmc/ci_example/wikis/catkin:-how-to-implement-a-demo
 */

#include "tuto_sphinx_doxygen/pid.hpp" 

/**
 * @brief Creates a PID controller and use the API in a small demo.
 */
void run_demo_pid(){

  // PID controller with default gains values
  tuto_sphinx_doxygen::PID& controller = tuto_sphinx_doxygen::get_default_pid();
  
  // example of force computation
  double current_position=1;
  double current_velocity=1;
  double delta_time=0.01;
  double target_position=2;
  double force = controller.compute(current_position,
				    current_velocity,
				    target_position,
				    delta_time);
  std::cout<< "computed force: " << force << std::endl;

  // resetting integral of the controller
  // (useless here because we do not reuse it)
  controller.reset_integral();
  
}


/**
 * @brief Execute the run_demo() trhough a try/catch expression.
 * 
 * @return int 
 */
int main(){
  
  try {
    run_pid_demo();
  } catch(const std::exception& e){
    std::cout << "demo failed !\nerror message:\n" << e.what() << std::endl;
    return 1; // informs continuous integration that this demo did not run successfully
  }

  return 0; // informs continuous integration that this demo did run successfully

}

/**
 * @example demo_pid.cpp
 * This demos present the PID controller API.
 */