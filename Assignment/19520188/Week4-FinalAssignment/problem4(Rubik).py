from sys import stdin, stdout

def rotateClockwise(a, b, c):
  return b, c, a

def Up(rubik):
  rubik[0][0], rubik[2][4], rubik[3][8] = rotateClockwise(rubik[0][0], rubik[2][4], rubik[3][8])
  return rubik

def Up_(rubik):
  rubik[0][0], rubik[3][8], rubik[2][4] = rotateClockwise(rubik[0][0], rubik[3][8], rubik[2][4])
  return rubik

def Bottom(rubik):
  rubik[1][0], rubik[3][4], rubik[2][8] = rotateClockwise(rubik[1][0], rubik[3][4], rubik[2][8])
  return rubik

def Bottom_(rubik):
  rubik[1][0], rubik[2][8], rubik[3][4] = rotateClockwise(rubik[1][0], rubik[2][8], rubik[3][4])
  return rubik

def Left(rubik):
  rubik[2][0], rubik[0][4], rubik[1][8] = rotateClockwise(rubik[2][0], rubik[0][4], rubik[1][8])
  return rubik

def Left_(rubik):
  rubik[2][0], rubik[1][8], rubik[0][4] = rotateClockwise(rubik[2][0], rubik[1][8], rubik[0][4])
  return rubik

def Right(rubik):
  rubik[3][0], rubik[1][4], rubik[0][8] = rotateClockwise(rubik[3][0], rubik[1][4], rubik[0][8])
  return rubik

def Right_(rubik):
  rubik[3][0], rubik[0][8], rubik[1][4] = rotateClockwise(rubik[3][0], rubik[0][8], rubik[1][4])
  return rubik

def Up2(rubik):
  rubik = Up(rubik)
  rubik[0][1], rubik[2][6], rubik[3][3] = rotateClockwise(rubik[0][1], rubik[2][6], rubik[3][3])
  rubik[0][2], rubik[2][5], rubik[3][7] = rotateClockwise(rubik[0][2], rubik[2][5], rubik[3][7])
  rubik[0][3], rubik[2][1], rubik[3][6] = rotateClockwise(rubik[0][3], rubik[2][1], rubik[3][6])
  return rubik

def Up2_(rubik):
  rubik = Up_(rubik)
  rubik[0][1], rubik[3][3], rubik[2][6] = rotateClockwise(rubik[0][1], rubik[3][3], rubik[2][6])
  rubik[0][2], rubik[3][7], rubik[2][5] = rotateClockwise(rubik[0][2], rubik[3][7], rubik[2][5])
  rubik[0][3], rubik[3][6], rubik[2][1] = rotateClockwise(rubik[0][3], rubik[3][6], rubik[2][1])
  return rubik

def Bottom2(rubik):
  rubik = Bottom(rubik)
  rubik[1][1], rubik[3][6], rubik[2][3] = rotateClockwise(rubik[1][1], rubik[3][6], rubik[2][3])
  rubik[1][2], rubik[3][5], rubik[2][7] = rotateClockwise(rubik[1][2], rubik[3][5], rubik[2][7])
  rubik[1][3], rubik[3][1], rubik[2][6] = rotateClockwise(rubik[1][3], rubik[3][1], rubik[2][6])
  return rubik

def Bottom2_(rubik):
  rubik = Bottom_(rubik)
  rubik[1][1], rubik[2][3], rubik[3][6] = rotateClockwise(rubik[1][1], rubik[2][3], rubik[3][6])
  rubik[1][2], rubik[2][7], rubik[3][5] = rotateClockwise(rubik[1][2], rubik[2][7], rubik[3][5])
  rubik[1][3], rubik[2][6], rubik[3][1] = rotateClockwise(rubik[1][3], rubik[2][6], rubik[3][1])  
  return rubik

def Left2(rubik):
  rubik = Left(rubik)
  rubik[2][1], rubik[0][6], rubik[1][3] = rotateClockwise(rubik[2][1], rubik[0][6], rubik[1][3])
  rubik[2][2], rubik[0][5], rubik[1][7] = rotateClockwise(rubik[2][2], rubik[0][5], rubik[1][7])
  rubik[2][3], rubik[0][1], rubik[1][6] = rotateClockwise(rubik[2][3], rubik[0][1], rubik[1][6])
  return rubik

def Left2_(rubik):
  rubik = Left_(rubik)
  rubik[2][1], rubik[1][3], rubik[0][6] = rotateClockwise(rubik[2][1], rubik[1][3], rubik[0][6])
  rubik[2][2], rubik[1][7], rubik[0][5] = rotateClockwise(rubik[2][2], rubik[1][7], rubik[0][5])
  rubik[2][3], rubik[1][6], rubik[0][1] = rotateClockwise(rubik[2][3], rubik[1][6], rubik[0][1])  
  return rubik

def Right2(rubik):
  rubik = Right(rubik)
  rubik[3][1], rubik[1][6], rubik[0][3] = rotateClockwise(rubik[3][1], rubik[1][6], rubik[0][3])
  rubik[3][2], rubik[1][5], rubik[0][7] = rotateClockwise(rubik[3][2], rubik[1][5], rubik[0][7])
  rubik[3][3], rubik[1][1], rubik[0][6] = rotateClockwise(rubik[3][3], rubik[1][1], rubik[0][6])
  return rubik

def Right2_(rubik):
  rubik = Right_(rubik)
  rubik[3][1], rubik[0][3], rubik[1][6] = rotateClockwise(rubik[3][1], rubik[0][3], rubik[1][6])
  rubik[3][2], rubik[0][7], rubik[1][5] = rotateClockwise(rubik[3][2], rubik[0][7], rubik[1][5])
  rubik[3][3], rubik[0][6], rubik[1][1] = rotateClockwise(rubik[3][3], rubik[0][6], rubik[1][1])
  return rubik  

# Driver code
c = [i for i in stdin.readline().split()]
step = [i for i in stdin.readline().split()]
rubik = [ [c[0]]*9, [c[1]]*9, [c[2]]*9, [c[3]]*9]
input()

for i in range(len(step)-1, -1, -1):
  if (step[i] == "U"):
    rubik = Up_(rubik)
  elif (step[i] == "U'"):
    rubik = Up(rubik)
  elif (step[i] == "B"):
    rubik = Bottom_(rubik)
  elif (step[i] == "B'"):
    rubik = Bottom(rubik)
  elif (step[i] == "L"):
    rubik = Left_(rubik)
  elif (step[i] == "L'"):
    rubik = Left(rubik)
  elif (step[i] == "R"):
    rubik = Right_(rubik)
  elif (step[i] == "R'"):
    rubik = Right(rubik)
  elif (step[i] == "u"):
    rubik = Up2_(rubik)
  elif (step[i] == "u'"):
    rubik = Up2(rubik)
  elif (step[i] == "b"):
    rubik = Bottom2_(rubik)
  elif (step[i] == "b'"):
    rubik = Bottom2(rubik)
  elif (step[i] == "l"):
    rubik = Left2_(rubik)
  elif (step[i] == "l'"):
    rubik = Left2(rubik)
  elif (step[i] == "r"):
    rubik = Right2_(rubik)
  elif (step[i] == "r'"):
    rubik = Right2(rubik)

for i in range(4):
    print(*rubik[i], end ='\n')