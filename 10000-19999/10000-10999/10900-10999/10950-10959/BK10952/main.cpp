#include <iostream>
using namespace std;

int main(void) {
    
    short a, b;

    while (true) {
        
        cin >> a >> b;
        if ((a == 0) && (b == 0)) break;
        if (a <= 0 || b >= 10) exit(0);
        cout << a + b << endl;
    } 
}