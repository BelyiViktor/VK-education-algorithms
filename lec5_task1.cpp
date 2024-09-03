#include <iostream>
#include <vector>
#include <stack>
// если число, которое достали длины больше 1, делим массив попалам, засовываем обратно
struct range
{
    int left, right;
};

using namespace std;

int main()
{
    vector<int> data;
    
    stack<range> recurtion;
    range temp;
    temp.left = -1;
    temp.right = 10;
    cout<< temp.right;
    vector<int> result(data.size());
    while(!recursion.empty()){
        range now = recursion.top();
        if (now.right - now.left > 1){
            range piece1, piece2;
            piece1.left = now.left;
            int step = (now.right - now.left) / 2;
            piece1.right = left + step;
            piece2.left = left + step + 1;
            piece2.right = now.right;
            recursion.push(piece1);
            recursion.push(piece2);
            recursion.pop();
            continue;
        }else if(now.right - now.left == 1){
            int ind = now.right - now.left
            int i = 0;
            vector<int> temp(result.size() + 1);
            while(result[i] < data[ind] || i < result.size()){
                if (result[i] > data[ind]){
                    temp.push_back(data[ind]);
                }else{
                    temp.push_back(result[i]);
                }
                i += 1;
            }
        }
    }
    stck.pop()
    return 0;
}
