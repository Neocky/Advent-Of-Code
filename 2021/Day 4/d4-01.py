"""
Day 4 Part 1

--- Day 4: Giant Squid ---
You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
Finally, 24 is drawn:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?
"""


def read_input() -> list:
    """
    Reads input and returns list of lines
    """
    with open("./d4_input.txt", "r") as input_file:
        return input_file.readlines()


def create_bingo_numbers(data) -> list:
    """
    Create list for bingo numbers
    """
    return list(map(int, data[0].split(",")))


def create_boards(data) -> list:
    """
    Create bingo boards
    """
    boards = []
    board = []
    for line in data[1:]:
        if len(line) == 1:
            boards.append(board)
            board = []
            continue

        line_numbers = list(map(int, line.split()))
        board.append([[line_number, False] for line_number in line_numbers])

    return boards


def mark_win_number(board, win_number) -> list:
    """
    Mark the field with a win number
    """
    for collum in board:
        for entry in collum:
            if entry[0] == win_number:
                entry[1] = True
    return board


def check_win_horizontally(board) -> bool:
    """
    Check if board has won horizontally
    """
    i = len(board)
    board_entries = len(board[0])
    for j in range(i):
        if sum(entry[1] for entry in board[j]) == board_entries:
            return True
    return False


def check_win_vertically(bingo_board)-> bool:
    """
    Check if board has won vertically
    """
    board_entries = len(bingo_board[0])
    for k in range(board_entries):
        temp_sum = 0
        for i in range(len(bingo_board)):
            if bingo_board[i][k][1] is True:
                temp_sum += 1
                if temp_sum == 5:
                    return True
                continue
    return False



def get_sum(bingo_board) -> int:
    """
    Gets sum of all unmarked numbers of winner board
    """
    bingo_sum = 0
    for i in range(len(bingo_board)):
        bingo_sum += sum(entry[0] for entry in bingo_board[i] if entry[1] is False)
    return bingo_sum



def main() -> None:
    """
    Main function which checks every board for every number if it has won
    """
    data = read_input()
    bingo_numbers = create_bingo_numbers(data)
    bingo_boards = create_boards(data)

    bingo_boards.pop(0) # first board is null

    for win_number in bingo_numbers:
        for board in bingo_boards:
            board = mark_win_number(board, win_number)
            has_won_horizontally = check_win_horizontally(board)
            has_won_vertically = check_win_vertically(board)
            if has_won_horizontally is True or has_won_vertically is True:
                bingo_sum = get_sum(board)
                print(bingo_sum * win_number)
                print(board)
                return board




if __name__ == "__main__":
    main()
