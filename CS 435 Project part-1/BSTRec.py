import sys

class Node:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.key = key
  
  def insertRec(self, key):
    child = Node(key)
    if key >= self.key:
      if self.right is None:
        self.right = child
      else:
        self.right.insertRec(key)
    else:
      if self.left is None:
        self.left = child
      else:
        self.left.insertRec(key)
    
  """
  def deleteRec(root, key):
    if not root:
      return root
    if key < root.key:
      root.left = deleteRec(root.left, key)
    elif(key > root.key):
      root.right= deleteRec(root.right, key)
  """
  def deleteRec(self, key):
    if self is None:
      return self
    if key > self.key and self.right is not None:
      self.right = self.right.deleteRec(key)
    elif key < self.key and self.left.key is not None:
      self.left = self.left.deleteRec(key)
    else:
      if self.left is None: 
        move = self.right
        self = None
        return move
      elif self.right is None:
        move = self.left
        self = None
        return move
      elif self.right is not None:
        successor_inorder = self.right
        while right.left is not None:
          successor_inorder = successor_inorder.left
        self.key = inorder_successor.key
        self.right = self.right.deleteRec(inorder_successor.key)  
    return self
  
def findMinRec(node):
  if node is None:
    return node
   #    if node.left == None:
  #        return node.key 
  # return findMinRec(node.left)
  temp = node
  while temp.left:
    temp = temp.left
  return temp.key

def findMaxRec(node):
  #if self.right is not None:
   # maxNode = self.right.findMaxRec()
  #return maxNode
  if node is None:
    return -sys.maxsize
  return max(node.key, findMaxRec(node.left), findMaxRec(node.right))
  
def findNextRec(node, key):
  auto = None
  
  if node is None:
    return
  temp = node
  #child = self.findRec(key)
  #if child is None:
  #  return 
  #elif child.right is None:
  if node.key == key:
    checker = None
    if temp.left:
      checker = temp.left
      while checker.rigth:
        checker = checker.right
      return checker
    else:
      return auto
  elif key < node.key:
    return findNextRec(node.left, key, auto=node)
  else:
    return findNextRec(node.right, key, auto=node)

def findPrevRec(node, key):
  auto = None
  if node is None:
    return
  temp = node
  #child = self.findRec(key)
  #if child is None:
    #return 
  #elif child.left is None:
  if node.key == key:
    checker = None
    if temp.left:
      checker = temp.left
      while checker.right:
        checker = checker.right
      return checker
    else:
      return auto
  elif key < node.key:
    return findPrevRec(node.left, key, auto=node)
  else:
    return findPrevRec(node.right, key, auto=node)
  
def sortHelper(child, arr):
  if child is None:
    return None
  sortHelper(child.left, arr)
  arr.append(child.key)
  sortHelper(child.right, arr)

def sort(arr):
  if len(arr) == 0: return None
  root = Node(arr[0])
  for element in arr[1:]:
    root.insertRec(element)
  sorted_arr = list()
  sortHelper(root, sorted_arr)
  return sorted_arr

def printInorder(root):  
    if root is not None:
        printInorder(root.left) 
        print(root.key), 
        printInorder(root.right)

def main():
  root = Node(21)
  root.insertRec(19)
  root.insertRec(25)
  root.insertRec(15)
  root.insertRec(18)
  root.insertRec(11)
  root = root.deleteRec(25)
  printInorder(root)
  print
  print('min',findMinRec(root))
  print('max',findMaxRec(root))
  pass
  

if __name__ == "__main__":
  main()
