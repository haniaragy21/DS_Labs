import sys


class Node:
  def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

class LinkedList:
  def __init__(self):
      self.head = None
    #################################################################
  def add(self, data):
      if self.head is None:
          NewNode= Node(data)
          NewNode.prev= None
          self.head = NewNode
          return
      else:
        NewNode= Node(data)
        currentNode = self.head
        while currentNode.next is not None:
          currentNode = currentNode.next
        NewNode.prev = currentNode
        currentNode.next = NewNode


#################################################################
  def addToIndex(self,x, num):
    if x<0:
      raise Exception
    if x==0:
      if self.head is None:
        self.head = Node(num)
        return
      else:
        NewNode = Node(num)
        NewNode.next = self.head
        self.head.prev = NewNode
        self.head = NewNode
        return
    if self.head is None and x != 0:
        raise Exception

    temp = self.head
    for _i in range(x-1):
        temp = temp.next
        if temp is None:
          raise Exception
    NewNode = Node(num)
    NewNode.prev = temp
    NewNode.next = temp.next
    temp.next = NewNode
    temp = temp.next.next
    temp.prev = NewNode
    

#################################################################
  def get(self, x):
    if x<0:
      raise Exception
    if self.head is None:   #empty list
       raise Exception
    if x > self.size():
       raise Exception
    temp = self.head
    for _i in range(x):
      temp = temp.next
    print(temp.data)
#################################################################
  def set(self, x, NewVal):
    if self.head is None:   #empty list
      raise Exception
    temp = self.head
    position = 0
    while temp is not None:
      if position == x:
        temp.data = NewVal
        return
      position += 1
      temp = temp.next

    if position <= x or x < 0:
       raise Exception

#################################################################

  def remove(self, x):
    if self.head is None or x<0: 
      raise Exception
    if x == self.size()-1:
      temp = self.head
      while temp.next is not None:
        temp = temp.next
      temp.prev.next = None
      return
    currentNode= self.head
    currentPosition= 0
    if x == 0:
      if currentNode.next is None:
        self.head = None
        return
      else:
        self.head = currentNode.next
        self.head.prev = None
        return
    while currentNode.next is not None:
       if currentPosition == x-1:
           NextNode = currentNode.next.next
           NextNode.prev = currentNode
           currentNode.next= NextNode
           return
       currentPosition +=1
       length= currentPosition + 1
       currentNode= currentNode.next

    if x > length-1 :
      raise Exception
#################################################################

  def contains (self, value):
    if self.head is None:   #empty list
      print("False")
      sys.exit()
    currentNode= self.head
    while currentNode is not None:
        if currentNode.data == value:
            print("True")
            exists = 1
            sys.exit()
        else:
            currentNode= currentNode.next
            exists = 0
    if exists == 0:
      print("False")
      sys.exit()
##########################size###################################

  def size(self):
    temp = self.head
    s=0
    while temp is not None:
      temp = temp.next
      s += 1
    return int(s)

###########################sublist###############################

  def sublist(self, x1, x2):
    if self.head is None:   
       raise Exception
    if x2 < x1:
       raise Exception
    if x2-x1 > self.size():
       raise Exception
    if x1<0 or x2<0:
      raise Exception

    temp= self.head
    sublist = LinkedList()
    position = 0  
    while 1:
      if position >= x1:
        sublist.add(temp.data)
      position+=1
      temp = temp.next
      if position == x2+1:
        break

    sublist.printList()


#################################################################
    
  def printList(self):
      if self.head is None:
        print("[]")
        return
      temp = self.head
      print("[",end="")     
      while temp.next is not None:
          print(temp.data, end=", ",flush=True)
          temp = temp.next
      print(temp.data,end="")     
      print("]")
    
#################################################################
string= sys.stdin.readline()
if(not(string and string.strip())):
       raise Exception ("Error")

string= string.replace("[", " ")
string=string.replace("]", " ")
string=string.replace(",", " ")
array1= string.split()

array2= []
for i in range (len(array1)):
    array2.append(int(array1[i]))

MyList = LinkedList()
for i in array2:
     MyList.add(i)

#################################################################
try:
  operation= input()
except:
  print("Error")#if empty string

match operation:
  case "add":
     try:
      value = input()
      MyList.add(value)
      MyList.printList()
     except:
      print("Error")


  case "addToIndex":
    indx = sys.stdin.readline()
    newelmnt = sys.stdin.readline()
    try:
      Indx= int(indx)
      NewElmnt= int(newelmnt)
      MyList.addToIndex(Indx,NewElmnt)
      MyList.printList()
    except:
      print("Error")

  case "get":
    skips = sys.stdin.readline()
    try:
      Skips= int(skips)
      MyList.get(Skips)
    except:
      print("Error")

  case "set":
    try:
      indx = sys.stdin.readline()
      newelmnt = sys.stdin.readline()
      Indx= int(indx)
      NewElmnt= int(newelmnt)
      MyList.set(Indx,NewElmnt)
      MyList.printList()
    except:
      print("Error")


  case "clear":
        MyList.head = None
        print("[]")


  case "isEmpty":
       if MyList.head is None:
         print("True")
       else:
         print("False")

  case "remove":
    try:
     indx = sys.stdin.readline()
     Indx= int(indx)
     MyList.remove(Indx)
     MyList.printList()
    except:
      print("Error")

  case "size":
    print(MyList.size())

  case "sublist":
    try: 
       indx1 = sys.stdin.readline()
       indx2 = sys.stdin.readline()
       Indx1= int(indx1)
       Indx2= int(indx2)
       MyList.sublist(Indx1,Indx2)  
    except:
      print("Error")

  case "contains":
    try:
       val= input()
       MyList.contains(int(val))
    except ValueError:
        print("Error")
  case _:
    print ("Error")
