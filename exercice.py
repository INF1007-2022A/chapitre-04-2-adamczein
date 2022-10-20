#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_first_part_of_name(name):

	first_name= name.split("-")[0]

	capitalized = first_name[0].upper() + first_name[1:].lower()

	return "Bonjour," + capitalized


def get_random_sentence(animals, adjectives, fruits):
	basic_sentence ="Aujourd’hui, j’ai vu un %s s’emparer d’un panier %s plein de %s."

	words=[]
	for word_set in (animals, adjectives, fruits):
		words += [word_set[random.randrange(0, len(word_set))]]

	return basic_sentence % tuple(words)

def encrypt(text, shift):
	return ""

def decrypt(encrypted_text, shift):
	return ""


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
