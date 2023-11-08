nums = { 1, 2 , 3, False, 5}

print(nums)                                     #   {False, 1, 2, 3, 5}

# Add elements to set

nums.add(8)

print(nums)                                     #   {False, 1, 2, 3, 5 8}


# Add elements from one set to another

nums2 = { 11, 23, 55, "Hi", True}

print(nums2)                                    #   {True, 'Hi', 55, 23, 11}

nums.update(nums2)

print(nums)                                     #   {False, 1, 2, 3, 5, 'Hi', 8, 11, 23, 55}


# You can use update with list, tuple or dictionary

# Merge 2 sets to create a new set

one = {1, 2, 3}

two = {4, 5, 6}

member1 = one.union(two)

print(member1)                                  #   {1, 2, 3, 4, 5, 6}


# Keep only the duplicates

one = {1, 2, 3}

two = {4, 3, 6, 2}

member2 = one.intersection(two)

print(member2)                                  #   {2, 3}

one.intersection_update(two)

print(one)                                      #   {2, 3}



# Keep everything except the duplicates

one = {1, 2, 3}

two = {4, 3, 6, 2}


member3 = one.symmetric_difference(two)

print(member3)                                  #   {1, 4, 6}

one.symmetric_difference_update(two)

print(one)                                      #   {1, 4, 6}