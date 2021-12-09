"""
Day 4 Part 2

--- Part Two ---
On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score be?
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

    board_won = [None] * len(bingo_boards)
    index_last = -1


    for win_number in bingo_numbers:
        for i, board in enumerate(bingo_boards):
            if not board_won[i]:
                board = mark_win_number(board, win_number)
                has_won_horizontally = check_win_horizontally(board)
                has_won_vertically = check_win_vertically(board)
                if has_won_horizontally is True or has_won_vertically is True:
                    bingo_sum = get_sum(board)
                    board_won[i] = bingo_sum * win_number
                index_last = i

    print(board_won[index_last])


if __name__ == "__main__":
    main()
