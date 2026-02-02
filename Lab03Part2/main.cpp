//Accept an array of integers and return the sum, average, and maximum value
//using a structure.
// Demonstrate function calls using a global variable for tracking the total number
//of elements processed across multiple function calls.
//2. Add a lambda function to sort the array in descending order and display the sorted array.

#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

int totalProcessed = 0;
struct dataFunctions
{
    /* data */
    private:
    int N;
    int values[];

    public:

    dataFunctions(int A, int B[]){
        N = A;
        std::copy(values,values + N ,B); //copy the input into the function
    }

    int sum(){
        int total = 0;
        for (int i = 0; i< N; i++){//itterate through the array 
            total += values[i];
            totalProcessed++;
        }
        return total;//returns the sum

    }

    int average(){ //devides the sum by the total 
        int total = sum() / N;
        return total;

    }

    int maximum(){
        int currentMax = 0;
        for (int i = 0; i< N; i++){//itterate through the array 
            if (values[i]>currentMax){
                currentMax = values[i]; //if the next value in the array is more then the max we found so far then replace it 
            }
            totalProcessed++;//global variable count 
        }
        return currentMax;
    }


};

int main(){
    int inputLength = 10;
    int inputArray[10] = {2,5,6,3,8,9,10,4,10,0}; //inputs for the code 
    dataFunctions(inputLength,inputArray); 

    std::sort(inputArray,inputArray+inputLength,greater<int>()); //this sorts the array 

    for (auto p : inputArray){ //this lambda prints the array
        cout<< p <<"\n";
    }
    


    return 0;
}
