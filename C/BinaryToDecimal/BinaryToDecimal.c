#include <stdio.h>
#include <math.h>

int binaryToDecimal(unsigned int binary[], int tamanho);

int main()
{
    unsigned int binary[7] = {1,1,0,0,0,1,1}; 
    int decimal = binaryToDecimal(binary, 7);
    printf("Decimal: %d\n", decimal);
    return 0;
}

int binaryToDecimal(unsigned int binary[], int tamanho){
    int decimal = 0;
    int expoente = tamanho - 1; 

    for (int i = 0; i < tamanho; i++)
    {
        decimal += binary[i] * pow(2, expoente);
        expoente--;
    }

    return decimal;
}