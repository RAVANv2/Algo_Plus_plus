//24/03/2020
#include<bits/stdc++.h>
using namespace std;

struct Node{
  int data;
  Node *left;
  Node *right;
};

void inorder(Node *root)
{
  if(root==NULL)
    return;
  inorder(root->left);
  cout<<root->data<<" ";
  inorder(root->right);
}

Node* Insert(Node *root, int key)
{
  if(root==NULL)
  {
    Node *temp = new Node;
    temp->data = key;
    temp->left=temp->right=NULL;
    return temp;
  }

  if(root->data>key)
    root->left = Insert(root->left,key);
  else if(root->data<key)
    root->right = Insert(root->right,key);
  return root;
}


Node* minValueNode(Node *root,int x)
{
  Node* current = root;
  while(current && current->left!=NULL)
    current = current->left;
  return current;
}

Node *deleteNode(Node *root,  int x)
{
  if(root==NULL)
    return root;
  else if(root->data>x)
      root->left = deleteNode(root->left,x);
  else if(root->data<x)
    root->right = deleteNode(root->right,x);
  else
  {
    if(root->left==NULL)
    {
      Node *temp=root->right;
      free(root);
      return temp;
    }
    else if(root->right==NULL)
    {
      Node *temp = root->left;
      free(root);
      return temp;
    }
    Node *temp=minValueNode(root->right,x);
    root->data = temp->data;
    root->right=deleteNode(root->right,temp->data);
  }
  // cout<<"Check"<<endl;
  return root;
}

int main()
{
  Node *root = new Node;
  root = NULL;
  int n;
  cout<<"Count of elements in BST :"<<endl;
  cin>>n;
  int arr[n];
  cout<<"Enter the elements :"<<endl;
  for(int i=0;i<n;i++)
    cin>>arr[i];
  for(int i=0;i<n;i++)
    root = Insert(root,arr[i]);

  int del;
  cout<<"Enter the element which you want to delete :"<<endl;
  cin>>del;
  root=deleteNode(root,del);
  inorder(root);
}
