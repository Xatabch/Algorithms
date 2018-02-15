#include <stdio.h>

double y(int n, double y, )

double newtown_interpolation(struct table *Table, int n_tables, int n, double x)
{
	int int_part = (int) x;
	double frac_part = (double) (x - int_part);
	int a; //начало отрезка
	int b; //конец отрезка

	//поиск отрезка для интерполяции значения
	for(int i = 0; i < (n_tables-1); i++)
	{
		if(x > Table[i].x) && (x < Table[i+1].x)
		{
			a = i;
			b = i + n;
		}
	}





	return y;
}