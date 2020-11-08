def open_write_close(file_name, string_write):
	file_object = open(file_name, "w")
	file_object.write(string_write + "\n")
	file_object.close()

open_write_close("test_fRile.txt", "Or maybe I should just stick to Sublime?")