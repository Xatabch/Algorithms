#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define PI 3.14

#include "main.h"
#include "newt_interp.h"
#include "get_data.h"

int main(void)
{	
	// 1-я часть задания (Прямой)
	int n_tables = 20;
	struct table *Table = malloc(n_tables * sizeof(struct table));
	struct table *Table_reverse = malloc(n_tables * sizeof(struct table));
	double refinement;
  double x;
  int n;

  get_data(Table, n_tables);

  printf(" № | X         | Y\n");
  printf("----------------------------\n");
  for (int i = 0; i<n_tables; i++)
    printf("%2d |%10f |%12f\n", i, Table[i].x, Table[i].y);
  printf("----------------------------\n\n");

  printf("Введите x: ");
  scanf("%lf", &x);
  printf("Введите степень полинома n: ");
  scanf("%d", &n);
  printf("\n");

  refinement = newtown_interpolation(Table, n_tables, n, x);

  printf("Refinement: %f\n", refinement);
  printf("Ethalone: %f\n\n", func(x));


  // 2-я часть задания (Обратный)
  get_data_y(Table_reverse, n_tables);

  printf(" № | Y           | X\n");
  printf("----------------------------\n");
  for (int i = 0; i<n_tables; i++)
     printf("%2d |%12f |%10f\n", i, Table_reverse[i].x, Table_reverse[i].y);
  printf("----------------------------\n\n");

  refinement = newtown_interpolation(Table_reverse, n_tables, n, 0.0);

  printf("Refinement: %f\n", refinement);
    
  free(Table);
  free(Table_reverse);


	return 0;
}