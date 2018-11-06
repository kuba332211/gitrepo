/*
 * minmax.cxx
 * 
 */


#include <iostream>

using namespace std;

void wypelnij(int tab[], int roz) {
    cout << "wprowadź " << roz << " liczb:"<< endl; 
    for(int i=0; i <roz; i++){
        cin >> tab[i];
    }
}


void drukuj(int tab[], int roz) { 
    for(int i = 0; i <roz; i++){
        cout << tab[i] << " ";
    }
}


void minmax(int tab[], int roz) {
    int minimum = tab[0];
    int maksimum = tab[0];
    for(int i = 0; i <roz; i++){
        if (minimum > tab[i])
            minimum = tab[i];
        if (maksimum < tab[i])
            maksimum = tab[i];
    }
    cout << "min. " << minimum << endl;
    cout << "max. " << maksimum << endl;
}
    

    
    
int main(int argc, char **argv)
{   
    const int rozmiar = 10;
    int tab[rozmiar];
    wypelnij(tab, rozmiar);
    drukuj(tab, rozmiar);
	return 0;
}

