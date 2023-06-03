#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[]) {
    time_t timer = strtol(argv[1], NULL, 10);
    srand((uint32_t)timer);
    printf("%d", rand());
}
