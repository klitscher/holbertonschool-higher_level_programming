#include "lists.h"

/**
 * check_cycle - checks to see if the list has a cycle in it
 * @list: list to check
 *
 * Return: 0 if no cycle, 1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	if (list == NULL || list->next == NULL)
		return (0);
	slow = list;
	fast = list->next;
	while (fast != NULL)
	{
		if (fast == slow)
			return (1);
		fast = fast->next;
		if (fast == NULL)
			break;
		if (fast == slow)
			return (1);
		fast = fast->next;
		if (fast == slow)
			return (1);
		slow = slow->next;
	}
	return (0);
}
