### len()

    Returns the length of the list

### Slicing is spplicable and is same as String slicing

    list[A:B] => Returns a new list containing elements including index A but excluding index B


# MUTATE the list

### append(el)

    To add an item to the end of the list

### insert(A, el)

    To insert a list item(el) at a specified index(A)

### extend(listB)

    To append elements from another list(listB) to the current list


### To change the value of a specific item

    Use index number

        Ex: fruits[2] = 'Berry'

### To change the value of items within a specific range

    1.  Define a list with the new values
    
        Refer to the range of index numbers where you want to insert the new values

            Ex: fruits[1:3] = ["kiwi", "watermelon"]

    2.  If you insert more items than you replace
    
        The new items will be inserted where you specified, and others will move accordingly

            Ex: fruits[1:2] = ["kiwi", "watermelon"]

    3.  If you insert less items than you replace
    
        The new items will be inserted where you specified, and others will move accordingly

            Ex: fruits[1:3] = ["watermelon"]


### remove(el)

    1.  Removes the specific value from the list

    2.  If the item has duplicates, it removes the first occurance

### pop(indexA)

    1.  Removes and returns the value at the specified index(indexA)

    2.  If you do not specify the index, it removes the last item.

### del

    1.  Removes the value at specific index(indexA)

        Ex: del list(indexA)

    2.  It can also delete the list completely.

        Ex: del list

### clear()

    Empties the list and returns the list that is empty.


### sort()

    1.  Sort the list in ascending order and return None

    2.  Capitalized words are arranged in ascending order first, then the lowercase words

        Ex: ['Bob', 'Jason', 'Kumar', 'Sai', 'dave', 'john']

    3.  To sort irrespective of capitalize/lowercase words:

            list.sort(key=str.lower)
        
        This also makes list include lowercase letters to sort in ascending order

    4.  To sort in reverse(descending) order:

            list.sort(reverse=True)


## list.reverse()

    Returns a list with elements reversed in original list

        Ex: mylist = [10, 2, 4, 77]

            mylist.reverse()    =>  [77, 4, 2, 10]


## NO MUTATION

### Get sorted array without mutating original array

    Returns a new list containing elemnts in ascending order

    1.  sorted(fruits)

    2.  sorted(fruits, reverse=True)


### Copy the list

    1.  myList.copy()

    2.  list(myList)

    3.  myList[:]

