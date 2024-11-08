from curses.textpad import rectangle

import data

# Write your functions for each part in the space below.

# Part 1
def create_rectangle(p1: data.Point,p2: data.Point):
    # finding the top left corner
    if p1.x-p2.x>=0:
        leftx = p1.x
    else:
        leftx = p2.x
    if p1.y-p2.y>=0:
        lefty = p1.y
    else:
        lefty = p2.y

    # Finding the bottom right corner
    if p1.x-p2.x>=0:
        rightx = p2.x
    else:
        rightx = p1.x
    if p1.y-p2.y>=0:
        righty = p2.y
    else:
        righty = p1.y

    newp1 = data.Point(leftx,lefty)
    newp2 = data.Point(rightx,righty)
    return rectangle(newp1,newp2)


# Part 2
def shorter_duration_than(d1: data.Duration, d2: data.Duration):
    if d2.minutes>d1.minutes:
        return True
    elif d2.seconds>d2.seconds:
        return True
    else:
        return False

# Part 3
# Define a function named song_shorter_than with two parameters; the first of type list[Song] and the second of type Duration indicating an upper bound on a
# song's length. This function must return a list of all songs (of type list[Song]) in the input list with duration less than the provided duration parameter.
def song_shorter_than(l1: list[data.Song], d: data.Duration):
    shortlist = []
    for i in range(len(l1)):
        if i.minutes<= d.minutes:
            shortlist.append(i.title)
        elif i.seconds<i.seconds:
            shortlist.append(i.title)
    return shortlist


# Part 4
def running_time(l1: list[data.Song], l2: [int]):
    totalmin = 0
    totalsec = 0
    for i in l2:
       totalmin = l1[i].duration.minutes + totalmin
       totalsec = l1[i].duration.seconds + totalsec
    return totalmin + totalsec%10


# Part 5



# Part 6

