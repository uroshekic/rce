from RCE import RCE

numErrors = 0
# Check whether X X' equals identity (solved state)
for move in (RCE.possible_turns + RCE.possible_rotations):
    rkT = RCE('{0} {0}\''.format(move).split())
    if rkT != RCE():
        print('{0}: {0}\' does not equal identity.'.format(move))
        numErrors += 1

check = {
    '' : 'wwwwwwwwwgggggggggrrrrrrrrrooooooooobbbbbbbbbyyyyyyyyy', 
    'U': 'wwwwwwwwwrrrggggggbbbrrrrrrgggoooooobbbbbboooyyyyyyyyy', 
    'F': 'wwwwwwooogggggggggwrrwrrwrrooyooyooybbbbbbbbbrrryyyyyy', 
    'R': 'wwgwwgwwgggyggyggyrrrrrrrrrooooooooobbwbbwbbwyybyybyyb', 
    'L': 'bwwbwwbwwwggwggwggrrrrrrrrroooooooooybbybbybbgyygyygyy', 
    'B': 'rrrwwwwwwgggggggggrryrryrrywoowoowoobbbbbbbbbyyyyyyooo', 
    'D': 'wwwwwwwwwggggggooorrrrrrgggoooooobbbrrrbbbbbbyyyyyyyyy', 
    'X': 'gggggggggyyyyyyyyyrrrrrrrrrooooooooowwwwwwwwwbbbbbbbbb', 
    'Y': 'wwwwwwwwwrrrrrrrrrbbbbbbbbbgggggggggoooooooooyyyyyyyyy', 
    'Z': 'ooooooooogggggggggwwwwwwwwwyyyyyyyyybbbbbbbbbrrrrrrrrr'
}
for f in check:
    rkT = RCE()
    rkT.alg(f)
    cube = rkT.export_cube()
    if check[f] != cube:
        print('{0: <1}: \nCurrently: {1}\nShould be: {2}'.format(f, cube, check[f]))
        numErrors += 1
        
if numErrors > 0:
    print('Something went wrong. Errors:', numErrors)
else:
    print('Great! Everything seems to work.')
