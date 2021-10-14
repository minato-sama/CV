import numpy as np

filename = "C:/figure1.txt"
size = np.genfromtxt(filename, max_rows=1, deletechars="\n")
row = np.any(np.genfromtxt(filename, skip_header=2, delimiter=" ", deletechars="\n", dtype="uint8"), axis=0)

first = 10000; last = -10000

for i, elem in enumerate(row):
    if(elem  !=0):
        if (first > i): first = i
        if (last < i): last = i
            
print(size / (last-first+1))
