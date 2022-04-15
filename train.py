import Gammon
import time
import net

net = net.Net()
count = 0
wins = 0

while count < 1000:
    count += 1
    print("Game #:{}".format(count))
    g = Gammon.Gammon()

    p1Roll = (0, 0)
    p2Roll = (0, 0)
    while sum(p1Roll) == sum(p2Roll):
        p1Roll = g.roll_dice()
        p2Roll = g.roll_dice()

    if sum(p1Roll) > sum(p2Roll):
        print("White gets the first turn")
        g.turn = g.players[0]
    else:
        print("Black gets the first turn")
        g.turn = g.players[1]
    start = 1
    moves = 0
    states = []

    while not g.game_over():
        actions = []

        if start == 1:
            actions = g.find_moves(p1Roll, g.turn)
            start = 0
        else:
            actions = g.find_moves(g.roll_dice(), g.turn)

        if len(actions) > 0:
            values = []

            for action in actions:
                g.take_action(g.turn, action)
                representation = g.get_representation(
                    g.board, g.players, g.on_bar, g.off_board, g.turn
                )
                values.append(net.getValue(representation))
                g.undo_action(g.turn, action)

            # Max for White and Min for Black
            max = 0
            max_index = 0
            min = 1
            min_index = 0
            for i in range(0, len(values)):
                if g.turn == "white":
                    if max < values[i][0]:
                        max = values[i][0]
                        max_index = i
                elif g.turn == "black":
                    if min > values[i][1]:
                        min = values[i][1]
                        min_index = i
            if g.turn == "white":
                best_action = actions[max_index]
            else:
                best_action = actions[min_index]
            g.take_action(g.turn, best_action)

            expected_board = g.get_representation(
                g.board, g.players, g.on_bar, g.off_board, g.turn
            )
            if g.turn == "white":
                states.append(expected_board)
                print('state size',len(states))
            moves += 1
            g.turn = g.get_opponent(g.turn)
            reward = 0

            if g.game_over():
                print("Game over in {} moves".format(moves))
                print("Num states: ", len(states))
                print("{} won".format(g.find_winner()))

                if g.find_winner() == "white":
                    reward = 1
                    wins += 1

                for i in range(len(g.board)):
                    g.print_point(i)

    for i in range(0, len(states) - 2):
        # print("State:", i)

        current_state = states[i]
        predicted_state = states[i + 1]

        error = net.getValue(predicted_state)[0] - net.getValue(current_state)[0]
        net.feedforward(current_state)
        net.do_td(current_state, net.getValue(current_state), error)
    print("Win percentage: {}".format(wins / count))
