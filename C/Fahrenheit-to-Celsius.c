#include <stdio.h>
int main() {
    float c,f;
    printf("Enter the temperature in Fahrenheit: ");
    scanf("%f", &f);
    c=(f-32)/1.8;
    printf("%0.3fF = %0.3fC",f,c);
    return 0;
}
