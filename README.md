# Algorithm
Projects and activities


#Kadane’s Algorithm
Kadane's algorithm is used to find the contiguous subarray within a one-dimensional array of numbers which has the largest sum. We use to find the maximum sum subarray in the given array. The subarray can be of any length, including the entire array. Kadane’s Algorithm works by scanning through the array and keeping track of the current subarray sum, updating it as it goes along.The algorithm returns the maximum subarray sum found.

#Maximum subarray problem 

- To find the maximum subarray sum createstwo variables: the firts one is where the temporary sum will be stored and the second one is where the greater sum found so far will be stored. This can be temporary if there is or not another sum that is greater than previous one.

~~~python
def max_array_sum(arr):
    msf = arr[0]
    mts = arr[0]

~~~
- In the variable mts is stored the current maximum sum of the array and in each iteration that we will update the value with the maximum value found in the array. On the other hand in the variable msf only the maximum sum found until the moment will be stored. In case mts is negative, the variable will start at 0. Finally, it returns mts by the value.

~~~python
def max_array_sum(arr):
    msf = arr[0]
    mts = arr[0]

    for i in range(0, len(arr)):
        mts = max(arr[i], mts + arr[i])
        msf = max(mts, msf)
        if mts < 0:
            mts = 0
    return mts

~~~

- For the graph we take the variable where our array is stored. We call the function max_array_sum(our initial function) for the maximum values of our sums. We create a list of indices of the array and in the max_sums list we store the maximum sums of the subarrays that are found in the iteration. Finally it is plotted 

~~~python
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
~~~



- Finally, we test the algorithm by calling the function and passing a test array and calculate the time:

~~~python
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


~~~

The result was:
![Resultado](img\resultpt1.PNG)
![Resultado](img\graph.PNG)
