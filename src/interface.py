import inspect

class interface(object):
    pass

def implements(interface):
    def _decorator(clazz):
        for name, method in inspect.getmembers(interface, lambda v: hasattr(v, 'im_class')):
            contract = inspect.getargspec(method)
            impl = getattr(clazz, name, None)
            signature = inspect.getargspec(impl) if impl else None
            if signature != contract:
                raise NotImplementedError("Class '{}' must implement method '{}({})' defined in interface '{}'.".format(
                    clazz.__name__, name, argspec_to_string(contract), interface.__name__
                ))
        return clazz
    return _decorator

def argspec_to_string(spec):
    args = spec.args or []
    defaults = spec.defaults or []
    nrequired = len(args) - len(defaults)
    required = args[:nrequired]
    optional = zip(args[nrequired:], defaults)
    optional = ['{}={}'.format(name, repr(default)) for name, default in optional]
    varargs = ['*' + spec.varargs] if spec.varargs else []
    keywords = ['**' + spec.keywords] if spec.keywords else []
    return ', '.join(required + optional + varargs + keywords)
