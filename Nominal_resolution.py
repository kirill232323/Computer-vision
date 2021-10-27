import numpy as np
import matplotlib.pyplot as plt
from typing import Dict
 
file = "figure2.txt"

def result(real_length, max_length):
    if max_length == 0:
        return "Фигура не найденa"
    else:
        return real_length/max_length
 
def find_ones(arr):
   max = 0
   for num in arr:
      if np.sum(num) > max: 
        max = np.sum(num)
   return max
    
def read_data() -> Dict:
    return_array = []
    with open(file, 'r') as f:
        data = f.read()
    splited_data = data.split('\n')
    resolution = float(splited_data[0])
    for row in splited_data[2:-1]:
        splited_row = row.split(' ')
        return_array.append(list(map(int, splited_row[:-1])))
    return {"resolution": resolution, "array": return_array}
 
max_length = find_ones(read_data()['array'])
res = result(read_data()['resolution'], max_length)
print("Result = " ,res)
 
plt.imshow(read_data()['array'])
plt.show()