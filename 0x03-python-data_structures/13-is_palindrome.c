#include "lists.h"
int is_palindrome(listint_t **head);
/**
 *is_palindrome - checks list if palindrome
 *@head: the linked list
 *Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	int i = 0;
	int *hold;
	listint_t *temp;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		i++;
		temp = temp->next;
	}
	temp = *head;
	hold = malloc(i * sizeof(int));
	i--;
	while (temp)
	{
		hold[i--] = temp->n;
		temp = temp->next;
	}
	temp = *head;
	i = 0;
	while (temp && temp->next)
	{
		if (temp->n != hold[i])
		{
			free(hold);
			return (0);
		}
		temp = temp->next;
		i++;
	}
	free(hold);
	return (1);
}
