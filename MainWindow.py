import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from NewteamDialog import Ui_NewTeamDialogBox
from EvaluateTeam import Ui_Form
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
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 464)
        self.seticon(MainWindow)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(False)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.v1 = QtWidgets.QWidget(self.centralwidget)
        self.v1.setStyleSheet("background-color: rgb(240, 240, 240);\n"
        "border:1px solid rgb(170,170,170);")
        self.v1.setObjectName("v1")
        self.vl1 = QtWidgets.QVBoxLayout(self.v1)
        self.vl1.setObjectName("vl1")
        self.Label_YourSelections = QtWidgets.QLabel(self.v1)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.Label_YourSelections.setFont(font)
        self.Label_YourSelections.setStyleSheet("border:rgb(240, 240, 240);")
        self.Label_YourSelections.setObjectName("Label_YourSelections")
        self.vl1.addWidget(self.Label_YourSelections)
        self.h1 = QtWidgets.QHBoxLayout()
        self.h1.setObjectName("h1")
        self.Label_Batsman = QtWidgets.QLabel(self.v1)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_Batsman.setFont(font)
        self.Label_Batsman.setStyleSheet("border:rgb(240, 240, 240);")
        self.Label_Batsman.setObjectName("Label_Batsman")
        self.h1.addWidget(self.Label_Batsman)
        self.Label_BatCount = QtWidgets.QLabel(self.v1)
        self.Label_BatCount.setStyleSheet("color: rgb(72,160,170);\n"
"border:rgb(240, 240, 240);\n"
"font: 10pt \"Comic Sans MS\";\n"
"")
        self.Label_BatCount.setObjectName("Label_BatCount")
        self.h1.addWidget(self.Label_BatCount)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h1.addItem(spacerItem)
        self.Label_Bowlers = QtWidgets.QLabel(self.v1)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_Bowlers.setFont(font)
        self.Label_Bowlers.setStyleSheet("border:rgb(240, 240, 240);")
        self.Label_Bowlers.setObjectName("Label_Bowlers")
        self.h1.addWidget(self.Label_Bowlers)
        self.Label_BowlCount = QtWidgets.QLabel(self.v1)
        self.Label_BowlCount.setStyleSheet("color: rgb(72,160,170);\n"
"border:rgb(240, 240, 240);\n"
"font: 10pt \"Comic Sans MS\";\n"
"")
        self.Label_BowlCount.setObjectName("Label_BowlCount")
        self.h1.addWidget(self.Label_BowlCount)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h1.addItem(spacerItem1)
        self.Label_AR = QtWidgets.QLabel(self.v1)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_AR.setFont(font)
        self.Label_AR.setStyleSheet("border:rgb(240, 240, 240);")
        self.Label_AR.setObjectName("Label_AR")
        self.h1.addWidget(self.Label_AR)
        self.Label_ARCount = QtWidgets.QLabel(self.v1)
        self.Label_ARCount.setStyleSheet("color: rgb(72,160,170);\n"
"border:rgb(240, 240, 240);\n"
"font: 10pt \"Comic Sans MS\";\n"
"")
        self.Label_ARCount.setObjectName("Label_ARCount")
        self.h1.addWidget(self.Label_ARCount)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h1.addItem(spacerItem2)
        self.Label_WK = QtWidgets.QLabel(self.v1)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_WK.setFont(font)
        self.Label_WK.setStyleSheet("border:rgb(240, 240, 240);")
        self.Label_WK.setObjectName("Label_WK")
        self.h1.addWidget(self.Label_WK)
        self.Label_WKCount = QtWidgets.QLabel(self.v1)
        self.Label_WKCount.setStyleSheet("color: rgb(72,160,170);\n"
"border:rgb(240, 240, 240);\n"
"font: 10pt \"Comic Sans MS\";\n"
"")
        self.Label_WKCount.setObjectName("Label_WKCount")
        self.h1.addWidget(self.Label_WKCount)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h1.addItem(spacerItem3)
        self.vl1.addLayout(self.h1)
        self.verticalLayout.addWidget(self.v1)
        self.v2 = QtWidgets.QVBoxLayout()
        self.v2.setObjectName("v2")
        self.h2 = QtWidgets.QHBoxLayout()
        self.h2.setObjectName("h2")
        spacerItem4 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.h2.addItem(spacerItem4)
        self.Label_PointsAvailable = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_PointsAvailable.setFont(font)
        self.Label_PointsAvailable.setObjectName("Label_PointsAvailable")
        self.h2.addWidget(self.Label_PointsAvailable)
        self.Label_AvailPtsCount = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Label_AvailPtsCount.setFont(font)
        self.Label_AvailPtsCount.setStyleSheet("color: rgb(72,160,170);\n"
"")
        self.Label_AvailPtsCount.setObjectName("Label_AvailPtsCount")
        self.h2.addWidget(self.Label_AvailPtsCount)
        spacerItem5 = QtWidgets.QSpacerItem(185, 10, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.h2.addItem(spacerItem5)
        self.Label_PointsUsed = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_PointsUsed.setFont(font)
        self.Label_PointsUsed.setObjectName("Label_PointsUsed")
        self.h2.addWidget(self.Label_PointsUsed)
        self.Label_UsedPtsCount = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Label_UsedPtsCount.setFont(font)
        self.Label_UsedPtsCount.setStyleSheet("color: rgb(72,160,170);\n"
"")
        self.Label_UsedPtsCount.setObjectName("Label_UsedPtsCount")
        self.h2.addWidget(self.Label_UsedPtsCount)
        spacerItem6 = QtWidgets.QSpacerItem(170, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.h2.addItem(spacerItem6)
        self.v2.addLayout(self.h2)
        self.h3 = QtWidgets.QHBoxLayout()
        self.h3.setObjectName("h3")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.h3.addItem(spacerItem7)
        self.List_AvailablePlayers = QtWidgets.QListWidget(self.centralwidget)
        self.List_AvailablePlayers.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"border:1px solid black;")
        self.List_AvailablePlayers.setObjectName("List_AvailablePlayers")

#Create a HorizontalLayout and add 4 RadioButtons to it.

        self.h4=QtWidgets.QHBoxLayout()
        self.batbutton=QtWidgets.QRadioButton()
        self.bowlbutton=QtWidgets.QRadioButton()
        self.arbutton=QtWidgets.QRadioButton()
        self.wkbutton=QtWidgets.QRadioButton()
        self.batbutton.setText("BAT")
        self.bowlbutton.setText("BOW")
        self.arbutton.setText("AR")
        self.wkbutton.setText("WK")
        self.h4.addWidget(self.batbutton)
        self.h4.addWidget(self.bowlbutton)
        self.h4.addWidget(self.arbutton)
        self.h4.addWidget(self.wkbutton)

#Convert the Layout to a ListItem and add it to a QListWidget. 

        wid=QtWidgets.QWidget()
        wid.setLayout(self.h4)
        wid.setStyleSheet("border:rgb(255,255,255)")
        item=QtWidgets.QListWidgetItem()
        self.List_AvailablePlayers.addItem(item)
        item.setSizeHint(wid.minimumSizeHint())
        self.List_AvailablePlayers.setItemWidget(item,wid)
        self.List_AvailablePlayers.setCurrentRow(2)
        self.h3.addWidget(self.List_AvailablePlayers)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.h3.addItem(spacerItem8)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.h3.addWidget(self.label)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.h3.addItem(spacerItem9)
        self.List_TeamPlayers = QtWidgets.QListWidget(self.centralwidget)
        self.List_TeamPlayers.setObjectName("List_TeamPlayers")

#Create another HorizontalLayout and add two lables to it.

        self.h5=QtWidgets.QHBoxLayout()
        self.NameOfNewTeam=QtWidgets.QLabel()
        self.NewTeam=QtWidgets.QLabel()
        self.NameOfNewTeam.setText("     "+"Team Name")
        self.h5.addWidget(self.NameOfNewTeam)       
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Comic Sans MS")
        font.setWeight(75)
        font.setBold(True)
        self.NameOfNewTeam.setFont(font)
        self.NewTeam.setFont(font)
        self.NewTeam.setText(" Displayed Here ") 
        self.NewTeam.setStyleSheet("color: rgb(40,160,170);") 
        self.h5.addWidget(self.NewTeam)

#Convert the Layout to a Widget and add it to QListWidget.

        wid2=QtWidgets.QWidget()
        wid2.setLayout(self.h5)
        item2=QtWidgets.QListWidgetItem()
        self.List_TeamPlayers.addItem(item2)
        item2.setSizeHint(wid2.minimumSizeHint())
        self.List_TeamPlayers.setItemWidget(item2,wid2)
        self.List_TeamPlayers.setCurrentRow(2) 
        self.h3.addWidget(self.List_TeamPlayers)
        self.List_TeamPlayers.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"border:1px solid black;")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.h3.addItem(spacerItem10)
        self.v2.addLayout(self.h3)
        self.verticalLayout.addLayout(self.v2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 27))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("QMenuBar::item {         \n"
"    padding:4px 25px 2px 25px;\n"
"    background-color:rgb(204,204,204); \n"
"    border:1px solid black;\n"
"}")
        self.menubar.setObjectName("menubar")
        self.Menu_ManageTeams = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Menu_ManageTeams.setFont(font)
        self.Menu_ManageTeams.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Menu_ManageTeams.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"background-color: rgb(204, 204, 204);\n"
"border:1px solid black;\n"
"color:rgb(0,0,0);\n"
"selection-background-color: rgb(0,150, 255);")
        self.Menu_ManageTeams.setObjectName("Menu_ManageTeams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Menu_OPENTeam = QtWidgets.QMenu(self.Menu_ManageTeams)
        self.Menu_OPENTeam.setObjectName("Menu_OPENTeam")
        self.Menu_EVALUATETeam = QtWidgets.QAction(MainWindow)
        self.Menu_EVALUATETeam.setObjectName("Menu_EVALUATETeam")
        self.Menu_NEWTeam = QtWidgets.QAction(MainWindow)
        self.Menu_NEWTeam.setObjectName("Menu_NEWTeam")
        self.Menu_SAVETeam = QtWidgets.QAction(MainWindow)
        self.Menu_SAVETeam.setObjectName("Menu_SAVETeam")
        self.Menu_ManageTeams.addAction(self.Menu_NEWTeam)
        self.Menu_ManageTeams.addAction(self.Menu_OPENTeam.menuAction())
        self.Menu_ManageTeams.addAction(self.Menu_SAVETeam)
        self.Menu_ManageTeams.addAction(self.Menu_EVALUATETeam)
        self.menubar.addAction(self.Menu_ManageTeams.menuAction())
        self.Menu_NEWTeam.triggered.connect(self.NewTeamOptionclicked)
        self.Menu_SAVETeam.triggered.connect(self.SAVETeamOptionclicked)
        self.Menu_EVALUATETeam.triggered.connect(self.EvaluateTeamOptionClicked)
        self.listingplayers()
        self.totplayers=0
        self.tname=None
        self.batbutton.clicked.connect(self.DisplayBatsman)
        self.bowlbutton.clicked.connect(self.DisplayBowlers)
        self.arbutton.clicked.connect(self.DisplayAR)
        self.wkbutton.clicked.connect(self.DisplayWK)
        self.List_AvailablePlayers.itemDoubleClicked.connect(self.addplayer)
        self.List_TeamPlayers.itemDoubleClicked.connect(self.removeplayer)
        cur.execute("SELECT DISTINCT Name FROM Teams;")
        self.team=Ui_Form.converttolist(Ui_Form,cur.fetchall())
        self.teamnames()
        self.Menu_OPENTeam.triggered[QtWidgets.QAction].connect(self.openteamclicked)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fantasy Cricket League"))
        self.Label_YourSelections.setText(_translate("MainWindow", "Your Selections"))
        self.Label_Batsman.setText(_translate("MainWindow", "Batsman(BAT)"))
        self.Label_BatCount.setText(_translate("MainWindow", "##"))
        self.Label_Bowlers.setText(_translate("MainWindow", "Bowlers(BOW)"))
        self.Label_BowlCount.setText(_translate("MainWindow", "##"))
        self.Label_AR.setText(_translate("MainWindow", "Allrounders(AR)"))
        self.Label_ARCount.setText(_translate("MainWindow", "##"))
        self.Label_WK.setText(_translate("MainWindow", "Wicket-keeper(WK)"))
        self.Label_WKCount.setText(_translate("MainWindow", "##"))
        self.Label_PointsAvailable.setText(_translate("MainWindow", "Points Available"))
        self.Label_AvailPtsCount.setText(_translate("MainWindow", "####"))
        self.Label_PointsUsed.setText(_translate("MainWindow", "Points Used"))
        self.Label_UsedPtsCount.setText(_translate("MainWindow", "####"))
        self.label.setText(_translate("MainWindow", ">"))
        self.Menu_ManageTeams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.Menu_OPENTeam.setTitle(_translate("MainWindow", "         OPEN Team "))
        self.Menu_EVALUATETeam.setText(_translate("MainWindow", "         EVALUATE Team"))
        self.Menu_NEWTeam.setText(_translate("MainWindow", "         NEW Team"))
        self.Menu_SAVETeam.setText(_translate("MainWindow", "         SAVE Team"))

#This Function is used to group players according to their category.       
    def listingplayers(self):
        cur.execute("SELECT Category FROM stats")
        self.newctg=Ui_Form.converttolist(Ui_Form,cur.fetchall())
        for ctg in self.newctg:
            cur.execute("SELECT player FROM Stats WHERE Category=?",(ctg,))
            if ctg=='BAT':
                self.batplayers=Ui_Form.converttolist(Ui_Form,cur.fetchall())
            elif ctg=='BOWL':
                self.bowlplayers=Ui_Form.converttolist(Ui_Form,cur.fetchall())
            elif ctg=='AR':
                self.arplayers=Ui_Form.converttolist(Ui_Form,cur.fetchall())
            elif ctg=='WK':
                self.wkplayers=Ui_Form.converttolist(Ui_Form,cur.fetchall())
        self.usersteamplayers=list()

#This Function is used to add teamnames which are in Teams table to the action openteam.
    def teamnames(self):
        if ((self.tname not in self.team) and (self.tname!=None)):
            self.actionopenteam=QtWidgets.QAction(self.Menu_OPENTeam)
            self.actionopenteam.setObjectName("action"+self.tname)
            self.actionopenteam.setText(self.tname)
            self.Menu_OPENTeam.addAction(self.actionopenteam)
        else:
            for i in self.team:
                self.actionopenteam=QtWidgets.QAction(self.Menu_OPENTeam)
                self.actionopenteam.setObjectName("action"+i)
                self.actionopenteam.setText(i)
                self.Menu_OPENTeam.addAction(self.actionopenteam)

#This function is used display a dialog prompt inorder to fetch the team name according to user.
    def NewTeamOptionclicked(self):
        NewTeamDialogBox = QtWidgets.QDialog()
        self.seticon(NewTeamDialogBox)
        ui = Ui_NewTeamDialogBox()
        ui.setupUi(NewTeamDialogBox)
        NewTeamDialogBox.show()
        response=NewTeamDialogBox.exec_()
        if response==NewTeamDialogBox.Accepted:
            UserInput=ui.Text_Input.text()
            if len(UserInput)<2:
                self.displayerrormessage("Enter a Team Name with at-least two characters.")
                self.NewTeamOptionclicked()
            else:
                cur.execute("SELECT DISTINCT Name FROM Teams;")
                self.newlst=Ui_Form.converttolist(Ui_Form,cur.fetchall())
                for i in self.newlst:
                    if i==UserInput:
                        self.displayerrormessage("You cannot create two Teams with the same name.")
                        self.NewTeamOptionclicked()
                        break
                else: 
                    self.centralwidget.setEnabled(True)
                    self.NewTeam.setText(UserInput)
                    self.clearList(self.List_AvailablePlayers)
                    self.clearList(self.List_TeamPlayers)
                    self.listingplayers()
                    self.clearall()
                    self.radiobuttonsoff()

#This Function is used to open a specified team when the user clicks on the teams available in action open team.
    def openteamclicked(self,action):
        self.radiobuttonsoff()
        self.clearList(self.List_TeamPlayers)
        self.clearList(self.List_AvailablePlayers)
        self.clearall()
        self.listingplayers()
        txt=(action.text())
        self.centralwidget.setEnabled(True)
        self.NewTeam.setText(txt) 
        cur.execute('SELECT Value FROM Teams WHERE Name=?',(txt,))
        pts=list(sum(cur.fetchall(),()))
        self.Label_UsedPtsCount.setText(str(sum(pts)))
        self.Label_AvailPtsCount.setText(str(int(1000-sum(pts))))
        cur.execute("SELECT Category FROM Stats JOIN Teams on Stats.Player=Teams.Players WHERE Teams.Name=?",(txt,))
        ctg=Ui_Form.converttolist(Ui_Form,cur.fetchall())
        self.Label_BatCount.setText(str(ctg.count('BAT')))
        self.Label_BowlCount.setText(str(ctg.count('BOWL')))
        self.Label_WKCount.setText(str(ctg.count('WK')))
        self.Label_ARCount.setText(str(ctg.count('AR')))
        cur.execute("SELECT Players FROM Teams WHERE Name=?",(txt,))
        names=Ui_Form.converttolist(Ui_Form,cur.fetchall())
        names.sort()
        for i in names:
            self.myplayers(i)
            ctg=self.fetchcategory(i)
            if ctg=="BAT":
                self.batplayers.remove(i)
            elif ctg=="BOWL":
                self.bowlplayers.remove(i)
            elif ctg=="AR": 
                self.arplayers.remove(i)
            elif ctg=="WK":
                self.wkplayers.remove(i)  
            i=self.colour(i)
            self.List_TeamPlayers.addItem(i)
        self.totplayers=len(names)

#This Function is used to save the team after the user creates his own team.
#If the user wishes to modify an existing team,then the changes made are updated into the database.
    def SAVETeamOptionclicked(self):

        duplicate=0
#duplicate is used to check whether the team already exists in the database.  

        self.tname=str(self.NewTeam.text())
        cur.execute("SELECT  Distinct Name FROM Teams")
        lst=Ui_Form.converttolist(Ui_Form,cur.fetchall())
        for i in lst:
            if i==self.tname:
                duplicate=1
        num=self.List_TeamPlayers.count()
        if num==1 or int(str(self.Label_WKCount.text()))==0 or self.totplayers!=11:
            self.displayerrormessage("You are violating the Game Rule . Please Create a Valid Team .")
        elif int(str(self.Label_BatCount.text()))<3 or int(str(self.Label_BowlCount.text()))<3 or int(str(self.Label_ARCount.text()))<1:
            self.displayerrormessage("Team Should Contain minimum 3 batsman,3 bowlers,3 all-rounders and one 1 wicket-keeper.")
        elif duplicate==1:
            cur.execute('DELETE FROM Teams WHERE Name=?',(self.tname,))
            lst=Ui_Form.converttolist(Ui_Form,cur.fetchall())
            for i in self.usersteamplayers:
                newlst=self.fetchvalue(i)
                cur.execute("INSERT INTO Teams(Name,Players,Value)Values(?,?,?);",(self.tname,i,newlst))
            conn.commit()
            self.displayteamsaved("Your Team has successfully been updated.")
            duplicate=0
        else:
            for i in self.usersteamplayers:
                newlst=self.fetchvalue(i)
                cur.execute('''INSERT INTO Teams(Name,Players,Value) Values(?,?,?);''',(self.tname,i,newlst))
            conn.commit() 
            self.displayteamsaved("Your Team has been sucessfully saved.")
            self.teamnames()

#This Function is used to display the Evaluate Team window.
    def EvaluateTeamOptionClicked(self):
        self.Form = QtWidgets.QWidget()
        self.seticon(self.Form)
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()
        self.Form.setStyleSheet(color)

#This Function is used to clear all the available labels.
    def clearall(self):
        self.Label_BatCount.setText("0")
        self.Label_BowlCount.setText("0")
        self.Label_WKCount.setText("0")
        self.Label_ARCount.setText("0")
        self.Label_AvailPtsCount.setText("1000")
        self.Label_UsedPtsCount.setText("0")
        self.totplayers=0

#This Function is used to display error message when any constraint fails.
    def displayerrormessage(self,message):
        ErrorMessage = QtWidgets.QDialog()
        ui = Ui_ErrorMessage()
        ui.setupUi(ErrorMessage)
        ErrorMessage.show()
        ui.ErrorMessageLabel.setText(message)
        ErrorMessage.exec_()

#This Function is used to display all the batsman when BAT radio button is clicked.
    def DisplayBatsman(self):
        self.clearList(self.List_AvailablePlayers)
        for x in self.batplayers: 
            item=self.colour(x)
            self.List_AvailablePlayers.addItem(item)

#This Function is used to display all the bowlers when BOW radio button is clicked.
    def DisplayBowlers(self):
        self.clearList(self.List_AvailablePlayers)
        for x in self.bowlplayers:
            item=self.colour(x)
            self.List_AvailablePlayers.addItem(item)

#This Function is used to display all the all-rounders when AR radio button is clicked.
    def DisplayAR(self):
        self.clearList(self.List_AvailablePlayers)
        for x in self.arplayers:
            item=self.colour(x)
            self.List_AvailablePlayers.addItem(item)

#This Function is used to display all the wicket-keepers when WK radio button is clicked.
    def DisplayWK(self):     
        self.clearList(self.List_AvailablePlayers)
        for x in self.wkplayers:
            item=self.colour(x)
            self.List_AvailablePlayers.addItem(item)

#This Function is used to add blue colour to list items. 
    def colour(self,y):
        item=QtWidgets.QListWidgetItem("          "+y)
        item.setForeground(QtGui.QColor(40,110,255))
        return item

#This Function is used to add players into the team. 
    def addplayer(self,player):
        value=self.List_AvailablePlayers.row(player)
        self.x=value
        player=player.text().strip()
        if value==0:
            pass
        else:
            self.ctg=self.fetchcategory(player)
            if self.ctg=="BAT":
                self.state=self.removepoints1(player)
                if self.state==1:
                    self.Label_BatCount.setText(str(int(self.Label_BatCount.text())+1))
                    self.batplayers.remove(player)
                    self.myplayers(player)
                    self.totplayers+=1
            elif self.ctg=="BOWL":
                self.state=self.removepoints1(player) 
                if self.state==1:
                    self.bowlplayers.remove(player)
                    self.myplayers(player)
                    self.Label_BowlCount.setText(str(int(self.Label_BowlCount.text())+1)) 
                    self.totplayers+=1
            elif self.ctg=="AR":
                    self.state=self.removepoints1(player)
                    if self.state==1:
                        self.arplayers.remove(player)
                        self.myplayers(player)
                        self.Label_ARCount.setText(str(int(self.Label_ARCount.text())+1)) 
                        self.totplayers+=1
            elif self.ctg=="WK":
                if int(self.Label_WKCount.text())==1:
                    self.displayerrormessage("You can't select more than one wicket-keeper.")
                else:
                    self.state=self.removepoints1(player)
                    if self.state==1:
                        self.wkplayers.remove(player)
                        self.myplayers(player)
                        self.Label_WKCount.setText(str(int(self.Label_WKCount.text())+1))
                        self.totplayers+=1

#This Function is used to remove players from the team.
    def removeplayer(self,player):
        value=self.List_TeamPlayers.row(player)
        if value==0:
            pass
        else:
            self.List_TeamPlayers.takeItem(self.List_TeamPlayers.row(player))
            strplayer=player.text().strip()
            self.ctg=self.fetchcategory(strplayer)
            if self.ctg=="BAT":
                self.batbutton.setChecked(True)
                self.batplayers.append(strplayer)
                self.myplayers2(strplayer)
                self.removepoints2(strplayer)
                self.DisplayBatsman()
                self.Label_BatCount.setText(str(int(self.Label_BatCount.text())-1))
                self.totplayers-=1
            elif self.ctg=="BOWL":
                self.bowlbutton.setChecked(True)
                self.bowlplayers.append(strplayer)
                self.myplayers2(strplayer)
                self.removepoints2(strplayer)
                self.DisplayBowlers()
                self.Label_BowlCount.setText(str(int(self.Label_BowlCount.text())-1))
                self.totplayers-=1
            elif self.ctg=="AR":
                self.arbutton.setChecked(True)
                self.arplayers.append(strplayer)
                self.myplayers2(strplayer)
                self.removepoints2(strplayer)
                self.DisplayAR()
                self.Label_ARCount.setText(str(int(self.Label_ARCount.text())-1))
                self.totplayers-=1
            elif self.ctg=="WK":
                self.wkbutton.setChecked(True)
                self.wkplayers.append(strplayer)
                self.myplayers2(strplayer)
                self.removepoints2(strplayer)
                self.DisplayWK() 
                self.Label_WKCount.setText(str(int(self.Label_WKCount.text())-1))
                self.totplayers-=1

#This Function is used to clear all the players from the list widget. 
    def clearList(self,listwidget):
        counter=listwidget.count()
        while counter>1:
            listwidget.takeItem(1)
            counter-=1

#This Function is used to add points to label(Points Used) when the user selects a player in to the team. 
    def removepoints1(self,player1):
        self.p1name=player1.strip()
        self.a1=self.fetchvalue(self.p1name)
        self.value1=int(self.Label_AvailPtsCount.text())-self.a1
        self.value2=int(self.Label_UsedPtsCount.text())+self.a1
        if (self.value1<0): 
            self.displayerrormessage("You can't use more than 1000 points.") 
            self.state=0
            return self.state
        elif self.totplayers==10 and int(self.Label_WKCount.text())==0 and self.ctg!='WK':
            self.displayerrormessage("You need to select atleast one Wicket-Keeper.") 
            self.state=0
            return self.state 
        elif self.totplayers==11 and int(self.Label_WKCount.text())==1:
            self.displayerrormessage("You cannot select more than 11 players.") 
            self.state=0
            return self.state 
        else:
            self.name=self.colour(self.p1name)
            self.List_TeamPlayers.addItem(self.name) 
            self.Label_AvailPtsCount.setText(str(self.value1))
            self.Label_UsedPtsCount.setText(str(self.value2))
            self.List_AvailablePlayers.takeItem(self.x)
            self.state=1
            return self.state

#This Function is used to add points to label(Points Available) when the user de-selects a player from the team.
    def removepoints2(self,player2):
        self.p2name=player2.strip()
        self.a2=self.fetchvalue(self.p2name)
        self.value1=int(self.Label_AvailPtsCount.text())+self.a2
        self.value2=int(self.Label_UsedPtsCount.text())-self.a2
        if (self.value1>=0 and self.value2<=1000):
            self.name=self.colour(self.p2name)
            self.Label_AvailPtsCount.setText(str(self.value1))
            self.Label_UsedPtsCount.setText(str(self.value2))

#This function displays a message after the team is saved
    def displayteamsaved(self,message):
        msg=QtWidgets.QMessageBox()
        msg.setWindowTitle("Team Saved")
        msg.setStyleSheet("font:10pt \"Comic Sans MS\";\n")
        msg.setText(message)
        self.seticon(msg)
        pixmap = QtGui.QPixmap("checkmarksign.jpg") 
        pixmap=pixmap.scaled(50,50,QtCore.Qt.KeepAspectRatio)
        msg.setIconPixmap(pixmap)
        msg.exec_() 

#This function adds player to the list usersteamplayers. 
    def myplayers(self,player):
        self.usersteamplayers.append(player.strip())

#This function removes player from the list usersteamplayers. 
    def myplayers2(self,player):
        self.usersteamplayers.remove(player.strip())

#This function is used to fetch the category of a specified player.
    def fetchcategory(self,x):
        cur.execute("SELECT Category FROM Stats WHERE Player=?",(x,))
        ctg=''.join(cur.fetchone())
        return ctg

#This function is used to fetch the value of a specified player.
    def fetchvalue(self,y):
        cur.execute("SELECT Value FROM Stats WHERE Player=?",(y,))
        return int(''.join(map(str,cur.fetchone())))

#This function is used to set the icon for Window,Dialog,MessageBox etc. 
    def seticon(self,widget):
        icon=QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Cricket.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        widget.setWindowIcon(icon)

#This function is used to off the radiobuttons if they are already selected.
    def radiobuttonsoff(self):
        if self.batbutton.isChecked():
            self.batbutton.setAutoExclusive(False)
            self.batbutton.setChecked(False)
            self.batbutton.setAutoExclusive(True)
        elif self.bowlbutton.isChecked():
            self.bowlbutton.setAutoExclusive(False)
            self.bowlbutton.setChecked(False)
            self.bowlbutton.setAutoExclusive(True)
        elif self.arbutton.isChecked():
            self.arbutton.setAutoExclusive(False)
            self.arbutton.setChecked(False)
            self.arbutton.setAutoExclusive(True)
        elif self.wkbutton.isChecked():
            self.wkbutton.setAutoExclusive(False)
            self.wkbutton.setChecked(False)
            self.wkbutton.setAutoExclusive(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
