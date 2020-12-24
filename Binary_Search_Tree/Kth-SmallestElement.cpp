//21/03/2020

---------------Approch-------------------------
We Know that the inorder of BST is same as sorting the Tree
Therefore we store the inorder element in vector return the (k-1)th element from the vector
If the (len of vector < k) then return -1


void inorder(Node *root,vector<int> &v)
{
  if(root==NULL)
    return;
  inorder(root->left,v);
  v.push_back(root->data);
  inorder(root->right,v);
}

int KthSmallestElement(Node *root, int k)
{
  vector<int> v;
  inorder(root,v);
  return v[k-1];
}
