def getX(x):
	return x[0]
def getY(x):
	return x[1]
class gameOfLife(object):
	'''
	'''
	def load(self, argv):
		self.cellSet = set(argv)
		self.status = 'RUNNING'
		
		self.mapRange = (min(self.cellSet, key=getX)[0],max(self.cellSet, key=getX)[0],
			min(self.cellSet, key=getY)[1],max(self.cellSet, key=getY)[1])
	def iterate(self):
		candidList = {}
		
		for cell in self.cellSet:
			for candid in self.Neighbourhood_8(cell):
				if candidList.has_key(candid):
					candidList[candid] += 1
				else:
					candidList[candid] = 1
		cellSetSet = set([])
		cellSetKeep = set([])
		cellSetReset = set([])
		for k,v in candidList.iteritems():
			if v == 3:
				cellSetSet.add(k)
			elif v == 2:
				cellSetKeep.add(k)
			else:
				cellSetReset.add(k)
		self.cellSet = ((self.cellSet & cellSetKeep) | cellSetSet) - cellSetReset
		self.mapRange = (min(self.cellSet, key=getX)[0],max(self.cellSet, key=getX)[0],
			min(self.cellSet, key=getY)[1],max(self.cellSet, key=getY)[1])

	def vision(self):
		return (self.mapRange, self.cellSet)

	def Neighbourhood_8(self, point):
		n8 = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
		for i in n8:
			yield (i[0]+point[0],i[1]+point[1])
		raise StopIteration() 

def loadWorld(path):
	w = gameOfLife()
	w.load([(0,1),(1,2),(2,0),(2,1),(2,2)])
	return w

def testMain():
	world = gameOfLife()
	world.load([(1,1),(1,2),(1,3)])
	for i in xrange(10):
		world.iterate()
		print world.status()
if __name__=="__main__":
	testMain()