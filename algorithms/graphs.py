from collections import deque

def breadth_first_search(**kwargs):
    """Searches through a network of names to find that ends with m"""
    search_queue = deque() # create a queue
    search_queue += {k:v for k,v in kwargs} # add the network to be searched through
    searched = []
    while search_queue:
        person = search_queue.popleft() # take out first person from queue
        if not person in searched:
            if person[-1]=="m":
                print("Found culprit")
                return True
            else:
                search_queue += graph[person] # add person's contacts to queue
                searched.append[person] # add their name to list of searched names
    return False

