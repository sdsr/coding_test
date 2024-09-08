#include <iostream>
#include <vector>

using namespace std;

int main() {
  cin.tie(NULL);
  ios_base::sync_with_stdio(false);

  int start, end;
  cin >> start >> end;

  vector<int> arr(end);

  int index = 0;

  for (int i = 1; index < end; i++) {
    for (int j = 0; j < i && index < end; j++) {
      if (index == 0)
        arr[index] = i;
      else
        arr[index] = (i + arr[index - 1]);
      index++;
    }
  }
  cout << arr[end - 1] - arr[start - 2];
  return 0;
}
