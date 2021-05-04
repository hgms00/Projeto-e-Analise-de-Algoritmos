class Results:
    def __init__(self, winner, loser):
        self.winner = winner
        self.loser = loser

map = dict()
def ordenarTimes(teams,matches):
    winner = 0

    for results in matches:
        winner = results.winner
        if(winner in map):
            map[winner].append(results.loser)
        else:
            map[winner].append(results.loser)

    output = []

    tabela(teams, map, len(teams), output)    

    classificacaoFinal(output)

def classificacaoFinal(output):
    i = 1
    print('Posição','|','Time','|','N° de vitórias')
    for times in reversed(output):

        print(i,'       ',times,'    ',len(map[times]))     
        i = i + 1

def tabela(teams, map, n, output):
    if n<1:
        return 

    if n==1:
        output.append(teams[n-1])
        return
    
    tabela(teams, map, n-1, output)
    key = teams[n-1]
    i = 0

    for times in output:
        team = output[i]

        losers = map[key]
        if team not in losers:
            break
        i = i + 1

    output.insert(i,key)

def iniciarConfrontos(teams):
    for team in teams:
        map[team] = []
    
teams = ['A','B','C','D']
iniciarConfrontos(teams)
results = [('B','A'), ('C','A'), ('A','D'), ('B','C'), ('B','D'), ('C','D')]
matches = []
for match in results:
    matches.append(Results(match[0],match[1]))

ordenarTimes(teams, matches)

