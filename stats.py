def count_words(text):
    return len(text.split())

def count_characters(text):
    dict = {}
    for char in text:
        if char.lower() in dict:
            dict[char.lower()] += 1
        else:
            dict[char.lower()] = 1

    return dict

def get_sorted_characters(text):
    dict = count_characters(text)
    arr = []
    for x in dict:
        temp = {"char": x, "count": dict[x]}
        arr.append(temp)

    def sort_on(items):
        return items["num"]

    arr.sort(reverse=True, key=sort_on)

    return arr