#Kadane’s Algorithm

import random
import time
import matplotlib.pyplot as plt

def max_array_sum(arr):
    msf = arr[0]
    mts = arr[0]

    for i in range(0, len(arr)):
        mts = max(arr[i], mts + arr[i])
        msf = max(mts, msf)
        if mts < 0:
            mts = 0
    return mts
def graph(arr):
    max_sum = max_array_sum(arr)
    indices = list(range(0, len(arr)))
    max_sums = [max_array_sum([arr[0]])]
    for j in range(1, len(arr)):
        max_sums.append(max_array_sum(arr[:j+1]))

    plt.plot(indices, arr, label='Array Values')
    plt.plot(indices, max_sums, label='Maximum Subarray Sums')
    plt.axhline(y=max_sum, color='r', linestyle='--', label='Maximum Sum')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Maximum Subarray Sum')
    plt.legend()
    plt.grid()
    plt.show()   

def main():
    arr = [random.randint(-10, 10) for i in range(10)]
    print("Maximum total sum is: ", max_array_sum(arr))
    graph(arr)
if __name__ == "__main__":
    # Your code goes here
   start = time.time()
   main()
   end = time.time()
   print(f"Tiempo: {(end-start)} seconds")

