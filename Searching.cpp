#include<bits/stdc++.h>
using namespace std;

struct node_t{
  int data;
  node_t *left;
  node_t *right;
};

node_t* input()
{ int x;
  node_t *temp = new node_t;
  cout<<"Enter the element :"<<endl;
  cin>>x;
  if(x==-1)
    return NULL;
  else{
    temp->data = x;
    cout<<"Left child :"<<x<<endl;
    temp->left=input();
    cout<<"Right child :"<<x<<endl;
    temp->right = input();
  }
  return temp;
}

void inorder(node_t *t)
{
  if(t==NULL)
    return;
  inorder(t->left);
  cout<<t->data;
  inorder(t->right);
}

node_t* rsearch(node_t *root,int key)
{
  if(root==NULL)
  {
    cout<<"NO"<<endl;
    return NULL;
  }

  if(key == root->data)
    {cout<<"YES"<<endl;return root;}

  else if(key<root->data)
    return rsearch(root->left,key);
  else
    return rsearch(root->right,key);
}

void search(node_t *t,int key)
{
  if(t==NULL)
    return;
  while(t!=NULL)
  {
    if(t->data==key)
    {cout<<"YES"<<endl;break;}
    else if(t->data>key)
      t = t->left;
    else
      t = t->right;
  }
  if(t==NULL)
    cout<<"NO"<<endl;
}

int main()
{
  int ch;
  node_t *root = new node_t;
  node_t *temp;
  do
  {
    cout<<"\n1. Input"<<endl;
    cout<<"2. Recursive Search"<<endl;
    cout<<"3. Non-Recursive Search"<<endl;
    cout<<"4. Inorder Search"<<endl;
    cout<<"5. Exit"<<endl;
    cin>>ch;
    if(ch==1)
    {
      root = input();
    }
    if(ch==2)
    {
      int key;
      cout<<"Enter the serching key"<<endl;
      cin>>key;
      temp = rsearch(root,key);
    }
    if(ch==3)
    {
      int key;
      cout<<"Enter the serching key"<<endl;
      cin>>key;
      search(root,key);
    }
    if(ch==4)
    {
      inorder(root);
    }
  }while(ch!=5);
}
