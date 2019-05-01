#include "lists.h"
#include <stdlib.h>
#include <unistd.h>

/**
 * insert_node - inserts a number in an ordered linked list
 * @head: double pointer to the linked list
 * @number: number to insert in the new node
 *
 * Return: address of the new node, or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new;
	listint_t *temp;

	if (!head || !*head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;

	while (current->n < number)
	{
		temp = current;
		current = current->next;
	}

	temp->next = new;
	new->next = current;

	return (new);
}
