OTHER_FILES += \
    pyCfg.py

include(../plugin_template.pri)

FORMS += \
    pyCfgDialog.ui

SOURCES += \
    dummy.cpp


CONFIG(debug, debug|release) {
  DSTDIR = $$PWD/../../../outputd
} else {
  DSTDIR = $$PWD/../../../output
}
WINPWD = $$PWD

DSTDIR ~= s,/,$$QMAKE_DIR_SEP,g
WINPWD ~= s,/,$$QMAKE_DIR_SEP,g

greaterThan(QT_MAJOR_VERSION, 4) {
  QMAKE_POST_LINK += $${PYTHONPATH}/pyuic5 -x $$quote($$PWD/pyCfgDialog.ui) -o $$quote($$PWD/pyCfgDialog.py) $$escape_expand(\\n)
  QMAKE_POST_LINK += $${PYTHONPATH}/pyrcc5 -o $$quote($$PWD/pyCfgResource_rc.py) $$quote($$PWD/pyCfgResource.qrc) $$escape_expand(\\n)
} else {
  QMAKE_POST_LINK += $${PYTHONPATH}/pyuic4 -x $$quote($$PWD/pyCfgDialog.ui) -o $$quote($$PWD/pyCfgDialog.py) $$escape_expand(\\n)
  QMAKE_POST_LINK += $${PYTHONPATH}/pyrcc4 -o $$quote($$PWD/pyCfgResource_rc.py) $$quote($$PWD/pyCfgResource.qrc) $$escape_expand(\\n)
}
QMAKE_POST_LINK += copy $$quote($$WINPWD\\pyCfg.py) $$quote($$DSTDIR\\plugins) $$escape_expand(\\n)
QMAKE_POST_LINK += xcopy /y /s /I $$quote($$WINPWD\\pyCfgDialog.py) $$quote($$DSTDIR\\plugins\\data\\) $$escape_expand(\\n)
QMAKE_POST_LINK += copy $$quote($$WINPWD\\pyCfgResource_rc.py) $$quote($$DSTDIR\\plugins\\data\\) $$escape_expand(\\n)
QMAKE_POST_LINK += copy $$quote($$WINPWD\\settings.json) $$quote($$DSTDIR\\plugins\\data) $$escape_expand(\\n)

RESOURCES += \
    pyCfgResource.qrc
