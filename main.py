import os
  
# os.makedirs() method will raise
# an OSError if the directory
# to be created already exists
# But It can be suppressed by
# setting the value of a parameter
# exist_ok as True
  
# Directory
create_directory = "Nikhil"
  
# Parent Directory path
parent_dir = os.path.dirname(os.path.realpath(__file__))
  
# Path
path = os.path.join(parent_dir, create_directory)
  
# Create the directory
# 'Nikhil'
try:
    os.makedirs(path, exist_ok = True)
    print("create_Directory '%s' created successfully" % create_directory)
except OSError as error:
    print("create_Directory '%s' can not be created" % create_directory)
  
# By setting exist_ok as True
# error caused due already
# existing directory can be suppressed
# but other OSError may be raised
# due to other error like
# invalid path name