# spiral

[![Python package](https://github.com/vcu-chfauerbach/spiral/actions/workflows/pytest.yml/badge.svg)](https://github.com/vcu-chfauerbach/spiral/actions/workflows/pytest.yml)

What is the sum of the numbers on the diagonals in a 501 by 501 spiral formed in the same way?


    def test_spiral(a):  
 
 
     squaresList = [i*i for i in range(1, a+1) if (i % 2 != 0)]
     nums = [i for i in range(1, a*a+1) if (i % 2 != 0)]

     index = 0
     b = 0
     totalSum = 0

     for i in nums:

         totalSum += nums[index]

         if (nums[index] == nums[len(nums)-1]):
             break

         if (nums[index] in squaresList):
             b += 1

         index += b 

     return totalSum
    
    print(test_spiral(int(input())))
