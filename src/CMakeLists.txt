CMAKE_MINIMUM_REQUIRED (VERSION 2.8)

SET(default_project_path "${CMAKE_SOURCE_DIR}/..")
GET_FILENAME_COMPONENT(${default_project_path} ${default_project_path} REALPATH)

SET(project_path "${default_project_path}" CACHE PATH "path to the other mo projects")

FIND_PATH(pyuic_path pyuic5.bat PATHS "${PYTHON_ROOT}")

EXECUTE_PROCESS(COMMAND ${PYTHON_ROOT}/pyuic5.bat -o ${CMAKE_CURRENT_BINARY_DIR}/pyCfgDialog.py ${CMAKE_CURRENT_SOURCE_DIR}/pyCfgDialog.ui WORKING_DIRECTORY ${PYTHON_ROOT})
EXECUTE_PROCESS(COMMAND ${PYTHON_ROOT}/pyrcc5.exe -o ${CMAKE_CURRENT_BINARY_DIR}/pyCfgResource_rc.py ${CMAKE_CURRENT_SOURCE_DIR}/pyCfgResource.qrc)


###############
## Installation

INSTALL(FILES
        ${CMAKE_CURRENT_SOURCE_DIR}/pyCfg.py
        DESTINATION bin/plugins)

INSTALL(FILES
        ${CMAKE_CURRENT_BINARY_DIR}/pyCfgDialog.py
        ${CMAKE_CURRENT_BINARY_DIR}/pyCfgResource_rc.py
        ${CMAKE_CURRENT_SOURCE_DIR}/settings.json
        DESTINATION bin/plugins/data)
