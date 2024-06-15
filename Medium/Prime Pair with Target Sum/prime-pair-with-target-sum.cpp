//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

class Array {
  public:
    template <class T>
    static void input(vector<T> &A, int n) {
        for (int i = 0; i < n; i++) {
            scanf("%d ", &A[i]);
        }
    }

    template <class T>
    static void print(vector<T> &A) {
        for (int i = 0; i < A.size(); i++) {
            cout << A[i] << " ";
        }
        cout << endl;
    }
};


// } Driver Code Ends

class Solution {
  public:
    vector<int> getPrimes(int n) {
        // code here
        vector<int> ans(2,-1);
        vector<bool> v(n+1,true);
        v[1]=false;
        v[0]=false;
        for(int i=2;i*i<=n;i++)
        {
            if(v[i])
            {
               for(int j = i*i ; j<=n;j+=i)
            {
                v[j]=false;
            } 
            }
            
        }
        map<int,int> m;
        for(int i= 2; i<=n ;i++)
        {
            if(v[i]) m[i]++;
        }
        for(auto i : m)
        {
            int x = i.first;
            int y = n - x;
            if(m.find(y)!=m.end())
            {
                ans[0]=x;
                ans[1]=y;
                return ans;
            }
            
        }
        return ans;
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    scanf("%d ", &t);
    while (t--) {

        int n;
        scanf("%d", &n);

        Solution obj;
        vector<int> res = obj.getPrimes(n);

        Array::print(res);
    }
}

// } Driver Code Ends