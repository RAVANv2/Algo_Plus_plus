//22/03/2020
#include<bits/stdc++.h>
using namespace std;

struct node_t{
  int data;
  node_t *left;
  node_t *right;
};

node_t* Insert(node_t *root, int key)
{
  if(root==NULL)
  {
    node_t *temp = new node_t;
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

void inorder(node_t *root)
{
  if(root==NULL)
    return;
  inorder(root->left);
  cout<<root->data<<" ";
  inorder(root->right);
}
int main()
{
  node_t *root = new node_t;
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
  inorder(root);
}
