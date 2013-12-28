
import os

for item in os.walk("."):
	for filename in item[2]:
		if filename[-4:] == '.pyc':
			os.remove(os.path.join(item[0],filename))
