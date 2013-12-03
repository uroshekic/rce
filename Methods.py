from RCE import RCE
import copy
import time

class Method:
    steps = []
    
    def __init__(self, rc, showProgress = False):
        self.cube = rc
        self.showProgress = showProgress
        self._solutions = []

    def solve(self):
        pass

    def _solveStep(self, solveFn, maxLen, alg = []):
        if self.showProgress and len(alg) == 1 and len(alg[0]) == 1: print('---- ' + alg[0] + ' ----')
        #print(' '.join(alg)) # Takes too long
        
        cube = copy.deepcopy(self.cube) # Much faster (2x) than creating a new cube and then applying the original algorithm
        
        cube.alg(alg)

        if solveFn(cube):
            if self.showProgress: print('=>', ' '.join(alg))
            self._solutions.append(alg)
            return True
        
        if len(alg) < maxLen:
            for t in RCE.all_possible_moves:
                if len(alg) > 0 and alg[-1][0] == t[0]: continue # Ignore algorithms of form ... X X'

                newAlg = alg[:]
                newAlg.append(t)
                s = self._solveStep(solveFn, maxLen, alg = newAlg)
                #if (s): return s # Uncomment if you only want one solution (not necessary the shortest one)
        
        return False if len(self._solutions) == 0 else True

    def solveStep(self, solveFn, maxLen):
        self._start = time.time()
        s = self._solveStep(solveFn, maxLen)
        self._stop = time.time()
        return s

    def solutions(self):
        a = self.sort(self._solutions)
        self._solutions = []
        return a

    @staticmethod
    def sort(solutions, reverse = False):
        return sorted(solutions, key=lambda x: len(x), reverse=reverse)


class Roux(Method):
    def __init__(self, *args, **kwargs):
        Method.__init__(self, *args, **kwargs)        

    @staticmethod
    def FirstBlock(rc):
        for i in range(3, 9):
            if rc.stickers[RCE.turns['L']][i][0] != rc.stickers[RCE.turns['L']][4][0]:
                return False

        f = [rc.stickers[RCE.turns['F']][3][0], rc.stickers[RCE.turns['F']][6][0]]
        b = [rc.stickers[RCE.turns['B']][3][0], rc.stickers[RCE.turns['B']][0][0]]
        colors = [rc.stickers[RCE.turns['F']][4][0], rc.stickers[RCE.turns['B']][4][0]]
        return len(set(f)) == 1 and len(set(b)) == 1 and f[0] != b[0] and f[0] in colors and b[0] in colors

    @staticmethod
    def SecondBlock(rc):
        pass
    
    @staticmethod
    def OneBlock(RC):
        for r in RCE.all_possible_rotations:
            rc = copy.deepcopy(RC)
            rc.alg(r)
            if Roux.FirstBlock(rc) or Roux.SecondBlock(rc):
                return True
        return False

    @staticmethod
    def TwoBlocks(rc):
        return Roux.FirstBlock(rc) and Roux.SecondBlock(rc)

    @staticmethod
    def CMLL(rc):
        pass

    @staticmethod
    def LS4E(rc):
        pass


class CFOP(Method):
    @staticmethod
    def Cross(rc, face = 'U'): # Currently works for U face only!
        a = rc.stickers[RCE.turns[face]][1][0] == face and \
            rc.stickers[RCE.turns[face]][3][0] == face and \
            rc.stickers[RCE.turns[face]][5][0] == face and \
            rc.stickers[RCE.turns[face]][7][0] == face
        b = True
        for otherFace in ['F', 'R', 'B', 'L']:
            if otherFace == 'B':
                c = (rc.stickers[RCE.turns[otherFace]][7][0] == rc.stickers[RCE.turns[otherFace]][4][0])
            else:
                c = (rc.stickers[RCE.turns[otherFace]][1][0] == rc.stickers[RCE.turns[otherFace]][4][0])
            b = b and c
        return (a and b)

    @staticmethod
    def ExtendedCross(rc):
        if not CFOP.Cross(rc): return False
        return (CFOP.firstPair(rc) or CFOP.secondPair(rc) or CFOP.thirdPair(rc) or CFOP.fourthPair(rc))

    @staticmethod
    def firstPair(rc):
        return (rc.stickers[RCE.turns['R']][0][0] == rc.stickers[RCE.turns['R']][4][0] and 
                rc.stickers[RCE.turns['F']][2][0] == rc.stickers[RCE.turns['F']][4][0] and 
                rc.stickers[RCE.turns['U']][8][0] == rc.stickers[RCE.turns['U']][4][0] and 
                rc.stickers[RCE.turns['R']][3][0] == rc.stickers[RCE.turns['R']][4][0] and 
                rc.stickers[RCE.turns['F']][5][0] == rc.stickers[RCE.turns['F']][4][0])

    @staticmethod
    def secondPair(rc):
        return (rc.stickers[RCE.turns['L']][2][0] == rc.stickers[RCE.turns['L']][4][0] and 
                rc.stickers[RCE.turns['U']][6][0] == rc.stickers[RCE.turns['U']][4][0] and 
                rc.stickers[RCE.turns['F']][0][0] == rc.stickers[RCE.turns['F']][4][0] and 
                rc.stickers[RCE.turns['L']][5][0] == rc.stickers[RCE.turns['L']][4][0] and 
                rc.stickers[RCE.turns['F']][3][0] == rc.stickers[RCE.turns['F']][4][0])

    @staticmethod
    def thirdPair(rc):
        return (rc.stickers[RCE.turns['L']][0][0] == rc.stickers[RCE.turns['L']][4][0] and
                rc.stickers[RCE.turns['U']][0][0] == rc.stickers[RCE.turns['U']][4][0] and
                rc.stickers[RCE.turns['B']][6][0] == rc.stickers[RCE.turns['B']][4][0] and
                rc.stickers[RCE.turns['L']][3][0] == rc.stickers[RCE.turns['L']][4][0] and
                rc.stickers[RCE.turns['B']][3][0] == rc.stickers[RCE.turns['B']][4][0])

    @staticmethod
    def fourthPair(rc):
        return (rc.stickers[RCE.turns['R']][2][0] == rc.stickers[RCE.turns['R']][4][0] and
                rc.stickers[RCE.turns['U']][2][0] == rc.stickers[RCE.turns['U']][4][0] and
                rc.stickers[RCE.turns['B']][8][0] == rc.stickers[RCE.turns['B']][4][0] and
                rc.stickers[RCE.turns['R']][5][0] == rc.stickers[RCE.turns['R']][4][0] and
                rc.stickers[RCE.turns['B']][5][0] == rc.stickers[RCE.turns['B']][4][0])
    
    @staticmethod
    def F2L_1(rc):
        return CFOP.ExtendedCross(rc)

    @staticmethod
    def F2L_2(rc):
        if not CFOP.Cross(rc): return False
        a = CFOP.firstPair(rc)
        b = CFOP.secondPair(rc)
        c = CFOP.thirdPair(rc)
        d = CFOP.fourthPair(rc)
        return (a and b) or (a and c) or (a and d) or (b and c) or (b and d) or (c and d)

    @staticmethod
    def F2L_3(rc):
        if not CFOP.Cross(rc): return False
        a = CFOP.firstPair(rc)
        b = CFOP.secondPair(rc)
        c = CFOP.thirdPair(rc)
        d = CFOP.fourthPair(rc)
        return (a and b and c) or (a and c and d) or (b and c and d)

    @staticmethod
    def F2L(rc):
        if not CFOP.Cross(rc): return False
        a = CFOP.firstPair(rc)
        b = CFOP.secondPair(rc)
        c = CFOP.thirdPair(rc)
        d = CFOP.fourthPair(rc)
        return a and b and c and d
