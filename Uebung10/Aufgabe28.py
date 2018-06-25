#sauce header
from random import randint


###################################

class Node:

    def __init__(self, value):
        self.pred = None
        self.succ = None
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
        count = 0
        currentNode = self.beginNode
        while currentNode != None:
            count += 1
            currentNode = currentNode.succ
        return count

    def __getitem__(self, position):
        if position < -1:
            currentNode = self.endNode
            for i in range(1, abs(position)):
                currentNode = currentNode.pred
            return currentNode.value
        elif position == -1:
            return self.endNode.value
        elif position == 0:
            return self.beginNode.value
        else:
            currentNode = self.beginNode
            for i in range(1,position+1):
                currentNode = currentNode.succ
            return currentNode.value

    def insert(self, newNodeins, position):
        if position == 0:
            #print("swag")
            newNodeins.succ = self.beginNode
            succNode = self.beginNode
            if self.beginNode != None:
                succNode.pred = newNodeins
            self.beginNode = newNodeins
            if self.endNode == None:
                self.endNode = newNodeins
                #print("ultraswag")
        elif position == -1:
            self.append(newNodeins)
        elif position < -1:
            if abs(position) > self.length():
                newNodeins.succ = self.beginNode
                self.beginNode = newNodeins
                if self.endNode == None:
                    self.endNode = newNodeins
            else:
                currentNode = self.endNode
                for i in range(1,abs(position)+1):
                    currentNode = currentNode.pred
                succNode = currentNode.succ
                succNode.pred = newNodeins
                currentNode.succ = newNodeins
                newNodeins.pred = currentNode
                newNodeins.succ = succNode
        elif position >= self.length():
            newNodeins.pred = self.endNode
            if self.endNode == None:
                self.endNode = newNodeins
                #print("schala")
                #print(self.endNode)
            if self.beginNode == None:
                self.beginNode = newNodeins
                #print("lala")
                #print(self.beginNode)
            else:
                predNode = self.endNode
                predNode.succ = newNodeins
                self.endNode = newNodeins
                #print("yolo")
        elif position > 0:
            currentNode = self.beginNode
            for i in range(1,position+1):
                currentNode = currentNode.succ
            predNode = currentNode.pred
            #print(currentNode.pred)
            predNode.succ = newNodeins
            currentNode.pred = newNodeins
            newNodeins.pred = predNode
            newNodeins.succ = currentNode

    def __delitem__(self, position):
        if position == -1:
            if self.beginNode == self.endNode:
                self.beginNode = None
                self.endNode = None
            else:
                currentNode = self.endNode
                self.endNode = currentNode.pred
                currentNode.pred = None
        elif position == 0:
            if self.beginNode == self.endNode:
                self.beginNode = None
                self.endNode = None
            else:
                currentNode = self.beginNode
                self.beginNode = currentNode.succ
                currentNode.succ = None
        elif position == self.length()-1:
            currentNode = self.endNode
            self.endNode = currentNode.pred
            predNode = currentNode.pred
            predNode.succ = None
            currentNode.pred = None
        elif position > 0:
            currentNode = self.beginNode
            for i in range(1,position):
                currentNode = currentNode.succ
            succNode = currentNode.succ
            predNode = currentNode.pred
            predNode.succ = succNode
            succNode.pred = predNode
            currentNode.succ = None
            currentNode.pred = None
        elif position < -1:
            currentNode = self.endNode
            for i in range(1,abs(position)):
                currentNode = currentNode.pred
            succNode = currentNode.succ
            predNode = currentNode.pred
            predNode.succ = succNode
            succNode.pred = predNode
            currentNode.succ = None
            currentNode.pred = None










"""
######Tests:

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")

testlist = Liste()

print(testlist.length())
testlist.insert(node1, 0)
print("##########")
print(testlist[0])
print(testlist.length())

testlist.insert(node2, 10)
print("##########")
print(testlist[0])
print(testlist[1])
print(testlist.length())

testlist.insert(node3, 1)
print("##########")
print(testlist[0])
print(testlist[1])
print(testlist[2])
print(testlist.length())

testlist.insert(node4, -3)
print("##########")
print(testlist[0])
print(testlist[1])
print(testlist[2])
print(testlist[3])
print(testlist.length())

l=Liste()
for i in range(100):
    k = randint(1,500)
    p = randint(0,99)
    print("position:",p)
    print("value k:", k, "bzw.", k//2)
    #l.insert(Node(k//2),0)
    l.insert(Node(k),p)
    l.insert(Node(k//2),0)
    print("durchlauf:",i)
    print(l[0])
    print(l[1])
    it = l.beginNode
    while it != None:
        print("value:",it.value,"Pred:", it.pred,"Succ:",it.succ)
        it = it.succ


"""



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
print(l.length())
print(len(realL))
count = 0
try:
    for i in range(max(l.length(), len(realL))):
        correct2 = (l[i] == realL[i])
        if(not correct2):
            print(realL[i], "expected at index",i)
            print(l[i], "found at index", i)
            count +=1
        correct = correct and correct2
    if correct:
        print("28.3: your list has the correct Values")
    else:
        print("28.3 still has some errors, values are incorrect")
        print(count)
except Exception as e:
    print("Evaluation did not work, some function throws an error")
    print(e)
