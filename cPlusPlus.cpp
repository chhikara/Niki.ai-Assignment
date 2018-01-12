#include<iostream>
#include<cstdio>
#include<math.h>
#include<algorithm>
#include<string>
#include<string.h>
#include<ctype.h>
 
#define mod 1000000007 
#define ll long long 
#define ull unsigned long long 
 
using namespace std;
 
ll a[2][2],sq[2][2],res[2][2];
 
void set( )
{
    res[0][0]=1;res[0][1]=0;res[1][0]=0;res[1][1]=1 ;
    a[0][0]=1;a[0][1]=1;a[1][0]=1;a[1][1]=0;
}
 
 
void copy(ll b[2][2],ll a[2][2])  //copies a to b
{
    for(int i=0;i<2;i++)
    for(int j=0;j<2;j++)
    b[i][j]=a[i][j];
}
 
void mul(ll A[2][2],ll B[2][2])
{
    for(int i=0;i<2;i++)
    {
        for(int j=0;j<2;j++)
        {
            sq[i][j]=0;
            for(int k=0;k<2;k++)
            sq[i][j]=(sq[i][j]+(A[i][k]*B[k][j])%mod)%mod;
        }
    }
    
    copy(A,sq);
}
 
 
void exponentiation(int exp)
{
    set();
    while(exp)
    {
        if(exp&1)
        mul(res,a);
        
        mul(a,a);
        exp/=2;
    }
}
 
 
int main()
{
    int t,n;
    
    cin>>t;
    while(t--)
    {
        cin>>n;
        
        exponentiation(n-1);
        
        cout<<res[0][0]<<endl;
        
    }
    return 0;
} 