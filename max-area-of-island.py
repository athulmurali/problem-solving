# Problem https://leetcode.com/problems/max-area-of-island/

# 695. Max Area of Island:
# While solving it for the second time 

# Initial thoughts  thoughts 


  # sol1  
  # for every element (i,j)
    # return dfs in all directions  with recursion
    # is all directions visited 
    # max_area = max(curr, max_area)
    
    #how to do I frame the dfs ? 
      # for every dfs 
     # mark visited with a different character 
      #  dfs(move_up)
      # dfs(move_down)
      # dfs (move_left)
      # dfs(move_right)
      #undo change 

  #How to avoid dfs on visited elements ? 
    # 1. mutate existing area and unmutate at the end 
      # Time complexity  : 2 x O(DFS)
          # O(DFS) =>  O ( V + E ), Vertex , Edges
        
def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
  LAND = 1 
  WATER = 0
  VISITED = -1
  #row count and col count
  m = len(grid)
  n = len(grid[0])

  def out_of_bounds(i,j):
      return True if i >=m or i < 0 or j >= n or j  < 0 else False                                    
  def dfs(grid, i , j, area):            
      if out_of_bounds(i,j):                
              return area               
      else:
          cell  = grid[i][j]
          if cell is VISITED  or cell is WATER:
              return area                
          # CONNECTED LAND FOUND
          grid[i][j] = VISITED 
          # dfs
          area = sum (
              [1, dfs(grid, i-1 , j,0 ),
              dfs(grid, i , j-1, 0 ),
              dfs(grid, i , j+1, 0 ),
              dfs(grid, i +1  , j, 0)]
          )
          return area
  max_area = 0
  for i in range(m):
      for j in range(n):
          area = dfs(grid, i , j , 0)
          max_area = max(area, max_area)                
  for i in range(m):
      for j in range(n):
          cell = grid[i][j]
          if cell is VISITED:
              cell = LAND
  return max_area
        
      
          
  



