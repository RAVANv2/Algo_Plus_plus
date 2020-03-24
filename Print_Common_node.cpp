//24/03/2020
#include<bits/stdc++.h>
using namespace std;

struct Node{
  int data;
  Node *left;
  Node *right;
};

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

void inorder(Node *root,vector<int> &v)
{
  if(root==NULL)
    return;
  inorder(root->left,v);
  v.push_back(root->data);
  inorder(root->right,v);
}

void printCommon(Node *root1, Node *root2)
{
  vector<int> v1,v2;
    if(root1==NULL || root2==NULL)
      return;
    inorder(root1,v1);
    inorder(root2,v2);

    for(auto i=v1.begin();i!=v1.end();i++)
    {
      for(auto j=v2.begin();j!=v2.end();j++)
      {
        if(*i==*j)
          cout<<*i<<" ";
      }
    }
}

int main()
{
  int arr[100],ch,ch2;
  Node *root1 = new Node;
  root1=NULL;
  Node *root2 = new Node;
  root2=NULL;
  while(ch!=-1)
  {
    cin>>ch;
    if(ch!=-1)
    {
      root1=Insert(root1,ch);
    }
  }
  cout<<"Enter root2 :"<<endl;
  while(ch2!=-1)
  {
    cin>>ch2;
    if(ch2!=-1)
    {
      root2=Insert(root2,ch2);
    }
  }
  printCommon(root1,root2);

}
