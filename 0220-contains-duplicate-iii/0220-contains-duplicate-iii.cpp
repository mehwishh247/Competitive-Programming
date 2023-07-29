class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int vl) {
     
    int n = nums.size();
        unordered_set<int> seen;
        
        for (int i = 0; i < n; i++) {
            if (seen.size() == k + 1) {
                seen.erase(nums[i - k - 1]);
            }
            for (int item : seen) {
                if (abs(nums[i] - item) <= vl) {
                    return true;
                }
            }
            seen.insert(nums[i]);
        }
        
        return false;
    }
};