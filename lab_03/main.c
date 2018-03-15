#include <stdio.h>
#include <stdlib.h>

#include "main.h"
#include "cubic_spline.h"
#include "get_data.h"

int main(void)
{
	int n_tables = 20;
  struct table *Table = malloc(n_tables * sizeof(struct table));
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
  	printf("Введите количество сплайнов N в сетке : ");
  	scanf("%d", &n);
  	printf("\n");

  	refinement = cubic_spline(Table, n, x);

  	printf("Refinement: %f\n", refinement);
  	printf("Ethalone: %f\n\n", func(x));

  	free(Table);


}