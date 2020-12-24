//22/03/2020
void inorder(Node *root,vector<int> &v)
{
  int i=0;
  if(root==NULL)
    return;
  inorder(root->left,v);
  v.push_back(root->data);
  inorder(root->right,v);
}


bool isPairPresent(struct Node *root, int target)
{
  if(root==NULL)
    return false;
  vector<int> v;
  inorder(root,v);

  int l=0;
  int r = v.size()-1;
  while(l<r)
  {
    if(v[l]+v[r]==target)
      return true;
    else if(v[l]+v[r]<target)
      l++;
    else
      r--;
  }
  return false;
}
