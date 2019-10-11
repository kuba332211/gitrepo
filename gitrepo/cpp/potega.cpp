/*
 * potega.cpp
 */



#include <iostream>
using namespace std;
// a^n = a * a * a....*a 
int potega_it(int a, int n) {
    int wynik = 1;
    for(int i = 0; i < n; i ++) {
        //wynik = wynik * a;
        wynik *= a;
    }
    return wynik;
}

// 2^4 = 2^3 *2
// a^n = a^(n-1) * a
int  potega_re(int a, int n) {
    //warunek (brzegowy) graniczny
    if (n == 0) return 1;
    return potega_re(a, n-1) * a;
}

int main(int argc, char **argv)
{
	int a, n;
    cout << "Podaj podstawę i wykładnik: ";
    cin >> a >> n;
    cout << "Potęga: " << potega_it(a, n) << endl;
    cout << "Potęga: " << potega_re(a, n) << endl;
	return 0;
}

