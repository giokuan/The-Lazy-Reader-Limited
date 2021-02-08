from gtts import gTTS 
import time
import playsound
import speech_recognition as sr
import sqlite3

# import Os module to start the audio file
import os 
import sys
#from pygame import mixer
import re
from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
#from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView, QVBoxLayout, QHBoxLayout, QHeaderView,QTableWidget
#from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
from langdetect import detect
#from googletrans import Translator


#conn = sqlite3.connect('tts.db') 
#cursor = conn.cursor()


#cursor.execute ("""DROP TABLE  story""")
#print("Table dropped... ")

#sql = """ INSERT INTO story ( title, content,idx) VALUES ("van", "gio", 1)"""

#sql=""" INSERT INTO radio (radioidx) VALUES (1)"""
#sql = """DELETE from lang_idx where idx = 5"""

#sql = """CREATE TABLE IF NOT EXISTS
#    story(title TEXT,  content TEXT , idx INTEGER PRIMARY KEY AUTOINCREMENT)"""
#  radio(radioidx INTEGER)

#cursor.execute(sql)
#print("Table created... ")

#conn.commit()
#conn.close()

class Ui_MainWindow(object):###
    def messageBox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setWindowIcon(QtGui.QIcon('icons/double3 .ico'))
        #msg.setWindowTitle("The Lazy Reader")
        mess.setStyleSheet('QMessageBox {background-color: rgb(87, 211, 221); color: white;}\
            QPushButton{color: white; font-size: 16px; background-color: rgb(9, 93, 140); \
            border-radius: 10px; padding: 10px; text-align: center;}QPushButton:hover{color: rgb(0, 170, 127);}') 
        mess.setText(message)
        mess.setIcon(QMessageBox.Information)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
        
        
    def theme_index(self):
        theme = self.theme_combo.currentText()
        if theme == ('Dino'):
            self.background_label.setPixmap(QtGui.QPixmap("icons/dino.png"))
            self.lang_combo.setStyleSheet("background-color: rgb(255,255,255);")
            self.theme_combo.setStyleSheet("background-color: rgb(255,255,255);")
            self.search_edit.setStyleSheet("background-color: rgb(35,141,183);")
            self.title_edit.setStyleSheet("background-color: rgb(46,148,188);")
            self.makefun_label.setStyleSheet("color: rgb(0,0,0);")
            self.thelazy_label.setStyleSheet("color: rgb(0,0,0);")

            self.clear_btn.setStyleSheet("QPushButton{background-color: rgb(227,29,28);\
                }QPushButton::hover{background-color : lightgreen;}")
            self.exit_btn.setStyleSheet("QPushButton{background-color: rgb(181,219,9);\
                }QPushButton::hover{background-color : lightgreen;}")
            self.delete_btn.setStyleSheet("QPushButton{background-color: rgb(42,115,0);\
                }QPushButton::hover{background-color : lightgreen;}")
            self.save_btn.setStyleSheet("QPushButton{background-color: rgb(138,50,114);\
                }QPushButton::hover{background-color : lightgreen;}")
            self.play_btn.setStyleSheet("QPushButton{background-color: rgb(56,154,191);\
                }QPushButton::hover{background-color : lightgreen;}")
            self.add_btn.setStyleSheet("QPushButton{background-color: rgb(56,154,191);\
                }QPushButton::hover{background-color : lightgreen;}")
            self.theme_btn.setStyleSheet("QPushButton{background-color: rgb(35,141,183);\
                }QPushButton::hover{background-color : lightgreen;}")
            self.about_btn.setStyleSheet("QPushButton{background-color: rgb(35,141,183);\
                 }QPushButton::hover{background-color : lightgreen;}")
            self.search_btn.setStyleSheet("QPushButton{background-color: rgb(35,141,183);\
                }QPushButton::hover{background-color : lightgreen;}")

            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("icons/addnew2.png"),\
             QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.add_btn.setIcon(icon1)

            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap("icons/exit2.png"),\
             QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.exit_btn.setIcon(icon2) 

            icon3 = QtGui.QIcon()
            icon3.addPixmap(QtGui.QPixmap("icons/play2.png"),\
             QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.play_btn.setIcon(icon3)

            icon4 = QtGui.QIcon()
            icon4.addPixmap(QtGui.QPixmap("icons/save2.png"),\
             QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.save_btn.setIcon(icon4)

            icon5 = QtGui.QIcon()
            icon5.addPixmap(QtGui.QPixmap("icons/delete2.png"),\
             QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.delete_btn.setIcon(icon5)

            icon6 = QtGui.QIcon()
            icon6.addPixmap(QtGui.QPixmap("icons/clear2.png"),\
             QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.clear_btn.setIcon(icon6)

            icon7 = QtGui.QIcon()
            icon7.addPixmap(QtGui.QPixmap("icons/search2.png"),\
             QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.search_btn.setIcon(icon7)

            icon8 = QtGui.QIcon()
            icon8.addPixmap(QtGui.QPixmap("icons/theme2.png"),\
             QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.theme_btn.setIcon(icon8)

            icon9 = QtGui.QIcon()
            icon9.addPixmap(QtGui.QPixmap("icons/about2.png"),\
             QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.about_btn.setIcon(icon9)

            icon10 = QtGui.QIcon()
            icon10.addPixmap(QtGui.QPixmap("icons/cancel2.png"),\
             QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.cancel_btn.setIcon(icon10)

            icon11 = QtGui.QIcon()
            icon11.addPixmap(QtGui.QPixmap("icons/update2.png"),\
             QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.update_btn.setIcon(icon11)
            self.theme_combo.hide()
           
               
            
        
            
        elif theme == ('Safari'):
            self.background_label.setPixmap(QtGui.QPixmap("icons/safari.png"))
            self.lang_combo.setStyleSheet("background-color: rgb(152,93,51);")
            self.theme_combo.setStyleSheet("background-color: rgb(152,93,51);")
            self.search_edit.setStyleSheet("background-color: rgb(152,93,51);")
            self.title_edit.setStyleSheet("background-color: rgb(152,93,51);")
            self.makefun_label.setStyleSheet("color: rgb(152,93,51);")
            self.thelazy_label.setStyleSheet("color: rgb(152,93,51);")

            self.clear_btn.setStyleSheet("QPushButton{background-color: rgb(152,93,51);\
                }QPushButton::hover{background-color : lightgreen;}")
            self.exit_btn.setStyleSheet("QPushButton{background-color: rgb(152,93,51);\
                }QPushButton::hover{background-color : lightgreen;}")
            self.delete_btn.setStyleSheet("QPushButton{background-color: rgb(152,93,51);\
                }QPushButton::hover{background-color : lightgreen;}")
            self.save_btn.setStyleSheet("QPushButton{background-color: rgb(152,93,51);\
                }QPushButton::hover{background-color : lightgreen;}")
            self.update_btn.setStyleSheet("QPushButton{background-color: rgb(152,93,51);\
                }QPushButton::hover{background-color : lightgreen;}")
            self.play_btn.setStyleSheet("QPushButton{background-color: rgb(152,93,51);\
                }QPushButton::hover{background-color : lightgreen;}")
            self.add_btn.setStyleSheet("QPushButton{background-color: rgb(152,93,51);\
                }QPushButton::hover{background-color : lightgreen;}")
            self.theme_btn.setStyleSheet("QPushButton{background-color: rgb(152,93,51);\
                }QPushButton::hover{background-color : lightgreen;}")
            self.about_btn.setStyleSheet("QPushButton{background-color: rgb(152,93,51);\
                 }QPushButton::hover{background-color : lightgreen;}")
            self.search_btn.setStyleSheet("QPushButton{background-color: rgb(152,93,51);\
                }QPushButton::hover{background-color : lightgreen;}")
            self.cancel_btn.setStyleSheet("QPushButton{background-color: rgb(152,93,51);\
                }QPushButton::hover{background-color : lightgreen;}")


            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("icons/addnew3.png"),\
             QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.add_btn.setIcon(icon1)

            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap("icons/exit3.png"),\
             QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.exit_btn.setIcon(icon2) 

            icon3 = QtGui.QIcon()
            icon3.addPixmap(QtGui.QPixmap("icons/play3.png"),\
             QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.play_btn.setIcon(icon3)

            icon4 = QtGui.QIcon()
            icon4.addPixmap(QtGui.QPixmap("icons/save3.png"),\
             QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.save_btn.setIcon(icon4)

            icon5 = QtGui.QIcon()
            icon5.addPixmap(QtGui.QPixmap("icons/delete3.png"),\
             QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.delete_btn.setIcon(icon5)

            icon6 = QtGui.QIcon()
            icon6.addPixmap(QtGui.QPixmap("icons/clear3.png"),\
             QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.clear_btn.setIcon(icon6)

            icon7 = QtGui.QIcon()
            icon7.addPixmap(QtGui.QPixmap("icons/search3.png"),\
             QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.search_btn.setIcon(icon7)

            icon8 = QtGui.QIcon()
            icon8.addPixmap(QtGui.QPixmap("icons/theme3.png"),\
             QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.theme_btn.setIcon(icon8)

            icon9 = QtGui.QIcon()
            icon9.addPixmap(QtGui.QPixmap("icons/about3.png"),\
             QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.about_btn.setIcon(icon9)

            icon10 = QtGui.QIcon()
            icon10.addPixmap(QtGui.QPixmap("icons/cancel3.png"),\
             QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.cancel_btn.setIcon(icon10)

            icon11 = QtGui.QIcon()
            icon11.addPixmap(QtGui.QPixmap("icons/update3.png"),\
             QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.update_btn.setIcon(icon11)
            self.theme_combo.hide()
            
        
            
        elif theme == ('Under the sea'):
            self.background_label.setPixmap(QtGui.QPixmap("icons/under_the_sea.png"))
            self.lang_combo.setStyleSheet("background-color: rgb(180, 225, 218);")
            self.theme_combo.setStyleSheet("background-color: rgb(87, 211, 221);")
            self.search_edit.setStyleSheet("background-color: rgb(180, 225, 218);")
            self.title_edit.setStyleSheet("background-color: rgb(87, 211, 221);")
            self.makefun_label.setStyleSheet("color: rgb(0,0,0);")
            self.thelazy_label.setStyleSheet("color: rgb(0,0,0);")

            self.clear_btn.setStyleSheet("QPushButton{background-color: rgb(9, 93, 140);\
                }QPushButton::hover{background-color : lightgreen;}")
            self.exit_btn.setStyleSheet("QPushButton{background-color: rgb(253, 238, 207);\
                }QPushButton::hover{background-color : lightgreen;}")
            self.delete_btn.setStyleSheet("QPushButton{background-color: rgb(235, 176, 136);\
               }QPushButton::hover{background-color : lightgreen;}")
            self.save_btn.setStyleSheet("QPushButton{background-color: rgb(9, 93, 140);\
                }QPushButton::hover{background-color : lightgreen;}")
            self.play_btn.setStyleSheet("QPushButton{background-color: rgb(9, 93, 140);\
                }QPushButton::hover{background-color : lightgreen;}")
            self.update_btn.setStyleSheet("QPushButton{background-color: rgb(9, 93, 140);\
                }QPushButton::hover{background-color : lightgreen;}")
            self.add_btn.setStyleSheet("QPushButton{background-color: rgb(66, 202, 218);\
                }QPushButton::hover{background-color : lightgreen;}")
            self.cancel_btn.setStyleSheet("QPushButton{background-color: rgb(66, 202, 218);\
                }QPushButton::hover{background-color : lightgreen;}")
            self.theme_btn.setStyleSheet("QPushButton{background-color: rgb(104, 202, 241);\
                }QPushButton::hover{background-color : lightgreen;}")
            self.about_btn.setStyleSheet("QPushButton{background-color: rgb(180, 225, 218);\
                 }QPushButton::hover{background-color : lightgreen;}")
            self.search_btn.setStyleSheet("QPushButton{background-color: rgb(180, 225, 218);\
                }QPushButton::hover{background-color : lightgreen;}")

            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("icons/addnew2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.add_btn.setIcon(icon1)

            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap("icons/exit2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.exit_btn.setIcon(icon2) 

            icon3 = QtGui.QIcon()
            icon3.addPixmap(QtGui.QPixmap("icons/play2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.play_btn.setIcon(icon3)

            icon4 = QtGui.QIcon()
            icon4.addPixmap(QtGui.QPixmap("icons/save2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.save_btn.setIcon(icon4)

            icon5 = QtGui.QIcon()
            icon5.addPixmap(QtGui.QPixmap("icons/delete2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.delete_btn.setIcon(icon5)

            icon6 = QtGui.QIcon()
            icon6.addPixmap(QtGui.QPixmap("icons/clear2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.clear_btn.setIcon(icon6)

            icon7 = QtGui.QIcon()
            icon7.addPixmap(QtGui.QPixmap("icons/search2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.search_btn.setIcon(icon7)

            icon8 = QtGui.QIcon()
            icon8.addPixmap(QtGui.QPixmap("icons/theme2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.theme_btn.setIcon(icon8)

            icon9 = QtGui.QIcon()
            icon9.addPixmap(QtGui.QPixmap("icons/about2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.about_btn.setIcon(icon9)

            icon10 = QtGui.QIcon()
            icon10.addPixmap(QtGui.QPixmap("icons/cancel2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.cancel_btn.setIcon(icon10)

            icon11 = QtGui.QIcon()
            icon11.addPixmap(QtGui.QPixmap("icons/update2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.update_btn.setIcon(icon11)
            self.theme_combo.hide()
            

    def delete(self):
        conn = sqlite3.connect('tts.db')
        cursor = conn.cursor()

        te = self.index_edit.text()

        

        msg=QMessageBox()
        msg.setStyleSheet('QMessageBox {background-color: rgb(87, 211, 221); color: white;}\
            QPushButton{color: white; font-size: 16px; background-color: rgb(9, 93, 140); \
            border-radius: 10px; padding: 10px; text-align: center;}QPushButton:hover{color: rgb(0, 170, 127);}') 
        msg.setWindowIcon(QtGui.QIcon('icons/double3 .ico'))
        msg.setWindowTitle("The Lazy Reader")
        msg.setText("Are you sure you wan't to delete this Story?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Ok| QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Ok)
        
        res = msg.exec_()
        if res == QMessageBox.Ok: 
            
            cursor.execute("DELETE FROM story WHERE idx = '"+te+"' ")
            conn.commit()
            self.messageBox('Delete','Story Deleted') 
            conn.close()
            self.title_edit.clear()
            self.plainTextEdit.clear()
            self.loadData()
        if res == QMessageBox.Cancel:
            pass 

    

    def cancel(self):
        self.add_btn.show()
        self.update_btn.show()
        self.save_btn.hide()
        self.cancel_btn.hide()
        self.clear()

        self.title_edit.setPlaceholderText("")
        self.plainTextEdit.setPlaceholderText("")
        self.lang_combo.setEnabled(True)




    def insert_data(self):
        conn = sqlite3.connect('tts.db')
        cursor = conn.cursor()

        idx = self.index_edit.text()
        te = self.title_edit.text()
        pt = self.plainTextEdit.toPlainText()
      

        #cursor.execute("INSERT INTO story (title, content) VALUES (te, pt)");
        sql = ('''INSERT INTO story VALUES (?,?,null)''')
        #cursor.execute(sql,(int(sid), te, pt))

        if (sql):
            mess=QMessageBox()
            if len(te) == 0:
                self.messageBox("Information", " Please enter the title of the story!")

            elif len(pt) == 0:
                self.messageBox("Information", " Please Type or paste text in the box!")
            else:
                cursor.execute(sql, (te, pt))
                self.messageBox("Add Story", " Story Saved")
                conn.commit()
                conn.close()
                self.loadData()
                self.clear()
                self.cancel()


    def update(self):
        conn = sqlite3.connect('tts.db')
        cursor = conn.cursor()

        idn = self.index_edit.text()
        te = self.title_edit.text()
        pt = self.plainTextEdit.toPlainText()

        if len(te)  == 0:
            self.messageBox('Information', 'Title is Empty')
        elif len(pt) == 0:
            self.messageBox('Information', 'Story field is empty')
        elif len(idn) == 0:
            self.messageBox('Information', 'No data can be updated\n Please press the add story button instead')

        else:

            sql = ("UPDATE story SET title = '"+te+"', content = '"+pt+"' WHERE  idx = '"+str(idn)+"' ")
            cursor.execute(sql)
            self.messageBox('Update', 'Story Updated')

            conn.commit()
            conn.close()
            self.loadData()


    def search(self):
    
        conn = sqlite3.connect('tts.db')
        cursor = conn.cursor()

        se = self.search_edit.text()
        if len(se) == 0:
                self.messageBox('Inforamtion', 'Please enter a title')
        else:
            cursor.execute("SELECT * FROM story WHERE title=?", [se])
            col = cursor.fetchone()

            if col:

                title = col[0]
                story = col[1]
                idx = col [2]

                self.index_edit.setText(str(idx))
                self.title_edit.setText(title)
                self.plainTextEdit.appendPlainText(story)
            else:
                self.messageBox('Information','No data found')
                return

       

    def add_story(self):
        self.save_btn.show()
        self.update_btn.hide()
        self.cancel_btn.show()
        self.add_btn.hide()
        self.lang_combo.setEnabled(False)
        self.title_edit.setPlaceholderText('Enter Title Here') 
        self.plainTextEdit.setPlaceholderText("Type or Paste your text here")
        self.clear()


    def languages(self):
        lc = self.lang_combo.currentText()

        if lc == 'English':
            self.thelazy_label.setText("THE LAZY READER")
            self.makefun_label.setText('Children\'s stories')
            self.choose_lang_label.setText('Choose your language')
            self.title_label.setText('Title')
            self.type_label.setText('Type or paste your text below') 
            item = self.tableWidget.horizontalHeaderItem(0)
            item.setText( "Select Story")

        elif lc == 'Filipino':
            self.thelazy_label.setText("ANG TAMAD NA MAGBASA")
            self.makefun_label.setText('Mga kuwentong pambata')
            self.choose_lang_label.setText('Piliin ang iyong wika')
            self.title_label.setText('Pamagat')
            self.type_label.setText('I-type o i-paste ang iyong teksto sa ibaba') 
            item = self.tableWidget.horizontalHeaderItem(0)
            item.setText("Pumili ng kuwento")

    def detect(self):

        s=self.plainTextEdit.toPlainText()

        if len(s) == 0:
            return
        else:
            r = detect(s)

            

            if r == 'en':
                self.lang_combo.setCurrentText('English')

            elif r == 'tl':
                self.lang_combo.setCurrentText('Filipino')


    def listen(self):
        #self.detect()
        
        s=self.plainTextEdit.toPlainText()

        if len(s) == 0:
            return

        else:
        
            langu = self.lang_combo.currentText()
            

            if langu == 'English':
                language= 'en'

            elif langu == 'Filipino':
                language = 'tl'

            #language = 'en'
            tts = gTTS(text= s, lang=language, slow=False) 
            filename = ('voice.mp3')
            tts.save(filename) 

            playsound.playsound(filename)
     
            os.remove(filename)
            self.update_index()
            self.languages()

        

    def loadData(self):
       
        row = 0
       
        conn = sqlite3.connect('tts.db')
        cursor = conn.cursor()
            
        cursor.execute("SELECT * FROM story ORDER BY title ASC" )
        result = cursor.fetchall()
            
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        
    def cell_click(self,columnCount,rowCount):

        conn = sqlite3.connect('tts.db')
        cursor = conn.cursor()

        item = self.tableWidget.selectedItems()
        i = (item[0].text())

        if rowCount != (0):
            return

        else:
            cursor.execute ("SELECT * from story WHERE title=?",[i] )
            col = cursor.fetchone()
            
            title = col[0]
            story = col[1]
            idx = col [2]

        self.title_edit.setText(title)
        self.plainTextEdit.setPlainText(story)
        self.index_edit.setText(str(idx))

    def update_index(self):
        conn = sqlite3.connect('tts.db')
        cursor = conn.cursor() 
     
        i = self.lang_combo.currentIndex()

        cursor.execute("UPDATE lang_idx SET idx = '"+str(i)+"'" )
        
        conn.commit()
        conn.close()
    
            
    def load_index(self):
        conn = sqlite3.connect('tts.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM lang_idx " )
        result = cursor.fetchone()
        x= result[0]
        self.lang_combo.setCurrentIndex(x)
    

    def clear(self):
        self.title_edit.clear()
        self.plainTextEdit.clear()
        self.search_edit.clear()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1016, 891)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/double3 .ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowFlags( QtCore.Qt.CustomizeWindowHint )
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        MainWindow.setIconSize(QtCore.QSize(120, 120))
        #MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.content_frame = QtWidgets.QFrame(self.centralwidget)
        self.content_frame.setGeometry(QtCore.QRect(120, 310, 871, 551))
        self.content_frame.setStyleSheet("")
        self.content_frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.content_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content_frame.setObjectName("content_frame")
        
        #TABLE
        self.tableWidget = QtWidgets.QTableWidget(self.content_frame)
        self.tableWidget.setGeometry(QtCore.QRect(620, 60, 231, 461))
        self.tableWidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0,\
             y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)       
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(227)
        self.tableWidget.verticalHeader().setVisible(False)
        self.loadData()
        self.tableWidget.cellClicked.connect(self.cell_click)
        
        # TYPE OR PASTE YOUR TEXT LABEL
        self.type_label = QtWidgets.QLabel(self.content_frame)
        self.type_label.setGeometry(QtCore.QRect(30, 20, 621, 31))
        font = QtGui.QFont()
        font.setFamily("Gunship")
        font.setPointSize(12)
        self.type_label.setFont(font)
        self.type_label.setObjectName("type_label")
        
        #PLAIN TEXT
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.content_frame)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 60, 581, 461))
        font = QtGui.QFont()
        #font.setFamily("Gunship")
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0,\
             y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));")
        self.plainTextEdit.setObjectName("plainTextEdit")
        
        
        #TITLE FRAME
        self.title_frame = QtWidgets.QFrame(self.centralwidget)
        self.title_frame.setGeometry(QtCore.QRect(20, 200, 971, 91))
        self.title_frame.setStyleSheet("")
        self.title_frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.title_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.title_frame.setObjectName("title_frame")
        
        #TITLE EDIT TEXTBOX
        self.title_edit = QtWidgets.QLineEdit(self.title_frame)
        self.title_edit.setGeometry(QtCore.QRect(120, 50, 581, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title_edit.setFont(font)
        self.title_edit.setStyleSheet("background-color: rgb(87, 211, 221);")
        self.title_edit.setObjectName("title_edit")
        
        #TITLE LABEL
        self.title_label = QtWidgets.QLabel(self.title_frame)
        self.title_label.setGeometry(QtCore.QRect(350, 20, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Gunship")
        font.setPointSize(15)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")      
        
        #BACKGROUND LABEL
        self.background_label = QtWidgets.QLabel(self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 1031, 891))
        self.background_label.setText("")
        self.background_label.setPixmap(QtGui.QPixmap("icons/under_the_sea.png"))
        self.background_label.setScaledContents(True)
        self.background_label.setObjectName("background_label")
        
        #BUTTON FRAME
        self.button_frame = QtWidgets.QFrame(self.centralwidget)
        self.button_frame.setGeometry(QtCore.QRect(20, 310, 81, 551))
        self.button_frame.setStyleSheet("background-color: qlineargradient(spread:pad,\
             x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));")
        self.button_frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_frame.setObjectName("button_frame")
        
        #ADD NEW BUTTON
        self.add_btn = QtWidgets.QPushButton(self.button_frame)
        self.add_btn.setGeometry(QtCore.QRect(10, 10, 61, 81))
        self.add_btn.setStyleSheet("QPushButton{background-color: rgb(66, 202, 218);\
            }QPushButton::hover{background-color : lightgreen;}")
        self.add_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/addnew2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_btn.setIcon(icon1)
        self.add_btn.setIconSize(QtCore.QSize(50, 50))
        self.add_btn.setFlat(False)
        self.add_btn.setObjectName("add_btn")
        self.add_btn.clicked.connect(self.add_story)


        #CANCEL BUTTON
        self.cancel_btn = QtWidgets.QPushButton(self.button_frame)
        self.cancel_btn.setGeometry(QtCore.QRect(10, 10, 61, 81))
        self.cancel_btn.setStyleSheet("QPushButton{background-color: rgb(66, 202, 218);\
            }QPushButton::hover{background-color : lightgreen;}")
        self.cancel_btn.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/cancel2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_btn.setIcon(icon10)
        self.cancel_btn.setIconSize(QtCore.QSize(50, 50))
        self.cancel_btn.setFlat(False)
        self.cancel_btn.setObjectName("cancel_btn")
        self.cancel_btn.hide()
        self.cancel_btn.clicked.connect(self.cancel)
        
        #EXIT BUTTON
        self.exit_btn = QtWidgets.QPushButton(self.button_frame)
        self.exit_btn.setGeometry(QtCore.QRect(10, 460, 61, 81))
        self.exit_btn.setStyleSheet("QPushButton{background-color: rgb(253, 238, 207);\
            }QPushButton::hover{background-color : lightgreen;}")
        self.exit_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/exit2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn.setIcon(icon2)
        self.exit_btn.setIconSize(QtCore.QSize(50, 50))
        self.exit_btn.setShortcut("Backspace")
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.clicked.connect(lambda:sys.exit())
        
        #PLAY BUTTON
        self.play_btn = QtWidgets.QPushButton(self.button_frame)
        self.play_btn.setGeometry(QtCore.QRect(10, 100, 61, 81))
        self.play_btn.setStyleSheet("QPushButton{background-color: rgb(9, 93, 140);\
            }QPushButton::hover{background-color : lightgreen;}")
        self.play_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/play2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_btn.setIcon(icon3)
        self.play_btn.setIconSize(QtCore.QSize(50, 50))
        self.play_btn.setShortcut("Backspace")
        self.play_btn.setObjectName("play_btn")
        #self.play_btn.clicked.connect(self.languages)
        self.play_btn.clicked.connect(self.detect)
        self.play_btn.clicked.connect(self.listen)
        
        #SAVE BUTTON
        self.save_btn = QtWidgets.QPushButton(self.button_frame)
        self.save_btn.setGeometry(QtCore.QRect(10, 190, 61, 81))
        self.save_btn.setStyleSheet("QPushButton{background-color: rgb(9, 93, 140);\
            }QPushButton::hover{background-color : lightgreen;}")
        self.save_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/save2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_btn.setIcon(icon4)
        self.save_btn.setIconSize(QtCore.QSize(50, 50))
        self.save_btn.setShortcut("Backspace")
        self.save_btn.setObjectName("save_btn")
        self.save_btn.clicked.connect(self.insert_data)
        self.save_btn.hide()


        #UPDATE BUTTON
        self.update_btn = QtWidgets.QPushButton(self.button_frame)
        self.update_btn.setGeometry(QtCore.QRect(10, 190, 61, 81))
        self.update_btn.setStyleSheet("QPushButton{background-color: rgb(9, 93, 140);\
            }QPushButton::hover{background-color : lightgreen;}")
        self.save_btn.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/update2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.update_btn.setIcon(icon11)
        self.update_btn.setIconSize(QtCore.QSize(50, 50))
        self.update_btn.setShortcut("Backspace")
        self.update_btn.setObjectName("update_btn")
        self.update_btn.clicked.connect(self.update)
        #self.update_btn.setEnabled(False)
        
        #DELETE BUTTON
        self.delete_btn = QtWidgets.QPushButton(self.button_frame)
        self.delete_btn.setGeometry(QtCore.QRect(10, 370, 61, 81))
        self.delete_btn.setStyleSheet("QPushButton{background-color: rgb(235, 176, 136);\
            }QPushButton::hover{background-color : lightgreen;}")
        self.delete_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/delete2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_btn.setIcon(icon5)
        self.delete_btn.setIconSize(QtCore.QSize(50, 50))
        self.delete_btn.setShortcut("Backspace")
        self.delete_btn.setObjectName("delete_btn")
        self.delete_btn.clicked.connect(self.delete)
        
        #CLEAR BUTTON
        self.clear_btn = QtWidgets.QPushButton(self.button_frame)
        self.clear_btn.setGeometry(QtCore.QRect(10, 280, 61, 81))
        self.clear_btn.setStyleSheet("QPushButton{background-color: rgb(9, 93, 140);\
            }QPushButton::hover{background-color : lightgreen;}")
        self.clear_btn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/clear2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_btn.setIcon(icon6)
        self.clear_btn.setIconSize(QtCore.QSize(50, 50))
        self.clear_btn.setShortcut("Backspace")
        self.clear_btn.setObjectName("clear_btn")
        self.clear_btn.clicked.connect(self.clear)
        
        #SEARCH FRAME
        self.search_frame = QtWidgets.QFrame(self.centralwidget)
        self.search_frame.setGeometry(QtCore.QRect(120, 120, 871, 71))
        self.search_frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.search_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.search_frame.setObjectName("search_frame")

         #LANGUAGE COMBOBOX
        self.lang_combo = QtWidgets.QComboBox(self.search_frame)
        self.lang_combo.setGeometry(QtCore.QRect(420, 30, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lang_combo.setFont(font)
        self.lang_combo.setStyleSheet("background-color: rgb(180, 225, 218);")
        self.lang_combo.setCurrentText("")
        self.lang_combo.setFrame(True)
        self.lang_combo.setObjectName("lang_combo")
        lang = ['English','Filipino']
        self.lang_combo.addItems(lang)
        size = QSize(35, 35) 
        self.lang_combo.setIconSize(size)
        self.lang_combo.setItemIcon(0, QIcon('icons/usa.jpg'))
        self.lang_combo.setItemIcon(1, QIcon('icons/philippines.jpg'))
        self.lang_combo.activated[str].connect(self.languages)
        self.lang_combo.activated[str].connect(self.clear)
        self.load_index()
        self.lang_combo.activated[str].connect(self.update_index)
   
        ##THEME COMBOBOX--------------------###########################
        self.theme_combo = QtWidgets.QComboBox(self.title_frame)
        self.theme_combo.setGeometry(QtCore.QRect(755, 51, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.theme_combo.setFont(font)
        self.theme_combo.setStyleSheet("background-color: rgb(87, 211, 221);")
        self.theme_combo.setObjectName("theme_combo")
        theme = ['Under the sea','Dino', 'Safari' ]
        self.theme_combo.addItems(theme)
        self.theme_combo.hide()
        #self.theme_combo.activated[str].connect(self.update_theme_index)
        self.theme_combo.activated[str].connect(self.theme_index)
        #self.load_theme_index()
        
        #CHOOSE YOU LANGUAGE LABEL
        self.choose_lang_label = QtWidgets.QLabel(self.search_frame)
        self.choose_lang_label.setGeometry(QtCore.QRect(420, 10, 431, 20))
        font = QtGui.QFont()
        font.setFamily("Gunship")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.choose_lang_label.setFont(font)
        self.choose_lang_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.choose_lang_label.setObjectName("choose_lang_label")
        
        #SEARCH EDIT TEXTBOX
        self.search_edit = QtWidgets.QLineEdit(self.search_frame)
        self.search_edit.setGeometry(QtCore.QRect(110, 30, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.search_edit.setFont(font)
        self.search_edit.setStyleSheet("background-color: rgb(180, 225, 218);")
        self.search_edit.setObjectName("search_edit")

        #combo current index left
        self.index_edit = QtWidgets.QLineEdit(self.search_frame)
        self.index_edit.setGeometry(QtCore.QRect(110, 5, 50, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.index_edit.setFont(font)
        self.index_edit.setStyleSheet("background-color: rgb(167, 203, 230);")
        self.index_edit.setObjectName("index_edit")
        self.index_edit.hide()
        
        #SEARCH BUTTON
        self.search_btn = QtWidgets.QPushButton(self.search_frame)
        self.search_btn.setGeometry(QtCore.QRect(20, 30, 81, 31))
        self.search_btn.setStyleSheet("QPushButton{background-color: rgb(180, 225, 218);\
            }QPushButton::hover{background-color : lightgreen;}")
        self.search_btn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/search2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn.setIcon(icon7)
        self.search_btn.setIconSize(QtCore.QSize(25, 25))
        self.search_btn.setObjectName("search_btn")
        self.search_btn.clicked.connect(self.search)
        
        
        #HEADER FRAME
        self.header_frame = QtWidgets.QFrame(self.centralwidget)
        self.header_frame.setGeometry(QtCore.QRect(20, 10, 971, 91))
        self.header_frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")
        
        #THE LAZY READER LABEL 
        self.thelazy_label = QtWidgets.QLabel(self.header_frame)
        self.thelazy_label.setGeometry(QtCore.QRect(70, 20, 751, 31))
        font = QtGui.QFont()
        font.setFamily("Gunship Bold")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.thelazy_label.setFont(font)
        self.thelazy_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.thelazy_label.setLineWidth(1)
        self.thelazy_label.setScaledContents(False)
        self.thelazy_label.setObjectName("thelazy_label")


        #MAKE FUN WITH YOUR KIDS LABEL 
        self.makefun_label = QtWidgets.QLabel(self.header_frame)
        self.makefun_label.setGeometry(QtCore.QRect(80, 50, 801, 31))
        font = QtGui.QFont()
        font.setFamily("Gunship Bold")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.makefun_label.setFont(font)
        self.makefun_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.makefun_label.setLineWidth(1)
        self.makefun_label.setScaledContents(False)
        self.makefun_label.setObjectName("makefun_label")
        
        #THEME BUTTON
        self.theme_btn = QtWidgets.QPushButton(self.title_frame)
        self.theme_btn.setGeometry(QtCore.QRect(890, 11, 61, 71)) 
        self.theme_btn.setStyleSheet("QPushButton{background-color: rgb(104, 202, 241);\
            }QPushButton::hover{background-color : lightgreen;}")
        self.theme_btn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/theme2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.theme_btn.setIcon(icon8)
        self.theme_btn.setIconSize(QtCore.QSize(50, 50))
        self.theme_btn.setObjectName("theme_btn")
        self.theme_btn.clicked.connect(lambda:self.theme_combo.show())
        
        #ABOUT BUTTON
        self.about_btn = QtWidgets.QPushButton(self.centralwidget)
        self.about_btn.setGeometry(QtCore.QRect(30, 120, 61, 61))
        self.about_btn.setStyleSheet("QPushButton{background-color: rgb(180, 225, 218);\
             }QPushButton::hover{background-color : lightgreen;}")
        self.about_btn.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/about2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.about_btn.setIcon(icon9)
        self.about_btn.setIconSize(QtCore.QSize(50, 50))
        self.about_btn.setFlat(False)
        self.about_btn.setObjectName("about_btn")
        #self.about_btn.clicked.connect(self.detect)
        
        
        self.background_label.raise_()
        self.content_frame.raise_()
        self.title_frame.raise_()
        self.button_frame.raise_()
        self.search_frame.raise_()
        self.header_frame.raise_()
        self.about_btn.raise_()
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionAdd_New = QtWidgets.QAction(MainWindow)
        self.actionAdd_New.setObjectName("actionAdd_New")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "The Lazy Reader"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Select Story"))

        self.type_label.setText(_translate("MainWindow", "Type or Paste your text below"))
        self.title_edit.setToolTip(_translate("MainWindow", "Title"))
        self.title_label.setText(_translate("MainWindow", "title:"))
        self.add_btn.setToolTip(_translate("MainWindow", "Add New Story"))
        self.exit_btn.setToolTip(_translate("MainWindow", "Exit"))
        self.play_btn.setToolTip(_translate("MainWindow", "Listen"))
        self.save_btn.setToolTip(_translate("MainWindow", "Save"))
        self.delete_btn.setToolTip(_translate("MainWindow", "Delete"))
        self.clear_btn.setToolTip(_translate("MainWindow", "Clear Field"))
        self.lang_combo.setToolTip(_translate("MainWindow", "Choose your Language"))
        self.choose_lang_label.setText(_translate("MainWindow", "Choose your Language"))
        self.search_edit.setToolTip(_translate("MainWindow", "Enter Ttile"))
        self.search_btn.setToolTip(_translate("MainWindow", "Search"))
        self.thelazy_label.setText(_translate("MainWindow", "The Lazy Reader"))
        self.makefun_label.setText(_translate("MainWindow", 'Children\'s stories'))
        self.theme_btn.setToolTip(_translate("MainWindow", "Themes"))
        self.about_btn.setToolTip(_translate("MainWindow", "About"))
        self.update_btn.setToolTip(_translate("MainWindow", "Update"))
        self.cancel_btn.setToolTip(_translate("MainWindow", "Cancel"))
        self.actionAdd_New.setText(_translate("MainWindow", "Add New"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
