#include "lists.h"
int is_palindrome(listint_t **head);
/**
 *is_palindrome - checks list if palindrome
 *@head: the linked list
 *Return: 1 if succ 0 if not
 */
int is_palindrome(listint_t **head)
{
	int i = 0, j = 0;
	listint_t *temp = *head;

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

	i--;
	while (temp)
	{
		hold[i--] = temp->n;
		temp = temp->next;
	}
	temp = *head;

	while (temp)
	{
		if (temp->n != hold[j])
		{
			free(hold);
			return (0);
		}
		temp = temp->next;
		j++;
	}
	free(hold);
	return (1);
}
