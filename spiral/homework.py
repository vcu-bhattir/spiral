def spiralize(number):
    
    squaresList = [i*i for i in range(1, number+1) if (i % 2 != 0)]
    nums = [i for i in range(1, number*number+1) if (i % 2 != 0)]

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

