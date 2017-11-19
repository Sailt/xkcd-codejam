from __future__ import print_function
import string
import random

# Fix input() vs raw_input() mess
try: input = raw_input
except NameError: pass

class World:

	class Room:
		def __init__(self):
			self.name = ""
			self.desc = ""
			self.exits = []
			self.npcs = []
			self.items = []

	def __init__(self):
		self.rooms = []
		self.createRooms()

	def move(self, newRoom):
		for exit in self.curRoom.exits:
			if string.find(exit['localName'].lower(), newRoom.lower()) == 0:
				self.curRoom = exit['room']
				self.displayRoom()
				return
		print("You can't go that way.")

	def displayRoom(self):
		print("")
		print(self.curRoom.name)
		print(self.curRoom.desc)

		self.displayExits()
		self.displayItems()
		self.displayNpcs()

	def displayExits(self):
		print("Exits: ", end="")
		for exit in self.curRoom.exits[:-1]:
			print(exit['localName'] + ", ", end="")
		print(self.curRoom.exits[-1]['localName'] + ".")

	def displayItems(self):
		if not self.curRoom.items:
			return

		print("Items: ", end="")
		self.displayList(self.curRoom.items)

	def displayNpcs(self):
		if not self.curRoom.npcs:
			return

		print("You see: ", end="")
		self.displayList(self.curRoom.npcs)

	def displayList(self, myList):
		for element in myList[:-1]:
			print(element.name + ", ", end="")
		print(myList[-1].name + ".")

	def look(self, targetName, player):
		if self.lookNpc(targetName) == True:
			return
		if self.lookGround(targetName) == True:
			return
		if player.lookInventory(targetName) == True:
			return

		print("That is not here.")

	def lookNpc(self, npcName):
		npc = self.getNpc(npcName)
		if npc != None:
			npc.printDescription()
			return True
		return False

	def lookGround(self, itemName):
		item = self.getItem(itemName)
		if item != None:
			item.printDescription()
			return True
		return False

	def getItem(self, itemName):
		for item in self.curRoom.items:
			if string.find(item.name, itemName) == 0:
				return item
		return None

	def removeItem(self, item):
		self.curRoom.items.remove(item)

	def getNpc(self, npcName):
		for npc in self.curRoom.npcs:
			if string.find(npc.name, npcName) == 0:
				return npc
		return None

	def createRooms(self):
		north = self.Room()
		south = self.Room()
		east = self.Room()
		west = self.Room()
		center = self.Room()

		north.name = "North"
		north.desc = "The north room."
		north.exits.append({"room": center, "localName": "South"})

		south.name = "South"
		south.desc = "The south room."
		south.exits.append({"room": center, "localName": "North"})

		east.name = "East"
		east.desc = "The east room."
		east.exits.append({"room": center, "localName": "West"})

		west.name = "West"
		west.desc = "The west room."
		west.exits.append({"room": center, "localName": "East"})

		center.name = "Center"
		center.desc = "The center room."
		center.exits.append({"room": north, "localName": "North"})
		center.exits.append({"room": south, "localName": "South"})
		center.exits.append({"room": east, "localName": "East"})
		center.exits.append({"room": west, "localName": "West"})

		self.curRoom = center
