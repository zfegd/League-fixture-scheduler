import random
import itertools

# schedules one fixture between teams only, no home and away
def execute_scheduler(numteams, homeandaway):
    teams = [i for i in range(1,numteams+1)]
    numrounds = numteams - 1
    matchweeks = []
    tophalf = teams[:int(numteams/2)]
    bottomhalf = teams[int(numteams/2):]
    # todo- check if numteams odd or even
    # implements circle method
    for i in range(numrounds):
        thismatchweek = list(zip(tophalf,bottomhalf))
        shiftedhalfitem = tophalf[-1]
        tophalf = tophalf[:1] + bottomhalf[:1] + tophalf[1:-1]
        bottomhalf = bottomhalf[1:] + [shiftedhalfitem]
        matchweeks += [thismatchweek]
    if homeandaway:
        newmatchweeks = []
        for matchweek in matchweeks:
            newweek = [(b,a) for (a,b) in matchweek]
            newmatchweeks += [newweek]
        matchweeks += newmatchweeks
    random.shuffle(matchweeks)
    return matchweeks

def print_matchweeks(matchweeks):
    for i in range(len(matchweeks)):
        print_matchweek(matchweeks[i], i+1)

def print_matchweek(matchweek, weekno):
    print("MATCHWEEK " + str(weekno))
    for (a,b) in matchweek:
        print(str(a) + " VS " + str(b))



matchweeks = execute_scheduler(4, True)
# matchweeks = execute_scheduler(10, False)
print_matchweeks(matchweeks)
