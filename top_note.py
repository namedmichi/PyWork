
def top_note(dic):
    highest = 0
    name = dic["name"]
    notes = dic["notes"]
    for n in notes:
        if n > highest:
            highest = n
    return name , " beste Note ist:", highest















print(top_note({ "name": "John", "notes": [3, 5, 4] }))