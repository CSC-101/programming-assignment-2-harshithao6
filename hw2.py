from curses.textpad import rectangle

import data

# Write your functions for each part in the space below.

# Part 1
def create_rectangle(p1: data.Point,p2: data.Point):
    # finding the top left corner
    if p1.x-p2.x>=0:
        leftx = p2.x
    else:
        leftx = p1.x
    if p1.y-p2.y>=0:
        lefty = p1.y
    else:
        lefty = p2.y

    # Finding the bottom right corner
    if p1.x-p2.x>=0:
        rightx = p1.x
    else:
        rightx = p2.x
    if p1.y-p2.y>=0:
        righty = p2.y
    else:
        righty = p1.y

    return data.Rectangle(data.Point(leftx,lefty),data.Point(rightx,righty))


# Part 2
def shorter_duration_than(d1: data.Duration, d2: data.Duration):
    if d2.minutes>d1.minutes:
        return True
    elif d2.minutes == d1.minutes and d2.seconds>d2.seconds:
        return True
    else:
        return False

# Part 3
# Define a function named song_shorter_than with two parameters; the first of type list[Song] and the second of type Duration indicating an upper bound on a
# song's length. This function must return a list of all songs (of type list[Song]) in the input list with duration less than the provided duration parameter.
def song_shorter_than(l1: list[data.Song], d: data.Duration):
    shortlist = []
    for i in range(len(l1)):
        if l1[i].duration.minutes < d.minutes:
            shortlist.append(l1[i])
        elif l1[i].duration.minutes==d.minutes and l1[i].duration.seconds < d.seconds:
            shortlist.append(l1[i])
    return shortlist




# Part 4
def running_time(l1: list[data.Song], l2: [int]):
    totalmin = 0
    totalsec = 0
    for i in l2:
       totalmin = l1[i].duration.minutes + totalmin
       totalsec = l1[i].duration.seconds + totalsec

    totalmin += totalsec// 60
    totalsec = totalsec % 60
    return data.Duration(totalmin,totalsec)


# Part 5
def validate_route(links:list[list[str]],names:list[str]):
    answers = []
    if names == [] or len(names) == 1:
        return True
    for i in range(len(links)-1):
        if(links[i][0]==links[i+1][0]or
                links[i][0] == links[i+1][1] or
                links[i][1] == links[i+1][0] or
                links[i][1] == links[i+1][1]):
            answers.append(True)
        else:
            answers.append(False)
        if False in answers:
            return False
        elif names == [] or len(names) == 1:
            return True
        else:
            return True




# Part 6
def longest_repetition(nums: list[int]):
    if not nums:
        return None

    max_len = 1
    current_len = 1
    max_index = 0
    current_start = 0

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            current_len += 1
        else:
            if current_len > max_len:
                max_len = current_len
                max_index = current_start

            current_len = 1
            current_start = i


    if current_len > max_len:
        max_index = current_start

    return max_index

        



