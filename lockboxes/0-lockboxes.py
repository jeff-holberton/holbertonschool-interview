#!/usr/bin/python3
"""Lockboxes algorithm"""


def canUnlockAll(boxes):
	n = len(boxes)
	opened = {0}
	to_visit = [0]

	while to_visit:
		current = to_visit.pop()
		for key in boxes[current]:
			if 0 <= key < n and key not in opened:
				to_visit.append(key)
				opened.add(key)

	return len(opened) == n
