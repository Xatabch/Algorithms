#include <stdio.h>
#include <math.h>

#include "main.h"

void find_x_place(double x, int *a, int *b, struct table *Table, int n_tables, int n)
{
	int a1 = 0;
	int b1 = 0;

	for(int i = 0; i<n_tables; i++)
	{
		if ((x > Table[i].x) && (x < Table[i+1].x))
		{
			a1 = i;
			b1 = i + 1;
		}
	}

	if((n+1)%2 == 0)
	{
		if ((a1 - (n-1)/2 >= 0) && (b1 + (n-1)/2 <= 19))
		{
			*a = a1 - (n-1)/2;
			*b = b1 + (n-1)/2;
		}

		if((a1 - (n-1)/2 < 0) && (b1 + (n-1)/2 <= 19))
		{
		    *a = 0;
		    *b = b1 + 2 * fabs(a1 - (n-1)/2);
		}

		if((a1 - (n-1)/2 >= 0) && (b1 + (n-1)/2 > 19))
		{
			*a = a1 - 2 * (b1 + (n-1)/2 - 19);
			*b = 19;
		}
	}
	else
	{	
		if((a1 - (n/2-1) >= 0) && (b1 + (((n+1) - n/2) - 1) <= 19))
		{
			*a = a1 - (n/2-1);
			*b = b1 + (((n+1) - n/2)-1);
		}

		if((a1 - (n/2-1) < 0) && (b1 + (((n+1) - n/2) - 1) <= 19))
		{
			*a = 0;
			*b = b1 + (((n+1) - n/2) - 1) + fabs(a1 - (n/2-1));
		}

		if((a1 - (n/2-1) >= 0) && (b1 + (((n+1) - n/2) - 1) > 19))
		{
			*a = a1 - (n/2-1) - (b1 + (((n+1) - n/2) - 1) - 19);
			*b = 19;
		}

	}

}

double newtown_interpolation(struct table *Table, int n_tables, int n, double x)
{
	int a = 0; //начало отрезка
	int b = 0; //конец отрезка
	double array[n+1]; // массив для вычисления 'коэффицентов'' y 
	int bias = 0; // расстояние от i до конца 
	int difference = 0; // разница между xi и xn-ым
	int count = n; // счетчик уменьшения массива
	double refinement; // результирующее уточнение
	double differences_x = 1; // разница x для уточнения

	find_x_place(x, &a, &b, Table, n_tables, n); // нахожу границы отрезка

	refinement = Table[a].y;

  	for (int i = 0; i<(n+1); i++)
    	array[i] = Table[a+i].y;
  
  	for (int i = 0; i<n; i++)
  	{
  		differences_x *= (x - Table[a+i].x);
    	bias += 1;
    	difference = Table[0].x - Table[0+bias].x;
    	
    	for (int j = 0; j<count; j++)
      		array[j] = (array[j] - array[j+1])/difference;
    	
    	refinement += differences_x * array[0];
    	count -= 1;    		
  	}

	return refinement;
}