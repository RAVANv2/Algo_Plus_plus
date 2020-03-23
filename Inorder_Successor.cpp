//23/03/2020

--------------------------
You have to check following condition
1-> root==NULL;
2-> Only one element in BST
3-> If the target element is the last element in vector than it gives segmentation falut
--------------------------

void inorder(Node *root,Node *x,vector<Node*> &v)
{
  if(root==NULL)
    return;
  inorder(root->left,x,v);
  v.push_back(root);
  inorder(root->right,x,v);
}

Node * inOrderSuccessor(Node *root, Node *x)
{
  int i=0;
  vector<Node*> v;
  if(root==NULL)
    return NULL;
  if(root->left==NULL && root->right==NULL)
    return NULL;
  inorder(root,x,v);
  for(i=0;i<v.size();i++)
  {
    if(v[i]->data == x->data)
      break;
  }
  i++;
  if(i>=v.size())
    return NULL
  return v[i];
}
