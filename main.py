#Mayara Rosa & Stella Rufino

from satisfaction_restriction import Restriction, SatisfactionRestriction

#todos os times
teams = {
  "Guardiões FC": {"cidade": "Guardião", "torcedores": 40},
  "SE Leões": {"cidade": "Leão", "torcedores": 40},
  "CA Protetores": {"cidade": "Guardião", "torcedores": 20},
  "CA Azedos": {"cidade": "Limões", "torcedores": 18},
  "Porto EC": {"cidade": "Porto", "torcedores": 45},
  "Secretos FC": {"cidade": "Escondidos", "torcedores": 25}  
}


ROUNDS = (len(teams)-1) * 2
GAMES = int(len(teams)/2)


def satisfied(self, assignment):
    round = list(assignment.keys())[-1]
    round = round[0:2]
    games = [x for x in list(assignment.keys()) if x.__contains__(round)]
    rounds = []

    for variable in games:
      teams_a = assignment[variable]
      if teams_a is not None:
        team1 = teams_a[0]
        team2 = teams_a[1]
        if (team1 in rounds or team2 in rounds):
          return False
        else:
          rounds.append(team1)
          rounds.append(team2)
    return True



class Restriction_a_team(Restriction):
  def __init__(self,variables):
    super().__init__(variables)

#combinação de jogos
game_combination = []
for t1 in teams.keys():
  for t2 in teams.keys():
    if t1 != t2: #retira time contra ele mesmo
      game_combination.append((t1, t2))

    #jogos que sao classicos
class classics(Restriction):
  
  def __init__(self,variables):
    super().__init__(variables)

    
  def satisfied(self, assignment):
    
    round = list(assignment.keys())[-1]
    
    round = round[0:2]
    
    games = [x for x in list(assignment.keys()) if x.__contains__(round)]
    
    classc = 0
    
    for variable in games:
      teams_a = assignment[variable]
      
      if teams_a is not None:
        team1 = teams_a[0]
        team2 = teams_a[1]
        
      if (teams[team1]["torcida"] >= 38 and teams[team2]["torcida"] >= 38):
        classc += 1
        
    if classc >= 2:
      return False
      
    else:
      return True

      
class Stadium(Restriction):
  def __init__(self,variables):
    super().__init__(variables)

  def satisfied(self, assignment):
     cities_rounds = []
    
     round = list(assignment.keys())[-1]
    
     round = round[0:2]
    
     games = [x for x in list(assignment.keys()) if x.__contains__(round)]

     for variable in games:
      teams_a = assignment[variable]
      
      if teams_a is not None:
        team1 = teams_a[0]
        
        if (teams[team1]["cidade"] in  cities_rounds):
          return False
          
        else:
           cities_rounds.append(teams[team1]["cidade"])
          
     return True


        
if __name__ == "__main__":
    variables = []
  
    for i in range(ROUNDS): 
      for j in range(GAMES): 
        
        variables.append("R" + str(i) + "J" + str(j))
      
    domains = {}
  
    for variable in variables:
        
        domains[variable] = game_combination
    
    problem = SatisfactionRestriction(variables, domains) 
                
    problem.add_restriction(Restriction_a_team(variables)) 
    problem.add_restriction(Stadium(variables))
  
    reply = problem.busca_backtracking()
    if reply is None:
      print("Nada foi encontrado.")
      
    else:
      for i in range(ROUNDS): # rounds
        print("-------------------------------------")
        print("\n"+ "************** " +  str(i+1) + "º rodada" + " ************* "+ " \n")
        for j in range(GAMES):
          game = reply["R" + str(i) + "J" + str(j)]
          
          print(str(j+1) + "º jogo " + ": " + game[0] + " x " + game[1] + "\nCidade (mandante): " + teams[game[0]]["cidade"] + "\n")

          