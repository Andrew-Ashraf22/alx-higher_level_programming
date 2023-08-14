#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

int is_palindrome(listint_t **head)
{
	int i = 0, j = 0;
	listint_t *temp;

	temp = *head;
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (temp)
	{
		i++;
		temp = temp->next;
	}
	temp = *head;
	int *hold = malloc(i * sizeof(int));
	if (hold == NULL)
		return (0);
	while (temp)
	{
		hold[j++] = temp->n;
		temp = temp->next;
	}
	listint_t *head2 = NULL;
	i--;
	while (i >= 0)
	{
		add_nodeint_end(&head2, hold[i]);
		i--;
	}
	temp = *head;
	while (temp && head2)
	{
		if (temp->n != head2->n)
		{
			free(hold);
			free_listint(head2);
			return (0);
		}
		temp = temp->next;
		head2 = head2->next;
	}
	free(hold);
	free_listint(head2);
	return (1);
}
