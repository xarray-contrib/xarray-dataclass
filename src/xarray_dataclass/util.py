import importlib
import importlib.util
import sys


def lazy_import(module_name: str):
    """postponed import of the module with the specified name.

    The import is not performed until the module is accessed in the code. This
    reduces the total time for an initial import by waiting to import the module
    until its attributes are accessed.
    """

    # see https://docs.python.org/3/library/importlib.html#implementing-lazy-imports
    try:
        ret = sys.modules[module_name]
        return ret
    except KeyError:
        pass

    spec = importlib.util.find_spec(module_name)
    if spec is None:
        raise ImportError(f'no module found named "{module_name}"')
    spec.loader = importlib.util.LazyLoader(spec.loader)  # type: ignore
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module
