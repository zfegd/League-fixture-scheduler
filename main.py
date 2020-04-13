import random
import itertools

# schedules one fixture between teams only, no home and away
def execute_scheduler(numteams):
    teams = [i for i in range(1,numteams+1)]
    numrounds = numteams - 1
    matchweeks = []
    firsthalfteams = teams[:int(numteams/2)]
    secondhalfteams = teams[:int(numteams/2)]
    # todo- check if numteams odd or even
    # naive implementation
    for i in range(int(numteams/2)):
        thisweekaway = shift_list(secondhalfteams,i)
        thismatchweek = list(zip(firsthalfteams,thisweekaway))
        matchweeks += [thismatchweek]
    # todo - schedule the rest
    random.shuffle(matchweeks)
    return matchweeks

def shift_list(list, num_shifts):
    numitems = len(list)
    return list[-num_shifts:] + list[:-num_shifts]

def greedy_scheduler(numteams):
    teams = [i for i in range(1,numteams+1)]
    numrounds = numteams - 1
    matchweeks = []
    matches_left = list(itertools.product(teams,teams))
    for i in range(1,numteams+1):
        matches_left.remove((i,i))
    pass

def schedule_matchweek(matches_left, teams):
    thismatchweek = []
    while len(teams) != 0:
        # pass
    return thismatchweek, matches_left



print(execute_scheduler(10))
