#include <bits/stdc++.h>
using namespace std;
#define int long long
signed main()
{
   int test;
   cin>>test;
   while(test--)
   {
       int start,end;
       cin>>start>>end;

        int result = INT_MAX;

       int arr[start];

       for(int i=0;i<start;i++)
       {
           cin>>arr[i];
       }

       if(end==1)
       {
           cout<<0<<endl;
           continue;
       }

       sort(arr,arr+start);
       
       for(int i=0;i<=start-end;i++)
       {
           if(arr[i+end-1]-arr[i]<result)
           {
              result=arr[i+end-1]-arr[i];
           }
       }
       
       cout<<result<<endl;
       
   }
}



