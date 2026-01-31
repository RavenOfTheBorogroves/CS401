#include <stdio.h>
#include "factorial.h"

unsigned int factorialRecursive(unsigned int n) {
  
    // Base Case:
    if (n == 1) {
        return 1;
    }

    // Multiplying the current N with the previous product of Ns
    return n * factorialRecursive(n - 1);
}
unsigned int factorialIterative(unsigned int N) {
    int fact = 1, i;

    // Loop from 1 to N to get the factorial
    for (i = 1; i <= N; i++) {
        fact *= i;
    }

    return fact;
}
