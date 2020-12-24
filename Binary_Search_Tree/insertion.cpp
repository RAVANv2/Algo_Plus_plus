//22/03/2020
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
  cout<<"Enter the element "<<endl;
  cin>>x;
  if(x==-1)
    return NULL;
  else{
    temp->data = x;
    cout<<"Enter the left child :"<<x<<endl;
    temp->left = input();
    cout<<"Enter the right child :"<<x<<endl;
    temp->right = input();
  }
  return temp;
}

void inorder(node_t *root)
{
  if(root==NULL)
    return;
  inorder(root->left);
  cout<<root->data<<" ";
  inorder(root->right);
}

node_t* Insert(node_t *root,int key)
{
  node_t *r;
  node_t *start = root;
  if(root==NULL)
    return NULL;
  while(root!=NULL)
  {   r = root;
    if(root->data==key)
      return NULL;
    else if(root->data>key)
      root = root->left;
    else
      root = root->right;
  }
  node_t *temp=new node_t;
  temp->data = key;
  temp->left=temp->right=NULL;
  if(temp->data>r->data)
    r->right = temp;
  else
    r->left = temp;
  r = start;
  return r;
}

int main()
{ int ch;
  node_t *root=new node_t;
  do
  {
    cout<<"\n1. Input"<<endl;
    cout<<"2. Insertion"<<endl;
    cout<<"3. Inorder"<<endl;
    cout<<"4. Exit"<<endl;
    cin>>ch;

    if(ch==1)
    {
      root = input();
    }

    if(ch==2)
    { int key;
      cout<<"Enter the element :";
      cin>>key;
      root=Insert(root,key);
    }

    if(ch==3)
    {
      inorder(root);
    }
  }while(ch!=4);
}
