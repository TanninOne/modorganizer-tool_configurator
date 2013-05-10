# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Tannin/Documents/Projects/modorganizer-sf/source/plugins/pyniEdit/pyCfgDialog.ui'
#
# Created: Thu May 09 15:13:18 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PyCfgDialog(object):
    def setupUi(self, PyCfgDialog):
        PyCfgDialog.setObjectName(_fromUtf8("PyCfgDialog"))
        PyCfgDialog.resize(625, 435)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/pyCfg/pycfgicon")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PyCfgDialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(PyCfgDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.categorySelection = QtGui.QComboBox(PyCfgDialog)
        self.categorySelection.setObjectName(_fromUtf8("categorySelection"))
        self.horizontalLayout.addWidget(self.categorySelection)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.advancedBtn = QtGui.QPushButton(PyCfgDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.advancedBtn.sizePolicy().hasHeightForWidth())
        self.advancedBtn.setSizePolicy(sizePolicy)
        self.advancedBtn.setCheckable(True)
        self.advancedBtn.setObjectName(_fromUtf8("advancedBtn"))
        self.horizontalLayout.addWidget(self.advancedBtn)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.settingsTree = QtGui.QTreeWidget(PyCfgDialog)
        self.settingsTree.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.settingsTree.setRootIsDecorated(False)
        self.settingsTree.setColumnCount(2)
        self.settingsTree.setObjectName(_fromUtf8("settingsTree"))
        self.settingsTree.headerItem().setText(0, _fromUtf8("1"))
        self.settingsTree.headerItem().setText(1, _fromUtf8("2"))
        self.settingsTree.header().setVisible(False)
        self.settingsTree.header().setDefaultSectionSize(270)
        self.settingsTree.header().setMinimumSectionSize(20)
        self.settingsTree.header().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.settingsTree)

        self.retranslateUi(PyCfgDialog)
        QtCore.QMetaObject.connectSlotsByName(PyCfgDialog)

    def retranslateUi(self, PyCfgDialog):
        PyCfgDialog.setWindowTitle(_translate("PyCfgDialog", "Configurator", None))
        self.advancedBtn.setText(_translate("PyCfgDialog", "Basic", None))

import pyCfgResource_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PyCfgDialog = QtGui.QDialog()
    ui = Ui_PyCfgDialog()
    ui.setupUi(PyCfgDialog)
    PyCfgDialog.show()
    sys.exit(app.exec_())

