#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main() {
    char input[100];  // Armazena a entrada do usuário
    fgets(input, sizeof(input), stdin); // Le a linha inteira

    input[strcspn(input, "\n")] = 0; // Remove o '\n' do final da string

    double valoresDaBhaskara[3]; 
    char *token = strtok(input, " "); // Primeiro valor separado por espaço

    for(int i = 0;token != NULL && i < 3; i++) {
        valoresDaBhaskara[i] = strtod(token, NULL); // Converte string para double
        token = strtok(NULL, " "); // Pega o próximo valor
    }

    double a = valoresDaBhaskara[0];
    double b = valoresDaBhaskara[1];
    double c = valoresDaBhaskara[2];

    // Calcula o delta
    double DELTA = pow(b, 2) - (4 * a * c);

    if (DELTA < 0 || a == 0) {
        printf("Impossivel calcular\n");
        return 0;
    }

    // Calcula as raízes
    double R1 = (-b + sqrt(DELTA)) / (2 * a);
    double R2 = (-b - sqrt(DELTA)) / (2 * a);

    printf("R1 = %.5lf\n", R1);
    printf("R2 = %.5lf\n", R2);

    return 0;
}