# Link tham khảo: https://codereview.stackexchange.com/questions/197287/codefights-pyraminx-puzzle

from sys import stdin

face_color = [i for i in stdin.readline().split()]
move = [i for i in stdin.readline().split()]
end = input()
move.reverse()


class Pyraminx:
    def __init__(self):
        self.pyraminx = [[i] * 9 for i in face_color]

    def U_(self):
        self.pyraminx[0][0], self.pyraminx[2][4], self.pyraminx[3][8] = (
        self.pyraminx[2][4], self.pyraminx[3][8], self.pyraminx[0][0])

    def U(self):
        self.pyraminx[0][0], self.pyraminx[3][8], self.pyraminx[2][4] = (
        self.pyraminx[3][8], self.pyraminx[2][4], self.pyraminx[0][0])

    def B_(self):
        self.pyraminx[1][0], self.pyraminx[3][4], self.pyraminx[2][8] = (
        self.pyraminx[3][4], self.pyraminx[2][8], self.pyraminx[1][0])

    def B(self):
        self.pyraminx[1][0], self.pyraminx[2][8], self.pyraminx[3][4] = (
        self.pyraminx[2][8], self.pyraminx[3][4], self.pyraminx[1][0])

    def L(self):
        self.pyraminx[0][4], self.pyraminx[2][0], self.pyraminx[1][8] = (
        self.pyraminx[2][0], self.pyraminx[1][8], self.pyraminx[0][4])

    def L_(self):
        self.pyraminx[0][4], self.pyraminx[1][8], self.pyraminx[2][0] = (
        self.pyraminx[1][8], self.pyraminx[2][0], self.pyraminx[0][4])

    def R(self):
        self.pyraminx[0][8], self.pyraminx[1][4], self.pyraminx[3][0] = (
        self.pyraminx[1][4], self.pyraminx[3][0], self.pyraminx[0][8])

    def R_(self):
        self.pyraminx[0][8], self.pyraminx[3][0], self.pyraminx[1][4] = (
        self.pyraminx[3][0], self.pyraminx[1][4], self.pyraminx[0][8])

    def u(self):
        self.U()
        self.pyraminx[0][1], self.pyraminx[3][3], self.pyraminx[2][6] = (
        self.pyraminx[3][3], self.pyraminx[2][6], self.pyraminx[0][1])
        self.pyraminx[0][2], self.pyraminx[3][7], self.pyraminx[2][5] = (
        self.pyraminx[3][7], self.pyraminx[2][5], self.pyraminx[0][2])
        self.pyraminx[0][3], self.pyraminx[3][6], self.pyraminx[2][1] = (
        self.pyraminx[3][6], self.pyraminx[2][1], self.pyraminx[0][3])

    def u_(self):
        self.U_()
        self.pyraminx[0][1], self.pyraminx[2][6], self.pyraminx[3][3] = (
        self.pyraminx[2][6], self.pyraminx[3][3], self.pyraminx[0][1])
        self.pyraminx[0][2], self.pyraminx[2][5], self.pyraminx[3][7] = (
        self.pyraminx[2][5], self.pyraminx[3][7], self.pyraminx[0][2])
        self.pyraminx[0][3], self.pyraminx[2][1], self.pyraminx[3][6] = (
        self.pyraminx[2][1], self.pyraminx[3][6], self.pyraminx[0][3])

    def b(self):
        self.B()
        self.pyraminx[1][1], self.pyraminx[2][3], self.pyraminx[3][6] = (
        self.pyraminx[2][3], self.pyraminx[3][6], self.pyraminx[1][1])
        self.pyraminx[1][2], self.pyraminx[2][7], self.pyraminx[3][5] = (
        self.pyraminx[2][7], self.pyraminx[3][5], self.pyraminx[1][2])
        self.pyraminx[1][3], self.pyraminx[2][6], self.pyraminx[3][1] = (
        self.pyraminx[2][6], self.pyraminx[3][1], self.pyraminx[1][3])

    def b_(self):
        self.B_()
        self.pyraminx[1][1], self.pyraminx[3][6], self.pyraminx[2][3] = (
        self.pyraminx[3][6], self.pyraminx[2][3], self.pyraminx[1][1])
        self.pyraminx[1][2], self.pyraminx[3][5], self.pyraminx[2][7] = (
        self.pyraminx[3][5], self.pyraminx[2][7], self.pyraminx[1][2])
        self.pyraminx[1][3], self.pyraminx[3][1], self.pyraminx[2][6] = (
        self.pyraminx[3][1], self.pyraminx[2][6], self.pyraminx[1][3])

    def l(self):
        self.L()
        self.pyraminx[2][1], self.pyraminx[1][3], self.pyraminx[0][6] = (
        self.pyraminx[1][3], self.pyraminx[0][6], self.pyraminx[2][1])
        self.pyraminx[2][2], self.pyraminx[1][7], self.pyraminx[0][5] = (
        self.pyraminx[1][7], self.pyraminx[0][5], self.pyraminx[2][2])
        self.pyraminx[2][3], self.pyraminx[1][6], self.pyraminx[0][1] = (
        self.pyraminx[1][6], self.pyraminx[0][1], self.pyraminx[2][3])

    def l_(self):
        self.L_()
        self.pyraminx[2][1], self.pyraminx[0][6], self.pyraminx[1][3] = (
        self.pyraminx[0][6], self.pyraminx[1][3], self.pyraminx[2][1])
        self.pyraminx[2][2], self.pyraminx[0][5], self.pyraminx[1][7] = (
        self.pyraminx[0][5], self.pyraminx[1][7], self.pyraminx[2][2])
        self.pyraminx[2][3], self.pyraminx[0][1], self.pyraminx[1][6] = (
        self.pyraminx[0][1], self.pyraminx[1][6], self.pyraminx[2][3])

    def r(self):
        self.R()
        self.pyraminx[0][3], self.pyraminx[1][6], self.pyraminx[3][1] = (
        self.pyraminx[1][6], self.pyraminx[3][1], self.pyraminx[0][3])
        self.pyraminx[0][7], self.pyraminx[1][5], self.pyraminx[3][2] = (
        self.pyraminx[1][5], self.pyraminx[3][2], self.pyraminx[0][7])
        self.pyraminx[0][6], self.pyraminx[1][1], self.pyraminx[3][3] = (
        self.pyraminx[1][1], self.pyraminx[3][3], self.pyraminx[0][6])

    def r_(self):
        self.R_()
        self.pyraminx[0][3], self.pyraminx[3][1], self.pyraminx[1][6] = (
        self.pyraminx[3][1], self.pyraminx[1][6], self.pyraminx[0][3])
        self.pyraminx[0][7], self.pyraminx[3][2], self.pyraminx[1][5] = (
        self.pyraminx[3][2], self.pyraminx[1][5], self.pyraminx[0][7])
        self.pyraminx[0][6], self.pyraminx[3][3], self.pyraminx[1][1] = (
        self.pyraminx[3][3], self.pyraminx[1][1], self.pyraminx[0][6])


if __name__ == "__main__":
    pyraminx = Pyraminx()
    for i in move:
        if i == 'U':
            pyraminx.U()
        elif i == "U'":
            pyraminx.U_()
        elif i == 'u':
            pyraminx.u()
        elif i == "u'":
            pyraminx.u_()
        elif i == 'B':
            pyraminx.B()
        elif i == "B'":
            pyraminx.B_()
        elif i == 'b':
            pyraminx.b()
        elif i == "b'":
            pyraminx.b_()
        elif i == 'L':
            pyraminx.L()
        elif i == "L'":
            pyraminx.L_()
        elif i == 'l':
            pyraminx.l()
        elif i == "l'":
            pyraminx.l_()
        elif i == 'R':
            pyraminx.R()
        elif i == "R'":
            pyraminx.R_()
        elif i == 'r':
            pyraminx.r()
        elif i == "r'":
            pyraminx.r_()
    for i in pyraminx.pyraminx:
        print(*i)

# Link tham khảo: https://codereview.stackexchange.com/questions/197287/codefights-pyraminx-puzzle