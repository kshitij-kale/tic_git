import random


def str_to_int(g_str):
    g_str = g_str.split(',')
    g_str = list(map(int, g_str))
    row = g_str[0] - 1
    column = g_str[1] - 1
    return [row, column]


def win_or_not(r_list):
    if r_list[0] == r_list[1] == r_list[2] != 0:
        if r_list[1] == 1:
            return 1
        return 2
    return 0


def taking_list(g_list):
    win_player = 0
    if win_player == 0:
        for row in range(len(g_list)):
            if win_player == 0:
                win_player = win_or_not(g_list[row])
    if win_player == 0:
        for i in range(len(g_list)):
            new_list = []
            for j in range(len(g_list)):
                new_list += [g_list[j][i]]
            if win_player == 0:
                win_player = win_or_not(new_list)
    if win_player == 0:
        diagonal1 = []
        diagonal2 = []
        for i in range(len(g_list)):
            diagonal1 += [g_list[i][i]]
            diagonal2 += [g_list[len(g_list) - 1 - i][i]]
        win_player = win_or_not(diagonal1)
        if win_player == 0:
            win_player = win_or_not(diagonal2)
    return win_player


def print_on_screen(g_list):
    for row in g_list:
        print(row)


print("Welcome to Tic-Tac-Toe")
while True:
    tic_list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    current_player = 2
    flag_for_input_error = False
    flag_for_occupied = False
    player_option = input("Do you want to play against a computer(y/n)>>")
    if player_option.lower() == "n":
        while True:
            if 0 in tic_list[0] or 0 in tic_list[1] or 0 in tic_list[2]:
                if not flag_for_input_error and not flag_for_occupied:
                    if current_player == 1:
                        current_player = 2
                    elif current_player == 2:
                        current_player = 1
                    flag_for_input_error = False
                print_on_screen(tic_list)
                input_from_player = input(f"Player {current_player}'s chance; input-->(x,y)>>")
                input_from_player = str_to_int(input_from_player)
                r = input_from_player[0]
                c = input_from_player[1]
                if 2 >= r >= 0 and 2 >= c >= 0:
                    if tic_list[r][c] == 0:
                        tic_list[r][c] = current_player
                        flag_for_occupied = False
                    else:
                        print("Position already occupied; choose another position")
                        flag_for_occupied = True
                    if taking_list(tic_list) in [1, 2]:
                        print_on_screen(tic_list)
                        print(f"Player {current_player} wins")
                        break
                    flag_for_input_error = False
                else:
                    print("Please enter valid co-ordinates from [1, 3]")
                    flag_for_input_error = True
            else:
                print("It's a tie")
                break
    else:
        first_chance = False
        u_break = False
        lis = ["c", "h"]
        lis1 = [0, 1, 2]
        correct = False
        first_player = random.choice(lis)
        if first_player == "c":
            print("Computer will go first")
            first_chance = True
        else:
            print("You may go first")
        while True:
            if 0 in tic_list[0] or 0 in tic_list[1] or 0 in tic_list[2]:
                if first_chance:
                    while not correct:
                        rw = random.choice(lis1)
                        cl = random.choice(lis1)
                        if tic_list[rw][cl] == 0:
                            tic_list[rw][cl] = 2
                            if taking_list(tic_list) in [2]:
                                print_on_screen(tic_list)
                                print(f"Computer wins")
                                u_break = True
                                break
                            correct = True
            if u_break:
                break
            if 0 in tic_list[0] or 0 in tic_list[1] or 0 in tic_list[2]:
                print_on_screen(tic_list)
                input_from_player = input(f"Player's chance; input-->(x,y)>>")
                input_from_player = str_to_int(input_from_player)
                r = input_from_player[0]
                c = input_from_player[1]
                if 2 >= r >= 0 and 2 >= c >= 0:
                    if tic_list[r][c] == 0:
                        tic_list[r][c] = 1
                        flag_for_occupied = False
                        correct = False
                        first_chance = True
                    else:
                        print("Position already occupied; choose another position")
                        flag_for_occupied = True
                    if taking_list(tic_list) in [1, 2]:
                        print_on_screen(tic_list)
                        print(f"Player wins")
                        break
                    flag_for_input_error = False
                else:
                    print("Please enter valid co-ordinates from [1, 3]")
                    flag_for_input_error = True
            else:
                print("It's a tie")
                break
    preference = input("Do you want to play again(y/n)>>")
    if preference.lower() == "n":
        print("Thank you for playing")
        break
    u_break = False
