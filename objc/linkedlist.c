#import "stdlib.h"
#import "stdio.h"
#import "assert.h"
struct node {
   int data;
   struct node *next;
};

int Reverse(struct node** head){
  struct node* current = *head;
  struct node* theNextOne = current->next;
  struct node* theThirdOne = theNextOne->next;
  while (current != NULL){
	  if(current == *head){
		current->next = NULL;
	  } 
	  theNextOne->next = current;
	  current = theNextOne;
      if(theThirdOne == NULL){
		 *head = theNextOne;
         return 1;
      }
      theNextOne = theThirdOne;
	  theThirdOne = theThirdOne->next;
  }

return 1;
}

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
      if (current->data == value){
		count++; 
	  }
      current = current->next;
  }
  return count;
}

int Length(struct node* head){
  struct node* current = head;
  int count = 0;
  while (current != NULL){
      count++; 
      current = current->next;
  }
  return count;
}

int PrintList(struct node* head){
  struct node* current = head;
  while (current != NULL){
      printf("%d", current->data);
      current = current->next;
  }
  return 1;
}

struct node* BuildOneTwoThree(){
  struct node* head = NULL;
  struct node* second = NULL;
  struct node* third = NULL;

  head = malloc (sizeof(struct node));
  second = malloc (sizeof(struct node));
  third = malloc (sizeof(struct node));

  head->data=1;
  head->next = second;

  second->data=2;
  second->next = third;

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
  printf("Problem 5: Add 6 as the 3th element\n");
  InsertNth(list, 3, 6);
  printf("print the list\n");
  PrintList(list);

  printf("\nProblem 17: Reverse the list\n");
  Reverse(&list);
  PrintList(list);
  printf("\n");
  //Reverse(list);
  return 1;
}
