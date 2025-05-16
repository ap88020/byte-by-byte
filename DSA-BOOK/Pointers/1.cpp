#include<iostream>
#include<vector>
using namespace std;

int main(){
    int a = 10;
    int* ptr = &a;
    // cout << ptr << endl;
    // cout << &a << endl;

    float price = 22.44;
    float* point = &price;
    float** pointPtr = &point;

    cout << *(&price) << endl;
    cout << pointPtr << endl;
    return 0;
}