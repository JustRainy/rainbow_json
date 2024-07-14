base_from = lambda cls, base_cls: (base_cls in cls.__bases__) if type(cls) == type(base_cls) == type else False
