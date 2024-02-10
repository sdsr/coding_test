#include <iostream>
using namespace std;

void division(int, int, int);

int paper[128][128];
int white = 0, blue = 0;

int main() {
  int num;
  cin >> num;
  string temp;

  for (int i = 0; i < num; i++) {
    for (int j = 0; j < num; j++) {
      cin >> paper[i][j];
    }
  }

  division(0, 0, num);

  cout << white << "\n" << blue;

  return 0;
}

void division(int x, int y, int size) {
  int color = paper[x][y];
  bool sameColor = true;

  for (int i = x; i < x + size; i++) {
    for (int j = y; j < y + size; j++) {
      if (paper[i][j] != color) {
        sameColor = false;
        break;
      }
    }
    if (!sameColor)
      break;
  }

  if (sameColor) {
    if (color == 0)
      white++;
    else
      blue++;
  } else {
    int newSize = size / 2;
    division(x, y, newSize);
    division(x + newSize, y, newSize);
    division(x, y + newSize, newSize);
    division(x + newSize, y + newSize, newSize);
  }
}
