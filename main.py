import display
import logic
import time,sys
from PyQt4 import QtGui
world = None
def main(aType, interval):
	global world
	world = logic.loadWorld(aType)
	app = QtGui.QApplication(sys.argv)
	widget = display.displayPanel(aType, iterateStep, interval)
	widget.refresh(world.vision(),world.status)
	widget.show()

	sys.exit(app.exec_())

def iterateStep(obj):
	global world
	world.iterate()
	if world.status == 'DEAD':
		print 'Your world is dead'
		return
	obj.refresh(world.vision(), world.status)

if __name__=="__main__":
	main('a', 100)