# unordered, unindexed, unchangeable, do not allow duplicate items

# set is collection of non-repititve elements

myset = {"danyal", "apple", 20}

print (myset)

print (len(myset))

print (type(myset))

# we can add items in a set

thisset = {"this", "is", "the", "addition", "of"}

thisset.add ("orange")

print (thisset)

# set constructor
sett = set(("danyal", "boy"))

print (sett)

# adding/updating set items 

set1 = {"apple", "banana", "cherry"}

set2 = {"orange", "mango", "banana"}

set1.update(set2)

print (set1)

# adding list, tuple, dictionary to a set

list1 = ["papaya"]

set1.update(list1)

print (set1)

# removing item from a set (if item is not present then .remove through an error)

r_set = {"apple", "banana", "cherry"}

r_set.remove("cherry")

print (r_set)

# discarding item from a set (if item is not present then there will be no error)

d_set = {"apple", "banana", "cherry"}

d_set.discard("banana")

print (d_set)

# .pop will remove last(any.. unordered) item
# Sets are unordered, so when using the pop() method, you do not know which item that gets removed. 

p_set = {"apple", "banana", "cherry"}

p_set.pop()

print (p_set)

# union/update and intersection of two sets

set_a = {"a", "b", "c"}

set_b = {"a", 1, 2, 3}

set_c = set_a.intersection(set_b)

print (set_c)