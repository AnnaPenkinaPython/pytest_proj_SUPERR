def get_val(collection, key, default='git'):
    if len(collection) == 0:
        return default
    elif key not in collection:
        return default

    return collection[key]
