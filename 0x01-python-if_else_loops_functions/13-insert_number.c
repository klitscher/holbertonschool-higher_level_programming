#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a node and new number into a linked list
 * @head: linked list to insert a node into
 * @number: number to add to the list
 *
 * Return: Pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node;
	listint_t *move;

	if (head == NULL)
		return (NULL);
	move = *head;
	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;
	node->next = NULL;
	if (*head == NULL)
		*head = node;
	else
	{
		while (move->next->n < number)
		{
			move = move->next;
		}
		node->next = move->next;
		move->next = node;
	}
	return (node);
}
