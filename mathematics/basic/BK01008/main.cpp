#include <iostream>
using namespace std;

int main(void) {

    double a, b;
    cin >> a >> b;
    if (a <= 0 || b >= 10) exit(0);

    cout.precision(16);
    cout << a / b;
}