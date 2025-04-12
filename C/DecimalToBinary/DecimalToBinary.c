#include <stdio.h>
#include <stdlib.h>

int* decimalToBinary(int decimal);

int main()
{
    int decimal = 99;
    int* binary = decimalToBinary(decimal);

    printf("Binario: ");
    for (int i = 0; i < 8; i++) {
        printf("%d", binary[i]);
    }
    printf("\n");

    free(binary); 
    return 0;
}

int* decimalToBinary(int decimal) {
    int* binary = (int*)malloc(8 * sizeof(int));
    for (int i = 7; i >= 0; i--) {
        binary[i] = decimal % 2;
        decimal /= 2;
    }
    return binary;
}