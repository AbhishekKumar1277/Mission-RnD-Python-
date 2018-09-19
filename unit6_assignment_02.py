__author__ = 'Kalyan'

notes='''
 This is a basic problem involving some file reading and writing. You can put what you have learnt in earlier units
 to use here - functions or nested functions, lists, sorting, generators(optional), comprehensions (optional) etc.

1. Review the relevant lessons if you are blocked.
2. Do not modify the given input files :), modify your code to handle them.
3. Write helper routines where as needed.
4. You can write your own test routines like test_sort_words2(), but comment them out before submitting.
5. Review the files lesson and write elegant code. Python api/features makes it possible to write concise and efficient code.
'''

import inspect
import os
import unit6utils
def open_input_file(file, mode="rt"):
	mod_dir = get_module_dir()
	test_file = os.path.join(mod_dir, file)
	return open(test_file, mode)
def get_module_dir():
	mod_file = inspect.getfile(inspect.currentframe())
	mod_dir = os.path.dirname(mod_file)
	return mod_dir
def open_temp_file(file, mode):
	data_dir = os.getenv("DATA_DIR", default=get_temp_dir())
	out_file = os.path.join(data_dir, file)
	return open(out_file, mode)
def get_temp_dir():
	module_dir = get_module_dir()
	temp_dir = os.path.join(module_dir, "tempfiles")
	if not os.path.exists(temp_dir):
		os.mkdir(temp_dir)
	return temp_dir

def sort_words(source, destination):
	g = open_input_file("unit6_testinput_02.txt")
	lines = g.readlines()
	val=[]
	for i in lines:
		if '#' in i:
			continue
		elif len(i.strip()) == 0 :
			continue
		else:
			s=i.lower()
			val.append(s)
	a=sorted(val)   
	# with open("unit6_output_02.txt", "w+") as k:
	f = open_temp_file("unit6_output_02.txt", "w+") 
	for item in a:
		f.write("%s" % item)
	f.close()
			
def test_sort_words():
	source = unit6utils.get_input_file("unit6_testinput_02.txt")
	expected = unit6utils.get_input_file("unit6_expectedoutput_02.txt")
	destination = unit6utils.get_temp_file("unit6_output_02.txt")
	sort_words(source, destination)
	result = [word.strip() for word in open(destination)]
	expected = [word.strip() for word in open(expected)]
	assert expected == result
