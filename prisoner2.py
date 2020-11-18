# Yilun Liu
# CS111 Intro to class
# HW2
# Professor Aaron Bauer
# 2019/10/04


import random
from history import History

rubric = {("c","c"):( 2, 2),
          ("c","d"):(-3, 5),
          ("d","c"):( 5,-3),
          ("d","d"):(-1,-1)}

# Plays a two-player prisoner's dilemma game
# strat0 and strat1 are functions that return either "c" or "d"
# count is the number of plays
def play_loop(strat0, strat1, count=100):
    history0 = History()
    history1 = History()
    for i in range(count):
        action0 = strat0(history0, history1)
        action1 = strat1(history1, history0)
        history0.add_action(action0)
        history1.add_action(action1)

    print_results(strat0, strat1, history0, history1)

# This fuction prints the average scores for a two-player prisoner's
# dilemma game

def print_results(strat0, strat1, history0, history1):
    assert history0.get_length() == history1.get_length(), "Histories have unequal length"
    score0 = score1 = 0
    for actions in zip(history0, history1):
        score0 += rubric[actions][0]
        score1 += rubric[actions][1]
    print("{} average score: {:.3f}".format(strat0.__name__, score0 / history0.get_length()))
    print("{} average score: {:.3f}".format(strat1.__name__, score1 / history1.get_length()))






#Question 1
def betrayer(my_history, other_history):
    return "d"

def friend(my_history, other_history):
    return "c"


def chaos(my_history, other_history):
    percent = random.random()

    if 0 <= percent < 0.5:
        return "d"
    else:
        return "c"


def judge(my_history, other_history):
    if my_history.get_length() == 0:
        return "c"
    elif my_history.get_length() > 0:
        other_c = other_history.get_num_coops()
        other_d = other_history.get_num_defects()
        if other_d > other_c:
            return "d"
        else:
            return "c"

def mimic(my_history, other_history):
    if my_history.get_length() == 0:
        return "c"
    elif my_history.get_length() > 0:
        return other_history.get_most_recent()




# Question 2
def careful_mimic(my_history, other_history):
    if my_history.get_length() < 2:
        return "c"
    elif other_history.has_recent_coop(2)==False:
        return "d"
    else:
        return "c"


# Question 3



def make_alternating_strategy(strat0, strat1):
    def alternating(my_history, other_history):
        if my_history.get_length() % 2 == 0:
            return strat0(my_history, other_history)
        else:
            return strat1(my_history, other_history)
    return alternating

alternating1 = make_alternating_strategy(mimic, judge)                      # alternating1 will alternate between mimic and judge for every other round
alternating2 = make_alternating_strategy(friend, betrayer)                  # alternating2 will alternate between friend and betrayer for every
                                                                            # other round.



# Question 4
def gentle(strat, gentleless_factor):

    def strat_gentle(my_history,other_history):

        if strat(my_history, other_history)== "d":
            if random.random() <= gentleless_factor:
                return "c"
            else:
                return "d"
        else:
            return "c"
    return strat_gentle


slightly_gentle_betrayer = gentle(betrayer, 0.1)                # For both slightly_gentle_mimic and slightly_gentle_betrayer,
slightly_gentle_mimic = gentle(mimic, 0.1)                      # the gentleless_factor is set fixed as 0.1




#printing out results
#problem 1
play_loop(betrayer,betrayer)
play_loop(friend,friend)
play_loop(chaos,chaos)
play_loop(judge,judge)
play_loop(mimic,mimic)

#problem 2
play_loop(careful_mimic, betrayer)
play_loop(careful_mimic, mimic)
play_loop(careful_mimic, judge)

#problem 3
play_loop(alternating1, betrayer)
play_loop(alternating1, mimic)
play_loop(alternating1, judge)
play_loop(alternating2, betrayer)
play_loop(alternating2, mimic)
play_loop(alternating2, judge)



#problem 4
play_loop(slightly_gentle_mimic, mimic)
play_loop(slightly_gentle_mimic, betrayer)
play_loop(slightly_gentle_mimic, judge)
play_loop(slightly_gentle_betrayer, mimic)
play_loop(slightly_gentle_betrayer, betrayer)
play_loop(slightly_gentle_betrayer, judge)
