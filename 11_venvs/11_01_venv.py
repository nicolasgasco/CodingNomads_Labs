'''
In your CodingNomads folder create a new folder. Inside of that folder:

1. Create a new virtual environment
2. Activate the virtual environment
3. Install at least 3 packages in the virtual environment.
4. Freeze the installed packages to a requirements.txt file.
5. Deactivate the virtual environment.
6. Delete the virtual environment.
7. Create a new virtual environment and install the packages from the requirements.txt file.

'''

# dir is venv_test

# 1
# python3 -m venv my_first_venv

# 2
# source bin/activate

# 3
# pip install django
# pip install flask
# pip install numpy
# pip install psutil


#4.
pip freeze --local > requirements.txt
cat requirements.txt

# 5.
# deactivate

# 6.
# rm -rf my_first_venv/

# 7.
# source env/bin/activate
# pip install -r requirements.txt

