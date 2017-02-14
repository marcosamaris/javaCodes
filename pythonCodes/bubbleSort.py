import random

def bubbleSort(array):
    temp = 0;
    if len(array) > 1:
        for i in range(len(array)):
            for j in range(len(array)):
                if array[i] < array[j]:                        
                    temp = array[i]
                    array[i] = array[j]
                    array[j] = temp

    
if __name__ == '__main__':
    
    N = int(input("Enter the size of the random vector: "))

    array = []
    for i in range(N):    
        array.append(random.randrange(1, 100, 1))
    
    print("Array mess: " + " ".join(str(x) for x in array))    
    bubbleSort(array)
    print("Array ordered: " + " ".join(str(x) for x in array))


