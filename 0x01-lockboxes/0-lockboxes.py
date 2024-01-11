#!/usr/bin/python3
""" a module that contain a function that determines if all the boxes
    can be opened. True if they can all be opened and false if they can't.
"""


def canUnlockAll(boxes):
    """ a function that finds whether all boxes has available keys """
    status = [True]
    i = len(boxes)
    y = 1
    while(y < i):
        status.append(False)
        y = y + 1
    for index, box in enumerate(boxes):
        for key in box:
            if key == index:
                continue
            status[key] = True
    for k in range(i):
        if not status[k]:
            return False
    return True
