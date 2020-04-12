class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linkedList:

    def __init__(self):
        self.head = node()

    def display(self):
        currNode = self.head
        while currNode.next!= None:
            currNode = currNode.next
            print(currNode.data)
        

    def append(self,data):
        new_node = node(data)
        currNode = self.head
        while currNode.next != None:
            currNode = currNode.next
        currNode.next = new_node

    def getLength(self):
        currNode = self.head
        curLen = 0
        while currNode.next != None:
            curLen+=1
            currNode = currNode.next
        return print(curLen)
        

    def getEle(self,index):
        currIdx = 0
        currNode = self.head
        while currNode.next != None:
            currNode = currNode.next
            if index == currIdx: 
                return print(currNode.data)
            currIdx += 1

    def delete(self,index):
        currIdx = 0
        currNode = self.head
        while currNode.next != None:
            last_node = currNode
            currNode = currNode.next
            if index == currIdx:
                last_node.next = currNode.next
                return
            currIdx += 1

    def insert(self,index,data):
        currIdx = 0
        currNode = self.head
        prevNode = self.head
        while currNode != None:
            currNode = currNode.next
            if currIdx == index :
                newNode = node(data)
                prevNode.next = newNode
                newNode.next = currNode
                return
            prevNode = currNode
            currIdx += 1





Li = linkedList()
Li.append(1)
Li.append(2)
Li.append(3)
Li.append(4)
Li.append(5)
Li.append(6)
Li.display()

print("\n ")

Li.insert(3,10)
Li.display()
print("\n ")

Li.insert(1,8)
Li.display()
print("\n ")