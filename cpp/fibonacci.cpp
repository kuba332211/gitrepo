/*
 * fibonacci.cpp 
 */


#include <iostream>

using namespace std;


long int fibonacci_it(int n){    
    long int wynik = 0;
    long int a = 0;
    long int b = 1;
    if (n==0)
        wynik = 0;
    if (n==1)
        wynik = 1;
    for (int i = 2; i <= m; i++ ) {
        wynik = a + b;
    }
    return wynik;
}


int main(int argc, char **argv)
{
    int n;
    cout << "Podaj numer wyrazu ciągu: ";
    cin >> n;
    cout << "ciąd fibonacciego do wyrazu " << n << ":" << endl;
    cout << fibonacci_it(n);
	
	return 0;
}

