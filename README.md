# Algorithm
Projects and activities


#Kadane’s Algorithm
Kadane's algorithm is used to find the contiguous subarray within a one-dimensional array of numbers which has the largest sum. We use to find the maximum sum subarray in the given array. The subarray can be of any length, including the entire array. Kadane’s Algorithm works by scanning through the array and keeping track of the current subarray sum, updating it as it goes along.The algorithm returns the maximum subarray sum found.

#Maximum subarray problem 

- To find the maximum subarray sum createstwo variables: the firts one is where the temporary sum will be stored and the second one is where the greater sum found so far will be stored. This can be temporary if there is or not another sum that is greater than previous one.

~~~python
def sum_array_total(arr):
    t = len(arr)
    mts = -1000000000000

~~~
- Then iterates through the array calculating the sum of each element with the previous ones. If the temporary sum is negative, it resets to 0 because negative. Then it creates a second iteation to compare the current sum with the greatest found so far and updates if greater. If it is greater , it stores in the variable where the maximum is, and then repeats this same step over the entire array to find the maximum sum total. Use the print function to show how the algorithm behaves since often the maximum_so_far does not become greater than the maximum_sum

~~~python
def sum_array_total(arr):
    t = len(arr)
    mts = -1000000000000

    for i in range(0, t):
        msf = 0
        for j in range(i, t):
            msf += arr[j]
            print('Maximum sum so far: ', msf)
            if msf < 0:
                msf = 0
                print('Maximum sum so far if it is negative: ', msf)
                print('Maximum sum: ', mts)
            if msf > mts:
                mts = msf
                print('Maximum sum: ', mts)



    return mts

~~~

- Finally, we test the algorithm by calling the function and passing a test array:

~~~python
if __name__ == "__main__":
    # Your code goes here
    kadane_proof = [47, -98, 1, -80, 66, -98, 93, -85, 83]
    print("Maximum total sum is: ", sum_array_total(kadane_proof))

~~~

The result was:
![Resultado](img\result1.PNG)
![Resultado](img\result2.PNG)
![Resultado](img\result3.PNG)
![Resultado](img\result4.PNG)