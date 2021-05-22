#################################################################
# LOTR ROTK GBA checksum calculator
# Fixes checksums in a .sav file after values have been modified.
# Please keep a backup before using this program.
#################################################################

import argparse

def calc_checksum(data):
	max_int = 65536

	START = 0
	CHECKSUM = 1
	END = 2
	# These variables give the Start, Checksum, and End location of each data block
	block1 = (0, 28, 32)
	block2 = (32, 84, 88)
	block3 = (88, 140, 144)
	block4 = (144, 196, 200)
	block5 = (200, 252, 256)

	# Set checksum values to 0
	data[block1[CHECKSUM]] = 0
	data[block2[CHECKSUM]] = 0
	data[block3[CHECKSUM]] = 0
	data[block4[CHECKSUM]] = 0
	data[block5[CHECKSUM]] = 0

	# Sum each value from the block, mod by max int, then subtract from max int to get the new checksum value
	data[block1[CHECKSUM]] = max_int - (sum(data[block1[START]:block1[END]])%max_int)
	data[block2[CHECKSUM]] = max_int - (sum(data[block2[START]:block2[END]])%max_int)
	data[block3[CHECKSUM]] = max_int - (sum(data[block3[START]:block3[END]])%max_int)
	data[block4[CHECKSUM]] = max_int - (sum(data[block4[START]:block4[END]])%max_int)
	data[block5[CHECKSUM]] = max_int - (sum(data[block5[START]:block5[END]])%max_int)
	

def main():
	parser = argparse.ArgumentParser(description="Calculates the checksums for a ROTK GBA save file. Must use either --inline or --output")
	parser.add_argument("sav", help=".sav file to calculate checksums on")
	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument("--inline", dest="inline", action='store_true', help="Select inline to overwrite the save file. DANGEROUS!")
	group.add_argument("--output", dest="output", help="Specify an ouput file to save the result to")
	args = parser.parse_args()

	data = None

	with open(args.sav, 'rb') as file:
		# Save file stored in hex format
		hexdata = file.read().hex()
		# Split the hex data into 4 character segments and convert each one to an integer
		data = [int(hexdata[i:i+4], 16) for i in range(0, len(hexdata), 4)]
	
	calc_checksum(data)

	filename = args.sav if args.inline else args.output
	with open(filename, 'wb') as file:
		for x in data:
			# 4 hex characters = 2 bytes.  Write to output file as bytes
			file.write(x.to_bytes(2, byteorder='big'))

if __name__ == "__main__":
	main()
