import sys
import random
import string
from pathlib import Path

if len(sys.argv)<4:
	sys.exit("File requires <# of files to generate> <# chars for files' name> <# of chars to populate in each file> ");

def generateFiles():
	alpha = string.ascii_letters+string.digits;
	data = alpha+string.whitespace;

	for num in range(int(sys.argv[1])):
		'''Random letter or digit is being created as many times as range has 
			so I pick random character will be created in list ex[a,c,e,r,g]
			then i join the characters with the string '' to make it one word.'''
		#file name + .txt
		filename = ''.join(random.choice(alpha) for num in range( int(sys.argv[2]) ) )+".txt";
		#path of file to accomedate any system
		file_path = Path("./"+filename);

		#each file created wi;l get populated with random data
		with open(filename,"w")as file:
			#populate the data
			filedata=''.join(random.choice(data)for i in range( int(sys.argv[3]) ) );
			#write the data in the file
			file.write(filedata);	
			print(filename+" created and populated!")
			#print(filedata);
generateFiles()

