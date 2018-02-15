#include <stdio.h>
#include <stdlib.h>

#include "main.h"

int count(FILE *f)
{	
	double num;
	int n = 0;

	if(fscanf(f, "%lf", &num) == 1)
	{
		n++;
		while(fscanf(f, "%lf", &num) == 1)
			n++;

	}

	return n/2;
}

struct table *get_data(FILE *f,struct table *Table)
{
	double num;
	int i = 0;

	if(fscanf(f, "%lf", &num) == 1)
	{
		Table[i].x = num;
		fscanf(f, "%lf", &num);
		Table[i].y = num;
		i++;

		while(fscanf(f, "%lf", &num) == 1)
		{
			Table[i].x = num;
			fscanf(f, "%lf", &num);
			Table[i].y = num;
			i++;
		}
	}

	return Table;
}