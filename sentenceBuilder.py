def sentenceBuilder(subjects, verbs, objects):
    """
    Builds a sentence of all possible combinations of subject, verb and object.

    Params: subjects(list), verbs(list), objects(list)

    Returns: None, prints out all the combinations of subject, verb and object
    with a number for each sentence. Each sentence is capitalized with a full stop
    at the end.
    """
    # Num stores our sentence number...
    num = 0
    # For each index in range of the length of all lists * 3 (total sentences)...
    for i in range((len(subjects) + len(verbs) + len(objects)) * 3):
        # If i == 3 we have iterated all 3 subjects with all combinations, so we break.
        if i == 3:
            break
        # Else...
        else:
            # For each j in range of length of verbs...
            for j in range(len(verbs)):
                # We iterate each of the objects to the range of the length of objects...
                for k in range(len(objects)):
                    # Increment the sentence counter...
                    num += 1
                    # And print the sentence number + subject + verb + object
                    print(f'{num:>3} {subjects[i].capitalize()} {verbs[j]} {objects[k]}.')

subjects = ["Peppa Pig", "my neighbour", "the Major"]
verbs = ["kissed", "ate", "read"]
objects = ["a book", "a steak", "a dog"]

sentenceBuilder(subjects, verbs, objects)