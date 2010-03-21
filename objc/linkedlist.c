#import "stdlib.h"
#import "stdio.h"
struct node {
   int data;
   struct node *next;
};

int Length(struct node* head){
  struct node* current = head;
  int count = 0;
  printf("\nentering loop");
  while (current != NULL){
      printf("\nincrementing count %d, value is %d", count, current->data);
      count++; 
      current = current->next;
  }
  printf("\nfinal count %d", count);
  return count;
}

struct node* BuildOneTwoThree(){
  struct node* head = NULL;
  struct node* second = NULL;
  struct node* third = NULL;

  head = malloc (sizeof(struct node));
  second = malloc (sizeof(struct node));
  third = malloc (sizeof(struct node));

  printf("1");
  head->data=1;
  head->next = second;

  printf("2");
  second->data=2;
  second->next = third;

  printf("3");
  third->data=3;
  third->next = NULL;

  return head;
}

void Push(struct node** head, int value){
  struct node* newNode = malloc(sizeof(struct node*));
  newNode->data = value;
  newNode->next = *head;
  *head = newNode; 
}

int main(){
  struct node* list = NULL;
  printf("\nlength of empty list  %d", Length(list));
  //list = BuildOneTwoThree();
  //printf("\nlength of 123 list %d", Length(list));
  Push(&list, 5);
  printf("\nlength of 5123 list %d", Length(list));
  return 1;
}
