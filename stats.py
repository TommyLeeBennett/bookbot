def count_words(string):
    return len(string.split())

def count_characters(string):
    counts = {}
    for character in string:
        character = character.lower()
        if character in counts:
            counts[character] += 1
        else:
            counts[character] = 1           
    return counts

def sort_counts(counts):
    sorted_counts = [{k: v} for k, v in counts.items()]
    sorted_counts.sort(key=lambda dictionary: list(dictionary.values())[0], 
                       reverse=True)
    return sorted_counts
