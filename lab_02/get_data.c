#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define PI 3.14

#include "main.h"

double func(double x, double y)
{
  return (pow(x, 2) + pow(y, 2));
}

void get_data(struct table *Table, int n_tables)
{
  
  double x = 0.0;
  double y = 0.0;

  for (int i = 0; i<n_tables; i++)
  {
    Table[i].y = y;
    Table[i].x = x;
    Table[i].z = malloc(n_tables * sizeof(double*));
    for (int j = 0; j<n_tables; j++)
    {
      Table[i].z[j] = func((double) j, Table[i].y);
    }
    y += 1.0;
    x += 1.0;
  }
  
}