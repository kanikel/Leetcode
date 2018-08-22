class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> q1{beginWord};
        unordered_set<string> q2{endWord};

        unordered_set<string> wl(wordList.begin(),wordList.end());
        unordered_map<string,int> words;
        words[beginWord] = -1;
        words[endWord] = -1;
        if (!wl.count(endWord))
            return 0;
            
        int step = 0;
        while (!q1.empty() && !q2.empty()){
            
            if (q1.size() > q2.size()) 
                std::swap(q1,q2);
            step++;
            
            unordered_set<string> temp;
            
            //for (int i = q1.size(); i>0; i--){ 少跑一个循环，从33%升高到98%
                for (string w : q1){ //这句话就起到了上面的作用，为什么加多了一个循环也没有报错？因为swap是放在外面的，而且temp不会加入重复的东西，所以才没有报错，但是当层数多了的时候等于重复跑了每层元素的个数次，所以时间会突然飙升，之前是要跑完一层的所有元素才能加一，现在也是，但是有了w:q1，上面那句话就变得多余了！！
                int loc = words[w];
                for(int i = 0; i < w.length(); i++){
                    if (loc == i) continue;
                    char ch = w[i];
                    for (char j = 'a'; j <= 'z'; j++){
                        w[i] = j;
                        if (q2.count(w)) return step+1;
                        if (!wl.count(w)) continue;
                        temp.insert(w);
                        wl.erase(w);
                        words[w]=i;
                        //cout<<w<<endl;
                    }
                    w[i] = ch;
                }
            }
            //}
            std::swap(q1,temp);
        }
        return 0;
        
        
        
        
    }
};

/*    ["hot","dot","dog","lot","log","cog"]
            hit
             |
            hot
            / \
         dot   lot
          |     |
         dog   log
           \   /
            cog
*/