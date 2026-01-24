#include <iostream>
#include <string>
using namespace std;

// Node structure
class Node {
public:
    char data;
    Node* next;
    
    Node(char x) {
        data = x;
        next = NULL;
    }
};

// Stack class
class myStack {
    
    // pointer to top node
    Node* top;  
    int count; // this is to store the size of the stack 
public:
    myStack() {
        
        // initially stack is empty
        top = NULL;  
        count = 0;
    }

// push operation
    void push(char x) {
        Node* temp = new Node(x);
        temp->next = top;
        top = temp;
        
        count++;
    }

    // pop operation
    char pop() {
        if (top == NULL) {
            cout << "Stack Underflow" << endl;
            return -1;
        }
        Node* temp = top;
        top = top->next;
        char val = temp->data;
        
        count--;
        delete temp;
        return val;
    }
    // check if stack is empty
    bool isEmpty() {
        return top == NULL;
    }
    int size() {
        return count;
    }
};
int main() {
    //string input = "(a+b+[c*d])";
    string userInput;
   
    cout << "Input your text: ";
    getline (cin, userInput);
    int length = userInput.size();
    string success = " are balanced";
    string failure = " are not balanced";
    myStack st;
    
    //declaring the char i am comparing agianst 
    for (int i = 0; i < length; i++) {
        char focus = userInput[i];
        if (focus == '(' || focus =='['|| focus =='{'){
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

        }   else if (focus == '}' ){
            char compare = st.pop();
            if ((compare != '{')){
                st.push(compare);
            }

        }    

    }
    cout << "Parentheses" << (st.isEmpty() ? success : failure) <<endl;
    


    return 0;
}