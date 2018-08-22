class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> wl(wordList.begin(),wordList.end()); // 将wordList从vector转换成set，才能使用count,erase等函数
        unordered_map<string, int> words; //generate key-value pairs
        queue<string> q;
        words[beginWord] = -1;
        q.push(beginWord);
        int step = 0;
        
        if(!wl.count(endWord)) // return if endWord doesn't exit in the WordList
            return 0;
        
        while(!q.empty()){
            step++;
            for (int i=q.size();i>0;i--){   //有三个循环，最外面这层循环是每次把q里面新加进来的（即同一层的）全部处理完才加一，不然就等于每pop一次就加1了
                string w = q.front();
                q.pop();
                int loc = words[w];
                for(int i=0; i<w.length(); i++){
                    if (loc==i) continue;
                    char ch = w[i];
                    for (char j = 'a'; j<='z'; j++){
                        w[i] = j;
                        if (w==endWord) return step+1; // add the current level
                        if (!wl.count(w)) continue;
                        wl.erase(w);
                        words[w]=i;
                        q.push(w); //queue uses push to add the elements in the end, not insert
                }
                w[i] = ch;
            }
            }
            
        }
        return 0;
    }
};