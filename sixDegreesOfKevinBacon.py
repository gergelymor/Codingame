import sys
import math

# 6 Degrees of Kevin Bacon!

actor_name = input()
casts = []
bacon = "Kevin Bacon"

if actor_name == bacon:
    print("0")
    quit()

class Node:
    def __init__(self,name):
        self.name = name
        self.children = []
    
    def get_name(self):
        return self.name

    def get_children(self):
        return self.children

elements = {}

n = int(input())
for i in range(n):
    movie_cast = (input().split(":")[1])[1:].split(", ")
    if actor_name in movie_cast and bacon in movie_cast:
        print("1")
        quit()
    
    for actor in movie_cast:
        person = Node(actor)
        for other_person in movie_cast:
            if actor != other_person and other_person not in person.get_children():
                person.children.append(other_person)
        if actor not in elements:
            elements[actor] = person.get_children()
        else:
            elements[actor].extend(person.get_children())


degrees = 1
to_visit = elements[actor_name]

while to_visit:
    if bacon in to_visit:
        print(degrees)
        break
    else:
        degrees += 1
        tmp = []
        for name in to_visit:
            for actor_name in elements[name]:
                tmp.append(actor_name)
        to_visit = tmp
