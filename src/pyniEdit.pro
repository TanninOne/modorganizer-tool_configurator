OTHER_FILES += \
    pyCfg.py

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

QMAKE_POST_LINK += pyuic4 -x $$quote($$PWD/pyCfgDialog.ui) -o $$quote($$PWD/pyCfgDialog.py) $$escape_expand(\\n)
QMAKE_POST_LINK += pyrcc4 -o $$quote($$PWD/pyCfgResource_rc.py) $$quote($$PWD/pyCfgResource.qrc) $$escape_expand(\\n)
QMAKE_POST_LINK += copy $$quote($$WINPWD\\pyCfg.py) $$quote($$DSTDIR\\plugins) $$escape_expand(\\n)
QMAKE_POST_LINK += xcopy /y /s /I $$quote($$WINPWD\\pyCfgDialog.py) $$quote($$DSTDIR\\plugins\\data\\) $$escape_expand(\\n)
QMAKE_POST_LINK += copy $$quote($$WINPWD\\pyCfgResource_rc.py) $$quote($$DSTDIR\\plugins\\data\\) $$escape_expand(\\n)
QMAKE_POST_LINK += copy $$quote($$WINPWD\\settings.json) $$quote($$DSTDIR\\plugins\\data) $$escape_expand(\\n)

RESOURCES += \
    pyCfgResource.qrc
