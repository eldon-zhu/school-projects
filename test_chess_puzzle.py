import pytest
from chess_puzzle import *


def test_location2index1():
    assert location2index("e2") == (5, 2)
def test_location2index2():
    assert location2index("a1") == (1, 1)
def test_location2index3():
    assert location2index("z1") == (26, 1)
def test_location2index4():
    assert location2index("a26") == (1, 26)
def test_location2index5():
    assert location2index("z26") == (26, 26)
def test_location2index6():
    assert location2index("h26") == (8, 26)
def test_index2location1():
    assert index2location(5, 2) == "e2"
def test_index2location2():
    assert index2location(1, 1) == "a1"
def test_index2location3():
    assert index2location(26, 1) == "z1"
def test_index2location4():
    assert index2location(1, 26) == "a26"
def test_index2location5():
    assert index2location(26, 26) == "z26"
def test_index2location6():
    assert index2location(8, 26) == "h26"


wq1 = Queen(4,4,True)
wk1 = King(3,5,True)
wq2 = Queen(3,1,True)

bq1 = Queen(5,3,False)
bk1 = King(2,3,False)


B1 = (5, [wq1, wk1, wq2, bq1, bk1])

"""
  ♔  
   ♕ 
 ♚  ♛
     
  ♕  
"""

def test_is_piece_at1():
    assert is_piece_at(2,2, B1) == False
def test_is_piece_at2():
    assert is_piece_at(4, 4, B1) == True
def test_is_piece_at3():
    B2 = (5, [wk1, wq2, bq1, bk1])
    assert is_piece_at(3, 5, B2) == True
def test_is_piece_at4():
    testBoard = (10, [Queen(1,2, True), King(3,2, True)])
    assert is_piece_at(10, 10, testBoard) == False
def test_is_piece_at5():
    testBoard = (26, [Queen(11,2, True), King(23,22, True)])
    assert is_piece_at(11, 2, testBoard) == True
def test_is_piece_at6():
    testBoard = (3, [Queen(2, 2, True), King(2, 3, True)])
    assert is_piece_at(2, 3, testBoard) == True

def test_piece_at1():
    assert piece_at(3,1, B1) == wq2
def test_piece_at2():
    B2 = (5, [wk1, wq2, bq1, bk1])
    assert piece_at(3, 5, B2) == wk1
def test_piece_at3():
    whiteQueen = Queen(1, 2, True)
    whiteKing = King(3, 2, True)
    testBoard = (10, [whiteQueen, whiteKing])
    assert piece_at(1, 2, testBoard) == whiteQueen
def test_piece_at4():
    whiteQueen = Queen(11, 2, True)
    whiteKing = King(23, 22, True)
    testBoard = (26, [whiteQueen, whiteKing])
    assert piece_at(23, 22, testBoard) == whiteKing
def test_piece_at5():
    whiteQueen = Queen(2, 2, True)
    whiteKing = King(2, 3, True)
    testBoard = (3, [whiteQueen, whiteKing])
    assert piece_at(2, 3, testBoard) == whiteKing
def test_piece_at6():
    whiteQueen = Queen(2, 2, True)
    whiteKing = King(2, 3, True)
    testBoard = (26, [whiteQueen, whiteKing])
    assert piece_at(2, 3, testBoard) == whiteKing

def test_can_reach1():
    assert wq1.can_reach(5,4, B1) == True
def test_can_reach2():
    assert wq2.can_reach(1, 2, B1) == False
def test_can_reach3():
    assert wq1.can_reach(1, 1, B1) == True
def test_can_reach4():
    assert bk1.can_reach(3, 3, B1) == True
def test_can_reach5():
    assert bk1.can_reach(1, 1, B1) == False
def test_can_reach6():
    B2 = (5, [wk1, wq2, bq1, bk1])
    assert bq1.can_reach(3, 5, B2) == True
def test_can_reach7():
    assert bq1.can_reach(3, 5, B1) == False
def test_can_reach8():
    assert bq1.can_reach(6, 5, B1) == False
def test_can_reach8():
    bq1 = Queen(1, 1, False)
    bk1 = King(1, 2, False)
    wq1 = Queen(1, 26, True)
    wk1 = King(26, 26, True)
    testBoard = (26, [bq1, bk1, wq1, wk1])
    assert bq1.can_reach(26, 26, testBoard) == True

def test_can_move_to1():
    assert wq1.can_move_to(5,4, B1) == False
def test_can_move_to2():
    assert wq2.can_move_to(5, 3, B1) == True
def test_can_move_to3():
    assert bk1.can_move_to(1, 4, B1) == False
def test_can_move_to4():
    assert bk1.can_move_to(3, 3, B1) == False
def test_can_move_to5():
    bk1 = King(1, 1, False)
    bq1 = Queen(2, 1, False)
    wq1 = Queen(5, 1, True)
    wq2 = Queen(5, 2, True)
    wk1 = King(5, 5, True)
    testBoard = (5, [bk1, bq1, wq1, wq2, wk1])
    assert bq1.can_move_to(2, 2, testBoard) == False
    assert bq1.can_move_to(5, 1, testBoard) == True
    assert bk1.can_move_to(1, 2, testBoard) == False
def test_can_move_to6():
    bq1 = Queen(1, 1, False)
    bk1 = King(1, 2, False)
    wq1 = Queen(2, 26, True)
    wk1 = King(26, 26, True)
    testBoard = (26, [bq1, bk1, wq1, wk1])
    assert bq1.can_move_to(26, 26, testBoard) == True

def test_move_to1():
    wk1a = King(4,5, True)

    Actual_B = wk1.move_to(4,5, B1)
    Expected_B = (5, [wq1, wk1a, wq2, bq1, bk1])
    print("actual B", Actual_B)
    print("expected B", Expected_B)
    # check if actual board has same contents as expected
    assert Actual_B[0] == 5

    for piece1 in Actual_B[1]: #we check if every piece in Actual_B is also present in Expected_B; if not, the test will fail
        found = False
        for piece in Expected_B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found


    for piece in Expected_B[1]:  #we check if every piece in Expected_B is also present in Actual_B; if not, the test will fail
        found = False
        for piece1 in Actual_B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found
def test_move_to2():
    bk1a = King(1, 3, False)

    actualBoard = bk1.move_to(1, 3, B1)
    expectedBoard = (5, [wq1, wk1, wq2, bq1, bk1a])
    print("actual B", actualBoard)
    print("expected B", expectedBoard)
    assert actualBoard[0] == expectedBoard[0]

    for actualPiece in actualBoard[1]:
        found = False
        for expectedPiece in expectedBoard[1]:
            if (expectedPiece.pos_x == actualPiece.pos_x
                    and expectedPiece.pos_y == actualPiece.pos_y
                    and expectedPiece.side == actualPiece.side
                    and type(expectedPiece) == type(actualPiece)):
                found = True
        assert found

    for expectedPiece in expectedBoard[1]:
        found = False
        for actualPiece in actualBoard[1]:
            if (actualPiece.pos_x == expectedPiece.pos_x
                    and actualPiece.pos_y == expectedPiece.pos_y
                    and actualPiece.side == expectedPiece.side
                    and type(actualPiece) == type(expectedPiece)):
                found = True
        assert found
def test_move_to3():
    bq1 = Queen(1, 2, False)
    bk1 = King(1, 1, False)
    wq1 = Queen(1, 26, True)
    wk1 = King(26, 26, True)
    testBoard = (26, [bq1, bk1, wq1, wk1])
    actualBoard = bq1.move_to(1, 26, testBoard)
    bq1New = Queen(1, 26, False)
    expectedBoard = (26, [bq1New, bk1, wk1])
    assert actualBoard[0] == expectedBoard[0]

    for actualPiece in actualBoard[1]:
        found = False
        for expectedPiece in expectedBoard[1]:
            if (expectedPiece.pos_x == actualPiece.pos_x
                    and expectedPiece.pos_y == actualPiece.pos_y
                    and expectedPiece.side == actualPiece.side
                    and type(expectedPiece) == type(actualPiece)):
                found = True
        assert found

    for expectedPiece in expectedBoard[1]:
        found = False
        for actualPiece in actualBoard[1]:
            if (actualPiece.pos_x == expectedPiece.pos_x
                    and actualPiece.pos_y == expectedPiece.pos_y
                    and actualPiece.side == expectedPiece.side
                    and type(actualPiece) == type(expectedPiece)):
                found = True
        assert found
def test_move_to4():
    bq1 = Queen(1, 2, False)
    bk1 = King(1, 1, False)
    wq1 = Queen(1, 26, True)
    wk1 = King(26, 26, True)
    testBoard = (26, [bq1, bk1, wq1, wk1])
    actualBoard = bq1.move_to(1, 25, testBoard)
    bq1New = Queen(1, 25, False)
    expectedBoard = (26, [bq1New, bk1, wq1, wk1])
    assert actualBoard[0] == expectedBoard[0]

    for actualPiece in actualBoard[1]:
        found = False
        for expectedPiece in expectedBoard[1]:
            if (expectedPiece.pos_x == actualPiece.pos_x
                    and expectedPiece.pos_y == actualPiece.pos_y
                    and expectedPiece.side == actualPiece.side
                    and type(expectedPiece) == type(actualPiece)):
                found = True
        assert found

    for expectedPiece in expectedBoard[1]:
        found = False
        for actualPiece in actualBoard[1]:
            if (actualPiece.pos_x == expectedPiece.pos_x
                    and actualPiece.pos_y == expectedPiece.pos_y
                    and actualPiece.side == expectedPiece.side
                    and type(actualPiece) == type(expectedPiece)):
                found = True
        assert found
def test_move_to5():
    bq1 = Queen(1, 2, False)
    bk1 = King(1, 1, False)
    wq1 = Queen(1, 26, True)
    wk1 = King(26, 26, True)
    testBoard = (26, [bq1, bk1, wq1, wk1])
    actualBoard = bk1.move_to(2, 2, testBoard)
    bk1New = King(2, 2, False)
    expectedBoard = (26, [bq1, bk1New, wq1, wk1])
    assert actualBoard[0] == expectedBoard[0]

    for actualPiece in actualBoard[1]:
        found = False
        for expectedPiece in expectedBoard[1]:
            if (expectedPiece.pos_x == actualPiece.pos_x
                    and expectedPiece.pos_y == actualPiece.pos_y
                    and expectedPiece.side == actualPiece.side
                    and type(expectedPiece) == type(actualPiece)):
                found = True
        assert found

    for expectedPiece in expectedBoard[1]:
        found = False
        for actualPiece in actualBoard[1]:
            if (actualPiece.pos_x == expectedPiece.pos_x
                    and actualPiece.pos_y == expectedPiece.pos_y
                    and actualPiece.side == expectedPiece.side
                    and type(actualPiece) == type(expectedPiece)):
                found = True
        assert found
def test_is_check1():
    B2 = (5, [wk1, wq2, bq1, bk1])
    assert is_check(True, B2) == True

def test_is_check2():
    B2 = (5, [wk1, wq2, bq1, bk1])
    assert is_check(False, B2) == False
def test_is_check3():
    testBoard = (3, [King(1, 1, True), Queen(1, 2, True), King(3, 3, False), Queen(3, 2, False)])
    assert is_check(True, testBoard) == False
def test_is_check4():
    testBoard = (26, [King(1, 1, True), Queen(1, 2, True), King(26, 26, False), Queen(26, 25, False)])
    assert is_check(False, testBoard) == False
def test_is_check5():
    testBoard = (26, [King(1, 1, True), Queen(1, 2, True), King(25, 26, False), Queen(3, 2, False)])
    assert is_check(False, testBoard) == True

def test_is_checkmate1():
    B2 = (5, [wk1, wq2, bq1, bk1])
    assert is_checkmate(True, B2) == False
def test_is_checkmate2():
    bk1 = King(1, 1, False)
    bq1 = Queen(2, 2, False)
    wq1 = Queen(5, 1, True)
    wk1 = King(5, 5, True)
    testBoard = (5, [bk1, bq1, wq1, wk1])
    assert is_check(False, testBoard) == True
    assert is_checkmate(False, testBoard) == False
def test_is_checkmate3():
    bk1 = King(1, 1, False)
    wq1 = Queen(1, 3, True)
    testBoard = (3, [bk1, wq1])
    assert is_check(False, testBoard) == True
    assert is_checkmate(False, testBoard) == False
def test_is_checkmate4():
    bk1 = King(1, 1, False)
    wq1 = Queen(1, 3, True)
    testBoard = (26, [bk1, wq1])
    assert is_check(False, testBoard) == True
    assert is_checkmate(False, testBoard) == False
def test_is_checkmate5():
    testBoard = (10, [King(1, 1, True), Queen(10, 1, False), Queen(1, 10, False), Queen(10, 10, False)])
    assert is_check(True, testBoard) == True
    assert is_checkmate(True, testBoard) == True

def test_is_stalemate1():
    bk1 = King(1, 1, False)
    bq1 = Queen(2, 1, False)
    bq2 = Queen(2, 2, False)
    bq3 = Queen(1, 2, False)
    testBoard = (2, [bk1, bq1, bq2, bq3])
    assert is_stalemate(False, testBoard) == True
def test_is_stalemate2():
    testBoard = (3, [King(1, 1, True), Queen(2, 3, False)])
    assert is_stalemate(True, testBoard) == True
def test_is_stalemate3():
    testBoard = (10, [King(1, 1, True), Queen(2, 2, True), King(10, 10, False), Queen(9, 9, False)])
    assert is_stalemate(True, testBoard) == False
    assert is_stalemate(False, testBoard) == False
def test_is_stalemate4():
    testBoard = (26, [King(1, 1, True), Queen(2, 26, False), Queen(26, 2, False)])
    assert is_stalemate(True, testBoard) == True
def test_stalemate5():
    testBoard = (5, [King(1, 1, True), King(5, 5, False)])
    assert is_stalemate(True, testBoard) == False
    assert is_stalemate(False, testBoard) == False

def test_read_board1():
    B = read_board("board_examp.txt")
    assert B[0] == 5

    for piece in B[1]:  #we check if every piece in B is also present in B1; if not, the test will fail
        found = False
        for piece1 in B1[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found

    for piece1 in B1[1]: #we check if every piece in B1 is also present in B; if not, the test will fail
        found = False
        for piece in B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found
def test_read_board2():
    wk1 = King(1, 1, True)
    wq1 = Queen(2,1, True)
    bk1 = King( 3, 3, False)
    bq1 = Queen(2, 3, False)
    expectedBoard = (3, [bk1, bq1, wk1, wq1])

    actualBoard = read_board("test_board_1.txt")
    assert actualBoard[0] == 3

    for actualPiece in actualBoard[1]:
        found = False
        for expectedPiece in expectedBoard[1]:
            if (expectedPiece.pos_x == actualPiece.pos_x
                    and expectedPiece.pos_y == actualPiece.pos_y
                    and expectedPiece.side == actualPiece.side
                    and type(expectedPiece) == type(actualPiece)):
                found = True
        assert found

    for expectedPiece in expectedBoard[1]:
        found = False
        for actualPiece in actualBoard[1]:
            if (actualPiece.pos_x == expectedPiece.pos_x
                    and actualPiece.pos_y == expectedPiece.pos_y
                    and actualPiece.side == expectedPiece.side
                    and type(actualPiece) == type(expectedPiece)):
                found = True
        assert found
def test_read_board3():
    actualBoard = read_board("test_board_2.txt")
    assert actualBoard[0] == 26
    expectedBoard = (26, [King(1, 1, True), Queen(2, 1, True), King(3, 3, False), Queen(2, 3, False)])
    for actualPiece in actualBoard[1]:
        found = False
        for expectedPiece in expectedBoard[1]:
            if (expectedPiece.pos_x == actualPiece.pos_x
                    and expectedPiece.pos_y == actualPiece.pos_y
                    and expectedPiece.side == actualPiece.side
                    and type(expectedPiece) == type(actualPiece)):
                found = True
        assert found

    for expectedPiece in expectedBoard[1]:
        found = False
        for actualPiece in actualBoard[1]:
            if (actualPiece.pos_x == expectedPiece.pos_x
                    and actualPiece.pos_y == expectedPiece.pos_y
                    and actualPiece.side == expectedPiece.side
                    and type(actualPiece) == type(expectedPiece)):
                found = True
        assert found
def test_read_board4():
    actualBoard = read_board("test_board_3.txt")
    assert actualBoard[0] == 10
    expectedBoard = (10, [King(1, 1, True), Queen(2, 1, True), King(3, 3, False), Queen(2, 3, False)])
    for actualPiece in actualBoard[1]:
        found = False
        for expectedPiece in expectedBoard[1]:
            if (expectedPiece.pos_x == actualPiece.pos_x
                    and expectedPiece.pos_y == actualPiece.pos_y
                    and expectedPiece.side == actualPiece.side
                    and type(expectedPiece) == type(actualPiece)):
                found = True
        assert found

    for expectedPiece in expectedBoard[1]:
        found = False
        for actualPiece in actualBoard[1]:
            if (actualPiece.pos_x == expectedPiece.pos_x
                    and actualPiece.pos_y == expectedPiece.pos_y
                    and actualPiece.side == expectedPiece.side
                    and type(actualPiece) == type(expectedPiece)):
                found = True
        assert found
def test_read_board5():
    actualBoard = read_board("test_board_4.txt")
    assert actualBoard[0] == 13
    expectedBoard = (13, [King(1, 1, True), Queen(2, 1, True), King(3, 3, False), Queen(2, 3, False)])
    for actualPiece in actualBoard[1]:
        found = False
        for expectedPiece in expectedBoard[1]:
            if (expectedPiece.pos_x == actualPiece.pos_x
                    and expectedPiece.pos_y == actualPiece.pos_y
                    and expectedPiece.side == actualPiece.side
                    and type(expectedPiece) == type(actualPiece)):
                found = True
        assert found

    for expectedPiece in expectedBoard[1]:
        found = False
        for actualPiece in actualBoard[1]:
            if (actualPiece.pos_x == expectedPiece.pos_x
                    and actualPiece.pos_y == expectedPiece.pos_y
                    and actualPiece.side == expectedPiece.side
                    and type(actualPiece) == type(expectedPiece)):
                found = True
        assert found

def test_conf2unicode1():
    assert conf2unicode(B1).rstrip("\n") == "  ♔  \n   ♕ \n ♚  ♛\n     \n  ♕  "
def test_conf2unicode2():
    board1 = (5, [])
    assert conf2unicode(board1).rstrip("\n") == "     \n     \n     \n     \n     "
def test_conf2unicode3():
    board2 = (3, [King(1, 1, True), King(3, 3, False)])
    assert conf2unicode(board2).rstrip("\n") == "  ♚\n   \n♔  "
def test_conf2unicode4():
    board3 = (26, [King(1, 1, True), King(3, 3, False)])
    assert conf2unicode(board3).rstrip("\n") == ("                          \n"
                                                 "                          \n"
                                                 "                          \n"
                                                 "                          \n"
                                                 "                          \n"
                                                 "                          \n"
                                                 "                          \n"
                                                 "                          \n"
                                                 "                          \n"
                                                 "                          \n"
                                                 "                          \n"
                                                 "                          \n"
                                                 "                          \n"
                                                 "                          \n"
                                                 "                          \n"
                                                 "                          \n"
                                                 "                          \n"
                                                 "                          \n"
                                                 "                          \n"
                                                 "                          \n"
                                                 "                          \n"
                                                 "                          \n"
                                                 "                          \n"
                                                 "  ♚                       \n"
                                                 "                          \n"
                                                 "♔                         "
                                                 )
def test_conf2unicode5():
    board4 = (4, [King(1, 1, True), King(4, 4, False)])
    assert conf2unicode(board4).rstrip("\n") == "   ♚\n    \n    \n♔   "
