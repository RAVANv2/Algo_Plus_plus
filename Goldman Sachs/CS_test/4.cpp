    #include<bits/stdc++.h> 
    using namespace std;                          
    #pragma GCC optimize("O3")
    typedef long long ll;
    typedef long double ld;
    #define fast  ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    int main()
    {    
        
        fast
        
        
        ll n,m;
            cin>>n>>m;
            ld p[n+1];
            ld x[n+1];
            ld y[n+1];
            ld ans[n+1];
            ld final=0.00;
            for(int i=0;i<n;i++)
            {
                cin>>p[i];
            }
            for(int i=0;i<n;i++)
            {
                cin>>x[i];
            }
            for(int i=0;i<n;i++)
            {
                cin>>y[i];
            }
            for(int i=0;i<n;i++)
            {
                ans[i]=1.00*(p[i]*x[i]-((1.00-p[i])*y[i]));
            }
            sort(ans,ans+n,greater<ld>());
            
            for(int i=0;i<min(n,m);i++)
            {
                if(ans[i]>0.00)
                {
                    final+=ans[i];
                }
            }
            cout<<fixed<<setprecision(2)<<final;


        return 0;
    }