import display
import logic
import time
world = None
def main(aType, interval):
	world = logic.loadWorld(aType)
	display.load(iterateStep)

def iterateStep():
	world.iterate()
	if world.status() == logic.DEAD:
		print 'Your world is dead'
		return
	display.refresh(world.vision(), world.status())

if __name__=="__main__":
	main('a', 1)