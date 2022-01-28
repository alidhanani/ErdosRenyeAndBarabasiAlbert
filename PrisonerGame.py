def PrisonerGame(G, R, T, S, P):
	""" This function would return the array of coperate states
	:param G:  Network
	:param R,T,S,P: payoff value
	:returns: array 
	"""
    states = networkx.get_node_attributes(G, 'state')
    PayOffB = networkx.get_node_attributes(G, 'payoff')
    store = 0
    for i in range(len(states)):
        if store == 0:
            states[i] = store
            store = 1
        else:
            states[i] = store
            store = 0
    R = R
    #T = [T]
    S = S
    P = P
    ArrayOfCoperateeB = []
    Worked = 0
    t = T
    for val in range(200):
        for i in range(10000):
            randNeig = [n for n in G.neighbors(i)]
            totalPayOff = 0
            for neigbour in randNeig:
                value1 = states[i]
                value2 = states[neigbour]
                if value1 == 0 and value2 == 0:
                    totalPayOff += 1
                elif value1 == 0 and value2 == 1:
                    totalPayOff += -0.1
                elif value1 == 1 and value2 == 0:
                    totalPayOff += t
                else:
                    totalPayOff += 0
            PayOffB[i] = totalPayOff
        for i in range(10000):
            randNeig = [n for n in G.neighbors(i)]        
            randValue = random.randint(0, len(randNeig)-1) 
            value1 = PayOffB[i]
            value2 = PayOffB[randNeig[randValue]]
            maxDegree = max(G.degree[i], G.degree[randValue])
            DMAX = max(t,R) - min(S,P)
            Prob = (value2 - value1)/(maxDegree*DMAX)
            if Prob >= 0.5:
                states[i] = states[randNeig[randValue]]
        Worked = 0
        for s in range(len(states)):
            if states[s] == 0:
                Worked += 1 
        ArrayOfCoperateeB.append(Worked)
    return ArrayOfCoperateeB
