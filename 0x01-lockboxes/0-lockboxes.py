#!/usr/bin/python3
"""
0-lockboxes.py
This module contains the function `def canUnlockAll(boxes)`,
which determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1 and
    each box may contain box_keys to the other boxes. Write a
    method that determines if all the boxes can be opened
    """
    def canUnlockAllRec(boxes, unlocked, box):
        """Recursive function for canUnlockAll"""
        if len(box) == 0:
            return

        for i in range(len(box)):
            if box[i] in unlocked or box[i] >= len(boxes):
                continue
            if box[i] != 0:
                unlocked.append(box[i])
            if box[i] == i and len(box) == 1:
                return
            canUnlockAllRec(boxes, unlocked, boxes[box[i]])

    unlocked = []
    number_boxes_to_unlock = len(boxes) - 1

    # print('All boxes:', boxes)

    if len(boxes) == 0:
        return True
    if len(boxes[0]) == 0:
        if len(boxes) == 1:
            return True
        return False

    canUnlockAllRec(boxes, unlocked, boxes[0])

    # print('Boxes unlocked:', unlocked)
    if len(unlocked) == number_boxes_to_unlock:
        return True
    return False
