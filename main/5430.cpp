#include <deque>
#include <iostream>
#include <string>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int T;
  char delimiter = ',';
  cin >> T;

  while (T--) {
    string func;
    string arrInput;
    int arrsize, num;

    cin >> func >> arrsize >> arrInput;

    deque<int> dq;
    string numStr;

    for (char ch : arrInput) {
      if (isdigit(ch)) {
        numStr += ch;
      } else if (ch == ',' || ch == ']') {
        if (!numStr.empty()) {
          dq.push_back(stoi(numStr));
          numStr.clear();
        }
      }
    }

    bool error = false;
    bool reversed = false;

    for (char op : func) {
      if (op == 'R') {
        reversed = !reversed;
      } else {
        if (dq.empty()) {
          error = true;
          cout << "error\n";
          break;
        } else {
          if (!reversed) {
            dq.pop_front();
          } else {
            dq.pop_back();
          }
        }
      }
    }

    if (!error) {
      cout << '[';
      while (!dq.empty()) {
        if (reversed) {
          cout << dq.back();
          dq.pop_back();
        } else {
          cout << dq.front();
          dq.pop_front();
        }
        if (!dq.empty()) {
          cout << ',';
        }
      }
      cout << "]\n";
    }
  }

  return 0;
}
