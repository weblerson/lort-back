def singleton(klass):
    instances = dict()

    def get_klass(*args, **kwargs):
        if klass not in instances:
            instances.update({klass: klass(*args, **kwargs)})

        return instances.get(klass)

    return get_klass
