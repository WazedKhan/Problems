grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

def numIslands(grid):
    islands = 0
    for item in grid:
        for i in range(len(item)):
            if item[i] == '1' and item[i+1] != '1':
                islands += 1
    print(islands)


numIslands(grid)