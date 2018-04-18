#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define PI 3.14

#include "main.h"

double func(double x)
{
  return (log(x+1));
}

void get_data(struct table *Table, int n_tables)
{
  double x = 0.0;
  
  for (int i = 0; i<n_tables; i++)
  {
    Table[i].x = x;
    Table[i].y = func(x);
    x = x + 1.0;
  }
  
}