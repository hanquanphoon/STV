class candidate:
    def __init__(self,name,ballots,n):
        self.name = name
        firstpref = [bal[0] for bal in ballots]
        self.tally = firstpref.count(self.name)
        quota = math.ceil(len(ballots)/(n+1))
        if self.tally >= quota:
            self.elected = True
        else: self.elected = False
        self.transfer = [bal for bal in ballots if (len(bal))>1 and bal[0]==self.name]
        if self.elected:
            if len(self.transfer) <= self.tally - quota:
                self.exhausted = True
            else: self.exhausted = False
    
    def __repr__(self):
        return self.name

# assume no exhaustion
def distributeSurplus(cands,ballots,n):
    elected = [cand for cand in cands if cand.elected]
    electedTally = [cand.tally for cand in elected]
    quota = math.ceil(len(ballots)/(n+1))
    while sum(electedTally) > quota*len(elected):
        m = max(electedTally)
        for cand in elected:
            if cand.tally==m:
                bal = random.choice(cand.transfer)
                cand.transfer.remove(bal)
                cand.tally -= 1
                for can in cands:
                    if can.name==bal[1]:
                        can.tally += 1
                bal.pop(0)
                if len(bal)==0:
                    cand.transfer.remove(bal)

        for cand in cands:
            if (cand.elected==False and cand.tally>=quota):
                elected.append(cand)
        electedTally = [cand.tally for cand in elected]

    return elected

def eliminate(eli,ballots,n):
    for bal in ballots:
        if eli in bal:
            bal.remove(eli)
    return ballots
