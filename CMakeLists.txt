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
    set(DOXYGEN_DOXYFILE_IN ${PROJECT_SOURCE_DIR}/cmake/Doxyfile.in)
    set(DOXYGEN_DOXYFILE ${PROJECT_BINARY_DIR}/docs/doxygen/Doxyfile)
    set(DOXYGEN_OUTPUT ${PROJECT_BINARY_DIR}/docs/doxygen)

    # Create the doxyfile in function of the current project.
    # If the Doxyfile.in does not exists, the cmake step stops.
    configure_file(${DOXYGEN_DOXYFILE_IN} ${DOXYGEN_DOXYFILE} @ONLY IMMEDIATE)

    # the doxygen target is generated
    add_custom_target (${PROJECT_NAME}_doc ALL
        COMMAND ${DOXYGEN_EXECUTABLE} ${DOXYGEN_DOXYFILE}
        SOURCES ${DOXYGEN_DOXYFILE} # if the file change rebuild
        WORKING_DIRECTORY ${DOXYGEN_OUTPUT})

endmacro(build_doxygen_documentation)

##########################
# building documentation #
##########################

# First we need to build the doxygen xml files.
build_doxygen_documentation()





   # # install the documentation
    # install(DIRECTORY ${doc_build_folder}/doc DESTINATION ${doc_install_folder})
    # install(FILES ${doc_build_folder}/${PROJECT_NAME}.tag DESTINATION ${doc_install_folder})
