#include <iostream>
#include <string>
using namespace std;

class myStack {
    
    // array to store elements
    char *arr;       
    
    // maximum size of stack
    int capacity;   
    
    // index of top element
    int top;        

public:

    // constructor
    myStack(int cap) {
        capacity = cap;
        arr = new char[capacity];
        top = -1;
    }

    // push operation
    void push(int x) {
        if (top == capacity - 1) {
            cout << "Stack Overflow\n";
            return;
        }
        arr[++top] = x;
    }

    // pop operation
    int pop() {
        if (top == -1) {
            cout << "Stack Underflow\n";
            return -1;
        }
        return arr[top--];
    }

    // peek (or top) operation
    int peek() {
        if (top == -1) {
            cout << "Stack is Empty\n";
            return -1;
        }
        return arr[top];
    }

    // check if stack is empty
    bool isEmpty() {
        return top == -1;
    }

    // check if stack is full
    bool isFull() {
        return top == capacity - 1;
    }
};

int main() {
    //string input = "(a+b+[c*d])";
    string userInput;
   
    cout << "Input your text: ";
    getline (cin, userInput);
    int length = userInput.size();
    string success = " is balanced";
    string failure = " is not balanced";
    myStack st(12);
    
    //declaring the char i am comparing agianst 
    for (int i = 0; i < length; i++) {
        char focus = userInput[i];
        if (focus == '(' || focus =='['){
            st.push(focus);

        } else if (focus == ']' ){
            char compare = st.pop();
            if ((compare != '[')){
                st.push(compare);
            }

        } else if ( focus == ')'){
            char compare = st.pop();
            if ((compare != '(')){
                st.push(compare);
            }

        }        

    }
    cout << userInput << (st.isEmpty() ? success : failure) <<endl;
    


    return 0;
}