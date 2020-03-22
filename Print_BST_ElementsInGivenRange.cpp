//21/03/2020

---------------Approch------------------
Traverse to all element if element is between the given range than print those elements

void printNearNodes(Node *root, int l, int h)
{
  vector<int> v;
  if(root==NULL)
      return;
  printNearNodes(root->left,l,h);
  if(root->data<=h && root->data>=l)
      cout<<root->data<<" ";
  printNearNodes(root->right,l,h);
}
