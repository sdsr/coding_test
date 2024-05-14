#include <iostream>
#include <queue>
#include <unordered_map>

using namespace std;


int main() {
    int T, k;
    char first;
    int second;

    cin >> T;
    while (T--) {

        priority_queue<int, vector<int>, less<int>> max_heap;
        priority_queue<int, vector<int>, greater<int>> min_heap;
        unordered_map<int, int> exist;

        cin >> k;
        while (k--) {
            cin >> first >> second;
            if (first == 'I') {
                max_heap.push(second);
                min_heap.push(second);
                exist[second]++;
            } else if (first == 'D') {
                if (second == 1 && !max_heap.empty()) {
                    while (!max_heap.empty() && exist[max_heap.top()] == 0) {
                        max_heap.pop();
                    }
                    if (!max_heap.empty()) {
                        exist[max_heap.top()]--;
                        max_heap.pop();
                    }
                } else if (second == -1 && !min_heap.empty()) {
                    while (!min_heap.empty() && exist[min_heap.top()] == 0) {
                        min_heap.pop();
                    }
                    if (!min_heap.empty()) {
                        exist[min_heap.top()]--;
                        min_heap.pop();
                    }
                }
            }

            while (!max_heap.empty() && exist[max_heap.top()] == 0) {
                max_heap.pop();
            }
            while (!min_heap.empty() && exist[min_heap.top()] == 0) {
                min_heap.pop();
            }
        }

        if (max_heap.empty() || min_heap.empty()) {
            cout << "EMPTY" << endl;
        } else {
            while (!max_heap.empty() && exist[max_heap.top()] == 0) {
                max_heap.pop();
            }
            while (!min_heap.empty() && exist[min_heap.top()] == 0) {
                min_heap.pop();
            }
            cout << max_heap.top() << " " << min_heap.top() << endl;
        }
    }

    return 0;

}
