#include <stdio.h>

char invertir(char cadena[]){
    char cadena_invertida[] ;
    int longitud = 0 ;
    while (cadena[longitud] != "\0"){
        longitud++ ;
    }
    for (i = 0, i < longitud, i++){
        cadena_invertida[i] = cadena[longitud - 1 - i] ;
    }
    return cadena_invertida ;
}

int main(){
    char cadena[] ;
    char cadena_invertida[] ;
    scanf(%s, cadena) ;
    cadena_invertida = invertir(cadena) ;
    printf(cadena_invertida) ;    
    return 0 ;
}
