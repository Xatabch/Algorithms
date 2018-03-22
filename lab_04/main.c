#include <stdio.h>
#include <stdlib.h>

#include "main.h"
#include "get_data.h"

int main(void)
{
	int n_tables = 20;
    struct table *Table = malloc(n_tables * sizeof(struct table));

    get_data(Table, n_tables);

    printf(" № | X         | Y         | W\n");
  	printf("--------------------------------------\n");
  	for (int i = 0; i<n_tables; i++)
    	printf("%2d |%10f |%10f |%10f\n", i, Table[i].x, Table[i].y, Table[i].w);
  	printf("--------------------------------------\n\n");

}