#include <stdio.h>
#include <stdlib.h>

#include "main.h"
#include "cubic_spline.h"
#include "get_data.h"

int main(void)
{
	int n_tables = 20;
  struct table *Table = malloc(n_tables * sizeof(struct table));
  double refinement = 0;
  int error = 1;
  double x;

  get_data(Table, n_tables);

	printf(" № | X         | Y\n");
  	printf("----------------------------\n");
  	for (int i = 0; i<n_tables; i++)
    	printf("%2d |%10f |%12f\n", i, Table[i].x, Table[i].y);
  	printf("----------------------------\n\n");

  	printf("Enter x: ");
  	scanf("%lf", &x);

  	error = cubic_spline(Table, n_tables, x, &refinement);
    if(!error)
    {
  	    printf("Refinement: %f\n", refinement);
  	    printf("Ethalone: %f\n\n", func(x));
    }
    else
      printf("Error\n");

  	free(Table);


}