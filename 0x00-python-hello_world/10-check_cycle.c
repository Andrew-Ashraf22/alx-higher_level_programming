#include "lists.h"

void add(listint_t *node, listint_t **tab);
int ccheck(listint_t *node, listint_t **tab);

int check_cycle(listint_t *list)
{
	listint_t *tab[20];
	listint_t *temp;

	temp = list;
	while (temp->next && temp)
	{
		if (ccheck(temp, tab))
		{
			return (1);
		}
		add(temp, tab);
		temp = temp->next;
	}
	return (0);
}

/*
 * ccheck - check if node in the array
 * @node: node to check
 * @tab: the array
 * Return: 1 if it matches 0 if not
 */
int ccheck(listint_t *node, listint_t **tab)
{
	int i = 0;

	for (i = 0; tab[i]; i++)
	{
		if (node == tab[i])
		{
			return (1);
		}
	}
	return (0);
}

/*
 * add - add node to the array
 * @node: node to add
 * @tab: the array
 */
void add(listint_t *node, listint_t **tab)
{
	static int j = 0;

	tab[j] = node;
	j++;
}
