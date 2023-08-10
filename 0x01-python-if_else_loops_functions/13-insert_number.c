#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
/**
 * insert_node - Inserts a number to the list
 * @head: pointer to the head
 * @number: number to add
 * Return: new node , if failed NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp;

	temp = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;

	if (temp == NULL)
	{
		new->next = temp;
		*head = new;
		return (new);
	}
	if (temp->n >= number)
	{
		new->next = temp;
		*head = new;
		return (new);
	}

	while (temp->next->n < number && temp->next && temp)
	{
		temp = temp->next;
	}

	new->next = temp->next;
	temp->next = new;
	return (new);

}
