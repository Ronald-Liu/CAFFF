from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
import sys

class displayPanel(QtGui.QWidget):
	def __init__(self, aType, iterateStep, interval):
		QtGui.QWidget.__init__(self, None)
	
		self.scene = QtGui.QGraphicsScene(self)
		self.view = QtGui.QGraphicsView(self.scene)
		self.startBtn=QtGui.QPushButton("Start")
		self.startBtn.clicked.connect(self.start)

		self.layout = QtGui.QGridLayout()
		self.layout.addWidget(self.view)
		self.layout.addWidget(self.startBtn)
		self.setLayout(self.layout)

		self.aType = aType		
		self.iterateStepFunc = iterateStep
	
		self.cTimer = QtCore.QTimer()
		QtCore.QObject.connect(self.cTimer, QtCore.SIGNAL("timeout()"), self.iterateStep)
		self.cTimer.setInterval(interval)
		self.mmap = None
		self.mapRange = None
		self.status = ''
		self.windowRect = None
	
	def start(self):
		self.cTimer.start()

	def iterateStep(self):
		self.iterateStepFunc(self)

	def refresh(self, vmap, status):
		self.mapRange, self.mmap = vmap
		self.status = status
		self.scene.clear()
		for i in self.mmap:
			self.scene.addRect(i[0]*20,i[1]*20,20,20)
			print i[0],i[1]

def iterateStep(obj):
	obj.refresh(((-10,10,-10,10),((-10,-10),(-9,0),(-8,0),(10,10))), '123')

if __name__=="__main__":
	app = QtGui.QApplication(sys.argv)
	widget = displayPanel('a', iterateStep, 300)
	widget.show()
	widget.start()
	sys.exit(app.exec_())