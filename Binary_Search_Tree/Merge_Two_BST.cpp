//20/03/2020

/* ---------Approch---------
Store all the elements of BST in vector and then sort them
*/
void join(Node *root,vector<int>&v)    // Reciving address of vector because this change is permanent change not temperory
{
  if(root==NULL)
    return;
  join(root->left,v);
  v.push_back(root->data);
  join(root->right,v);
}

vector<int> merge(Node *root1, Node *root2)
{
  vector<int> v;
  join(root1,v);
  join(root2,v);
  sort(v.begin(),v.end())
  return v;
}
