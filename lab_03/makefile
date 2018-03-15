ifeq ($(mode), debug)
    # Отладочная сборка: добавим генерацию отладочной информации
    CFLAGS += -g3
endif

ifeq ($(mode), release)
    # Финальная сборка: исключим отладочную информацию и утверждения (asserts)
    CFLAGS += -DNDEBUG -g0
endif

main.exe: main.o cubic_spline.o get_data.o
	gcc -o main.exe cubic_spline.o get_data.o main.o -lm
main.o: main.c main.h
	gcc -std=c99 -Wall -Werror -c main.c
get_data.o: get_data.c get_data.h main.h
	gcc -std=c99 -Wall -Werror -c get_data.c
cubic_spline.o: cubic_spline.c cubic_spline.h main.h
	gcc -std=c99 -Wall -Werror -c cubic_spline.c

clean:
	rm *.o *.exe