#include<stdio.h>
#include<stdlib.h>

bool contains(int i, int *items) {
    for (int *x = items; *x != 0; x++) {
        if (*x == i) {
            return true;
        }
    }
    return false;
}

int middle(int a, int b)
{
    int mid;
    if ((a + b) % 2 != 0)
    {
        return 0;
    }
    mid = (a + b) / 2;
    if ((mid == 5) || (a % 3 == b % 3) || ((a - 1) / 3 == (b - 1) / 3))
    {
        return mid;
    }
    return 0;
}

int *next(int *base)
{
    int *x = (int*)malloc(10*sizeof(int));
    for (int i = 0; i < 10; i++) x[i]=i+1;
    int n = (sizeof(base)/sizeof(*base));
    if (n >= 9) {
        return NULL;
    } else if (n == 0) {
        return x;
    }
    int *tmp = (int*)malloc(100*sizeof(int));
    int j = 0;
    for (int i = 0; i < 10; i++) {
        if (!contains(i, base)) {
            int mid = middle(i, base[sizeof(base)/sizeof(base[0])]);
            if (mid == 0 || contains(mid, base)) {
                tmp[j++] = i;
            }
        }
    }
    return tmp;
}

// void generate(int *base) {
//     for (int *n = base; *n != 0; n++) {
//         int *s = (int*)malloc((sizeof(base)/sizeof(base[0])+sizeof(base[0]))*sizeof(int));
        
//     }
// }

int main()
{
    return 0;
}   