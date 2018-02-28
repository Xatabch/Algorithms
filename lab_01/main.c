#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define PI 3.14

#include "main.h"
#include "newt_interp.h"
#include "get_data.h"

int main(void)
{	
	// 1-я часть задания
	int n_tables = 20;
	struct table *Table = malloc(n_tables * sizeof(struct table));
	struct table *Table_reverse = malloc(n_tables * sizeof(struct table));
	double refinement;
  
  	get_data(Table, n_tables);
    refinement = newtown_interpolation(Table, n_tables, 3, 0.2);

    // Прямой
    printf("Refinement: %f\n", refinement);
    printf("Ethalone: %f\n", pow(0.2-1,2) - 0.5*exp(0.2));


    get_data_y(Table_reverse, n_tables);
    refinement = newtown_interpolation(Table_reverse, n_tables, 6, 0.029);

    // Обратный
    printf("\nRefinement: %f\n", refinement);
    printf("Ethalone: %f\n", 0.2);
    
  	free(Table);
  	free(Table_reverse);


	return 0;
}