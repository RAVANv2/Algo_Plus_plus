//22/03/2020
#include<bits/stdc++.h>
using namespace std;

struct node_t{
  int data;
  node_t *left;
  node_t *right;
};

node_t* insert(node_t *root,int key)
{
  if(root==NULL)
  {
    node_t *temp=new node_t;
    temp->data = key;
    temp->left=temp->right=NULL;
    return temp;
  }
  if(root->data>key)
    root->left = insert(root->left,key);
  else if(root->data<key)
    root->right = insert(root->right,key);
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

node_t* minValueNode(node_t *root)
{
  node_t *current = root;
  while(current && current->left!=NULL)
    current = current->left;
  return current;
}

node_t* deleteNode(node_t *root,int del)
{
  if(root==NULL)
    return root;
  else if(del < root->data)
    root->left = deleteNode(root->left,del);
  else if(del>root->data)
    root->right = deleteNode(root->right,del);
  else
  {
    if(root->left==NULL)
    {
      node_t *temp = root->right;
      free(root);
      return temp;
    }
    else if(root->right==NULL)
    {
      node_t *temp = root->left;
      free(root);
      return temp;
    }
    node_t *temp = minValueNode(root->right);
    root->data = temp->data;
    root->right = deleteNode(root->right,temp->data);
  }
  return root;
}

int main()
{ int ch;
  node_t *root=NULL;
  do
  {
    cout<<"\n1. Input"<<endl;
    cout<<"2. Delete"<<endl;
    cout<<"3. Inorder"<<endl;
    cin>>ch;

    if(ch==1)
    { int n;
      cout<<"Enter the node count :"<<endl;
      cin>>n;
      int arr[n];
      cout<<"Enter the tree elements"<<endl;
      for(int i=0;i<n;i++)
        cin>>arr[i];
      for(int i=0;i<n;i++)
        root = insert(root,arr[i]);
    }
    if(ch==2)
    { int del;
      cout<<"Enter the deleted element"<<endl;
      cin>>del;
      root = deleteNode(root,del);
    }
    if(ch==3)
    {
      inorder(root);
    }
  }while(ch!=4);
}
