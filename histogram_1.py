
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'histogram_1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
from cmath import rect

from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtCore.QTextCodec import kwargs
from PyQt5.QtWidgets import QWidget
# from matplotlib.backends.backend_qt5agg import FigureCanvas
from bokeh.plotting import Figure
from boto.ec2.elb import listener
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QDialog, QFileDialog
import threading
from threading import Thread
from PyQt5.QtWidgets import *
import numpy as np
from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap, QImage
from matplotlib.figure import Figure
import numpy
import multiprocessing
import cv2
from time import sleep


# Global Thread Decalrations

# class Ui_MainWindow(QWidget):
# def setupUi(self, MainWindow):
# from main_histogram import Ui_MainWindow


class Display_Histogram(QMainWindow):
    def setupUi(self, MainWindow):
        QMainWindow.__init__(self)
        # loadUi("histogram_1.ui",self)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pbImage = QtWidgets.QPushButton(self.centralwidget)
        self.pbImage.setGeometry(QtCore.QRect(130, 270, 75, 23))
        self.pbImage.setObjectName("pbImage")
        # self.t1 = Thread(target=ui.display_histogram)

        # self.pbImage.clicked.connect(self.t1.start)

        # self.pbImage.clicked.connect(self.t2.start)
        self.pbImage.clicked.connect(self.start_1)

        self.labelImage = QtWidgets.QLabel(self.centralwidget)
        self.labelImage.setGeometry(QtCore.QRect(40, 50, 311, 191))
        self.labelImage.setObjectName("labelImage")
        self.widgetDisplay = newHistogram(self.centralwidget)
        self.widgetDisplay.setGeometry(QtCore.QRect(369, 49, 351, 191))
        self.widgetDisplay.setObjectName("widgetDisplay")
        # self.widgetDisplay.canvas.draw()
        self.labelFilter = QtWidgets.QLabel(self.centralwidget)
        self.labelFilter.setGeometry(QtCore.QRect(30, 310, 311, 191))
        self.labelFilter.setObjectName("labelFilter")
        self.widgetDisplay2 = newHistogram(self.centralwidget)
        self.widgetDisplay2.setGeometry(QtCore.QRect(380, 320, 351, 191))
        self.widgetDisplay2.setObjectName("widgetDisplay2")
        self.pbFilter = QtWidgets.QPushButton(self.centralwidget)
        self.pbFilter.setGeometry(QtCore.QRect(130, 520, 75, 23))
        self.pbFilter.setObjectName("pbFilter")
        # self.pbFilter.clicked.connect(QtCore.QCoreApplication.instance().quit)
        # self.pbFilter.clicked.connect(self.t2.stop)
        # self.pbFilter.clicked.connect(self.stop)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # sleep(0.2)
        print("ui_thread created")
        if (self.pbImage.clicked):
            self.pbImage.clicked.connect(self.start_1)

        ########

    '''def onclick(self):

        self.t1.start()
        print("Hist Thread")'''

    # self.widgetDisplay.canvas.show()
    # f, axarr = plt.subplots(2, 2)

    # axarr[0, 1] = plt.show()
    # self.labelImage.setPixmap(pixmap)
    # self.labelImage.setScaledContents(True);

    # self.widgetDisplay.canvas.draw()

    '''def filter_histogram(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'd:\\', "Image Files (*.jpg *.gif *.bmp *.png *.tiff)")
        read_img = cv2.imread(fname[0], cv2.IMREAD_COLOR)

        # To filter image using kernel 5x5
        kernel_5x5 = np.ones((5, 5), np.float32) / 25.0
        output = cv2.filter2D(read_img, -1, kernel_5x5)

        # To convert back from BGR to RGB space color
        cv2.cvtColor(output, cv2.COLOR_BGR2RGB, output)

        # To display image in label widget
        height, width, channel = output.shape
        bytesPerLine = 3 * width
        qImg = QImage(output.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        self.labelFilter.setPixmap(pixmap)
        self.labelFilter.setScaledContents(True);

        #self.widgetDisplay2.canvas.axes1.clear()
        color = ('b', 'g', 'r')
        for i, col in enumerate(color):
            histr = cv2.calcHist([output], [i], None, [256], [0, 256])
            self.widgetDisplay2.canvas.axes1.plot(histr, color=col, linewidth=3.0)
            self.widgetDisplay2.canvas.axes1.set_ylabel('Y', color='blue')
            self.widgetDisplay2.canvas.axes1.set_xlabel('X', color='blue')
            self.widgetDisplay2.canvas.axes1.set_title('Histogram of Filtered Image')
            self.widgetDisplay2.canvas.axes1.set_facecolor('xkcd:wheat')
            self.widgetDisplay2.canvas.axes1.grid()
        self.widgetDisplay2.canvas.draw()'''

    '''def start(self):



        display_thread = Display_Histogram(self)
        display_thread.start()'''

    '''def stop(self):
        "Finishes the video recording therefore the thread too"
        if self.open:
            self.open = False



            #self.display_histogram.terminate()
        cv2.destroyAllWindows()'''

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pbImage.setText(_translate("MainWindow", "Read Image"))
        self.labelImage.setText(_translate("MainWindow", "TextLabel"))
        self.labelFilter.setText(_translate("MainWindow", "TextLabel"))
        self.pbFilter.setText(_translate("MainWindow", "stop"))

    def start(self):
        "Launches the video recording function using a thread"
        ui_thread = threading.Thread(target=self.setupUi)
        ui_thread.start()
        # self.start_1()

    def start_1(self):
        "Launches the video recording function using a thread"
        global histogram_thread

        histogram_thread = threading.Thread(target=display_histogram_class.display_histogram)
        histogram_thread.start()
        # histogram_thread = Display_Histogram()
        # self.pbImage.clicked.connect(histogram_thread.start)
        # self.pbImage.clicked.connect(display_histogram_class.start)


class display_histogram_class():
    def display_histogram(self):

        global fname
        fname = QFileDialog.getOpenFileName(Display_Histogram, 'Open file', 'd:\\',
                                            "Image Files (*.jpg *.gif *.bmp *.png *.tiff)")
        pixmap = QPixmap(fname[0])
        Display_Histogram(QMainWindow).labelImage.setPixmap(pixmap)
        Display_Histogram(QMainWindow).labelImage.setScaledContents(True);

        Display_Histogram(QMainWindow).widgetDisplay.canvas.axes1.clear()
        read_img = cv2.imread(fname[0], cv2.IMREAD_COLOR)
        color = ('b', 'g', 'r')
        for i, col in enumerate(color):
            histr = cv2.calcHist([read_img], [i], None, [256], [0, 256])

            Display_Histogram(QMainWindow).widgetDisplay.canvas.axes1.plot(histr, color=col, linewidth=3.0)
            Display_Histogram(QMainWindow).widgetDisplay.canvas.axes1.set_ylabel('Y', color='blue')
            Display_Histogram(QMainWindow).widgetDisplay.canvas.axes1.set_xlabel('X', color='blue')
            Display_Histogram(QMainWindow).widgetDisplay.canvas.axes1.set_title('Histogram')
            Display_Histogram(QMainWindow).widgetDisplay.canvas.axes1.set_facecolor('xkcd:wheat')
            Display_Histogram(QMainWindow).widgetDisplay.canvas.axes1.grid()
        Display_Histogram(QMainWindow).widgetDisplay.canvas.draw()
        read_img = cv2.imread(fname[0], cv2.IMREAD_COLOR)

        # To filter image using kernel 5x5
        kernel_5x5 = np.ones((5, 5), np.float32) / 25.0
        output = cv2.filter2D(read_img, -1, kernel_5x5)
        cv2.cvtColor(output, cv2.COLOR_BGR2RGB, output)

        # To display image in label widget
        height, width, channel = output.shape
        bytesPerLine = 3 * width
        qImg = QImage(output.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        Display_Histogram(QMainWindow).labelFilter.setPixmap(pixmap)
        Display_Histogram(QMainWindow).labelFilter.setScaledContents(True);

        # self.widgetDisplay2.canvas.axes1.clear()
        color = ('b', 'g', 'r')
        for i, col in enumerate(color):
            histr = cv2.calcHist([output], [i], None, [256], [0, 256])
            Display_Histogram(QMainWindow).widgetDisplay2.canvas.axes1.plot(histr, color=col, linewidth=3.0)
            Display_Histogram(QMainWindow).widgetDisplay2.canvas.axes1.set_ylabel('Y', color='blue')
            Display_Histogram(QMainWindow).widgetDisplay2.canvas.axes1.set_xlabel('X', color='blue')
            Display_Histogram(QMainWindow).widgetDisplay2.canvas.axes1.set_title('Histogram of Filtered Image')
            Display_Histogram(QMainWindow).widgetDisplay2.canvas.axes1.set_facecolor('xkcd:wheat')
            Display_Histogram(QMainWindow).widgetDisplay2.canvas.axes1.grid()
        Display_Histogram(QMainWindow).widgetDisplay2.canvas.draw()
        sleep(0.2)
        print("hist_thread_created")

    '''def start(self):
        "Launches the video recording function using a thread"
        histogram_thread = threading.Thread(target=self.display_histogram)
        histogram_thread.start()'''


def start_Thread():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Display_Histogram()
    ui.setupUi(MainWindow)
    MainWindow.show()
    global ui_thread
    global histogram_thread

    ui_thread = Display_Histogram()
    ui_thread.start()
    # histogram_thread = display_histogram_class()

    # self.pbImage.clicked.connect(display_histogram_class.display_histogram)

    # audio_thread = AudioRecorder(name)
    # audio_thread.start()
    sys.exit(app.exec_())


from Histogram import newHistogram


def evnt_handle1():
    # Start Button
    print("Event Handling")
    # Start A Img Thread


def evnt_handle2():
    # Stop Buttopn
    print("Event Handling")
    t1.strat()
    # Stop A Img Thread


def evnt_handle2():
    # Img Processing Done
    # Update UI Event Rise
    ent_tmp.rise()


'''def main():
    import sys
    #ent_tmp = Qevent()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Display_Histogram()


    t2 = Thread(target=ui.setupUi(MainWindow))
    t2.start()
    MainWindow.show()

    MainWindow.pbImage.clicked.connect(start_AVrecording)





    sys.exit(app.exec_())'''

# ex = Display_Histogram()
# ex.show()
# sys.exit(app.exec_())

'''
if __name__ == "__main__":
    main()
'''
'''

if __name__ == "__main__":
    import sys

    # ent_tmp = Qevent()
    ui = Display_Histogram()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    #t1 = Thread(target=ui.display_histogram)
    # ent_tmp.connect(MainWindow.updateUI_Fun)
    #MainWindow.pbFilter.clicked.connect(t1)

    ui.setupUi(MainWindow)
    t2 = Thread(target=ui.setupUi(MainWindow))
    t2.start()

    # t2.join()
    # Thread(target=ui.setupUi, args=[MainWindow]).start()

    MainWindow.show()
    sys.exit(app.exec_())
    # t2 = Thread(target=ui.setupUi(MainWindow))
    # t2.start()

    # MainWindow.show()
    # ui.pbImage.clicked.connect(start_AVrecording'''


def main():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Display_Histogram()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # Display_Histogram(QMainWindow).pbImage.clicked.connect(Display_Histogram.start)
    start_Thread()

    # main()
    # sys.exit(app.exec_())


if __name__ == '__main__':
    start_Thread()

    '''app = QApplication(sys.argv)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Display_Histogram()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()


    MainWindow.main()

    #####
    app = QApplication(sys.argv)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    MainWindow.show()

    sys.exit(app.exec_())'''