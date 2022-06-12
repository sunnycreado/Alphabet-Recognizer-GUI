from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QFileDialog
import sys
from PyQt5.QtGui import QPixmap
from matplotlib.image import  imread
import numpy as np
import tensorflow.keras.models
from PIL import Image
model = tensorflow.keras.models.load_model(r'font.h5')

a=[]



class Receipt(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = None
        self.load_ui()



    def load_ui(self):
        self.ui = loadUi('Character_recognition.ui', self)
        self.upload_button = self.findChild(QPushButton, "upload_button")
        self.predict_button = self.findChild(QPushButton, "predict")
        self.label = self.findChild(QLabel, "label")
        # Dropdown
        self.upload_button.clicked.connect(self.clicker)
        self.predict_button.clicked.connect(self.clicked_btn)


        self.show()

    def clicker(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "C:\\",
                                            "All Files (*);;PNG Files(*.png);;Jpg Files(*.jpg)")

        # Open Image
        self.pixmap = QPixmap(fname[0])
        # Add pic to label
        self.label.setPixmap(self.pixmap)
        global a
#        a = cv2.imread(fname[0])
        a=fname[0]



    def clicked_btn(self,clicker):
        classes = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L',
                   12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W',
                   23: 'X', 24: 'Y', 25: 'Z'}

        global a
        if len(a)==0:
            self.label_2.setText("Upload an Image")

        else:
            self.label_2.setText("Upload an Image first")

#            img_copy = a.copy()
#            img = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
#            img = cv2.resize(img, (400, 440))
#            img_copy = cv2.GaussianBlur(img_copy, (7, 7), 0)
#            img_gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
#            _, img_thresh = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY_INV)
#            img_final = cv2.resize(img_thresh, (28, 28))
#            img_final = np.reshape(img_final, (1, 28, 28, 1))
#            img_pred = classes[np.argmax(model.predict(img_final))]
#            a = img_pred

            img = Image.open(a)
            new_img = img.resize((28, 28), Image.Resampling.LANCZOS)
            finalImageNotProcessed = new_img.convert('L')
            finalImageProcessed=np.array(finalImageNotProcessed).reshape((1,28,28,1))
            img_pred = classes[np.argmax(model.predict(finalImageProcessed))]
            b = img_pred
            self.label_2.setText("Predicted Value:  {}".format(b))




app = QApplication(sys.argv)
receipt = Receipt()
sys.exit(app.exec_())