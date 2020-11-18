# Yilun Liu
# CS111 Intro to class
# HW2
# Professor Aaron Bauer
# 2019/10/04


from prisoner2 import mimic
from prisoner2 import chaos
from prisoner2 import betrayer
from prisoner2 import friend
import random

from history import History

rubric = {("c","c","c"):( 3, 3, 3),
          ("d","c","c"):( 5, 0, 0),
          ("c","d","c"):( 0, 5, 0),
          ("c","c","d"):( 0, 0, 5),
          ("c","d","d"):(-5, 2, 2),
          ("d","c","d"):( 2,-5, 2),
          ("d","d","c"):( 2, 2,-5),
          ("d","d","d"):(-2,-2,-2)}

# Plays a three-player prisoner's dilemma game
# strat0, strat1 and strat2 are functions that return either "c" or "d"
# count is the number of plays
def play_loop(strat0, strat1, strat2, count=100):
    history0 = History()
    history1 = History()
    history2 = History()
    for i in range(count):
        action0 = strat0(history0, history1, history2)
        action1 = strat1(history1, history0, history2)
        action2 = strat2(history2, history0, history1)
        history0.add_action(action0)
        history1.add_action(action1)
        history2.add_action(action2)

    print_results(strat0, strat1, strat2, history0, history1, history2)

# This fuction prints the average scores for a three-player prisoner's
# dilemma game
def print_results(strat0, strat1, strat2, history0, history1, history2):
    assert history0.get_length() == history1.get_length() == history2.get_length(), "Histories have unequal length"
    score0 = score1 = score2 = 0
    for actions in zip(history0, history1, history2):
        score0 += rubric[actions][0]
        score1 += rubric[actions][1]
        score2 += rubric[actions][2]
    print("{} average score: {:.3f}".format(strat0.__name__, score0 / history0.get_length()))
    print("{} average score: {:.3f}".format(strat1.__name__, score1 / history1.get_length()))
    print("{} average score: {:.3f}".format(strat2.__name__, score2 / history2.get_length()))



# Question 6
def betrayer3(my_history, oppo1_history, oppo2_history):
    return "d"

def friend3(my_history, oppo1_history, oppo2_history):
    return "c"

def chaos3(my_history, oppo1_history, oppo2_history):
    percent = random.random()

    if 0 <= percent < 0.5:
        return "d"
    else:
        return "c"



def tough_mimic(my_history, oppo1_history, oppo2_history):
    if oppo1_history.has_recent_defect(1)==True or oppo2_history.has_recent_defect(1)==True:
        return "d"
    else:
        return "c"


def soft_mimic(my_history, oppo1_history, oppo2_history):
    if oppo1_history.has_recent_defect(1)==True and oppo2_history.has_recent_defect(1)==True:
        return "d"
    else:
        return "c"

play_loop(tough_mimic, soft_mimic, chaos3)              # as per requested in Question 6






# Question 7
def make_combined_strategy(comstrat1, comstrat2, combining):

    def combined_strat(my_history, oppo1_history, oppo2_history):

        choice0 = comstrat1(my_history, oppo1_history)
        choice1 = comstrat2(my_history, oppo2_history)

        return combining(choice0, choice1)
    return combined_strat



def tough_combine(choice0, choice1):
    if choice0 == "d" or choice1 == "d":
        return "d"
    return "c"

def soft_combine(choice0, choice1):
    if choice0 == "c" or choice1 == "c":
        return "c"
    return "d"                                                      # These two strategies are defined as either prioritizes "d" (if one's action is "d" then "d")
                                                                    # or prioritizes "c" (if one's action is "c" then "c")


new_strat1 = make_combined_strategy(mimic, mimic,tough_combine)     # This is just an illustation of what might be one strategy in a three
                                                                    # prisoner dilemma game.
play_loop(new_strat1, soft_mimic, chaos3)


new_strat2 = make_combined_strategy(chaos, betrayer,soft_combine)   # This is just an illustation of what might be one strategy in a three
                                                                    # prisoner dilemma game.
play_loop(new_strat2, chaos3, friend3)
