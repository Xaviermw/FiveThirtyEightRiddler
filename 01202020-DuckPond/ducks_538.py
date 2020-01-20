import random

class Location:

	def __init__(self, row, col):
		self.row = row
		self.col = col

class Spot:

	adjacent_spots = None

	def __init__(self, i, j):
		self.location = Location(i, j)

	def getRandomNeighbor(self):
		return self.adjacent_spots[random.randint(0, len(self.adjacent_spots)-1)]

class Duck:

	def __init__(self, id):
		self.id = id

	def move(self):
		self.spot = self.spot.getRandomNeighbor()

class Pond:

	def __init__(self, rows, cols, num_ducks):
		self.rows = rows
		self.cols = cols
		self.ducks = [Duck(i+1) for i in range(num_ducks)]
		self.layout = [[Spot(i, j) for j in range(cols)] for i in range(rows)]
		self.pond_age = 0 

	def setStartingPosition(self, row, col):
		self.startingPosition = self.layout[row][col]
		for duck in self.ducks:
			duck.spot = self.startingPosition

	def initializeAdjacencies(self):
		for i in range(self.rows):
			for j in range(self.cols):
				neighbors = []
				if (i != 0):
					neighbors.append(self.layout[i-1][j])
				if (i != self.rows-1):
					neighbors.append(self.layout[i+1][j])
				if (j != 0):
					neighbors.append(self.layout[i][j-1])
				if (j != self.cols-1):
					neighbors.append(self.layout[i][j+1])
				self.layout[i][j].adjacent_spots = neighbors

	def move(self):
		for duck in self.ducks:
			duck.move()
		self.pond_age = self.pond_age + 1

	def checkIfSameSpot(self):
		same_spot = True
		firstSpot = self.ducks[0].spot
		for duck in self.ducks:
			if duck.spot != firstSpot:
				same_spot = False
		return same_spot


POND_ROWS = 3
POND_COLS = 3
STARTING_ROW = 1
STARTING_COL = 1
DUCKS = 2
SIMS = 100000

age = 0
for i in range(SIMS):
	pond = Pond(POND_ROWS, POND_COLS, DUCKS)
	pond.initializeAdjacencies()
	pond.setStartingPosition(STARTING_ROW, STARTING_COL)
	same_spot = False
	while(same_spot == False):
		pond.move()
		same_spot = pond.checkIfSameSpot()
		print(pond.pond_age)
	age = age + pond.pond_age
	print("End Pond Age: " + str(pond.pond_age))

print("Average Age: " + str(age/SIMS))



