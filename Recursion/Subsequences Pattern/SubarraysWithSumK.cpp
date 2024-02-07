/* 

Problem statement
You are given an array 'A' of size 'N' and an integer'K'’. You need to generate and return all subarrays of array ‘A’ whose sum = ‘K’.

Note: In the output, you will see the 2D array lexicographically sorted.

Example:
Input: ‘N’ = 6 ‘K’ = 3
‘A’ = [1, 2, 3, 1, 1, 1]
Output: [[1,2],[3],[1,2,3]]
Explanation: Subarrays whose sum = ‘3’ are:
[1, 2], [3], and [1, 1, 1]

Just for practice, recursion is a brute force approach and gives TLE if submitted

*/

#include<bits/stdc++.h>

set<vector<int>>st;

void helper(int ind, vector<int> &a, long long k, vector<int> &store_res, vector<vector<int>> &res) {

    if(ind > a.size()) return;

    if(k == 0 && st.find(store_res) == st.end()) {

        res.push_back(store_res);

        st.insert({store_res});

    }

 

    if(a[ind] <= k) {

        for(int i = ind; i <= a.size(); i++) {

            store_res.push_back(a[i]);

            helper(i+1, a, k - a[i], store_res, res);

            store_res.pop_back();

        }

    }

    return;

}

vector<vector<int>> subarraysWithSumK(vector<int> a, long long k) {

    vector<vector<int>>res;

    vector<int>store_res;

    helper(0, a, k, store_res, res);

    return res;

}

