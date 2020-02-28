import sys


class Node:
  def __init__(self, key):
      self.left = None
      self.right = None
      self.key = key

  def insertIter(self, key):
      currentNode = self
      child = Node(key)
      while True:
          if key <= currentNode.key:
              if currentNode.left is None:
                  currentNode.left = child
                  return
              currentNode = currentNode.left
          else:
              if currentNode.right is None:
                  currentNode.right = child
                  return
              currentNode = currentNode.right

  def deleteRoot(self, node):
      if node == None:
          return None
      if node.left == None:
          return node.right
      if node.right == None:
          return node.left
      
      nxt = self.findMinIter(node.right)
      nxt.left = node.left
      return node.right

  def deleteIter(self, node, node_delete):
      current = node
      previous = None
      while current != None and current.key != node_delete:
          previous = current
          if node_delete < current.key:
              current = current.left
          elif node_delete > current.key:
              current = current.right

      if previous == None:
          return self.deleteRoot(current)
      if previous.left == curr:
          previous.left = self.deleteRoot(current)
      else:
          previous.right = self.deleteRoot(current)
  
      return root

# print("hi")
  def findMinIter(self, node = None):
      currentNode = self if node is None else node
      while currentNode.left is not None:
          currentNode = currentNode.left
      return currentNode
# print("hi")
  def findMaxIter(self):
      currentNode = self
      while currentNode.right is not None:
          currentNode = currentNode.right
      return currentNode
# print("hi")

  def findNextIter(self, node, key):
      temp = node
      while temp != key and temp.key != key:
          if key < temp.key:
              temp = temp.left
          elif key > temp.key:
              temp = temp.rigt
      checker = None
      if temp.right:
          checker = temp.right
          while checker.left:
              checker = checker.left
          return checker
      while node:
          if temp.key < node.key:
              checker = node
              node = node.left
              continue
          elif temp.key > node.key:
              node = node.right
            # continue
          else:
              break

      return checker
# print("hi")
  def findPrevIter(self, node, key):
      if node is None:
          return node
      temp = node    
      previousNode = None
      while temp != key and temp.key != key:
          if key > temp.key:
              temp = temp.right
          elif key < temp.key:
              previousNode = temp
              temp = temp.left

          if temp and temp.right:
              checker = temp.right
          while checker.left:
              checker = checker.left
          return checker
      return previousNode

# print("hi")
def printInorder(root):
  if root is not None:
      printInorder(root.left)
      print(root.key),
      printInorder(root.right)
# print("hi")      
def main():
  root = Node(2)
  root.insertIter(1)
  printInorder(root)
  print("end")
  root.insertIter(6)
  printInorder(root)
  print("added6")
  root.insertIter(5)
  printInorder(root)
  print("added5")
  root.insertIter(4)
  printInorder(root)
  print("added4")
  root.insertIter(3)
  printInorder(root)
  print("added3")
  root = root.deleteIter(root, 2)
  printInorder(root)
  print("deleted2")

if __name__ == "__main__":
  main()
