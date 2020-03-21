#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # Each ticket is represented as an instance of Class Ticket
    for ticket in tickets:
        source = ticket.source
        destination = ticket.destination
        print(f"source: {source}")
        print(f"destination: {destination}")
        # Add items to the hash table
        # Starting location = key / the destination = value
        hash_table_insert(hashtable, source, destination)

    # Reconstruct the intinerary with the correct link order in an array

    pass


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

reconstruct_trip(tickets, 3)
