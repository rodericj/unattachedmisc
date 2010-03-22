#import "stdlib.h"
#import "stdio.h"
#import "assert.h"
struct node {
   int data;
   struct node *next;
};

int InsertNth(struct node* head, int n, int value){
  assert(n >=0); 
  struct node* current = head;
  int count = 0;
  while (current != NULL){
      if (n-1 == count){
        //malloc
		struct node* newNode = malloc(sizeof(struct node));
		newNode->data = value;

        //set new->next to n
		newNode->next = current->next;

        //change n-1th->next to new
		current->next = newNode;

		return current->data;
	  }
	  count++;
      current = current->next;
  }
  return -1;
}

int GetNth(struct node* head, int n){
  assert(n >=0); 
  struct node* current = head;
  int count = 0;
  while (current != NULL){
      if (n == count){
		return current->data;
	  }
	  count++;
      current = current->next;
  }
  return -1;
}

int Count(struct node* head, int value){
  struct node* current = head;
  int count = 0;
  while (current != NULL){
      printf("checking if %d = %d\n", value, current->data);
      if (current->data == value){
		printf("it does\n");
		count++; 
	  }
      current = current->next;
  }
  return count;
}

int Length(struct node* head){
  struct node* current = head;
  int count = 0;
  printf("entering loop\n");
  while (current != NULL){
      printf("incrementing count %d, value is %d\n", count, current->data);
      count++; 
      current = current->next;
  }
  printf("final count %d\n", count);
  return count;
}

int PrintList(struct node* head){
  struct node* current = head;
  printf("entering loop\n");
  while (current != NULL){
      printf("%d", current->data);
      current = current->next;
  }
  printf("\n");
  return 1;
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
  printf("length of empty list  %d\n", Length(list));
  list = BuildOneTwoThree();
  printf("\nlength of 123 list %d", Length(list));
  Push(&list, 5);
  Push(&list, 5);
  printf("length of 55123 list %d\n", Length(list));
  printf("Problem 1: number of 5's %d\n", Count(list, 5));
  printf("Problem 1: number of 1's %d\n", Count(list, 1));
  printf("Problem 2: the 3rd (list[2]) element is: %d\n", GetNth(list, 2));
  printf("Problem 5: Add 6 as the 3th element");
  InsertNth(list, 3, 6);
  PrintList(list);
  return 1;
}
