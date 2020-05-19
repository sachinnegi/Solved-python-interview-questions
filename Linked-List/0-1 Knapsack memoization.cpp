#include <iostream>
#include<bits/stdc++.h>
using namespace std;
//int n=1000+1;
int dp[1000+1][1000+1];

int knapsack(int value[], int weight[], int W, int n){
    if ( n==0 || W==0)              //base condition is use in initialiaztion of bottom up(tabulation method)
        return 0;
    else if (dp[n][W] != -1)
        return dp[n][W];
    else if ( W < weight[n-1] )
        return dp[n][W] = knapsack(value, weight, W, n-1);
    else
        return dp[n][W] = max( value[n-1]+ knapsack(value, weight, W-weight[n-1], n-1), knapsack(value, weight, W, n-1));
        
        
}

void solve(){
    int n,W;
    cin>>n; cin>>W;
    int value[n],weight[n];
    for (int i=0; i<n;i++) cin>>value[i];
    for (int i=0; i<n;i++) cin>>weight[i];
    cout<<knapsack(value,weight,W,n)<<'\n';
    
    
}

int main() {
    memset(dp,-1,sizeof(dp));
	int t;
	cin>>t;
	while(t--){
	    solve();
	}
	return 0;
}
