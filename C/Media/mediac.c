#include <stdio.h>
#include <stdlib.h> 

int main() {
    printf("Quer saber a media de quantos numeros? ");
    int quant_num = 0;
    scanf("%d", &quant_num);

    if (quant_num <= 0) {
        printf("Fim de Programa!");
        return 0; 
    }

    int *list_numeros = (int *)malloc(quant_num * sizeof(int));

    for (int i = 0; i < quant_num; i++) {
        printf("Insira o %d numero: ", i + 1);
        scanf("%d", &list_numeros[i]);
    }

    int somador = 0;
    for (int i = 0; i < quant_num; i++) {
        somador += list_numeros[i];
    }

    int media = somador / quant_num;
    printf("O resultado da media: %d", media);

    free(list_numeros); 
    return 0;
}
