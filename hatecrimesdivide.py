# Replace year with the next year

import csv
import tempfile
import shutil

#inputs appropriate file from same folder
input_file = '2000_state_profiles_percent.csv'

#opens input_file and temporary file, where it will write results
with open(input_file, 'rb') as f, \
	tempfile.NamedTemporaryFile(delete=False) as out_f:

#In order to be able to not have to read everything in memory, we have to write every processed row to disk immediately.
#For that, we need a temporary file because we can't read and write a single file at the same time.
	reader = csv.reader(f)
	writer = csv.writer(out_f)

#Header row
	writer.writerow(next(reader))

#Try/Except block prevents the code from stopping at every string, since there are strings in the csvs.
	for row in reader:
		try:
			val1 = float(row[1])
			val2 = float(row[0])
			writer.writerows([row + [val1 / val2]])
		except ValueError:
			print('Error.')

#Overwrites original file with new content.
shutil.move(out_f.name, input_file)