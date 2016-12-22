import sys
import mcts

def play(human=False, n=1000):
# Testing ConnectFour - mcts_uct()
    #height = 6
    height =4 
    #width = 7
    width=5  
    #target = 4
    target=3
    initial = ((),) * width

    game = mcts.ConnectFour(height=height, width=width, target=target)
    state = initial
    player = game.players[0]
    computer = game.players[1]

    counter_for_games_played=0  #YOTAM: added here
    while not game.terminal(state):
        # **********YOTAM: here I want to check the games' outcome via Johtn Tromp's table***********************
        if counter_for_games_played==8:
            print "THIS IS NUMBER 8!!!!!!!!!!!!!!!!!!!!"
            print state
        print game.pretty_state(state, False)
        if human:
            prompt = 'Choose a move, choices are %s: ' % (game.actions(state),)
            success = False
            while not success:
                choice = raw_input(prompt)
                try:
                    action = int(choice)
                    state = game.result(state, action, player)
                    success = True
                except ValueError:
                    pass
                except Exception:
                    pass
        else:
            #YOTAM: I ADDED THIS LINE AND ERASED THE LATTER (WITH MCTS)
            #action = mcts.minimax(game,state,player)
            #YOTAM END ADDING
            action = mcts.mcts_uct(game, state, player, n)
            print "next action is: ", action
            state = game.result(state, action, player)
            counter_for_games_played+=1 #YOTAM: added here

        print 'Player 1 chose %s' % action
        print game.pretty_state(state, False)


        # Intermediate win check
        if game.terminal(state):
            break

        # Computer plays now
        action = mcts.mcts_uct(game, state, computer, n)
        state = game.result(state, action, computer)
        counter_for_games_played += 1  # YOTAM: added here

        print 'Player 2 chose %s' % action
    print "counter for games played: ", counter_for_games_played    #YOTAM: added here
    print game.pretty_state(state, False)
    print
    outcome = game.outcome(state, player)
    if outcome == 1:
        print 'Player 1 wins.'
    elif outcome == -1:
        print 'Player 2 wins.'
    else:
        print 'Tie game.'
    

n = 30000 #YOTAM: n is the budget
if len(sys.argv) > 1:
    try:
        n = int(sys.argv[1])
    except ValueError:
        pass

#n = 1000
if '-n' in sys.argv:
    try:
        n = int(sys.argv[sys.argv.index('-n') + 1])
    except:
        pass

human = False #Yotam: mark as 'True' if I want to play against MCTS bot
if '-c' in sys.argv:
    human = False

print 'Number of Sample Iterations: ' + str(n)
print 'Human Player: ' + str(human)
play(human=human,n=n)

