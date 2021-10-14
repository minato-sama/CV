import numpy as np

def get_size(filename):
    size = np.genfromtxt(filename, max_rows = 1, deletechars = "\n")
    array = np.genfromtxt(filename, skip_header = 2, delimiter = " ", deletechars = "\n", dtype = "uint8")
    row = np.any(array, axis = 0)
    col = np.any(array, axis = 1)
    
    begin_r = 10000; end_r = -10000
    begin_c = 10000; end_c = -10000
    
    for i, elem in enumerate(row):
        if(elem != 0):
            if (begin_r > i): begin_r = i
            if (end_r < i): end_r = i
                
    for i, elem in enumerate(col):
        if(elem != 0):
            if (begin_c > i): begin_c = i
            if (end_c < i): end_c = i
                
    return {"begin_r": begin_r, "end_r": end_r, "begin_c": begin_c, "end_c": end_c}

image1 = get_size("C:\img1.txt")
image2 = get_size("C:\img2.txt")

print(f'сдвиг по оси x = {image2["begin_r"] - image1["begin_r"]}, по оси y = {image2["begin_c"] - image1["begin_c"]}')
