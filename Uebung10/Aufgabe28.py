#sauce header
from random import randint


###################################

class Node:

    def __init__(self, value, pred = None, succ = None):
        self.pred = pred
        self.succ = succ
        self.value = value


class Liste:

    def __init__(self, beginNode = None, endNode = None):
        self.beginNode = beginNode
        self.endNode = endNode

    def append(self, newNodeapp):
        if self.beginNode == None:
            self.beginNode = newNodeapp
        else:
            newNodeapp.pred = self.endNode
            self.endNode.succ = newNodeapp
        self.endNode = newNodeapp

    def length(self):
        pass

    def __getitem__(self, position):
        pass

    def insert(self, position, newNodeins):
        pass

    def __delitem__(self, position):
        pass




















##################################
#sauce footer:

print("#Testing for 28.1 and 28.2")
l = Liste()
realL = list()
# Try to append items in your implementation
try:
    l.append(Node(17))
    realL.append(17)
    if l.endNode.value != 17:
        print("append on empty list did not work correctly, endNode does not have the expected Value")
    if l.beginNode.value != 17:
        print("append on empty list did not work correctly, beginNode does not have the expected Value")
    l.append(Node(28))
    realL.append(28)
    if l.endNode.value != 28:
        print("append did not work correctly, endNode does not have the expected Value!")
    for i in range(100):
        k = randint(0,100)
        l.append(Node(k))
        realL.append(k)
except Exception as e:
    print("append() not working or not implemented")
    print(e)
# Try the length function
try:
    if l.length() != len(realL):
        print("length is different, some operation must have failed")
except Exception as e:
    print("length() not working or not implemented")
    print(e)
# See if both lists are equal (also test the __getitem__ implementation
try:
    correct = True
    for i in range(100):
        correct1 = l[i] == realL[i]
        if(not correct1):
            print("Element at index",i, "is", l[i])
            print("But", realL[i], "was expected")
        correct2 = l[-i-1] == realL[-i-1]
        if(not correct2):
            print("Element at index",-i-1, "is", l[-i-1])
            print("But", realL[-i-1], "was expected")
        correct = correct and correct1 and correct2
    if correct:
        print("28.1 and 28.2: your list has the correct Values")
    else:
        print("28.1 or 28.2 still have errors")
except Exception as e:
    print("operator [] not working or not implemented")
    print(e)

print("#Try some special cases (mostly for exercies 28.3)")
l = Liste()
# Note: if one call fails, all subsequent calls can also fail!
try:
    l.insert(Node(1),0)
    if(l[0] != 1):
        print("insert on empty list not working")
    l.insert(Node(2), 10)
    if(l.endNode.value != 2):
        print("insert with too big index not working, end Node does not have the correct value")
    l.insert(Node(3), 1)
    if(l[1] != 3):
        print("insert not working on regular insertion")
except Exception as e:
    print("some errors occured during testing of insert, cannot test (are all functions implemented?)")
    print(e)
try:
    if(l.length() != 3):
        print("length not working correctly (or a previous call did not insert correctly)")
    del l[2]
    if(l.length() != 2 or l.endNode.value != 3):
        print("del does not correctly remove the last element (or a previous call did not work correctly)")
    del l[0]
    if(l[0] != 3):
        print("del not working correctly on removing the first element (or a previous call did not work correctly)")
    del l[0]
    if not (l.beginNode is None and l.endNode is None):
        print("del not working correctly on single element list (or a previous call did not work correctly)")
except Exception as e:
    print("some errors occured during testing of del, cannot test (are all functions implemented?)")
    print(e)

print("#Testing general cases for 28.3")
l = Liste()
realL = list()
# Try the insert implementation and compare to real list
try:
    for i in range(100):
        k = randint(1,500)
        p = randint(0,99)
        l.insert(Node(k),p)
        realL.insert(p,k)
        l.insert(Node(k//2),0)
        realL.insert(0,k//2)
    for i in range(10):
        k = randint(1,500)
        p = randint(0,99)
        l.insert(Node(k),-p)
        realL.insert(-p,k)
except Exception as e:
    print("insert() not working or not implemented")
    print(e)
# try the __delitem__ implementation
try:
    for i in range(5):
        p = randint(0,99)
        del l[-p]
        del realL[-p]
        del l[l.length()-1]
        del realL[len(realL)-1]
except Exception as e:
    print("del list[] not working or not implemented")
    print(e)
correct = True

try:
    for i in range(max(l.length(), len(realL))):
        correct2 = (l[i] == realL[i])
        if(not correct2):
            print(realL[i], "expected at index",i)
            print(l[i], "found at index", i)
        correct = correct and correct2
    if correct:
        print("28.3: your list has the correct Values")
    else:
        print("28.3 still has some errors, values are incorrect")
except Exception as e:
    print("Evaluation did not work, some function throws an error")
    print(e)
