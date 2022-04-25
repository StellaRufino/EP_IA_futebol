class Restriction():
    def __init__(self, variables):
        self.variables = variables

    def satisfied(self, assignment):
      return True

class SatisfactionRestriction():
  def __init__(self, variables, domains):
    self.variables = variables 
      
    self.domains = domains 
    self.restrictions = {}
    for variable in self.variables:
        self.restrictions[variable] = []
        if variable not in self.domains:
            raise LookupError("A variavel necessita de um dominio")

  def add_restriction(self, restriction):
    for variable in restriction.variables:
      if variable not in self.variables:
        raise LookupError("Essa variavel nao foi definida")
      else:
        self.restrictions[variable].append(restriction)


  def consistent(self, variable, assignment):
    for restrictions in self.restrictions[variable]:
      if not restrictions.satisfied(assignment):
        return False
    return True
  
  def busca_backtracking(self, assignment = {}):
    
    if len(assignment) == len(self.variables):
      return assignment

   
    variables_nao_atribuida  = [v for v in self.variables if v not in assignment]
    
    first_variable = variables_nao_atribuida[0]
    for valor in self.domains[first_variable]:
      if (valor not in assignment.values()):
        assignment_local = assignment.copy()
        assignment_local[first_variable] = valor
       
        if self.consistent(first_variable, assignment_local):
          result  = self.busca_backtracking(assignment_local)
         
          if result is not None:
            return result
    return None