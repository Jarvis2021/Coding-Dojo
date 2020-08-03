#Assignment: Filter by Type


def FilterTypes(x):

    if isinstance(x,int) and x >= 100:
        return "That's a big Number"

    elif isinstance(x,int) and x <100:
        return "That's a small number!"

    if isinstance(x,list) and len(x) >= 10:
        return "Big List"

    elif isinstance(x, list) and len(x) < 10:
        return "Short List"

    if isinstance(x, str) and len(x) >= 50:
        return "Long Sentence"

    elif isinstance(x, str) and len(x) < 50:
        return "Short sentence"


print(FilterTypes('Pramod Is Clever'))
