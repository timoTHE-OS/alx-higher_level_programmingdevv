#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <stdlib.h>
#include <float.h>

void print_python_float(PyObject *p)
{
    PyFloatObject *f = (PyFloatObject *)p;

    printf("[.] float object info\n");
    if (!PyFloat_Check(f))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    printf("  value: %f\n", f->ob_fval);
}

void print_python_bytes(PyObject *p)
{
    long int size;
    int i;
    char *trying_str = NULL;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    PyBytes_AsStringAndSize(p, &trying_str, &size);

    printf("  size: %li\n", size);
    printf("  trying string: %s\n", trying_str);
    if (size < 10)
        printf("  first %li bytes:", size + 1);
    else
        printf("  first 10 bytes:");
    for (i = 0; i <= size && i < 10; i++)
        printf(" %02hhx", trying_str[i]);
    printf("\n");
}

void print_python_list(PyObject *p)
{
    long int size;
    int i;
    PyListObject *list = (PyListObject *)p;
    const char *type;

    printf("[*] Python list info\n");
    if (!PyList_Check(list))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_GET_SIZE(p);
    printf("[*] Size of the Python List = %li\n", size);
    printf("[*] Allocated = %li\n", list->allocated);
    for (i = 0; i < size; i++)
    {
        type = (list->ob_item[i])->ob_type->tp_name;
        printf("Element %i: %s\n", i, type);
        if (!strcmp(type, "bytes"))
            print_python_bytes(list->ob_item[i]);
        if (!strcmp(type, "float"))
            print_python_float(list->ob_item[i]);
    }
}
