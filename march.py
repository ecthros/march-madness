round1Probabilities = {
    1:   99.3,
    2:   93.8,
    3:   84.7,
    4:   78.5,
    5:   64.6,
    6:   62.5,
    7:   60.4,
    8:   49.3,
    9:   50.7,
    10:  39.6,
    11:  37.5,
    12:  35.4,
    13:  21.5,
    14:  15.3,
    15:  6.3,
    16:  0.7
}

round2Probabilities = {
    1:  85.4, 
    2:  63.2, 
    3:  52.1, 
    4:  46.5, 
    5:  34.0, 
    6:  29.9, 
    7:  19.4, 
    8:  9.7, 
    9:  4.9, 
    10: 16.0, 
    11: 16.7, 
    12: 15.3, 
    13: 4.2, 
    14: 1.4, 
    15: 1.4, 
    16: 0.0
}

round3Probabilities = {
    1:  69.4,
    2:  45.1,
    3:  25.7,
    4:  14.6,
    5:  6.3,
    6:  10.4,
    7:  6.9,
    8:  5.6,
    9:  2.8,
    10: 5.6,
    11: 6.3,
    12: 1.4,
    13: 0.0,
    14: 0.0,
    15: 0.0,
    16: 0.0
}

round4Probabilities = {
    1:  41.0,
    2:  20.8,
    3:  11.8,
    4:  9.0,
    5:  4.9,
    6:  2.1,
    7:  2.1,
    8:  3.5,
    9:  0.7,
    10: 0.7,
    11: 3.5,
    12: 0.0,
    13: 0.0,
    14: 0.0,
    15: 0.0,
    16: 0.0
}

round5Probabilities = {
    1:  25.0,  
    2:  9.0,  
    3:  7.6,  
    4:  2.1,  
    5:  2.1,  
    6:  1.4,  
    7:  0.7,  
    8:  2.1,  
    9:  0.0,  
    10: 0.0,  
    11: 0.0,  
    12: 0.0,  
    13: 0.0,  
    14: 0.0,  
    15: 0.0,  
    16: 0.0
}

round6Probabilities = {
    1:  16.0,
    2:  3.5,
    3:  2.8,
    4:  0.7,
    5:  0.0,
    6:  0.7,
    7:  0.7,
    8:  0.7,
    9:  0.0,
    10: 0.0,
    11: 0.0,
    12: 0.0,
    13: 0.0,
    14: 0.0,
    15: 0.0,
    16: 0.0
}

class Picks():
    '''
    Create a class of picks, which is a series of 6 arrays.
    You can use picks[roundNum] (1-based) to access any of the rounds.
    '''
    def __init__(self, r1Picks, r2Picks, r3Picks, r4Picks, r5Picks, r6Picks):
        self.round1Picks = r1Picks
        self.round2Picks = r2Picks
        self.round3Picks = r3Picks
        self.round4Picks = r4Picks
        self.round5Picks = r5Picks
        self.round6Picks = r6Picks
        self.picks = [r1Picks, r2Picks, r3Picks, r4Picks, r5Picks, r6Picks]

    def __getitem__(self, key):
        return self.picks[key-1]

def score(picks, results):
    ''' 
    Scores picks against results.
    '''
    roundNum = 1
    score = 0
    while roundNum <= 6:
        pickNum = 0
        for pick in results[roundNum]: # Note that this array is 1-based
            if pick == picks[roundNum][pickNum]:
                score += roundNum * int(pick) # We choose int here to distinguish finalists
                print("Round " + str(roundNum) + " pick: " + str(pick))
            pickNum += 1
        roundNum += 1
    return score


myPicks = Picks([1,8,12,4,11,14,7,15,1,8,12,4,6,3,10,2,1,9,5,13,11,14,7,2,1,9,12,13,6,3,10,2], [1,4,11,7,8,12,3,2,1,5,11,2,9,12,3,2], [4,11,12,3,5,11,9,2], [4,3,5,2], [3.2,5.3], [3.2])

res = Picks([1,9,12,4,11,3,7,2,1,8,5,4,6,3,7,15,1,9,5,4,11,3,7,2,1,9,12,4,11,3,10,2], [1,4,3,2,8,4,3,15,1,5,11,2,1,4,11,10], [4,2,8,15,5,2,1,10], [], [], [])

class Game():
    def __init__(self, seed1, seed2):
        self.seed1 = seed1
        self.seed2 = seed2

def makePicks():
    '''
    Probabilistically create picks given historical accuracy.
    '''
    pass

