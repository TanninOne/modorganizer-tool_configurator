import os
import sys
import json
import ConfigParser
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt,  pyqtWrapperType

if not "mobase" in sys.modules:
    import mock_mobase as mobase

class CaselessDict(dict):
    """Dictionary that enables case insensitive searching while preserving case sensitivity 
when keys are listed, ie, via keys() or items() methods. 
 
Works by storing a lowercase version of the key as the new key and stores the original key-value 
pair as the key's value (values become dictionaries)."""
 
    def __init__(self, initval={}):
        if isinstance(initval, dict):
            for key, value in initval.iteritems():
                self.__setitem__(key, value)
        elif isinstance(initval, list):
            for (key, value) in initval:
                self.__setitem__(key, value)
            
    def __contains__(self, key):
        return dict.__contains__(self, key.lower())
  
    def __getitem__(self, key):
        return dict.__getitem__(self, key.lower())['val'] 
  
    def __setitem__(self, key, value):
        return dict.__setitem__(self, key.lower(), {'key': key, 'val': value})
 
    def get(self, key, default=None):
        try:
            v = dict.__getitem__(self, key.lower())
        except KeyError:
            return default
        else:
            return v['val']
 
    def has_key(self,key):
        if self.get(key):
            return True
        else:
            return False    
 
    def items(self):
        return [(v['key'], v['val']) for v in dict.itervalues(self)]
    
    def keys(self):
        return [v['key'] for v in dict.itervalues(self)]
    
    def values(self):
        return [v['val'] for v in dict.itervalues(self)]
    
    def iteritems(self):
        for v in dict.itervalues(self):
            yield v['key'], v['val']
        
    def iterkeys(self):
        for v in dict.itervalues(self):
            yield v['key']
        
    def itervalues(self):
        for v in dict.itervalues(self):
            yield v['val']


class MainWindow(QtGui.QDialog):
    def __init__(self,  settings,  parent = None):
        super(MainWindow,  self).__init__(parent)
        self.__settings = settings

        from pyCfgDialog import Ui_PyCfgDialog

        self.__ui = Ui_PyCfgDialog()
        self.__ui.setupUi(self)

        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        self.__updateCategories()
        self.__ui.categorySelection.currentIndexChanged[int].connect(self.__sectionChanged)
        self.__ui.advancedBtn.clicked.connect(self.__advancedClicked)
        self.__ui.settingsTree.header().setResizeMode(1,  QtGui.QHeaderView.Stretch)
        self.__lastSelectedCategory = ""

    def __advancedClicked(self):
        self.sender().setText("Advanced" if self.sender().isChecked() else "Basic")
        self.__updateCategories()
        newIdx = self.__ui.categorySelection.findText(self.__lastSelectedCategory)
        if newIdx != -1:
            self.__ui.categorySelection.setCurrentIndex(newIdx)

    def __updateCategories(self):
        self.__ui.categorySelection.clear()
        self.__ui.categorySelection.addItem("")
        advanced = self.__ui.advancedBtn.isChecked()
        for cat in self.__settings.keys():
            display = advanced
            if not display:
                for setting in self.__settings[cat].values():
                    if "basic" in setting.get("flags",  []):
                        display = True
                        continue

            if display:
                self.__ui.categorySelection.addItem(cat)

    def __rgbClicked(self):
        col = QtGui.QColorDialog.getColor(self.sender().palette().color(QtGui.QPalette.ButtonText))
        palette = self.sender().palette()
        palette.setColor(QtGui.QPalette.ButtonText,  col)
        self.sender().setPalette(palette)

    def __boolClicked(self):
        if self.sender().isChecked() :
            self.sender().setText("true")
            self.sender().setIcon(QtGui.QIcon(":/pyCfg/true"))
        else:
            self.sender().setText("false")
            self.sender().setIcon(QtGui.QIcon(":/pyCfg/false"))

    def __genSelectionEntry(self,  key,  setting):
        newItem = QtGui.QTreeWidgetItem(self.__ui.settingsTree,  [ key ] )
        selectionWidget = QtGui.QComboBox(self.__ui.settingsTree)
        for val in setting["values"]:
            selectionWidget.addItem(str(val),  val)
            if setting["value"] == val:
                selectionWidget.setCurrentIndex(selectionWidget.count() - 1)

        self.__ui.settingsTree.setItemWidget(newItem,  1,  selectionWidget)
        return newItem

    def __genBooleanEntry(self,  key,  setting):
        newItem = QtGui.QTreeWidgetItem(self.__ui.settingsTree,  [ key ] )
        enableBtn = QtGui.QPushButton("true" if setting["value"] else "false",  self.__ui.settingsTree)
        enableBtn.setCheckable(True)
        enableBtn.setChecked(setting["value"])
        enableBtn.setIcon(QtGui.QIcon(":/pyCfg/true") if setting["value"] else QtGui.QIcon(":/pyCfg/false"))
        enableBtn.clicked.connect(self.__boolClicked)
        self.__ui.settingsTree.setItemWidget(newItem,  1,   enableBtn)
        return newItem

    def __genDoubleEditEntry(self,  key,  setting):
        newItem = QtGui.QTreeWidgetItem(self.__ui.settingsTree,  [ key,  "" ] )
        editWidget = QtGui.QDoubleSpinBox(self.__ui.settingsTree)
        if "range" in setting:
            editWidget.setRange(setting["range"]["lower"],  setting["range"]["upper"])
        else:
            editWidget.setRange(-sys.float_info.max,  sys.float_info.max)
        editWidget.setSingleStep(setting.get("step",  1.0))
        editWidget.setValue(setting["value"])
        self.__ui.settingsTree.setItemWidget(newItem,  1,   editWidget)
        return newItem

    def __genSlider(self,  range,  step,  value):
            newWidget = QtGui.QWidget(self.__ui.settingsTree)
            layout = QtGui.QHBoxLayout(newWidget)
            layout.setStretch(2,  1)
            slider = QtGui.QSlider(Qt.Horizontal,  newWidget)
            spin = QtGui.QSpinBox(self.__ui.settingsTree)
            slider.setRange(range["lower"],  range["upper"])
            spin.setRange(range["lower"],  range["upper"])
            slider.setSingleStep(step)
            spin.setSingleStep(step)
            slider.setValue(value)
            spin.setValue(value)
            layout.addWidget(slider)
            layout.addWidget(spin)
            slider.sliderMoved.connect(spin.setValue)
            slider.valueChanged.connect(spin.setValue)
            spin.valueChanged.connect(slider.setValue)
            newWidget.setLayout(layout)
            return newWidget

    def __genIntEditEntry(self,  key,  setting):
        newItem = QtGui.QTreeWidgetItem(self.__ui.settingsTree,  [ key,  "" ] )
        if "range" in setting:
            newWidget = self.__genSlider(setting["range"],  setting.get("step",  1),  setting["value"])
        else:
            newWidget = QtGui.QSpinBox(self.__ui.settingsTree)
            newWidget.setRange(-sys.maxint,  sys.maxint)
            newWidget.setSingleStep(setting.get("step",  1))
            newWidget.setValue(setting["value"])
        self.__ui.settingsTree.setItemWidget(newItem,  1,   newWidget)
        return newItem

    def __genUnsignedEditEntry(self,  key,  setting):
        newItem = QtGui.QTreeWidgetItem(self.__ui.settingsTree,  [ key,  "" ] )
        if "range" in setting:
            newWidget = self.__genSlider(setting["range"],  setting.get("step",  1),  setting["value"])
        else:
            newWidget = QtGui.QSpinBox(self.__ui.settingsTree)
            newWidget.setRange(0,   sys.maxint)
            newWidget.setSingleStep(setting.get("step",  1))
            newWidget.setValue(setting["value"])
        self.__ui.settingsTree.setItemWidget(newItem,  1,   newWidget)
        return newItem

    def __genEditEntry(self,  key,  setting):
        newItem = QtGui.QTreeWidgetItem(self.__ui.settingsTree,  [ key ] )
        editBox = QtGui.QLineEdit(str(setting["value"]),  self.__ui.settingsTree)
        self.__ui.settingsTree.setItemWidget(newItem,  1,   editBox)

        return newItem

    def __genColorEntry(self,  key,  setting):
        newItem = QtGui.QTreeWidgetItem(self.__ui.settingsTree,  [ key ] )
        colorBtn = QtGui.QPushButton("Color",  self.__ui.settingsTree)
        if setting["value"] == "":
            rgb = [ 0,  0,  0 ]
        else:
            rgb = [ int(col) for col in str(setting["value"]).split(",") ]
        color = QtGui.QColor(rgb[0],  rgb[1],  rgb[2])
        palette = colorBtn.palette()
        palette.setColor(QtGui.QPalette.ButtonText,  color)
        colorBtn.setPalette(palette)
        font = colorBtn.font()
        font.setBold(True)
        colorBtn.setFont(font)
        colorBtn.clicked.connect(self.__rgbClicked)
        self.__ui.settingsTree.setItemWidget(newItem,  1,   colorBtn)
        return newItem

    def __addSetting(self,  key,  setting):
        if "values" in setting:
            return self.__genSelectionEntry(key,  setting)
        else:
            keyType = key[0]
            if keyType == 'b':
                return self.__genBooleanEntry(key,  setting)
            elif keyType == 'f':
                return self.__genDoubleEditEntry(key,  setting)
            elif keyType == 'i':
                return self.__genIntEditEntry(key,  setting)
            elif keyType == 'u':
                return self.__genUnsignedEditEntry(key,  setting)
            elif keyType == 'r':
                return self.__genColorEntry(key,  setting)
            else:
                return self.__genEditEntry(key,  setting)

    def __updateTree(self):
        self.__ui.settingsTree.clear()
        if not str(self.__ui.categorySelection.currentText()) in self.__settings:
            return
        category = str(self.__ui.categorySelection.currentText())
        self.__lastSelectedCategory = category
        for settingKey in sorted(self.__settings[category].keys(),  key=lambda setKey: setKey[1:]):
            setting = self.__settings[category][settingKey]
            if not self.__ui.advancedBtn.isChecked() and not "basic" in setting.get("flags",  []):
                continue
            newItem = self.__addSetting(settingKey,  setting)
            if "description" in setting:
                newItem.setToolTip(0,  setting["description"])
            newItem.setToolTip(1,  "Default: " + str(setting["default"]))
            self.__ui.settingsTree.addTopLevelItem(newItem)

        self.__ui.settingsTree.resizeColumnToContents(0)

    def __sectionChanged(self,  sectionIdx):
        self.__updateTree()


class IniEdit(mobase.IPluginTool):
    def init(self, organizer):
        sys.path.append(organizer.pluginDataPath())
        import pyCfgResource_rc

        self.__organizer = organizer
        try:
                f = open(organizer.pluginDataPath() + "/settings.json", "r")
        except IOError:
                return False
        self.__settings = json.loads(f.read())
        f.close()
        return True

    def name(self):
        return "Configurator"

    def author(self):
        return "Tannin"

    def description(self):
        return "Plugin to allow easier customization of game settings"

    def version(self):
        return mobase.VersionInfo(1, 0, 0, mobase.ReleaseType.beta)

    def isActive(self):
        return True

    def settings(self):
        return []

    def displayName(self):
        return "Configurator"

    def tooltip(self):
        return "Modify game Configuration"

    def icon(self):
        return QtGui.QIcon(":/pyCfg/pycfgicon")

    def setParentWidget(self, widget):
        self.__parentWidget = widget

    def __iniFiles(self):
        gameType = self.__organizer.gameInfo().type()
        if str(gameType) == "oblivion":
            return [ "oblivion.ini",  "oblivionprefs.ini" ]
        elif str(gameType) == "fallout3" or gameType == "falloutnv":
            return [ "fallout.ini",  "falloutprefs.ini" ]
        elif str(gameType) == "skyrim":
            return [ "skyrim.ini",  "skyrimprefs.ini" ]
        else:
            return []

    def __filteredSettings(self):
        newSettings = CaselessDict()
        gameName = str(self.__organizer.gameInfo().type())
        for sectionKey in self.__settings.keys():
            section = self.__settings[sectionKey]
            filteredSection = CaselessDict()
            for key,  setting in section.iteritems():
                if "hidden" in setting.get("flags",  []):
                    # set to hidden
                    continue
                if "games" in setting and not gameName in setting["games"]:
                    # not for this game
                    continue
                setting["value"] = setting["default"]
                filteredSection[str(key)] = setting
            if len(filteredSection) > 0:
                newSettings[sectionKey] = filteredSection
        return newSettings

    def updateSettings(self,  settings,  file):
        parser = ConfigParser.SafeConfigParser()
        parser.optionxform = str
        parser.read(file)
        for section in parser.sections():
            if not section in settings:
                settings[section] = CaselessDict()
            for setting in parser.items(section):
                newData = settings[section].get(setting[0],  {})
                value = setting[1]
                if setting[0][0] == 'b':
                    value = bool(value)
                elif setting[0][0] == 'i' or setting[0][0] == 'u':
                    value = int(value)
                elif setting[0][0] == 'f':
                    value = float(value)
                newData["value"] = value
                if not "default" in newData:
                    newData["default"] = value
                settings[section][str(setting[0])] = newData

    def display(self):
        settings = self.__filteredSettings()
        for iniFile in self.__iniFiles():
            self.updateSettings(settings,  self.__organizer.profilePath() + "/" + iniFile)
        win = MainWindow(settings)
        win.exec_()

def createPlugin():
        return IniEdit()
