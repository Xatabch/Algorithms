#include <stdio.h>
#include <math.h>

#include "main.h"
#include "get_data.h"

void find_x_place(double x, int *a, int *b,struct table *Table, int n_tables, int n)
{
	int a1 = 0;
	int b1 = 0;

	if (x != 0)
	{
		for(int i = 0; i<n_tables; i++)
		{
			if ((x >= Table[i].x) && (x <= Table[i+1].x))
			{
				a1 = i;
				b1 = i + 1;
			}
		}
	}
	else
	{
		for(int i = 0; i<n_tables; i++)
		{
			if (((Table[i].x >= 0) && (Table[i+1].x) < 0) || ((Table[i].x <= 0) && (Table[i+1].x) > 0))
			{
				a1 = i;
				b1 = i + 1;
			}
		}
	}

	printf("Detected x on: [%d:%d]\n", a1, b1);

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
	//double difference = 0; // разница между xi и xn-ым
	int count = n; // счетчик уменьшения массива
	double refinement = 0; // результирующее уточнение
	double differences_x = 1; // разница x для уточнения
	double xx[n+1];


	find_x_place(x, &a, &b, Table, n_tables, n); // нахожу границы отрезка

	printf("Line segment: [%d:%d]\n", a, b);

	refinement = Table[a].y;

  	for (int i = 0; i<(n+1); i++)
  	{
    	array[i] = Table[a+i].y;
    	xx[i] = Table[a+i].x;
  	}

  	for (int i = 0; i<n; i++)
  	{
  		differences_x *= (x - xx[i]);
    	bias += 1;
    	
    	for (int j = 0; j<count; j++)
      		array[j] = (array[j] - array[j+1])/(xx[j] - xx[j + bias]);
    	
    	refinement += differences_x * array[0];
    	count -= 1;    		
  	}

	return refinement;
}