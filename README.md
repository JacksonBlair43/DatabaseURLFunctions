DBURLFunctions.py

INTRODUCTION
This file uses Python and flask to create an efficient way 
to maintain a database containing one row full of messages.

SETUP
You will need to have Python, Flask and sqlite working.
Execute the python file and you will be directed to a URL
link in the python terminal. Follow the link and open the
new browser page. A database file in the local repository
of this file should be created.
You can use the URL of the browser to execute the defined
functions on your new database.

FUNCTIONS:
  CREATE - Add a new item to your database.
    EXAMPLE: "http://127.0.0.1:5000/create?item=insert here"
  READ - Look at the current contents of the database.
  Filter can be applied to show certain items only, but
  is not necessary.
    EXAMPLE: "http://127.0.0.1:5000/read?filter=%Here"
  UPDATE - Identify old item already present in database
  to replace with new item.
    EXAMPLE: "http://127.0.0.1:5000/update?old=insert here&new=insert there"
  DELETE - Remove an existing item from the database.
    EXAMPLE: "http://127.0.0.1:5000/delete?item=insert there"
  RESET - Remove all items from database.
    EXAMPLE: "http://127.0.0.1:5000/reset"
    
