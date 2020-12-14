def increment_dictionary_values(d: dict, i: int) -> dict:
    """This function increments a dictionary value by a given number."""
    for key, value in d.items():
        d[key] = value + i  
    return d 
