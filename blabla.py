# Adjacency List
from inspect import stack
import queue
from re import T


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
 
    def is_empty(self):
        if(self.head == None):
            return True
        return False
 
    def enQueue(self, node):
        if(self.is_empty()):
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node
 
    def deQueue(self):
        if(self.is_empty()):
            return None
        node = self.head
        self.head = self.head.next
        node.next = None
        return node
 
    def print(self):
        temp = self.head
        while(temp != None):
            print(temp.data, end=" ")
            temp = temp.next
        print()

class Stack:
    def __init__(self):
        self.top = None
 
    def is_empty(self):
        if(self.top == None):
            return True
        return False
 
    def push(self, node):
        node.next = self.top
        self.top = node
 
    def pop(self):
        if(not self.is_empty()):
            node = self.top
            self.top = self.top.next
            node.next = None
            return node
        return None
 
    def print(self):
        temp = self.top
        while(temp != None):
            print(temp.data, end=" ")
            temp = temp.next
        print()
        
class Graph:
    def __init__(self, size):
        self.graph = [None for _ in range(size)]
        
    def addEdge(self, start, dest):
        newNode = Node(dest)
        newNode.next = self.graph[start]
        self.graph[start] = newNode
        
        newNode = Node(start)
        newNode.next = self.graph[dest]
        self.graph[dest] = newNode
        
    def printGraph(self):
        for i in range(len(self.graph)):
            print('Vertice', i, end=': ')
            itr = self.graph[i]
            while (itr):
                print(itr.data, end='-->')
                itr = itr.next
            print()
            
    def BFS(self, source):
        visited = [False for _ in range(len(self.graph))]
        queue = Queue()
        visited[source] = True
        queue.enQueue(Node(source))
        print("BFS:", end= " ")
        while(not (queue.is_empty())):
            src = queue.deQueue().data
            print(chr(src + 65), end = ", ")
            
            itr = self.graph[src]
            while (itr):
                if (not visited[itr.data]):
                    visited[itr.data] = True
                    queue.enQueue(Node(itr.data))
                itr = itr.next
        print()

    def DFS(self, source):
        visited = [False for _ in range(len(self.graph))]
        stack = Stack()
        visited[source] = True
        stack.push(Node(source))
        print("DFS:", end= " ")
        while(not (stack.is_empty())):
            src = stack.pop().data
            print(chr(src + 65), end = ", ")
            
            itr = self.graph[src]
            while (itr):
                if (not visited[itr.data]):
                    visited[itr.data] = True
                    stack.push(Node(itr.data))
                itr = itr.next
        print()

g = Graph(6)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,4)
g.addEdge(3,4)
g.addEdge(3,5)
g.addEdge(4,5)

g.BFS(0)
g.DFS(0)