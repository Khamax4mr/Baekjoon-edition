#include <iostream>
using namespace std;

int main(void) {

    short a, b;
    cin >> a >> b;
    if (a <= 0 || b >= 10) exit(0);

    cout << a - b;
}