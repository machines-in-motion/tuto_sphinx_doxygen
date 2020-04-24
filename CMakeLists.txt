#
# @file CMakeLists.txt
# @author Maximilien Naveau (maximilien.naveau@gmail.com)
# @copyright Copyright (c) 2019, New York University and Max Planck Gesellschaft.
# @license License BSD-3 clause
# @date 2019-05-06
#
# @brief This file allow the build of this package using cmake
#

######################
# set up the project #
######################
cmake_minimum_required(VERSION 3.5.1)

project(sphinx_tuto)

###########################
# depend on catkin macros #
###########################
find_package(catkin REQUIRED)

#################
# Doxygen Macro #
#################

macro(build_doxygen_documentation)

    message(STATUS "building doxygen documentation for ${PROJECT_NAME}")

    # Find "doxygen"
    find_package(Doxygen)
    if (NOT DOXYGEN_FOUND)
        message(FATAL_ERROR
            "Doxygen is needed to build the documentation. "
            "Please install it correctly")
    endif()

    # set the destination folder to be devel/share/[project_name]/doc/
    set(doc_build_folder ${CATKIN_DEVEL_PREFIX}/${CATKIN_PACKAGE_SHARE_DESTINATION})
    set(doc_install_folder ${CMAKE_INSTALL_PREFIX}/${CATKIN_PACKAGE_SHARE_DESTINATION})

    

    # Create the doxyfile in function of the current project.
    # If the Doxyfile.in does not exists, the cmake step stops.
    configure_file(${PROJECT_SOURCE_DIR}/doc_config_files/Doxyfile.in
                    ${doc_build_folder}/Doxyfile
                    @ONLY IMMEDIATE)

    # the doxygen target is generated
    add_custom_target (${PROJECT_NAME}_doc ALL
        COMMAND ${DOXYGEN_EXECUTABLE} ${doc_build_folder}/Doxyfile
        SOURCES ${doc_build_folder}/Doxyfile
        WORKING_DIRECTORY ${doc_build_folder})

    # install the documentation
    install(DIRECTORY ${doc_build_folder}/doc DESTINATION ${doc_install_folder})
    install(FILES ${doc_build_folder}/${PROJECT_NAME}.tag DESTINATION ${doc_install_folder})

endmacro(build_doxygen_documentation)


##############################
# manage python file install #
##############################
catkin_python_setup()

##########################################
# export the package as a catkin package #
##########################################
catkin_package(
  CFG_EXTRAS
    ${MPI_CMAKE_MODULES_RESOURCES_DIR}/package_paths.cmake
    ${cmake_files}
)

##########################################
# Install the interesting resource files #
##########################################
configure_file(
    ${MPI_CMAKE_MODULES_RESOURCES_DIR}/_clang-format
    ${CATKIN_DEVEL_PREFIX}/${CATKIN_PACKAGE_PYTHON_DESTINATION}/_clang-format
    @ONLY IMMEDIATE
)

##########################
# building documentation #
##########################
build_doxygen_documentation()