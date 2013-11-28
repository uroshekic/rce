# Rubik's Cube Engine (RCE)

# The 'stickers' variable:
#       0 - U, 1 - F, 2 - R, 3 - B, 4 - L, 5 - D
# 'stickers' colors:    0 - white   1 - green
#                       2 - red     3 - blue
#                       4 - orange  5 - yellow
# Possible turns: P, P', P2 where P element of { U, F, R, B, L, D } + { x, y, z }

# Rotations (x, y, z) HAVE NOT BEEN TESTED YET!

class RCE:
    turns = {'U' : 0, 'F' : 1, 'R' : 2, 'L' : 3, 'B' : 4, 'D' : 5}
    turns_i = {0 : 'U', 1 : 'F', 2 : 'R', 3 : 'L', 4 : 'B', 5 : 'D'}
    colors = {'U' : 'w', 'F' : 'g', 'R' : 'r', 'B' : 'b', 'L' : 'o', 'D' : 'y'}

    possible_raw_moves = list(range(6))
    possible_turns = ['U', 'F', 'R', 'L', 'B', 'D']
    possible_rotations = ['X', 'Y', 'Z']
            
    def __init__(self, alg = ''):
        self.stickers = [[self.turns_i[face] + str(sticker) for sticker in range(9)] for face in range(6)]
        if type(alg) == type(""):
            alg = alg.split()
        self.alg(alg)

    def __eq__(self, other):
        return self.stickers == other.stickers # TO-DO: Check other 5 combinations (when colors are swapped)

    def turn(self, f): # Clockwise
        f = self.turns[f]
        self.stickers[f] = [self.stickers[f][6], self.stickers[f][3], self.stickers[f][0], \
                           self.stickers[f][7], self.stickers[f][4], self.stickers[f][1], \
                           self.stickers[f][8], self.stickers[f][5], self.stickers[f][2]]
        if f == 0: # U
            self.stickers[3][0], self.stickers[3][1], self.stickers[3][2], \
            self.stickers[1][0], self.stickers[1][1], self.stickers[1][2], \
            self.stickers[2][0], self.stickers[2][1], self.stickers[2][2], \
            self.stickers[4][8], self.stickers[4][7], self.stickers[4][6] \
            = \
            self.stickers[1][0], self.stickers[1][1], self.stickers[1][2], \
            self.stickers[2][0], self.stickers[2][1], self.stickers[2][2], \
            self.stickers[4][8], self.stickers[4][7], self.stickers[4][6], \
            self.stickers[3][0], self.stickers[3][1], self.stickers[3][2]
        elif f == 1: # F
            self.stickers[2][0], self.stickers[2][3], self.stickers[2][6], \
            self.stickers[5][2], self.stickers[5][1], self.stickers[5][0], \
            self.stickers[3][2], self.stickers[3][5], self.stickers[3][8], \
            self.stickers[0][8], self.stickers[0][7], self.stickers[0][6] \
            = \
            self.stickers[0][6], self.stickers[0][7], self.stickers[0][8], \
            self.stickers[2][0], self.stickers[2][3], self.stickers[2][6], \
            self.stickers[5][0], self.stickers[5][1], self.stickers[5][2], \
            self.stickers[3][2], self.stickers[3][5], self.stickers[3][8]
        elif f == 2: # R
            for i in [8, 5, 2]:
                self.stickers[4][i], self.stickers[5][i], self.stickers[1][i], self.stickers[0][i] \
                = \
                self.stickers[0][i], self.stickers[4][i], self.stickers[5][i], self.stickers[1][i]
        elif f == 3: # L
            for i in [6, 3, 0]:
                self.stickers[0][i], self.stickers[4][i], self.stickers[5][i], self.stickers[1][i] \
                = \
                self.stickers[4][i], self.stickers[5][i], self.stickers[1][i], self.stickers[0][i]
        elif f == 4: # B
            self.stickers[3][0], self.stickers[3][3], self.stickers[3][6], \
            self.stickers[5][6], self.stickers[5][7], self.stickers[5][8], \
            self.stickers[2][8], self.stickers[2][5], self.stickers[2][2], \
            self.stickers[0][2], self.stickers[0][1], self.stickers[0][0]  \
            = \
            self.stickers[0][2], self.stickers[0][1], self.stickers[0][0], \
            self.stickers[3][0], self.stickers[3][3], self.stickers[3][6], \
            self.stickers[5][6], self.stickers[5][7], self.stickers[5][8], \
            self.stickers[2][8], self.stickers[2][5], self.stickers[2][2]
        elif f == 5: # D
            self.stickers[2][6], self.stickers[2][7], self.stickers[2][8], \
            self.stickers[4][2], self.stickers[4][1], self.stickers[4][0], \
            self.stickers[3][6], self.stickers[3][7], self.stickers[3][8], \
            self.stickers[1][6], self.stickers[1][7], self.stickers[1][8]  \
            = \
            self.stickers[1][6], self.stickers[1][7], self.stickers[1][8], \
            self.stickers[2][6], self.stickers[2][7], self.stickers[2][8], \
            self.stickers[4][2], self.stickers[4][1], self.stickers[4][0], \
            self.stickers[3][6], self.stickers[3][7], self.stickers[3][8]
                
    def rotate(self, s):
        if s == 'X':
            self.stickers[1], self.stickers[5], self.stickers[4], self.stickers[0] \
            = \
            self.stickers[5], self.stickers[4], self.stickers[0], self.stickers[1]
        elif s == 'Y':
            self.stickers[1], self.stickers[2], self.stickers[4], self.stickers[3] \
            = \
            self.stickers[2], self.stickers[4], self.stickers[3], self.stickers[1]
        elif s == 'Z':
            self.stickers[2], self.stickers[0], self.stickers[3], self.stickers[5] \
            = \
            self.stickers[0], self.stickers[3], self.stickers[5], self.stickers[2]
    
    def alg(self, alg):
        for m in alg:
            if m[0] in self.possible_rotations:
                if len(m) == 1:
                    self.rotate(m)
                elif len(m) > 1:
                    if m[1] == "2":
                        self.rotate(m[0])
                        self.rotate(m[0])
                    elif m[1] == "'":
                        self.rotate(m[0])
                        self.rotate(m[0])
                        self.rotate(m[0])
            elif m[0] in self.possible_turns:
                if len(m) == 1:
                    self.turn(m)
                elif len(m) > 1:
                    if m[1] == "2":
                        self.turn(m[0])
                        self.turn(m[0])
                    elif m[1] == "'":
                        self.turn(m[0])
                        self.turn(m[0])
                        self.turn(m[0])

    # For testing purposes
    def output(self, style = 'text_net'):
        if style == 'text_vertical':
            for face, stickers in enumerate(self.stickers):
                print(self.turns_i[face].upper(), end=':\n')
                for i, sticker in enumerate(stickers):
                    print(self.colors[sticker[0]], end='')
                    if i % 3 == 2:
                        print()
                print()
        elif style == 'text_net':
            for i in range(6): print("{: ^5}|".format(self.turns_i[i]), end='', sep='')
            print()
            print(('-'*5 + '+')*6)

            for i in range(3):
                for j in range(6):
                    print(' ', self.colors[self.stickers[j][3*i][0]], self.colors[self.stickers[j][3*i+1][0]], self.colors[self.stickers[j][3*i+2][0]], ' ', end='|', sep='')
                print()

    def export_cube(self):
        return ''.join([ ''.join([self.colors[sticker[0]] for sticker in face ]) for face in self.stickers ])
