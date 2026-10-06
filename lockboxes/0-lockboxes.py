#!/usr/bin/python3
"""Lockboxes algorithm"""
def openBox(boxes, current_index, unopened_boxes, keys):
	for key in boxes[current_index]:
		if key in unopened_boxes:
			unopened_boxes.remove(key)
			keys.append(key)
			openBox(boxes, key, unopened_boxes, keys)
			

def canUnlockAll(boxes):
	unopened_boxes = list(range(len(boxes)))
	keys = []
	for index, box in enumerate(boxes):
		if index in unopened_boxes and (index in keys or index == 0):
			unopened_boxes.remove(index)
			openBox(boxes, index, unopened_boxes, keys)
		print(unopened_boxes)
	if not unopened_boxes:
		return True
	return False
