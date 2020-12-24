//24/03/2020

Node* insert(Node* node, int data)
{
    if(node==NULL)
    {
      Node *temp;
      temp = newNode(data);
      return temp;
    }

    if(node->data>data)
      node->left = insert(node->left,data);
    else
      node->right = insert(node->right,data);

      return node;
}
