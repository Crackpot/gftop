#coding=utf-8
"""
    def _makeGetterFactory(url, factoryFactory, *args, contextFactory=None, **kwargs):  (source)
    Create and connect an HTTP page getting factory.
    Any additional positional or keyword arguments are used when calling factoryFactory.
        Parameters    factoryFactory    Factory factory that is called with url, args and kwargs to produce the getter
                      contextFactory    Context factory to use when creating a secure connection, defaulting to None
        Returns    The factory created by factoryFactory
"""