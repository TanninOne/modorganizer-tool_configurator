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

QMAKE_POST_LINK += echo %PATH% $$escape_expand(\\n)

QMAKE_POST_LINK += pyuic5 -x $$PWD/pyCfgDialog.ui -o $$PWD/pyCfgDialog.py $$escape_expand(\\n)
QMAKE_POST_LINK += pyrcc5 -o $$PWD/pyCfgResource_rc.py $$PWD/pyCfgResource.qrc $$escape_expand(\\n)
QMAKE_POST_LINK += copy $$WINPWD\\pyCfg.py $$quote($$DSTDIR)\\plugins $$escape_expand(\\n)
QMAKE_POST_LINK += xcopy /y /s /I $$WINPWD\\pyCfgDialog.py $$quote($$DSTDIR)\\plugins\\data\\ $$escape_expand(\\n)
QMAKE_POST_LINK += copy $$WINPWD\\pyCfgResource_rc.py $$quote($$DSTDIR)\\plugins\\data\\ $$escape_expand(\\n)
QMAKE_POST_LINK += copy $$WINPWD\\settings.json $$quote($$DSTDIR)\\plugins\\data $$escape_expand(\\n)

RESOURCES += \
    pyCfgResource.qrc
