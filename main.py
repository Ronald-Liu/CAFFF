import display
import logic
import time

def main(aType, interval):
	world = logic.loadWorld(aType)
	display.load(world.vision())
	while True:
		world.iterate()
		if world.status() == logic.DEAD:
			print 'Your world is dead'
			return
		display.refresh(world.vision(), world.status())
		time.sleep(interval)

if __name__=="__main__":
	main('a', 1)