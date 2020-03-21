#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # Add items to the hash table
    i = 0
    for weight in weights:
        hash_table_insert(ht, weight, i)
        i += 1

    # Find two items whose sum of weights equals the weight limit

    # Return an instance of an Answer tuple (zero, one)

    # If such a pair doesn’t exist, return None.
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
