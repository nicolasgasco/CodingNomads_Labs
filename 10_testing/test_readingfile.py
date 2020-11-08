import unittest

def open_write_close(file_name, string_write):
	file_object = open(file_name, "w")
	file_object.write(string_write + "\n")
	file_object.close()




if __name__ == '__main__':
    unittest.main()