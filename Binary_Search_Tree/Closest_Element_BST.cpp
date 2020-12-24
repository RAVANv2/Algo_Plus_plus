  //21/03/2020

  
 ---------------Approch----------------
 Checking the difference of every node with given element of k
 print the minimum difference in the entire BST


void sol(Node *root,int k, int &ans)
{
  if(root==NULL)
    return;

  ans = min(ans,abs(root->data-k));
  if(root->data>k)
    sol(root->left,k,ans);
  else
    sol(root->right,k,ans);
}


int maxDiff(Node *root, int k)
{
  int ans = INT_MAX;
  sol(root,k,ans);
  return ans;
}
