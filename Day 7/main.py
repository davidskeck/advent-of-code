# David Keck
# Advent of Code 2016
# Day 7 Parts 1 & 2


import re


class IPAddress:
	def __init__(self):
		self.supports_TLS = False
		self.supports_SSL = False
		self.hypernet_sequences = []
		self.ip_sequences = []
		self.aba_sequences = []
		self.bab_sequences = []


def add_ABAs(ip_in):
	for ip in ip_in.ip_sequences:
		for i in range(len(ip) - 2):
			three_character_slice = ip[i:3+i]
			if str(three_character_slice) == str(three_character_slice)[::-1]:
				if three_character_slice[0] != three_character_slice[1]:
					ip_in.aba_sequences.append(three_character_slice)

				
def add_BABs(ip_in):
	for hypernet in ip_in.hypernet_sequences:
		for i in range(len(hypernet) - 2):
			three_character_slice = hypernet[i:3+i]
			if str(three_character_slice) == str(three_character_slice)[::-1]:
				if three_character_slice[0] != three_character_slice[1]:
					ip_in.bab_sequences.append(three_character_slice)


def convert_BAB(bab_in):
	first_char = bab_in[0]
	second_char = bab_in[1]
	
	return second_char + first_char + second_char


def determine_SSL_support(ip_in):
	add_ABAs(ip_in)
	add_BABs(ip_in)
	if len(ip_in.aba_sequences) > 0:
		for aba in ip_in.aba_sequences:
			for bab in ip_in.bab_sequences:
				if aba == convert_BAB(bab):
					ip_in.supports_SSL = True


def determine_ABBA_status(sequence_in):
	for i in range(len(sequence_in) - 3):
		four_character_slice = sequence_in[i:4+i]
		if four_character_slice == four_character_slice[::-1]:
			if four_character_slice[0] != four_character_slice[1]:
				return True
	return False


def determine_TLS_support(ip_in):	
	for ip in ip_in.ip_sequences:
		if determine_ABBA_status(ip):
			ip_in.supports_TLS = True
	for hypernet in ip_in.hypernet_sequences:
		if determine_ABBA_status(hypernet):
			ip_in.supports_TLS = False


def main():
	puzzle_input = open("puzzle_input.txt")
	
	ip_addresses = []
	for index, address in enumerate(puzzle_input):
		temp_ip_address = IPAddress()
		split_address_components = re.split(r"[\[\]]", address)
		
		for i, component in enumerate(split_address_components):
			if i % 2 == 0:
				temp_ip_address.ip_sequences.append(component.strip())
			else:
				temp_ip_address.hypernet_sequences.append(component.strip())
				
		determine_TLS_support(temp_ip_address)
		determine_SSL_support(temp_ip_address)
		ip_addresses.append(temp_ip_address)
		
	num_TLS_supporting_addresses = 0
	num_SSL_supporting_addresses = 0
	
	for address in ip_addresses:
		if address.supports_TLS:
			num_TLS_supporting_addresses += 1
		if address.supports_SSL:
			num_SSL_supporting_addresses += 1
	
	print("The number of IP addresses with TLS support is " + str(num_TLS_supporting_addresses) + ".")
	print("The number of IP addresses with SSL support is " + str(num_SSL_supporting_addresses) + ".")

main()


