//23/03/2020
void inorder(Node *root,vector<int> &v)
{
  if(root==NULL)
    return;
  inorder(root->left,v);
  v.push_back(root->data);
  inorder(root->right,v);
}
void kthLargest(Node *root, int k)
{    int size;
  if(root==NULL)
    return;
  vector<int> v;
  inorder(root,v);
  size = v.size();
  cout<<v[k]<<endl;
}
