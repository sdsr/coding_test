#include <iostream>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int song_length;
  float tic = 4.0;
  cin >> song_length;

  cout << fixed;
  cout.precision(2);
  cout << (float)(song_length / tic);

  return 0;
}
