#import "stdlib.h"
#import "stdio.h"
struct node {
   int data;
   struct node *next;
};

int main(){
  int* x;
  int* y;

  x = malloc(sizeof(int));
  *x = 42;
  printf("\nx = %d", *x);
  *y = 13;
  printf("\ny = %d, %d (doesn't crash as expected booooo)", *y, *x);
  x = y;
  printf("\ny = %d, %d (lost the other reference)", *y, *x);
  return 1;
}
