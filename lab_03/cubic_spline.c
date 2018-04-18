#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "main.h"

int x_position(struct table *Table, double x, int n)
{
	if((Table[0].x <= Table[n-1].x) && x < Table[0].x)
		return -1;

	int position = 0;
	for(int i = 1; i<(n+1); i++)
	{
		if((Table[i-1].x <= x && Table[i].x > x) || (Table[i-1].x >= x && Table[i].x < x))
			break;
		position += 1;
	}

	return position;
}

int cubic_spline(struct table *Table, int n, double x, double *result)
{
	int code = 0;
	int position = x_position(Table, x, n); // return x position
	if(position < 0 || position >=n)
		return 1;

	position += 1;

	//coefficients
	double *Ca = calloc((n+2), sizeof(double));
	double *Cb = calloc((n+2), sizeof(double));
	double *Cc = calloc((n+2), sizeof(double));
	double *Cd = calloc((n+2), sizeof(double));

	//steps
	double *h = calloc((n+2), sizeof(double));

	//coefficients for method "progonka"
	double *A = calloc((n+2), sizeof(double));
	double *B = calloc((n+2), sizeof(double));
	double *D = calloc((n+2), sizeof(double));
	double *F = calloc((n+2), sizeof(double));

	double *Xi = calloc((n+2), sizeof(double));
	double *Eta = calloc((n+2), sizeof(double));

	//calculate array of steps
	for(int i = 1; i<=(n+1); i++)
		h[i] = Table[i].x - Table[i-1].x;

	//coefficients a = yi
	for(int i = 1; i<=(n+1); i++)
		Ca[i] = Table[i-1].y;
	//coefficients c[0] and c[n+1] = 0 (borders)
	//Xi[1] and Eta[1] = 0 because ^
	Cc[1] = Cc[n+1] = 0;
	Xi[2] = Eta[2] = 0;

	for(int i = 2; i<=(n+1); i++)
	{
		A[i] = h[i-1];
		B[i] = -2*(h[i-1] + h[i]);
		D[i] = h[i];
		F[i] = -3*((Table[i].y - Table[i-1].y)/h[i] - (Table[i-1].y - Table[i-2].y)/h[i-1]);
	}

	//calculate Xi and Eta (straight run)
	for(int i = 2; i<=(n+1); i++)
	{
		Xi[i+1] = D[i] / (B[i] - A[i]*Xi[i]);
		Eta[i+1] = (A[i] * Eta[i] + F[i]) / (B[i] - A[i]*Xi[i]);
	}

    //going backward (calculating c)
    for(int i = 1; i<=n; i++)
        Cc[i] = Xi[i+1]*Cc[i+1] + Eta[i+1];

    //calculating b and d
	for(int i = n; i>=1; i--)
	{
		Cb[i] = (Table[i].y-Table[i-1].y)/h[i] - h[i]/3 * (2*Cc[i] + Cc[i+1]);
		Cd[i] = (Cc[i+1] - Cc[i])/(3*h[i]);
	}

	//result
	(*result) = Ca[position] + Cb[position] * (x - Table[position-1].x) + 
	Cc[position]*(x - Table[position-1].x)*(x - Table[position-1].x) + 
	Cd[position]*(x-Table[position-1].x)*(x-Table[position-1].x)*(x-Table[position-1].x);

	printf("Коэффициенты: \n");
	printf("A: %lf\nB: %lf\nC: %lf\nD: %lf\n", Ca[position], Cb[position], Cc[position], Cd[position]);

	//free memory
	free(Ca);
	free(Cb);
	free(Cc);
	free(Cd);
	free(h);
	free(A);
	free(B);
	free(D);
	free(F);
	free(Xi);
	free(Eta);

	return code;
}