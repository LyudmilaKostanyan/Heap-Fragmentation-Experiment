#include <iostream>

int main()
{
    while (true) {
        int *n = new int[1000000];
        delete [] n;
    }
}