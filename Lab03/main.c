#include <stdio.h>
#include "factorial.h"

int main() {
    int N = 5;
    int fact = factorialIterative(N);
    printf("Factorial calculated with iteration of %d is %d", N, fact);

    printf("Factorial calculated recursively of %d is %d", N, factorialRecursive(N));
    return 0;
}