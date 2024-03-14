#Kadane’s Algorithm
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


if __name__ == "__main__":
    # Your code goes here
    kadane_proof = [47, -98, 1, -80, 66, -98, 93, -85, 83]
    print("Maximum total sum is: ", sum_array_total(kadane_proof))

