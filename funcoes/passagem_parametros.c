#include <stdio.h>

int teste(int num) {
    while (num != 0) {
        num--;
    }
    return num;
}

int teste2(int *num) {
    while (*num != 0) {
        *num = *num - 1;
    }
    return *num;
}

int main() {
    int c = 10;
    int resp;
    resp = teste(c);
    printf("passagem de parametros por valor: %d %d\n", resp, c);

    resp = teste2(&c);
    printf("passagem de parametros por ref: %d %d\n", resp, c); 
}