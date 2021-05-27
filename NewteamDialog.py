from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_NewTeamDialogBox(object):
    def setupUi(self, NewTeamDialogBox):
        NewTeamDialogBox.setObjectName("NewTeamDialogBox")
        NewTeamDialogBox.resize(367, 150)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        NewTeamDialogBox.setFont(font)
        NewTeamDialogBox.setStyleSheet("")
        NewTeamDialogBox.setInputMethodHints(QtCore.Qt.ImhNone)
        self.verticalLayout = QtWidgets.QVBoxLayout(NewTeamDialogBox)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Label_TeamName = QtWidgets.QLabel(NewTeamDialogBox)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_TeamName.setFont(font)
        self.Label_TeamName.setObjectName("Label_TeamName")
        self.horizontalLayout.addWidget(self.Label_TeamName)
        spacerItem = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Text_Input = QtWidgets.QLineEdit(NewTeamDialogBox)
        self.Text_Input.setEnabled(True)
        self.Text_Input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";\n"
"border:1px solid black;")
        self.Text_Input.setObjectName("Text_Input")
#The Team Name should be in the specified format as displayed.
        self.Text_Input.setPlaceholderText("Eg:CSK123")
        exp=QtCore.QRegExp()
        exp.setPattern("^[a-zA-Z].+[0-9].*")
        rgexp=QtGui.QRegExpValidator(exp)
        self.Text_Input.setValidator(rgexp)
        self.horizontalLayout.addWidget(self.Text_Input)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewTeamDialogBox)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.buttonBox.setFont(font)
        self.buttonBox.setStyleSheet("font: 10pt \"Comic Sans MS\";")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(NewTeamDialogBox)
        self.buttonBox.accepted.connect(NewTeamDialogBox.accept)
        self.buttonBox.rejected.connect(NewTeamDialogBox.reject)
        QtCore.QMetaObject.connectSlotsByName(NewTeamDialogBox)


    def retranslateUi(self, NewTeamDialogBox):
        _translate = QtCore.QCoreApplication.translate
        NewTeamDialogBox.setWindowTitle(_translate("NewTeamDialogBox", "New Team"))
        self.Label_TeamName.setText(_translate("NewTeamDialogBox", "Team  Name:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewTeamDialogBox = QtWidgets.QDialog()
    ui = Ui_NewTeamDialogBox()
    ui.setupUi(NewTeamDialogBox)
    NewTeamDialogBox.show()
    sys.exit(app.exec_())
