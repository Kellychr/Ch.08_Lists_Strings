'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
import random

room_list=[]

room=["front porch",2,None,None,None] #room 0
room_list.append(room)

room=["bedroom 2",2,None,None,None] #room 1
room_list.append(room)

room=["south hall",2,None,None,None] #room 2
room_list.append(room)

room=["dining room",2,None,None,None]
room_list.append(room)

room=["bedroom 1",2,None,None,None]
room_list.append(room)

room=["north hall",2,None,None,None]
room_list.append(room)

room=["kitchen",2,None,None,None]
room_list.append(room)

current_room = 0


#sart progarm

done=False
while not done:
    print()
    print(room_list[current_room][0])
    drct = input("which way? N, E, S, W or Q t quit")
    if drct.lower()=="n"
        next_room = room_list[current_room][1]
        if next_room==None:
            print("you cant go that way!")
        else:
            current_room = next_room

    print()
    print(room_list[current_room][0])
    drct = input("which way? N, E, S, W or Q t quit")
    if drct.lower()=="e"
        next_room = room_list[current_room][1]
        if next_room==None:
            print("you cant go that way!")
        else:
            current_room = next_room

    print()
    print(room_list[current_room][0])
    drct = input("which way? N, E, S, W or Q t quit")
    if drct.lower()=="s"
        next_room = room_list[current_room][1]
        if next_room==None:
            print("you cant go that way!")
        else:
            current_room = next_room

    print()
    print(room_list[current_room][0])
    drct = input("which way? N, E, S, W or Q t quit")
    if drct.lower()=="w"
        next_room = room_list[current_room][1]
        if next_room==None:
            print("you cant go that way!")
        else:
            current_room = next_room

    print()
    print(room_list[current_room][0])
    drct = input("which way? N, E, S, W or Q t quit")
    if drct.lower() == "q"
        next_room = room_list[current_room][1]
        if next_room == None:
            print("you cant go that way!")
        else:
            current_room = next_room


