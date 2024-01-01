from PyQt5 import QtWidgets
import sys
from MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog,QMessageBox,QApplication

#my modules
import downloadmp4
import downloadmp3

#ekstralar
import os
from pathlib import Path

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnSearch.clicked.connect(self.showPathDialog)
        self.ui.btnDownload.clicked.connect(self.downloadYT)
        self.ui.radioBtnMP3.setChecked(True)
        self.ui.radioBtnMP4.setChecked(False)
        self.ui.QualityWidget.hide()


        self.ui.radioBtnMP3.clicked.connect(self.hideQualitySettings)
        self.ui.radioBtnMP4.clicked.connect(self.showQualitySettings)

        self.ui.tbxOutput.setText(self.get_downloads_folder())
    


    def showPathDialog(self):
        # Klasör seçme penceresini aç
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, 'Klasör Seç', '')

        # Seçilen klasörün yolunu LineEdit'e yaz
        if directory:
            self.ui.tbxOutput.setText(directory)

    def downloadYT(self):
        if(self.ui.radioBtnMP3.isChecked()):
            print("mp3teyiz")
            try:               
                downloadmp3.download_mp3(self.ui.tbxUrl.text(),self.ui.tbxOutput.text())
                self.showSuccess()
            except Exception as e:
                self.showError()
            
        elif(self.ui.radioBtnMP4.isChecked()):
            print("mp4teyiz")
            try:
                downloadmp4.download_mp4(self.ui.tbxUrl.text(),self.ui.tbxOutput.text(),self.ui.cbxQuality.currentText())
                self.showSuccess()
            except Exception as e:
                self.showError()
                
        else:
            print("elsedeyiz")
            self.showError()
        
    def showSuccess(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("İndirme işlemi tamamlandı!")
        msgBox.setWindowTitle("Başarılı!")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()

    def showError(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("Bir hata oluştu! Lütfen tekrar deneyiniz.")
        msgBox.setWindowTitle("Hata")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()

    def showQualitySettings(self):
        self.ui.QualityWidget.show()
    def hideQualitySettings(self):
        self.ui.QualityWidget.hide()


    def get_downloads_folder(self):
        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        return downloads_folder


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())


app()