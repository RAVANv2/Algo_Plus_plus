//20/03/2020
#include<bits/stdc++.h>
using namespace std;
int uniqueNo(long long int n,long long int k)
{ long long int res=1;
  if(k>n-k)
    k=n-k;
  for(long long int i=0;i<k;i++)
  {
    res *=(n-i);
    res /=(i+1);
  }
  // cout<<"res :"<<res<<endl;
  return res;
}

long long int numTrees(int n)
{
  long long int count;
  count=uniqueNo(2*n,n);
  // cout<<"coount :"<<count<<endl;
  return count/(n+1);
}

int main()
{
  int n;
  cin>>n;
  cout<<numTrees(n);
}
