/*

Problem statement
You are given two strings 'A' and 'B' of length 'N' and 'M' respectively.

Return the string that has more distinct subsequences, if both strings have the same number of distinct subsequences, then return 'A'.

For Example:
'N' = 2, 'M' = 2, 'A' = "ab", 'B' = "dd".

'A' has distinct subsequences = ["a", "b", "ab"].
'B' has distinct subsequences = ["d", "dd"].
So our answer is "ab".

*/

void getCombo(string s , set<string>&result ,string str, int index){

    if(index>=s.length()){
        return;
    }
    for(int i=index;i<s.length();i++){

        result.insert(str+s[i]);
        getCombo(s, result, str+s[i], i+1);
    }
}

set<string> generateSubsequences(string s)
{

    // Write your code here.
    set<string>result;
    getCombo(s,result,"",0);
    return result; 
}

string moreSubsequence(int n, int m, string a, string b)
{

    set<char>sc1;
    set<char>sc2;
    for(int i=0;i<n;i++){
        sc1.insert(a[i]);
    }

    for(int i=0;i<m;i++){
        sc2.insert(b[i]);
    }

    if(sc1.size()>=sc2.size() && n>=m){
        return a;
    }

    else if(sc1.size()<=sc2.size() && n<=m){
        return b;
    }

    set<string>s1= generateSubsequences(a);
    set<string>s2= generateSubsequences(b);

    return s1.size()>=s2.size()?a:b;

}

