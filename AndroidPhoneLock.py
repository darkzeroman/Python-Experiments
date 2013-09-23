


def generate_valid_codes():
  for i in range(1,10,1):
    bfs([i])
  
def bfs(state):
  pass

def generate_neighbors(state):
  grid = []
  for row in range(3):
    temp = []
    for col in range(3):
      temp.append(col)
    grid.append(temp)


  num = state[-1]

  offsets = [[1, 0], [-1, 0], [0, 1], [0, -1]]






