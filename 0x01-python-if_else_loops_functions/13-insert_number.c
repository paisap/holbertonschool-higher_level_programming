#include "lists.h"
/**
 * insert_node - prints all elements of a listint_t list
 * @head: pointer to head of list
 * @number: the number
 * Return: the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *aux = (*head);

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	while (aux->next != NULL)
	{
		if (number > aux->n && number < aux->next->n)
		{
			new->next = aux->next;
			aux->next = new;
			break;
		}
		aux = aux->next;
	}
	if (aux->next == NULL)
		new->next = NULL;
	return (new);
}
