#include <stdio.h>
#include <stdlib.h>

#include "main.h"
#include "newt_interp.h"
#include "get_data.h"

int main(void)
{	
	int n_tables = 20;
	struct table *Table = malloc(n_tables * sizeof(struct table));
	double refinement;
  
  	get_data(Table, n_tables);
    refinement = newtown_interpolation(Table, n_tables, 2, 3.25);

    printf("%f\n", refinement);
    
  	free(Table);

	return 0;
}