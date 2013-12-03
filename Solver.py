from RCE import RCE
from Methods import *

###### Roux
#### First Block
##alg = "D L' D R F2 R' F U L2 D' L U R2 U D L' F' L2 D R'" + " X2 Y' F2 R U"
##method = Roux(RCE(alg), showProgress=False)
###r = method.solveStep(Roux.OneBlock, 2)
##r = method.solveStep(Roux.OneBlock, 3)
##solutions = method.solutions()
##print('Execution time: {:.4f}s'.format(method._stop - method._start))
##if r:
##    for i, s in enumerate(solutions):
##        s = [ x.ljust(2) for x in s ]
##        print('{1: >2}: {0}'.format(' '.join(s), str(i + 1)))
##else:
##    print('No solutions found!')


###### CFOP
#### Solve cross
cube = RCE("F2 U' R' U' B U2 R D2 F U' F' U2 F U R' F L B2 L'".split()) 
method = CFOP(cube, showProgress=True)
r = method.solveStep(CFOP.Cross, 4)

#### Extended Cross, F2L
##sol = [] # Solution
##
#### Extended cross
##cube = RCE("R' D' R2 D' R' D R U2 B L' U B' R F2 B L F B' U2 F' L2 D' B U' B2 U'".split())
##method = CFOP(cube, showProgress=True)
##method.solveStep(CFOP.ExtendedCross, 3)
##solutions1 = method.solutions()
##sol.extend(solutions1[0])
##print()
##
#### 2nd pair
##cube.alg(solutions1[0])
##method.solveStep(CFOP.F2L_2, 4)
##solutions2 = method.solutions()
##sol.extend(solutions2[0])
##print()
##
#### 3rd pair
### We don't want to search for solutions for another 24h
##a = "X2 F' U2 F U' B' X2".split()
##sol.extend(a)
##cube.alg(solutions2[0] + a)
##
##method.solveStep(CFOP.F2L_3, 2)
##solutions3 = method.solutions()
##sol.extend(solutions3[0])
##print()
##
#### 4th pair
##a = "X2 U' R U R' U R U2 R' F' U2 F X2".split()
##sol.extend(a)
##cube.alg(solutions3[0] + a)
##
##method.solveStep(CFOP.F2L, 4)
##solutions4 = method.solutions()
##sol.extend(solutions4[0])
##
##cube.alg(solutions4[0])
##
##print()
##print("F2L SOLUTION: ")
##print(' '.join(sol))
