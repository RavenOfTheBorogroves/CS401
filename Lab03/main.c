#include <stdio.h>
#include "factorial.h"

int main() {
    int N = 5;
    int fact = factorialIterative(N);
    printf("Factorial calculated with iteration of %d is %d \n", N, fact);

    printf("Factorial calculated recursively of %d is %d \n", N, factorialRecursive(N));
    return 0;
}

//to run run this command gcc main.c -L. -lfactorial -o myprogram
//and then run the myprogram exicutable 