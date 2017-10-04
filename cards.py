names = []
def everyone_sign(names):
    cards = {}
    redo_names = []
    for x in names:
        pos = names.index(x)
        names.remove(x)
        new_redo_names = str(redo_names).replace("'", "")[1:-1]
        new_names = str(names).replace("'", "")[1:-1]
        cards[x] ='Thank you. From ' + new_names + " " + new_redo_names
        redo_names.append(x)
        names.insert(pos,x)
    print cards
    return cards
everyone_sign([])
