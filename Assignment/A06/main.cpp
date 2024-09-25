class Solution {
public:
    string frequencySort(string s) {
        map<char, int> mp;
        string ans = "";
        // map of chars -> ints 
        for(char c : s){
            mp[c]++;
        }
        //create a vector of pairs from map
        vector<pair<int, char>> vec;
        map<char, int>::iterator it = mp.begin();
        while(it != mp.end()){
            vec.push_back(make_pair(it->second, it->first));
            ++it;
        }
        // sort vector of pairs using a lambda function
       sort(vec.begin(), vec.end(), [](const auto& a, const auto& b) { return a.first > b.first; });
       // iterate over vector and print char based on int 
       for(auto&pair : vec){
            for(int j = 0; j < pair.first; j++)
                ans += pair.second;
        }
        // return answer
        return ans;
    }
};
