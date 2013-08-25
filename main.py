import display
import logic
import time
from PyQt4 import QtGui

def main(aType, interval):
	world = logic.loadWorld(aType)
	app = QtGui.QApplication(sys.argv)
	widget = display.displayPanel(aType, iterateStep, interval)
	widget.show()

	sys.exit(app.exec_())

def iterateStep(obj):
	world.iterate()
	if world.status() == logic.DEAD:
		print 'Your world is dead'
		return
	obj.refresh(world.vision(), world.status())

if __name__=="__main__":
	main('a', 1)