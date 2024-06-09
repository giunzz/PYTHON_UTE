#include<bits/stdc++.h>
using namespace std;

string s;
int main()
{
    int t;
    cin >> t;
    while(t--)
    {
        cin >> s;
        string ans = "";
        stack<char> f;
        for (int i = 0; i < s.length(); i++)
        {
            if (s[i] >= 'a' && s[i] <= 'z') ans += s[i];
            else if (s[i] == '+' || s[i] == '-' || s[i] == '*' || s[i] == '/' || s[i] == '^') f.push(s[i]);
            else if (s[i] == ')')
            {
                ans += f.top();
                f.pop();
            }
        }
        cout << ans <<endl;
    }
}