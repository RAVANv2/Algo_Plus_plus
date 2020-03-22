//22/03/2020
#include<bits/stdc++.h>
using namespace std;

struct node_t{
    int data;
    node_t *left;
    node_t *right;
};

node_t* insertToBST(node_t *root,int key)
{
  if(root==NULL)
  {
    node_t *temp = new node_t;
    temp->data=key;
    temp->left=temp->right=NULL;
    return temp;
  }
  if(root->data>key)
  root->left = insertToBST(root->left,key);
  else if(root->data<key)
  root->right = insertToBST(root->right,key);
}

void postorder(node_t *root)
{
  if(root==NULL)
    return;
  postorder(root->left);
  postorder(root->right);
  cout<<root->data<<" ";
}


int main()
{
  int t;
  cin>>t;
  if(t<10)
  {
    int testcase=t;
    while(testcase--)
  {
    int n,ele;
    node_t *root = new node_t;
    root=NULL;
    cin>>n;
    while(n--)
    { cin>>ele;
      root = insertToBST(root,ele);
    }
    postorder(root);
  }
  }
  else
  {
    int n,ele;
    node_t *root = new node_t;
    root=NULL;
    while(t--)
    { cin>>ele;
      root = insertToBST(root,ele);
    }
    postorder(root);
  }

  }
