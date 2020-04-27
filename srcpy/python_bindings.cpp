#include <pybind11/pybind11.h>
#include "sphinx_tuto/pid.hpp"


namespace sphinx_tuto{

PYBIND11_MODULE(basic_pid,m) {

  pybind11::class_<PID>(m,"PID")
    .def(pybind11::init<>())
    .def("compute",&PID::compute)
    .def("reset_integral",&PID::reset_integral);

}

} // namespace sphinx_tuto