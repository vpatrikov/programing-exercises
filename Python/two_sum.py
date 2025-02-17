def twoSum(self, nums, target):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
    return result

def addTwoNumbers(l1, l2):
    l1 = int(''.join(reversed(str(l1))))
    l2 = int(''.join(reversed(str(l2))))
    return l1 + l2

print(addTwoNumbers([2,3,4], [5,6,4]))