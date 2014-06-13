"""Import utilities."""


def import_member(import_string):
    """Import one member of Python module by path.

    >>> import os.path
    >>> imported = import_member('os.path.supports_unicode_filenames')
    >>> os.path.supports_unicode_filenames is imported
    True

    """
    module_name, factory_name = str(import_string).rsplit('.', 1)
    module = __import__(module_name, globals(), locals(), [factory_name], 0)
    return getattr(module, factory_name)
