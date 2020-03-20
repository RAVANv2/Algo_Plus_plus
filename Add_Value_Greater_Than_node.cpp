//20/03/2020

// Medium
/*----------Approch--------
The inorder of BST is same as sorting the tree so i find inorder in vector and update the array's element by its sum fo all greater elements
*/

vector<Node*> v;
void inorder(Node *root)
{
  if(root==NULL)
    return;
  inorder(root->left);
  v.push_back(root);
  inorder(root->right);
}
void modify(Node **root)
{
  inorder(*root);
  for(int i=v.size()-2; i>=0;i--)
    v[i]->data += v[i+1]->data;
}
