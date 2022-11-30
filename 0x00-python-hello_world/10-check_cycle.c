#include "lists.h"
/**
 * check_cycle - checks for a cycle in a linked list
 * @list: head of the list
 * Return: 0 on failure, 1 on success
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow != NULL && fast->next && fast->next->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
