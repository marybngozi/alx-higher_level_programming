#include "lists.h"
/* 
 * check_cycle - checks if a listint has a cycle
 * @list: the list to check
 * Return: 0 for no cycle, 1 for cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *j = list;
	listint_t *k = list;

	if (!list)
		return (0);
	while (j && k && k->next)
	{
		j = j->next;
		k = k->next->next;
		if (j == k)
			return (1);
	}
	return (0);
}