def MoveLayer1(arg):
    switcher = {
        "U'":[(0, 0), (2, 4), (3, 8)],
		"U": [(0, 0), (3, 8), (2, 4)],
        "B'":[(1, 0), (3, 4), (2, 8)],
		"B": [(1, 0), (2, 8), (3, 4)],
		"L'":[(2, 0), (0, 4), (1, 8)],
		"L": [(2, 0), (1, 8), (0, 4)],
    	"R'":[(3, 0), (1, 4), (0, 8)],
		"R": [(3, 0), (0, 8), (1, 4)]
    }
    return switcher.get(arg)

def MoveLayer2(arg):
	switcher = {
		"u'":[(0, 1), (2, 6), (3, 3),
              (0, 2), (2, 5), (3, 7),
        	  (0, 3), (2, 1), (3, 6)],
		"u": [(0, 1), (3, 3), (2, 6),
			  (0, 2), (3, 7), (2, 5),
			  (0, 3), (3, 6), (2, 1)],
        "b'":[(1, 1), (3, 6), (2, 3),
              (1, 2), (3, 5), (2, 7),
              (1, 3), (3, 1), (2, 6)],
		"b": [(1, 1), (2, 3), (3, 6),
			  (1, 2), (2, 7), (3, 5),
 			  (1, 3), (2, 6), (3, 1)],
        "l'":[(2, 1), (0, 6), (1, 3),
              (2, 2), (0, 5), (1, 7),
              (2, 3), (0, 1), (1, 6)],
        "l": [(2, 1), (1, 3), (0, 6),
			  (2, 2), (1, 7), (0, 5),
		 	  (2, 3), (1, 6), (0, 1)],        
        "r'":[(3, 1), (1, 6), (0, 3),
              (3, 2), (1, 5), (0, 7),
              (3, 3), (1, 1), (0, 6)],
		"r": [(3, 1), (0, 3), (1, 6),
			  (3, 2), (0, 7), (1, 5),
			  (3, 3), (0, 6), (1, 1)]
    }
	return switcher.get(arg)


Type1 = {"U", "B", "L", "R", "U'", "B'", "L'", "R'"}
Type2 = {"u", "b", "l", "r", "u'", "b'", "l'", "r'"}

def Swap(a, b, c):
	return b, c, a

def SolveRubik(rubik, move):
	dim = []
	for k in range(len(move)-1, -1, -1):
		if move[k] in Type1:
			dim = MoveLayer1(move[k])
			rubik[dim[0][0]][dim[0][1]], rubik[dim[1][0]][dim[1][1]], rubik[dim[2][0]][dim[2][1]] \
				= Swap(rubik[dim[0][0]][dim[0][1]], rubik[dim[1][0]][dim[1][1]], rubik[dim[2][0]][dim[2][1]])
		else:
			dim = MoveLayer1(move[k].upper())
			rubik[dim[0][0]][dim[0][1]], rubik[dim[1][0]][dim[1][1]], rubik[dim[2][0]][dim[2][1]] \
				= Swap(rubik[dim[0][0]][dim[0][1]], rubik[dim[1][0]][dim[1][1]], rubik[dim[2][0]][dim[2][1]])

			dim = MoveLayer2(move[k])
			for i in range(0, 8, 3):
				rubik[dim[i][0]][dim[i][1]], rubik[dim[i+1][0]][dim[i+1][1]], rubik[dim[i+2][0]][dim[i+2][1]] \
					= Swap(rubik[dim[i][0]][dim[i][1]], rubik[dim[i+1][0]][dim[i+1][1]], rubik[dim[i+2][0]][dim[i+2][1]])
	return rubik
		
side = [i for i in input().split()]
move = [i for i in input().split()]
rubik = [[c] * 9 for c in side]

rubik = SolveRubik(rubik, move)
for i in range(4):
	print(*rubik[i], end = '\n')