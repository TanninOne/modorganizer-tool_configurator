#OTHER_FILES += \
#    pyCfg.py

TARGET = dummy

include(../plugin_template.pri)

FORMS += \
    pyCfgDialog.ui

SOURCES += \
    dummy.cpp

OTHER_FILES += \
    pyCfg.py\
    settings.json

TRANSLATIONS = $${TARGET}_en.ts \
               $${TARGET}_de.ts \
               $${TARGET}_es.ts \
               $${TARGET}_fr.ts \
               $${TARGET}_zh_TW.ts \
               $${TARGET}_zh_CN.ts \
               $${TARGET}_cs.ts \
               $${TARGET}_tr.ts \
               $${TARGET}_ko.ts \
               $${TARGET}_ru.ts

CONFIG(debug, debug|release) {
  DSTDIR = $$PWD/../../../outputd
} else {
  DSTDIR = $$PWD/../../../output
}
WINPWD = $$PWD

DSTDIR ~= s,/,$$QMAKE_DIR_SEP,g
WINPWD ~= s,/,$$QMAKE_DIR_SEP,g

# Warning. If you *build* pyqt, you get your files in one place. If you
# install it you get them in another...
greaterThan(QT_MAJOR_VERSION, 4) {
  QMAKE_POST_LINK += $$quote($${PYTHONPATH}\\pyuic5) $$quote($$PWD/pyCfgDialog.ui) -o $$quote($$PWD/pyCfgDialog.py) $$escape_expand(\\n)
  QMAKE_POST_LINK += $$quote($${PYTHONPATH}\\pyrcc5) -o $$quote($$PWD/pyCfgResource_rc.py) $$quote($$PWD/pyCfgResource.qrc) $$escape_expand(\\n)
} else {
  QMAKE_POST_LINK += $$quote($${PYTHONPATH}\\Lib\\site-packages\\PyQt4\\pyuic4) -x $$quote($$PWD\\pyCfgDialog.ui) -o $$quote($$PWD\\pyCfgDialog.py) $$escape_expand(\\n)
  QMAKE_POST_LINK += $$quote($${PYTHONPATH}\\Lib\\site-packages\\PyQt4\\pyrcc4) -o $$quote($$PWD/pyCfgResource_rc.py) $$quote($$PWD/pyCfgResource.qrc) $$escape_expand(\\n)
}
QMAKE_POST_LINK += copy $$quote($$WINPWD\\pyCfg.py) $$quote($$DSTDIR\\plugins) $$escape_expand(\\n)
QMAKE_POST_LINK += xcopy /y /s /I $$quote($$WINPWD\\pyCfgDialog.py) $$quote($$DSTDIR\\plugins\\data\\) $$escape_expand(\\n)
QMAKE_POST_LINK += copy $$quote($$WINPWD\\pyCfgResource_rc.py) $$quote($$DSTDIR\\plugins\\data\\) $$escape_expand(\\n)
QMAKE_POST_LINK += copy $$quote($$WINPWD\\settings.json) $$quote($$DSTDIR\\plugins\\data) $$escape_expand(\\n)

RESOURCES += \
    pyCfgResource.qrc

OTHER_FILES +=\
    SConscript
