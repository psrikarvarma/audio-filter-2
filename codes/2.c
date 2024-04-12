#include <stdio.h>
#include <math.h>
#include <complex.h>

#define N 4
#define EPSILON 0.3
#define OMEGA_LP 1
#define PI 3.14159265358979323846

int main() {
    // Calculate B_k coefficient
    double B_k = asinh(1 / EPSILON) / N;

    // Initialize an array to store the poles
    double complex poles[2*N]; // Only need N poles, since they come in conjugate pairs for LPF

    // Calculate the poles
    for (int k = 0; k < 2*N; ++k) {
        double theta = PI * (2.0*k + 1) / (2.0 * N); // Angle for the pole
        double sigma = -sinh(B_k) * sin(theta); // Real part of the pole
        double omega = cosh(B_k) * cos(theta); // Imaginary part of the pole

        poles[k] = OMEGA_LP * (sigma + I * omega);
    }

    // Save poles to a .dat file
    FILE *file = fopen("sk.txt", "w");
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }
    fprintf(file, "Real Part, Imaginary Part\n");
    for (int i = 0; i < 2*N; ++i) { // Corrected loop to iterate over 2*N poles
        fprintf(file, "%.4f, %.4f\n", creal(poles[i]), cimag(poles[i]));
    }
    fclose(file);

    printf("Poles saved to sk.txt file.\n");

    return 0;
}
