#include <iostream>
#include <string>

using namespace std;

int main() {

    int N, M, count = 0;
    string S;
    cin >> N >> M >> S;
    string checkN;

    for (int i = 0; i < M; i++) {
        if (S[i] == 'I') {
            int countOI = 0;
            while (S[i + 1] == 'O' && S[i + 2] == 'I') {
                countOI++;
                i += 2;
                if (countOI >= N) {
                    count++;
                }
            }
        }
    }

    cout << count;

    return 0;
}
