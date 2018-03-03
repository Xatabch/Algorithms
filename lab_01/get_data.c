#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define PI 3.14

#include "main.h"

double func(double x)
{
  return (pow(x, 3) - 5);
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

void get_data_y(struct table *Table, int n_tables)
{
  double x = -10.0;
  
  for (int i = 0; i<n_tables; i++)
  {
    (Table+i)->x = func(x);
    (Table+i)->y = x;
    x = x + 1.0;
  }
  
}