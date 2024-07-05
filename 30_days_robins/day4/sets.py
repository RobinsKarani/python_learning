'''
Removing Items from a Set
We can remove an item from a set using remove() method.
If the item is not found remove() method will raise errors,
so it is good to check if the item exist in the given set.
However, discard() method doesn't raise any errors.
'''

# item1 = "value1"
# item2 = "value2"
# item3 = "value3"
# item4 = "value4"
# item5 = "value5"
#
# my_set = {item1, item2, item3, item4, item5}
# my_set.remove(item3)


# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item2', 'item3'}
# st2.difference(st1)  # set()
# st1.difference(st2)  # {'item1', 'item4'} => st1\st2

'''Finding Symmetric Difference Between Two Sets
It returns the the symmetric difference between two sets.
It means that it returns a set that contains all items from both sets,
except items that are present in both sets, mathematically: (A\B) ∪ (B\A)'''

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1)  # {'item1', 'item4'}