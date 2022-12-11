from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QProgressBar
import os
import time
import datetime

# GUI dosyasını yükle
UIClass, UIWidget = uic.loadUiType("RTLGUINEW_LATEST.ui")

# GUI'ye fonksiyonellik kazandıran class
class GUIFunction(UIWidget,UIClass):
    #Değişkenler
    CenterFreq = 24000000
    Bw = 2400000
    Dur = 15

    # Buton fonksiyonları
    def __init__(self,width,height):
        super(GUIFunction,self).__init__()
        self.setFixedSize(width,height)
        self.setupUi(self)
        #slider
        self.horizontalSlider.valueChanged.connect(self.updateFreq)
        #radio buttons
        self.radioButton.setChecked(True)
        self.radioButton_4.setChecked(True)
        # HPT için Kayıt seçme butonu fonksiyonu
        self.stackedWidget.setCurrentWidget(self.page_2)
        self.toolButton.clicked.connect(self.wbfmFunction)
        self.toolButton_2.clicked.connect(self.nbfmFunction)
        self.toolButton_3.clicked.connect(self.ismFunction)
        self.toolButton_4.clicked.connect(self.adsbFunction)
        self.toolButton_5.clicked.connect(self.recordFunction)
        self.pushButton.clicked.connect(self.startRecord)
        self.pushButton_2.clicked.connect(self.returnMain)
        self.radioButton.clicked.connect(self.updateBw1)
        self.radioButton_2.clicked.connect(self.updateBw2)
        self.radioButton_3.clicked.connect(self.updateBw3)
        self.radioButton_4.clicked.connect(self.updateDur1)
        self.radioButton_5.clicked.connect(self.updateDur2)
        self.radioButton_6.clicked.connect(self.updateDur3)

    def updateBw1(self):
        self.Bw = 2400000
    def updateBw2(self):
        self.Bw = 2048000
    def updateBw3(self):
        self.Bw = 1024000

    def updateDur1(self):
        self.Dur = 15
    def updateDur2(self):
        self.Dur = 30
    def updateDur3(self):
        self.Dur = 60



    def sleep5sec(self):
        self.toolButton.setEnabled(False)
        self.toolButton_2.setEnabled(False)
        self.toolButton_3.setEnabled(False)
        self.toolButton_4.setEnabled(False)
        self.toolButton_5.setEnabled(False)
        QTimer.singleShot(5000,lambda:self.toolButton.setDisabled(False))
        QTimer.singleShot(5000, lambda: self.toolButton_2.setDisabled(False))
        QTimer.singleShot(5000, lambda: self.toolButton_3.setDisabled(False))
        QTimer.singleShot(5000, lambda: self.toolButton_4.setDisabled(False))
        QTimer.singleShot(5000, lambda: self.toolButton_5.setDisabled(False))
    def progress(self,val):
        self.progressBar.setValue(val)


    def updateFreq(self,value):
        self.label_8.setText(str(value) + " MHz")
        CenterFreq = value * 1000000
    #DEmodülasyon için mod tipi seçimi
    def wbfmFunction(self):
        self.sleep5sec()
        self.worker = wideFmThread()
        self.worker.start()
    def nbfmFunction(self):
        self.sleep5sec()
        self.worker = narrowFmThread()
        self.worker.start()
    def ismFunction(self):
        self.sleep5sec()
        self.worker = ismThread()
        self.worker.start()
    def adsbFunction(self):
        self.sleep5sec()
        self.worker = adsbThread()
        self.worker.start()
    def recordFunction(self):
        self.stackedWidget.setCurrentWidget(self.page)
    def startRecord(self):
        self.pushButton.setEnabled(False)
        QTimer.singleShot(self.Dur*1000,lambda:self.pushButton.setDisabled(False))
        self.progThread = updateProgress()
        self.progThread.durationSet(self.Dur)
        self.progThread.progVal.connect(self.progress)
        self.progThread.start()
        self.worker = workerThread()
        self.worker.durationSet(self.Dur)
        self.worker.BwSet(self.Bw)
        self.worker.freqSet(self.CenterFreq)
        self.worker.start()
        # self.worker.finished.connect(self.workerFinished)
    def returnMain(self):
        self.stackedWidget.setCurrentWidget(self.page_2)

class updateProgress(QThread):
    Dur = 0
    def durationSet(self,Dur):
        self.Dur = Dur
    progVal = pyqtSignal(int)
    def run(self):
        # self.progVal.emit(90)
        for i in range(100):
            time.sleep(self.Dur/100)
            self.progVal.emit(i+1)


# #Bu class Qthread classını inherit eder ve veri gönderme işlerini GUI'den ayrı bir threadde gerçekleştirir.
class workerThread(QThread):
    Dur = 0
    Bw = 0
    CenterFreq = 0
    def durationSet(self,Dur):
        self.Dur = Dur
    def BwSet(self,Bw):
        self.Bw = Bw
    def freqSet(self,CenterFreq):
        self.CenterFreq = CenterFreq

    def run(self):
        filename = ""
        current_time = datetime.datetime.now()
        current_date = current_time.date()
        current_clock = current_time.time()
        filename = str(current_date) + "_" + str(current_clock) + "_" + str(self.CenterFreq) + "_" + str(self.Bw) + ".cu8"
        cmdMsg = "rtl_sdr -f " + str(self.CenterFreq) + " -s " + str(self.Bw) + " -n " + str(self.Dur * self.Bw) + filename
        os.system(cmdMsg)

class narrowFmThread(QThread):
    def run(self):
        os.system("gqrx -c narrowConf.conf")
class wideFmThread(QThread):
    def run(self):
        os.system("gqrx -c wideConf.conf")
class ismThread(QThread):
    def run(self):
        os.system("gqrx -c ismConf.conf")
class adsbThread(QThread):
    def run(self):
        print("empty")
    #24 MHz- 1700 MHz
    # Değişkenler
    # Fonksiyonlar
    # Bu fonksiyon

# Main function
if __name__ == "__main__":
    import sys
    print('----------LOG----------')
    app = QtWidgets.QApplication(sys.argv)
    screen = app.primaryScreen()
    size = screen.size()
    print(size.width())
    print(size.height())
    MainWindow = QtWidgets.QMainWindow()
    ui = GUIFunction(size.width(),size.height())
    ui.showFullScreen()
    sys.exit(app.exec_())
