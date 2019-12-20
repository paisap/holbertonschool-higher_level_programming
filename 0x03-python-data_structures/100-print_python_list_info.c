#include <Python.h>
#include <stdio.h>
void print_python_list_info(PyObject *p)
{
	PyObject *new;
	int len = 0, i = 0;
	
	len = PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < len; i++)
	{
		new = PyList_GetlIem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(new)->tp_name);
	}


}
