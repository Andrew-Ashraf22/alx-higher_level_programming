#include <Python.h>
#include <listobject.h>
#include <object.h>
/**
 * print_python_list_info - Prints python list info
 * @p: a list
 */
void print_python_list_info(PyObject *p)
{
	int len, i, ls_Msize;

	len = Py_SIZE(p);
	ls_Msize = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", ls_Msize);

	for (i = 0; i < len; i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
