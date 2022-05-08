def solution(array):
  dp = []
  bakc_tracking=[]
  dp.append(array[0])
  
  for i in range(1, len(array)):
    for j in range(len(array[0])):
      if j==0:
        max_val = max(array[i-1][j], array[i-1][j+1])
        array[i][j] = max(array[i-1][j], array[i-1][j+1]) + array[i][j]
        
      elif j==len(array[0])-1:
        max_val = max(array[i-1][j-1], array[i-1][j])
        array[i][j] = max(array[i-1][j-1], array[i-1][j]) + array[i][j]
      
      else:
        max_val = max(array[i-1][j-1], array[i-1][j], array[i-1][j+1])
        array[i][j] = max(array[i-1][j-1], array[i-1][j], array[i-1][j+1]) + array[i][j]
  
  for i in range(len(array)):
    print(i, array[i])

  return max(array[-1])

array = [
        [3, 4, 9, -2, 2, 51, -23, 2, -1],
        [223, 7, 8, -11, 5, -99, 2, 3, -4],
        [2, 51, -23, -23, 6, 3, 2, 4, 5],
        [5, -99, 2, -1, 32, 2, 5, -99, 2],
        [6, 3, 3, -4, 2, -1, 6, 3, 3],
        [32, 2, 4, 5, 3, -4, 2, -1, 4],
        [4, 4, 23, 6, 2, -1, 3, -4, 34],
        [78, 32, 1, 7, 3, -4, -23, -23, 6],
    ]

solution(array)