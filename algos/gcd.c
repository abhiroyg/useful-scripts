#include "stdio.h"

//http://www.geeksforgeeks.org/euclids-algorithm-when-and-operations-are-costly/
//http://www.geeksforgeeks.org/gcd-of-two-numbers-when-one-of-them-can-be-very-large-2/
//http://www.geeksforgeeks.org/steins-algorithm-for-finding-gcd/
//https://en.wikipedia.org/wiki/Euclidean_algorithm#Algorithmic_efficiency

long long int gcd_sub (long long int a, long long int b) {
    if (b == 0 || a == b) {
        return a;
    }
    if (a == 0) {
        return b;
    }
    return (a > b) ? gcd(a-b , b) : gcd(a, b-a);
}

// Takes lesser number of iterations but as numbers grow bigger
// % operation becomes costly.
// wiki for euclidean algorithm says, the above sub function
// can rival this function in running time.
long long int gcd_div (long long int a, long long int b) {
    if (b == 0 || a == b) {
        return a;
    }
    if (a == 0) {
        return b;
    }
    return (a > b) ? gcd(a%b , b) : gcd(a, b%a);
}

long long int gcd_sub_bin (long long int a, long long int b) {
    if (b == 0 || a == b) {
        return a;
    }
    if (a == 0) {
        return b;
    }

    int is_a_even = (a & 1 == 0);  // ~a & 1 == 1
    int is_b_even = (b & 1 == 0);

    if (is_a_even) {
        if (is_b_even) {
            return gcd(a>>1, b>>1) << 1;
        } else {
            return gcd(a>>1, b);
        }
    } else if (is_b_even) {
        return gcd(a, b>>1);
    }
    return (a > b) ? gcd(a-b, b) : gcd(a, b-a);
}

// geeksforgeeks way
// Efficient C/C++ program when % and / are not allowed
int gcd(int a, int b) {
    // Base cases
    if (b == 0 || a == b) return a;
    if (a == 0) return b;

    // If both a and b are even, divide both a
    // and b by 2. And multiply the result with 2
    if ( (a & 1) == 0 && (b & 1) != 0 )
        return gcd(a>>1, b>>1) << 1;

    // If a is even and b is odd, divide a by 2
    if ( (a & 1) == 0 && (b & 1) == 0 )
        return gcd(a>>1, b);

    // If a is odd and b is even, divide b by 2
    if ( (a & 1) != 0 && (b & 1) == 0 )
        return gcd(a, b>>1);

    // If both are odd, then apply normal subtraction
    // algorithm. Note that, odd-odd case always 
    // converts to odd-even case after one recursion
    return (a > b) ? gcd(a-b, b) : gcd(a, b-a);
}

// one number is very large
// function to find gcd of two integer numbers
long long int gcd(long long int a, long long int b) {
    if (!a)
        return b;
    return gcd(b%a, a);
}

// Here 'a' is integer and 'b' is string.
// The idea is to make the second number (represented
// as b) less than and equal to first number, by
// calculating its mod with first integer number
// using basic mathematics
long long int reduceB(long long int a, char b[]) {
    // Initialize result
    long long int mod = 0;

    // Calculating mod of b with a to make
    // b like 0 <= b < a
    for (int i = 0; i < strlen(b); i++)
        mod = (mod * 10 + b[i] - '0') % a;

    return mod;  // return modulo
}

// This function returns GCD of 'a' and 'b'
// where b can be very large and is represented
// as a character array or string.
long long int gcdLarge(long long int a, char b[]) {
    // Reduce 'b' (second number) after modulo with a
    long long int num = reduceB(a, b);

    // gcd of two numbers
    return gcd(a, num);
}
