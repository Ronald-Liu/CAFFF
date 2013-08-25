from PyQt4 import QtGui, QtCore
import sys

class displayPanel(QtGui.QWidget):
	def __init__(self, aType, iterateStep, interval):
		QtGui.QWidget.__init__(self, None)
	
		self.aType = aType		
		self.iterateStepFunc = iterateStep
	
		self.cTimer = QtCore.QTimer()
		QtCore.QObject.connect(self.cTimer, QtCore.SIGNAL("timeout()"), self.iterateStep)
		self.cTimer.setInterval(interval)
		self.map = None
		self.status = ''
		self.cTimer.start()
	
	def start(self):
		self.cTimer.start()

	def paintEvent(self, event):
		qp = QtGui.QPainter()
		qp.begin(self)
		qp.drawText(QtCore.QPoint(0,10), self.aType)
		qp.drawText(QtCore.QPoint(0,20), self.status)
		print self.status
		qp.end()

	def iterateStep(self):
		self.iterateStepFunc(self)

	def refresh(self, vmap, status):
		self.mapw, self.maph, self.mmap = vmap
		self.status = status
		self.repaint()
def iterateStep(obj):
	obj.refresh((0,0,None), '123')

if __name__=="__main__":
	app = QtGui.QApplication(sys.argv)
	widget = displayPanel('a', iterateStep, 300)
	widget.show()
	sys.exit(app.exec_())