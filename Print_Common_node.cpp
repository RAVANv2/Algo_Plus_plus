
void inorder(Node *root,vector<int> &v)
{
  if(root==NULL)
    return;
  inorder(root->left,v);
  v.push_back(root->data);
  inorder(root->right,v);
}


void printCommon(Node *root1, Node *root2)
{
  vector<int> v1,v2;
    if(root1==NULL || root2==NULL)
      return;
    inorder(root1,v1);
    inorder(root2,v2);

    for(auto i=v1.begin();i!=v1.end();i++)
    {
      for(auto j=v2.begin();j!=v2.end();j++)
      {
        if(*i==*j)
          cout<<*i<<" ";
      }
    }
}
