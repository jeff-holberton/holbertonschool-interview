#!/usr/bin/python3
"""Lockboxes algorithm"""


class Counter:
	"""class counter"""
	def __init__(self):
		"""init method"""
		self.recursion_depth = 0


def openBox(boxes, current_index, unopened_boxes, keys):
	counter = Counter()
	if counter.recursion_depth < 800:
		for key in boxes[current_index]:
			if key in unopened_boxes:
				unopened_boxes.remove(key)
				keys.append(key)
				counter.recursion_depth += 1
				openBox(boxes, key, unopened_boxes, keys)
	else:
		for key in boxes[current_index]:
			if key in unopened_boxes:
				unopened_boxes.remove(key)
				keys.append(key)
				counter.recursion_depth += 1
				openBox2(boxes, key, unopened_boxes, keys)

def openBox2(boxes, current_index, unopened_boxes, keys):
	for key in boxes[current_index]:
		if key in unopened_boxes:
			unopened_boxes.remove(key)
			keys.append(key)
			openBox2(boxes, key, unopened_boxes, keys)

def canUnlockAll(boxes):
	unopened_boxes = list(range(len(boxes)))
	keys = []
	for index, box in enumerate(boxes):
		if index in unopened_boxes and (index in keys or index == 0):
			unopened_boxes.remove(index)
			openBox(boxes, index, unopened_boxes, keys)
	if not unopened_boxes:
		return True
	return False
