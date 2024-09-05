#include <iostream>
#include <vector>

int main() {
  using namespace std;
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int N, M;
  cin >> N >> M;
  vector<vector<int>> array(N, vector<int>(N, 0));
  vector<vector<int>> prefix_sum(N + 1, vector<int>(N + 1, 0));

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      cin >> array[i][j];
      prefix_sum[i + 1][j + 1] = array[i][j] + prefix_sum[i][j + 1] +
                                 prefix_sum[i + 1][j] - prefix_sum[i][j];
    }
  }

  int x1, y1, x2, y2;
  for (int roop = 0; roop < M; roop++) {
    cin >> x1 >> y1 >> x2 >> y2;
    int result = prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2] -
                 prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1];
    cout << result << "\n";
  }

  return 0;
}
