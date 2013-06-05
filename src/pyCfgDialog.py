# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Tannin/Documents/Projects/modorganizer-sf/source/plugins/pyniEdit/pyCfgDialog.ui'
#
# Created: Tue Jun 04 14:58:07 2013
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
        PyCfgDialog.resize(625, 503)
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
        self.advancedButton = QtGui.QPushButton(PyCfgDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.advancedButton.sizePolicy().hasHeightForWidth())
        self.advancedButton.setSizePolicy(sizePolicy)
        self.advancedButton.setCheckable(True)
        self.advancedButton.setObjectName(_fromUtf8("advancedButton"))
        self.horizontalLayout.addWidget(self.advancedButton)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.settingsTree = QtGui.QTreeWidget(PyCfgDialog)
        self.settingsTree.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.settingsTree.setRootIsDecorated(False)
        self.settingsTree.setColumnCount(2)
        self.settingsTree.setObjectName(_fromUtf8("settingsTree"))
        self.settingsTree.headerItem().setText(0, _fromUtf8("Key"))
        self.settingsTree.headerItem().setText(1, _fromUtf8("Value"))
        self.settingsTree.header().setVisible(True)
        self.settingsTree.header().setDefaultSectionSize(270)
        self.settingsTree.header().setMinimumSectionSize(20)
        self.settingsTree.header().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.settingsTree)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.saveButton = QtGui.QPushButton(PyCfgDialog)
        self.saveButton.setEnabled(False)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout_2.addWidget(self.saveButton)
        self.closeButton = QtGui.QPushButton(PyCfgDialog)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.horizontalLayout_2.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(PyCfgDialog)
        QtCore.QMetaObject.connectSlotsByName(PyCfgDialog)

    def retranslateUi(self, PyCfgDialog):
        PyCfgDialog.setWindowTitle(_translate("PyCfgDialog", "Configurator", None))
        self.advancedButton.setText(_translate("PyCfgDialog", "Basic", None))
        self.saveButton.setText(_translate("PyCfgDialog", "Save", None))
        self.closeButton.setText(_translate("PyCfgDialog", "Close", None))

import pyCfgResource_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PyCfgDialog = QtGui.QDialog()
    ui = Ui_PyCfgDialog()
    ui.setupUi(PyCfgDialog)
    PyCfgDialog.show()
    sys.exit(app.exec_())

