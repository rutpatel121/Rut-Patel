#include <iostream> 
using namespace std; 

struct Node 
{ 
    int data; 
    struct Node* left, *right; 
}; 

//creating a new binary tree with the given value 
Node* newNode(int value)
{
	Node* node = new Node;
	node->data = value;
	node->left = node->right = NULL; 
	return node;
}

Node* insertNode(Node* curr, int value)
{
	if (curr == NULL) // the value becomes the root of the tree if its empty
		return newNode(value);
 
	if (value < curr->data) //the value gets added to the left subtree if its less than the current root and keep recurring until its added 
		curr->left = insertNode(curr->left, value);
  if (value > curr->data)//the value gets added to the right subtree if its greater than the current root and keep recurring until its added 
		curr->right = insertNode(curr->right, value); 

	return curr;
}

void printTraversal(struct Node* curr)
{
  cout << curr->data;
  cout << " "; 
}

void traverseInorder(struct Node* curr) 
{ 
    if (curr == NULL) 
        return; 
    //recurring on the left child of the current node 
    traverseInorder(curr->left); 
    //print the current node
    printTraversal(curr);
    //recurring on the right child of the current node
    traverseInorder(curr->right); 
} 
  
  int main() 
{ 
  Node* root = NULL;
  //Unsorted list
	int values[] = { 5, 8, 2 , 12, 9, 3, 7, 1 };
 
 //Sorting the list by inserting one value at a time in the tree
	for (int value : values)
		root = insertNode(root, value);

//print out the inorder of the sorted list
  cout << "\nSorted List is: \n";
	traverseInorder(root); 

  return 0; 
} 