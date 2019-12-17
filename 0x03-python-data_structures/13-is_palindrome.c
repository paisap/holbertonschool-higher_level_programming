#include "lists.h"
/**
 * is_palindrome - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * Return: address of the new element or NULL if it fails
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *tmp1, *limit, *tmp_prev;
	int len = 0, i = 0;

	if (*head == NULL || head == NULL)
		return (1);
	tmp1 = *head, limit = *head;
	while (limit->next != NULL)
		len++, tmp_prev = limit, limit = limit->next;
	len++;
	if (len == 1)
		return (1);
	while (i < (len / 2))
	{
		if (tmp1->n != limit->n)
			return (0);
		limit = tmp_prev;
		tmp = tmp1;
		while (tmp != limit)
			tmp_prev = tmp, tmp = tmp->next;
		tmp1 = tmp1->next;
		i++;
	}
	return (1);
}
