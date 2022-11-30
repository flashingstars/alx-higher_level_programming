#include <lists.h>

/**
 * check_cycle - checks for a cycle in a linked list
 *
 * @list: head of the list
 *
 * Return: 0 on success, 1 on failure
 */

int check_cycle(list_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list == NULL)
		return (1);
	while (slow->next && fast->next->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (0);
	}
	return (0);
}
