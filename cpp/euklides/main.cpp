#include <iostream>

using namespace std;

int nwd_klasyczny(int a, int b){
    while(a != b) {
        if(a > b)
            a = a - b;
        else b = b - a;
    }
    return a;
}

int nwd_optymalny(int a, int b) {
while(a>0){
    if( a > 0 ){
        a = a % b;
        a = b - a;
    }else
        cout << "Powtórzeń: " << licznik b;
        }
    return b;
}

int main()
{
    int a, b;
    a = b = 0;
    cout << "Podaj dwie liczby: ";
    cin >> a >> b;
    int wynik = nwd_klasyczny(a, b);
    cout << "NWD(" << a << ", " << b << ") ="
         << nwd_klasyczny(a, b) << endl;
    cout << "NWD(" << a << ", " << b << ") ="
         << nwd_optymalny(a, b) << endl;
    return 0;
}
