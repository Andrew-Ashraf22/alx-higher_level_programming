#include "lists.h"

listint_t *reverse(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse - Reverses a LIST
 * @head: the list
 * Return: new reversed list
 */
listint_t *reverse(listint_t **head)
{
	listint_t *temp = *head, *next, *prev = NULL;

	while (temp)
	{
		next = temp->next;
		temp->next = prev;
		prev = temp;
		temp = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if  palindrome.
 * @head: A list
 * Return: 1 is succ 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *rev, *mid;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmp = *head;
	while (tmp)
	{
		size++;
		tmp = tmp->next;
	}

	tmp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		tmp = tmp->next;

	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);

	tmp = tmp->next->next;
	rev = reverse(&tmp);
	mid = rev;

	tmp = *head;
	while (rev)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}
	reverse(&mid);
	return (1);
}

