#include <stdio.h>
#include <stdlib.h>

#include "main.h"


double cubic_spline(struct table *Table, int n, double x)
{
	struct spline_tuple *splines = malloc(n * sizeof(double));

	for (int i = 0; i<n; i++)
	{
		splines[i].x = Table[i].x;
		splines[i].a = Table[i].y;
	}
	splines[0].c = 0; // наша задача отыскать все c[i] а здесь ноль потому что по условию начальные
					  // коэф равны 0


// 	struct spline_tuple
// {
// 	double a, b, c, d, x;
// };

	// найдем все alph и bet методом прямой прогонки
	double *alpha = malloc((n-1) * sizeof(double));
	double *beta = malloc((n-1) * sizeof(double));

	double A, B, C, F, h_i, h_i1, z;  // это как в общем линейном уравнении Ai*yi-1 - Bi*yi + Di*yi+1 = -Fi
									 // при этом yi = Di/(Bi - Ai*alphai)*yi+1 + Fi+Ai*betai/(Bi - Ai*alphai)
									// alphai+1 = Di/(Bi - Ai*alphai) betai+1 = Fi + Ai*betai/(Bi - Ai*alphai)
	alpha[0] = beta[0] = 0; // начальная кофигурация alpha[0] и beta[0]

	for(int i = 1; i<(n-1); i++)
	{
		h_i = Table[i].x - Table[i-1].x; h_i1 = Table[i+1].x - Table[i].x; // рассмотрим hi = x[i] - x[i-1], hi1 = x[i+1] - x[i]
																		  // это предыдущий и поледующий шаги

		A = h_i; // коэффициент A в линейке равен h_i (?)
		C = 2 * (h_i + h_i1); // коэффициент B в линейке
		B = h_i1; // Коэффициент D в линейке
		F = 6 * ((Table[i+1].y - Table[i].y)/h_i1 - (Table[i].y - Table[i-1].y)/h_i); 
		z = (A * alpha[i-1] + C);// делители у alpha и beta
		alpha[i] = -B/z;
		beta[i] = (F - A * beta[i-1])/z;
	}


	//нахождение решения - обратный ход метода прохода

	for(int i = (n - 2); i>0; i--)
	{
		splines[i].c = alpha[i] * splines[i+1].c + beta[i];
	}

	//по известным коэфф c[i] находим значения b[i] и d[i]

	for (int i = n-1; i>0; i--)
	{
		h_i = Table[i].x - Table[i-1].x;
		splines[i].d = (splines[i].c - splines[i-1].c)/h_i;

		splines[i].b = h_i * (2*splines[i].c + splines[i-1].c)/6 + (Table[i].y - Table[i-1].y)/h_i;
	}

	struct spline_tuple *s;

	if(x <= splines[0].x)
		s = splines + 1;
	else if (x >= splines[n-1].x)
		s = splines + n -1;
	else
	{
		int i = 0, j = n - 1;
		int k;

		while(i + 1 < j)
		{
			k = i + (j - i)/2;
			if(x <= splines[k].x)
				j = k;
			else
				i = k;
		}
		s = splines + j;
	}

	double dx = (x - s->x);
	return (s->a + (s->b + (s->c/2 + s->d * dx/6) * dx) * dx);
}