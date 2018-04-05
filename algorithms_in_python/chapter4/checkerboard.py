# this recursively places each "L" shaped piece, it will take 21 L shaped pieces to cover the board
# we pass in the board
# we start with label 1 for the tile
# we start with the top, left corner; , will tell you which board
def cover(board, lab_L_tile=1, top=0, left=0, side=None):
    print("label L tile {}".format(lab_L_tile))

    # first time in we will take the length of one of the sides of the board
    if side is None: side = len(board)

    # Side length of sub board
    # first time in we will split the board into 4, then it will split again to 2 then to 1
    ## the first split to 4 is splitting the board into quarters
    ### then the split to 2 is for each of the sub boards
    s = side // 2
    print('s value {}'.format(s))

    # Offsets for outer/inner squares of sub boards, the negative one in (0, -1) is for index offsetting
    offsets = (0, -1), (side - 1, 0) #  side - 1 is for index offsetting

    print('BEFORE FOR LOOP')
    print('offsets {}'.format(offsets))
    
    for dy_outer, dy_inner in offsets:
        print('========BEGIN OUTER LOOP')
        print('dy_outer {}'.format(dy_outer))
        print('dy_inner {}'.format(dy_inner))
        for dx_outer, dx_inner in offsets:
            print('BEGIN INNER LOOP ==========')
            print('dx_outer {}'.format(dx_outer))
            print('dx_inner {}'.format(dx_inner))
            print('top {}'.format(top), 'left {}'.format(left))
            #print('dx_outer {}'.format(dx_outer))
            #print('dy_outer {}'.format(dy_outer))
            print('s {}'.format(s))
            # if the outer corner is not set ...
            print('if not filled: top + dy_outer {}'.format(top + dy_outer), ' left + dx_outer {}'.format(left + dx_outer))
            if not board[top + dy_outer][left + dx_outer]:
                # ... label the inner corner
                print('x {}'.format(left + s + dx_inner), 'y {}'.format(top + s + dy_inner))
                board[top + s + dy_inner][left + s + dx_inner] = lab_L_tile
                print('just filled square with {}'.format(board[top + s + dy_inner][left + s + dx_inner]))
            else:
                print('board is filled with {}'.format(board[top + dy_outer][left + dx_outer]))

    # Next label:
    # bump up lable for next Triomino piece
    lab_L_tile += 1
    if s >1: # if the size is one, there is no need to break down the problem any more
        for dy in [0, s]:
            for dx in [0, s]:
                # Recursive calls , if s is at least 2
                # s is what will change the offsets
                lab_L_tile = cover(board, lab_L_tile, top + dy, left + dx, s)

    # Return the next available label:
    return lab_L_tile

board = [[0] * 8 for i in range(8)] # Eight by Eight checkerboard
board[7][7] = -1 # Missing corner
cover(board)

for row in board:
    print((" %2i"*8) % tuple(row))
