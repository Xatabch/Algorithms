#include <stdio.h>
#include <stdlib.h>

#include "main.h"
#include "get_data.h"
#include "newt_interp.h"

int main(void)
{	
	// 1-я часть задания (Прямой)
	int n_tables = 20;
	struct table *Table = malloc(n_tables * sizeof(struct table));
	struct table *Table_z = malloc(n_tables * sizeof(struct table));
	struct table *Table_y = malloc(n_tables * sizeof(struct table));
	double refinement;
	double refinement_z;
  	double x;
  	double y;
  	int n;


  	get_data(Table, n_tables);
  	printf("    X/Y  ");
  	for (int i = 0; i<6; i++)
    	printf("|%10lf", Table[i].x);
    printf("\n");

  	for (int i = 0; i<6; i++)
  	{
  		printf("%9lf", Table[i].y);
    	for (int j = 0; j<6; j++)
    	{
    		printf("|%10lf", Table[i].z[j]);
    	}
    	printf("\n");
    }
    printf("\n");

    printf("Введите x: ");
  	scanf("%lf", &x);
  	printf("Введите y: ");
  	scanf("%lf", &y);
  	printf("Введите степень полинома n: ");
  	scanf("%d", &n);
  	printf("\n");

    for (int i = 0; i<n_tables; i++)
    {
    	for (int j = 0; j<n_tables; j++)
    	{
    		Table_y[j].x = Table[j].x;
    		Table_y[j].y = Table[i].z[j];
     	}

     	refinement_z = newtown_interpolation(Table_y, n_tables, n, x);

     	Table_z[i].x = Table[i].y;
     	Table_z[i].y = refinement_z;

    }

  	refinement = newtown_interpolation(Table_z, n_tables, n, y);

  	printf("refinement: %lf\n", refinement);

  	printf("real_func: %lf\n", func(x, y));


  	return 0;
}