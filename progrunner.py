import sys
from PyQt5.QtWidgets import QDialog, QApplication
from GUI import *
from sklearn.externals import joblib

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.b1.clicked.connect(self.predictions)
        self.show()
    def predictions(self):
        final = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        #PARENTS
        if(self.ui.p1.isChecked()):
            final[2] = 1
        elif(self.ui.p2.isChecked()):
            final[1] = 1
        elif(self.ui.p3.isChecked()):
            final[0] = 1
        #HAS NURS
        if(self.ui.n1.isChecked()):
            final[6] = 1
        elif(self.ui.n2.isChecked()):
            final[5] = 1
        elif(self.ui.n3.isChecked()):
            final[4] = 1
        elif(self.ui.n4.isChecked()):
            final[3] = 1
        elif(self.ui.n5.isChecked()):
            final[7] = 1
        #FORMS
        if(self.ui.f1.isChecked()):
            final[8] = 1
        elif(self.ui.f2.isChecked()):
            final[9] = 1
        elif(self.ui.f3.isChecked()):
            final[11] = 1
        elif(self.ui.f4.isChecked()):
            final[10] = 1
        #No. OF CHILDREN
        if(self.ui.c1.isChecked()):
            final[12] = 1
        elif(self.ui.c2.isChecked()):
            final[13] = 1
        elif(self.ui.c3.isChecked()):
            final[14] = 1
        elif(self.ui.c4.isChecked()):
            final[15] = 1
        #HOUSING
        if(self.ui.h1.isChecked()):
            final[16] = 1
        elif(self.ui.h2.isChecked()):
            final[18] = 1
        elif(self.ui.h3.isChecked()):
            final[17] = 1
        #FINANCE
        if(self.ui.fi1.isChecked()):
            final[19] = 1
        elif(self.ui.fi2.isChecked()):
            final[20] = 1
        #Social
        if(self.ui.s1.isChecked()):
            final[21] = 1
        elif(self.ui.s2.isChecked()):
            final[23] = 1
        elif(self.ui.s3.isChecked()):
            final[22] = 1
        #HEALTH
        if(self.ui.he1.isChecked()):
            final[26] = 1
        elif(self.ui.he2.isChecked()):
            final[25] = 1
        elif(self.ui.he3.isChecked()):
            final[24] = 1
        dtree = joblib.load("dtree.sav")
        res = dtree.predict([final])
        prob = dtree.predict_log_proba([final])
        self.ui.res.setText(res[0])
if __name__=="__main__":   
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
