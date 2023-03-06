#include "lists.h"
/**
 * check_cycle - function checks if a singly linked list has a cycle in it.
 * @list: pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *curr, *temp;

	if (list == NULL || list->next == NULL)
		return (0);
	curr = list;
	temp = curr->next;

	while (curr != NULL && temp->next != NULL && temp->next->next != NULL)
	{
		if (curr == temp)
			return (1);
		curr = curr->next;
		temp = temp->next->next;
	}
	return (0);
}
