#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: linked list to check
 *
 * Return: 0 if not palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int arr[1024] = {0};
	int end = 0;
	int beg = 0;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	current = *head;
/*	while (current != NULL)
	{
		current = current->next;
		end++;
	}
	arr = malloc(sizeof(int) * end);
	if (arr == NULL)
		return (0);
	current = *head;
	end = 0;
*/	while (current != NULL)
	{
		arr[end] = current->n;
		current = current->next;
		end++;
	}
	end--;
	for (; beg < end; beg++, end--)
	{
		if (arr[beg] != arr[end])
		{
			/*free(arr);*/
			return (0);
		}
	}
	/*free(arr);*/
	return (1);
}
