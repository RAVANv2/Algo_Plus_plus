//20/03/2020
#include<bits/stdc++.h>
using namespace std;

int catalan(int n,int k)
{
  int res=1;
  if(k>n-k)
    k = n-k;
  for(int i=0;i<k;i++)
  {
    res *=(n-i);
    res /=(i+1);
  }
  return res;
}

int main()
{
  int t;
  cin>>t;
  while(t--)
  {
    int n,count;
    cin>>n;
    count = catalan(2*n,n);
    count = count/(n+1);
    cout<<count<<endl;
  }
}
