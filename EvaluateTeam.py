import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from ErrorDialogBox import Ui_ErrorMessage
conn=sqlite3.connect("Fantasy_Cricket_League.db")
cur=conn.cursor()
color = '''
QComboBox:drop-down{
    border-image: url(DropDown.jpeg) 2;
    border:1px solid black; 
    width:32px
}
QComboBox{
    height: 30px;
    background-color:rgb(255,255,255);
}
QPushButton:hover{
    background: lightblue;
}
QPushButton:pressed{
    background: rgb(204,204,204);
}
'''
class Ui_Form(object):
   def setupUi(self, Form):
      Form.setObjectName("Form")
      Form.resize(611, 458)
      Form.setMinimumSize(QtCore.QSize(611, 458))
      Form.setMaximumSize(QtCore.QSize(611, 458))
      Form.setStyleSheet("background-color: rgb(204, 204, 204);")
      self.verticalLayout = QtWidgets.QVBoxLayout(Form)
      self.verticalLayout.setSpacing(10)
      self.verticalLayout.setObjectName("verticalLayout")
      self.horizontalLayout = QtWidgets.QHBoxLayout()
      self.horizontalLayout.setObjectName("horizontalLayout")
      spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
      self.horizontalLayout.addItem(spacerItem)
      self.label = QtWidgets.QLabel(Form)
      self.label.setStyleSheet("font: 75 10pt \"Comic Sans MS\";")
      self.label.setObjectName("label")
      self.horizontalLayout.addWidget(self.label)
      spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
      self.horizontalLayout.addItem(spacerItem1)
      self.verticalLayout.addLayout(self.horizontalLayout)
      self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
      self.horizontalLayout_2.setObjectName("horizontalLayout_2")
      spacerItem2 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
      self.horizontalLayout_2.addItem(spacerItem2)
      self.combo_TeamsList = QtWidgets.QComboBox(Form)
      self.combo_TeamsList.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";\n"
" border:1px solid black;\n"
"")
      self.combo_TeamsList.setPlaceholderText("Select Team")
      self.combo_TeamsList.setObjectName("combo_TeamsList")
      self.horizontalLayout_2.addWidget(self.combo_TeamsList)
      spacerItem3 = QtWidgets.QSpacerItem(75, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
      self.horizontalLayout_2.addItem(spacerItem3)
      self.combo_MatchesList = QtWidgets.QComboBox(Form)
      self.combo_MatchesList.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";\n"
" border:1px solid black;")
      self.combo_MatchesList.setPlaceholderText("Select Match")
      self.combo_MatchesList.setObjectName("combo_MatchesList")
      self.horizontalLayout_2.addWidget(self.combo_MatchesList)
      spacerItem4 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
      self.horizontalLayout_2.addItem(spacerItem4)
      self.verticalLayout.addLayout(self.horizontalLayout_2)
      self.line = QtWidgets.QFrame(Form)
      self.line.setMinimumSize(QtCore.QSize(0, 0))
      self.line.setStyleSheet("background-color: rgb(0, 0, 0);")
      self.line.setFrameShape(QtWidgets.QFrame.HLine)
      self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
      self.line.setObjectName("line")
      self.verticalLayout.addWidget(self.line)
      self.v2 = QtWidgets.QVBoxLayout()
      self.v2.setObjectName("v2")
      self.h2 = QtWidgets.QHBoxLayout()
      self.h2.setObjectName("h2")
      spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
      self.h2.addItem(spacerItem5)
      self.Label_Players = QtWidgets.QLabel(Form)
      font = QtGui.QFont()
      font.setFamily("Comic Sans MS")
      font.setPointSize(10)
      font.setBold(True)
      font.setWeight(75)
      self.Label_Players.setFont(font)
      self.Label_Players.setStyleSheet("")
      self.Label_Players.setObjectName("Label_Players")
      self.h2.addWidget(self.Label_Players)
      spacerItem6 = QtWidgets.QSpacerItem(330, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
      self.h2.addItem(spacerItem6)
      self.Label_Points = QtWidgets.QLabel(Form)
      font = QtGui.QFont()
      font.setFamily("Comic Sans MS")
      font.setPointSize(10)
      font.setBold(True)
      font.setWeight(75)
      self.Label_Points.setFont(font)
      self.Label_Points.setObjectName("Label_Points")
      self.h2.addWidget(self.Label_Points)
      self.Label_NOfPoints = QtWidgets.QLabel(Form)
      font = QtGui.QFont()
      font.setFamily("Comic Sans MS")
      font.setPointSize(10)
      font.setBold(True)
      font.setWeight(75)
      self.Label_NOfPoints.setFont(font)
      self.Label_NOfPoints.setStyleSheet("color: rgb(72,160,170);")
      self.Label_NOfPoints.setObjectName("Label_NOfPoints")
      self.h2.addWidget(self.Label_NOfPoints)
      spacerItem7 = QtWidgets.QSpacerItem(310, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
      self.h2.addItem(spacerItem7)
      self.v2.addLayout(self.h2)
      self.h4 = QtWidgets.QHBoxLayout()
      self.h4.setObjectName("h4")
      spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
      self.h4.addItem(spacerItem8)
      self.List_PlayersList = QtWidgets.QListWidget(Form)
      self.List_PlayersList.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";\n"
" border:1px solid black;\n"
"")
      self.List_PlayersList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
      self.List_PlayersList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
      self.List_PlayersList.setObjectName("List_PlayersList")
      self.h4.addWidget(self.List_PlayersList)
      spacerItem9 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
      self.h4.addItem(spacerItem9)
      self.List_PointsList = QtWidgets.QListWidget(Form)
      self.List_PointsList.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";\n"
"color: rgb(72,160,170);\n"
" border:1px solid black;")
      self.List_PointsList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
      self.List_PointsList.setObjectName("List_PointsList")
      self.h4.addWidget(self.List_PointsList)
      spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
      self.h4.addItem(spacerItem10)
      self.v2.addLayout(self.h4)
      self.verticalLayout.addLayout(self.v2)
      self.h7 = QtWidgets.QHBoxLayout()
      self.h7.setSpacing(6)
      self.h7.setObjectName("h7")
      spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
      self.h7.addItem(spacerItem11)
      self.button_calscore = QtWidgets.QPushButton(Form)
      self.button_calscore.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
      "border:1px solid black ;\n"
"padding:2px 20px 2px 20px;")
      self.button_calscore.setObjectName("button_calscore")
      self.h7.addWidget(self.button_calscore)
      spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
      self.h7.addItem(spacerItem12)
      self.verticalLayout.addLayout(self.h7)
      self.button_calscore.clicked.connect(self.scoreofplayers)
      self.totpoints=0
      self.teamslist()
      self.retranslateUi(Form)
      QtCore.QMetaObject.connectSlotsByName(Form)


   def retranslateUi(self, Form):
      _translate = QtCore.QCoreApplication.translate
      Form.setWindowTitle(_translate("Form", "Evaluate Team"))
      self.label.setText(_translate("Form", "Evaluate The Performance Of Your Fantasy Team"))
      self.Label_Players.setText(_translate("Form", "Players"))
      self.Label_Points.setText(_translate("Form", "Points "))
      self.Label_NOfPoints.setText(_translate("Form", "####"))
      self.button_calscore.setText(_translate("Form", "Calculate Score"))

#This Function is used to fetch the names of distinct team names and matches from database and add it to the respective ComboBoxes.
   def teamslist(self):
      cur.execute("SELECT DISTINCT Name FROM Teams;")
      teams=self.converttolist(cur.fetchall())
      for i in teams:
         self.combo_TeamsList.addItem(i)
      matches=cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'Match%';")
      matches=self.converttolist(cur.fetchall())
      for i in matches:
         self.combo_MatchesList.addItem(i)

#This function is used to convert list of tuples to list of strings.
   def converttolist(self,listoftuple):
      newlist=list(map(''.join,listoftuple))
      return newlist

#This function is used to display points of the players when user selects a valid team and a valid match.
   def scoreofplayers(self):
      team=self.combo_TeamsList.currentText()
      match=self.combo_MatchesList.currentText()
      if team=="Select Team" or match=="Select Match":
#Display Error message if no Team or no Match is selected.
         ErrorMessage = QtWidgets.QDialog()
         ui = Ui_ErrorMessage()
         ui.setupUi(ErrorMessage)
         ErrorMessage.show()
         ui.ErrorMessageLabel.setText("Please select a Valid Team and a Valid Match.")
         ErrorMessage.exec_()
      else:
         self.totpoints=0 
         d=list()
         self.List_PlayersList.clear()
         self.List_PointsList.clear()
         self.combo_MatchesList.setEnabled(False)
         self.combo_TeamsList.setEnabled(False)
         cur.execute("SELECT Players FROM Teams WHERE Name=?",(team,))
         teams=self.converttolist(cur.fetchall())
         for i in teams:
            columnnames=cur.execute("SELECT * FROM '"+match+"' WHERE Player=?",(i,))
#Add  white spaces at the begining  
            i='    '+i
            self.List_PlayersList.addItem(i)
            colname=[i[0] for i in columnnames.description]
            lst=cur.fetchall() 
            for i in lst:
               d.append(dict(zip(colname,i)))
         for i in d:
            p=self.pts(i)
#'  ' is used to add white spaces
            item='    '+str(p)
            self.List_PointsList.addItem(item)
         self.Label_NOfPoints.setText(str(self.totpoints))

#This function is used to calculate individual points of the player.
   def pts(self,d):
      points=0
      runscored=d.get("Scored")
      ballsfaced=d.get("Faced")
      fours=d.get("Fours")
      sixes=d.get("Sixes")
      bowl_overs=(d.get("Bowled"))/6
      runs_given=d.get("Given")
      wkts_taken=d.get("Wkts")
      caught_out=d.get("Catches")
      stump=d.get("Stumping")
      field_ro=d.get("Run-Out")
   
      points=int(runscored/2)
      if runscored>=50:
         points+=5
      if runscored>=100:
         points+=10
      try:
         sr=(runscored/ballsfaced)*100   
         if 80<=sr<100:
            points+=2
         elif sr>=100:
            points+=4
      except:
         pass 
      points=points+fours
      points=points+(2*sixes)
      points=points+(wkts_taken*10)                       
      if wkts_taken>=3:
         points+=5
      elif wkts_taken>=5:
         points+=10
      try:
         er=(runs_given/bowl_overs)
         if er<=2:
            points+=10
         elif 2<er<=3.5:
            points+=7
         elif 3.5<er<=4.5:
            points+=4
      except:
         pass
      points=points+(10*caught_out)
      points=points+(10*stump)
      points=points+(10*field_ro)
      self.totpoints=self.totpoints+int(points)
      return int(points)


if __name__ == "__main__":
   import sys
   app = QtWidgets.QApplication(sys.argv)
   Form = QtWidgets.QWidget()
   app.setStyleSheet(color)
   ui = Ui_Form()
   ui.setupUi(Form)
   Form.show()
   sys.exit(app.exec_())
