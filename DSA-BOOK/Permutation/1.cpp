#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

void getPerm(vector<int>&nums, int idx, vector<vector<int>>&ans){
    
    if(idx == nums.size()){
        ans.push_back({nums});
        return;
    }

    for(int i=idx; i<nums.size(); i++){
        swap(nums[idx],nums[i]);
        getPerm(nums,idx+1,ans);
        swap(nums[idx],nums[i]);
    }
}

vector<vector<int>> permut(vector<int> &nums){
    vector<vector<int>>ans;
    getPerm(nums,0,ans);

    return ans;
}

int main(){
    vector<int> nums = {1,2,3};
    vector<vector<int>> ans = permut(nums);

    sort(ans.begin(),ans.end());

    for(auto &perm : ans){
        for(int num : perm){
            cout << num << " ";
        }
        cout << endl;
    }
    return 0;
}