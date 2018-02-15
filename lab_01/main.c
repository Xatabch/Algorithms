#include <stdio.h>

#include "main.h"
#include "function.h"
#include "get_data.h"

int main(void)
{
	FILE *f;
	int n_table = 0;
	//int n = 0;
	//float x = 0;

	f = fopen("in.txt","r");
	if(!f)
		printf("Ошибка открытия файла\n");
	else
	{
		n_table = count(f);
		fclose(f);
		struct table Table[n_table];

		f = fopen("in.txt","r");
		get_data(f, Table);
		fclose(f);

		//printf("Введите степень полинома: ");
		//scanf("%d", &n);
		//printf("Введите X: ");
		//scanf("%f", &x);

		//printf("%d %f %d\n", n, x, n_table);

		printf("\n");
		for(int i = 0; i < n_table; i++)
		{
			printf("%f %f\n", Table[i].x,Table[i].y);
		}

		
	}


	return 0;
}