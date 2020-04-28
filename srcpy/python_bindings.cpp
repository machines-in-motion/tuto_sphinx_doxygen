#include <pybind11/pybind11.h>
#include "tuto_sphinx_doxygen/pid.hpp"


namespace tuto_sphinx_doxygen{

PYBIND11_MODULE(basic_pid,m) {

  pybind11::class_<PID>(m,"PID")
    .def(pybind11::init<>())
    .def("compute",&PID::compute)
    .def("reset_integral",&PID::reset_integral);

}

} // namespace tuto_sphinx_doxygen