# include "stdio.h"

// http://www.geeksforgeeks.org/c-program-find-lcm-two-numbers/
int lcm(int a, int b) {
    g = gcd(a, b);
    if (g == 0) {
        return 0;
    }
    return (a * b) / g;
}
