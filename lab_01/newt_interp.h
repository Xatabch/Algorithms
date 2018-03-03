//function
#ifndef __NEWT_INTERP_H__
#define __NEWT_INTERP_H__
double newtown_interpolation(struct table *Table, int n_tables, int n, double x);
double compute_newton_poly(struct table *Table, int n_tables, int n, double x);
double reverse_newtown_interpolation(struct table *Table, int n_tables, int n, double x);
#endif