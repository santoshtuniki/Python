nums = { 1, 2, 3, 4 }

nums2 = set((1, 2, 3, 4))

print(nums)                                     #   {1, 2, 3, 4}

print(nums2)                                    #   {1, 2, 3, 4}

print(type(nums))                               #   <class 'set'>

print(len(nums2))                               #   4


# No duplicates allowed

nums = { 1, 2, 3, 4, 2, 3, 5 }

print(nums)                                     #   {1, 2, 3, 4, 5}


# True is a duplicate of 1 & False is a duplicate of 0

nums = { 1, True, 2, False, 5, 3, 0 }

print(nums)                                     #   {False, 1, 2, 3, 5}


# First occurance is taken and duplicate not considered 

nums = { True, 2, False, 5, 1, 3, 0 }

print(nums)                                     #   {False, True, 2, 3, 5}


# Check if a value is in a set

print(2 in nums)                                #   True


# Cannot refer to an element with an index position or a key