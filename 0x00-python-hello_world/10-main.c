#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
#include <time.h>
/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
	listint_t *head;
	listint_t *current;
	listint_t *temp;
	int i;
	clock_t clk;
	clock_t clk2;
	head = NULL;
	for (i = 0; i < 1000000; i++)
		add_nodeint(&head, 50);
	add_nodeint(&head, 0);
	add_nodeint(&head, 1);
	add_nodeint(&head, 2);
	add_nodeint(&head, 3);
	add_nodeint(&head, 4);
	add_nodeint(&head, 98);
	add_nodeint(&head, 402);
	add_nodeint(&head, 1024);

	clk = clock();
	i = check_cycle(head);
	clk = clock() - clk;
	printf("Time elapsed: %f\n", (double)clk/CLOCKS_PER_SEC);
	if (i == 0)
		printf("Linked list has no cycle\n");
	else if (i == 1)
		printf("Linked list has a cycle\n");

	current = head;
	for (i = 0; i < 1000000; i++)
		current = current->next;
	temp = current->next;
	current->next = head;

	clk2 = clock();
	i = check_cycle(head);
	clk2 = clock() - clk2;
	printf("Time elapsed: %f\n", (double)clk2/CLOCKS_PER_SEC);
	if (i == 0)
		printf("Linked list has no cycle\n");
	else if (i == 1)
		printf("Linked list has a cycle\n");

	current = head;
	for (i = 0; i < 4; i++)
		current = current->next;
	current->next = temp;

	free_listint(head);

	return (0);
}
