"""
Create a program that prints every email, linked to its domain name.
"""

emails = {"ucsd.edu" : ["annie","joseph","savitha"],
"gmail.com" : ["ben10","annie","dio"],
"aol.com" : ["joseph", "hotmail", "coda"]}

for key in emails:
    for val in emails[key]:
        print(val + '@' + key)

Output:
annie@ucsd.edu
joseph@ucsd.edu
savitha@ucsd.edu
ben10@gmail.com
annie@gmail.com
dio@gmail.com
joseph@aol.com
hotmail@aol.com
coda@aol.com
