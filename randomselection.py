def count(ballots,n,candidates):
    quota = math.ceil(len(ballots)/(n+1))
    tally = {}
    elected = {}
	transfer = {}  
    
    for i in candidates:
        tally[i] = 0
        
    for i in ballots:
        tally[i[0]] += 1
    
    for i in tally:
        if tally[i] >= quota:
            elected[i] = tally[i]

	for i in candidates:
		transfer[i] = []
	for i in ballots:
		if len(i) > 1:
			transfer[i[0]].append(i)

	return quota, tally, elected, transfer

def checksurplus():
	for i in elected:
		if len(transfer[elected]) < elected[i]-quota:
			electedexhausted = []
			electedexhausted.append[i]
	for i in ballots:
		if i[0] in electedexhauted:
			

def distribute(
