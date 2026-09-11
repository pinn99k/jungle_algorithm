//////////////////////////////////////////////////////////////////////////////////

/* CE1007/CZ1007 Data Structures
Lab Test: Section A - Linked List Questions
Purpose: Implementing the required functions for Question 1 */

//////////////////////////////////////////////////////////////////////////////////

#include <stdio.h>
#include <stdlib.h>

//////////////////////////////////////////////////////////////////////////////////

// You should not change the definition of ListNode
// 리스트 노드 구조체
typedef struct _listnode{
	int item;
	struct _listnode *next;
} ListNode;

// You should not change the definition of LinkedList
// 리스트 노드의 0을 반환하는 리스트 호출 구조체
typedef struct _linkedlist{
	int size;
	ListNode *head;
} LinkedList;			

///////////////////////// function prototypes ////////////////////////////////////

//You should not change the prototype of this function
// 아래에서 사용하기 위해 먼저 선언해야 함
// 정의는 아래에서
int insertSortedLL(LinkedList *ll, int item);

void printList(LinkedList *ll);
void removeAllItems(LinkedList *ll);
ListNode *findNode(LinkedList *ll, int index);
int insertNode(LinkedList *ll, int index, int value);
int removeNode(LinkedList *ll, int index);


//////////////////////////// main() //////////////////////////////////////////////

int main()
{
	// 연결 리스트를 선언
	LinkedList ll;
	// c는 무엇인지 파악 못함
	int c, i, j;
	c = 1;

	//Initialize the linked list 1 as an empty linked list
	// 링크드 리스트의 처음의 헤드를 비우고 사이즈를 0으로 
	// 아마 사이즈를 만들고 헤드를 연결하는 것
	ll.head = NULL;
	ll.size = 0;

	printf("1: Insert an integer to the sorted linked list:\n");
	printf("2: Print the index of the most recent input value:\n");
	printf("3: Print sorted linked list:\n");
	printf("0: Quit:");

	// c는 boolean 처럼 사용 
	// 참 인동안 반복
	while (c != 0)
	{
		printf("\nPlease input your choice(1/2/3/0): ");
		scanf("%d", &c);

		switch (c)
		{
		case 1:
			printf("Input an integer that you want to add to the linked list: ");
			scanf("%d", &i); // 추가할 정수의 주소를 입력
			// 추측 / j 에 넣은 주소를 저장하는 건가요? 흠...
			j = insertSortedLL(&ll, i); // 인덱스를 리턴해야 함
			printf("The resulting linked list is: ");
			// 현재 리스트 값들을 출력
			// printList 라는 함수로 출력하는 것 같음
			// 추측 / 반복문으로 노드를 건너가며 출력하지 않을까 싶음
			printList(&ll);
			break;
		case 2:
			// j 의 인덱스에 추가된 i 값을 알려줌
			printf("The value %d was added at index %d\n", i, j);
			break;
		case 3:
			// 정렬된 리스트를 출력함
			printf("The resulting sorted linked list is: ");
			printList(&ll);
			break;
		case 0: // 종료 조건
			// 리스트를 비우는 건가?
			// 추측 / for 문을 돌면서 노드마다 free를 해주면 되지 않을까 싶음
			removeAllItems(&ll);
			break;
		default:
			printf("Choice unknown;\n");
			break;
		}


	}
	return 0;
}

//////////////////////////////////////////////////////////////////////////////////

// 직접 구현해봄
// 이걸 리펙토링 하면서 아래 함수와 비교해 볼 듯
int insertSortedLL(LinkedList *ll, int item)
{
    ListNode *cur = ll->head;
    ListNode *prev = NULL;
    ListNode *node;

	int i = 0;

    // 위치 찾기: cur->item >= item인 지점까지 전진
    while (cur != NULL && cur->item < item) {
        prev = cur; // 아이템의 이전 노드
        cur = cur->next; // 아이템의 다음 노드
        i++;
    }

    if (cur != NULL && cur->item == item){
		return -1;
	}

    ListNode *node = (ListNode *)malloc(sizeof(ListNode));
    node->item = item;
    node->next = NULL;
	
    if (prev == NULL) {
        node->next = ll->head;
        ll->head = node;
    } else {
        node->next = cur;
        prev->next = node;
    }
    ll->size++;

    return i;
}
///////////////////////////////////////////////////////////////////////////////////

void printList(LinkedList *ll){

	ListNode *cur;
	if (ll == NULL)
		return;
	cur = ll->head;

	if (cur == NULL)
		printf("Empty");
	while (cur != NULL)
	{
		printf("%d ", cur->item);
		cur = cur->next;
	}
	printf("\n");
}


void removeAllItems(LinkedList *ll)
{
	ListNode *cur = ll->head;
	ListNode *tmp;

	while (cur != NULL){
		tmp = cur->next;
		free(cur);
		cur = tmp;
	}
	ll->head = NULL;
	ll->size = 0;
}


ListNode *findNode(LinkedList *ll, int index){

	ListNode *temp;

	if (ll == NULL || index < 0 || index >= ll->size)
		return NULL;

	temp = ll->head;

	if (temp == NULL || index < 0)
		return NULL;

	while (index > 0){
		temp = temp->next;
		if (temp == NULL)
			return NULL;
		index--;
	}

	return temp;
}

int insertNode(LinkedList *ll, int index, int value){

	ListNode *pre, *cur;

	if (ll == NULL || index < 0 || index > ll->size + 1)
		return -1;

	// If empty list or inserting first node, need to update head pointer
	if (ll->head == NULL || index == 0){
		cur = ll->head;
		ll->head = malloc(sizeof(ListNode));
		ll->head->item = value;
		ll->head->next = cur;
		ll->size++;
		return 0;
	}


	// Find the nodes before and at the target position
	// Create a new node and reconnect the links
	if ((pre = findNode(ll, index - 1)) != NULL){
		cur = pre->next;
		pre->next = malloc(sizeof(ListNode));
		pre->next->item = value;
		pre->next->next = cur;
		ll->size++;
		return 0;
	}

	return -1;
}


int removeNode(LinkedList *ll, int index){

	ListNode *pre, *cur;

	// Highest index we can remove is size-1
	if (ll == NULL || index < 0 || index >= ll->size)
		return -1;

	// If removing first node, need to update head pointer
	if (index == 0){
		cur = ll->head->next;
		free(ll->head);
		ll->head = cur;
		ll->size--;

		return 0;
	}

	// Find the nodes before and after the target position
	// Free the target node and reconnect the links
	if ((pre = findNode(ll, index - 1)) != NULL){

		if (pre->next == NULL)
			return -1;

		cur = pre->next;
		pre->next = cur->next;
		free(cur);
		ll->size--;
		return 0;
	}

	return -1;
}
