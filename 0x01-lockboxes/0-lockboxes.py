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
    if not boxes:
        return False

    n = len(boxes)
    unlocked = set([0])
    queue = [0]

    while queue:
        current_box = queue.pop()
        for key in boxes[current_box]:
            if key < n and key not in unlocked:
                unlocked.add(key)
                queue.append(key)

    return len(unlocked) == n
