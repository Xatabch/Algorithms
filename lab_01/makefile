ifeq ($(mode), debug)
    # Отладочная сборка: добавим генерацию отладочной информации
    CFLAGS += -g3
endif

ifeq ($(mode), release)
    # Финальная сборка: исключим отладочную информацию и утверждения (asserts)
    CFLAGS += -DNDEBUG -g0
endif

main.exe: main.o function.o get_data.o
	gcc -o main.exe function.o get_data.o main.o
main.o: main.c main.h
	gcc -std=c99 -Wall -Werror -c main.c
get_data.o: get_data.c get_data.h main.h
	gcc -std=c99 -Wall -Werror -c get_data.c
function.o: function.c function.h
	gcc -std=c99 -Wall -Werror -c function.c

clean:
	rm *.o *.exe