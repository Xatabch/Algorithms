#ifndef __MAIN_H__
#define __MAIN_H__
//структура, описывающая сплайн
struct spline_tuple
{
	double a, b, c, d, x;
};
//структура, описывающая таблицу
struct table
{
	double x, y;
};
#endif