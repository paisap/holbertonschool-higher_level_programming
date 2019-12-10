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

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	if (*head == NULL)
		*head = new;
	new->n = number;
	if (number < aux->n)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
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
	}
	if (aux->next == NULL)
	{
		aux->next = new;
		new = NULL;
	}
	return (new);
}
