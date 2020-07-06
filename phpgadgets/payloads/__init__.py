import importlib
import pkgutil

__all__ = []
for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    module = importlib.import_module('.'.join([__package__, name]))
    if hasattr(module, 'META') and hasattr(module, 'construct'):
        __all__.append(name)
