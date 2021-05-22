# rotk-gba
Programs/Scripts useful for playing LOTR ROTK on GBA

## checksum.py

This script is used to recalculate checksum values if you are editing a save file.

You will need to install Python3, then run it in the command line using `python checksum.py`
or `python3 checksum.py`, depending on your environment.  You can have it modify the input file directly, but I would recommend specifying an output file instead, just in case something goes wrong.

`python3 checksum.py --output new_file.sav old_file.sav`

More information can be found using `python3 checksum.py -h`