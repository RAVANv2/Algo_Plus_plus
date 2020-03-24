//24/03/2020
#include<bits/stdc++.h>
using namespace std;

struct Node{
  int data;
  Node *left;
  Node *right;

  Node(int x)
  {
    data = x;
    right=left=NULL;
  }
};

Node* insert(int arr[],int l, int r)
{
  if(l>r) return NULL;
  int mid = (l+r)/2;
  Node *temp = new Node(arr[mid]);
  temp->left = insert(arr,l,mid-1);
  temp->right = insert(arr,mid+1,r);
  return temp;
}

void preorder(Node *root)
{
    if(root==NULL)
      return;
    cout<<root->data<<" ";
    preorder(root->left);
    preorder(root->right);
}

int main()
{
  int t,n;
  cin>>t;
  while(t--)
  {
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)
      cin>>arr[i];
    Node *root = insert(arr,0,n-1);
    preorder(root);
  }
}
