import sqlite3
import requests
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def main():
    try:
        connection = sqlite3.connect('myDB.db')
    except:
        return "Failure: could not connect to database."
    cursor = connection.cursor()

    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS content (item TEXT, PRIMARY KEY(item))''')
    except:
        connection.close()
        return "Failure: could not create table format in database."
    connection.commit()
    connection.close()
    return "Database myDB should now exist."

# http://127.0.0.1:5000/create?item=insert here
@app.route('/create')
def create():
    item = request.args.get('item')
    if item == None:
        return "Failure: no item found to add to URL."
    url = 'http://127.0.0.1:5000/DBcreate'
    data = {"item": item}
    try:
        r = requests.post(url, verify=False, json=data)
    except:
        return "Failure: unable to execute create process on database."
    return r.text

@app.route('/DBcreate', methods=['GET', 'POST'])
def DBcreate():
    if request.json == None:
        return "Failure: value not obtainable to use with SQL."
    content = request.json
    try:
        connection = sqlite3.connect('myDB.db')
    except sqlite3.DatabaseError as error:
        return "Failure: file used for connection is not a database file."
    except:
        return "Failure: could not connect to database."
    cursor = connection.cursor()
    sql = "INSERT INTO content VALUES (?)"
    try:
        text = content["item"]
    except:
        return "Failure: unable to obtain value from post argument as JSON data."
    try:
        cursor.execute(sql, (text,))
    except sqlite3.IntegrityError as error:
        connection.close()
        return "Failure: could not add \"" + text + "\" to database as this item already exists."
    except sqlite3.OperationalError as error:
        connection.close()
        return "Failure: could not add \"" + text + "\" to database as database does not match the correct pattern for operations."
    except:
        connection.close()
        return "Failure: could not add \"" + text + "\" to database."
    if cursor.rowcount < 1 or cursor.rowcount == None:
        outcome = "Failure: \"" + text + "\" to database."
    else:
        outcome = "Success: item \"" + text + "\" successfully added to database."
    connection.commit()
    connection.close()
    return outcome

# http://127.0.0.1:5000/read?filter=%Here
@app.route('/read')
def read():
    filter = request.args.get('filter')
    if filter == None:
        data = None
    else:
        data = {"filter": filter}
    url = 'http://127.0.0.1:5000/DBread'
    try:
        r = requests.post(url, verify=False, json=data)
    except:
        return "Failure: unable to execute read process on database."
    return r.text

@app.route('/DBread', methods=['GET', 'POST'])
def DBread():
    try:
        connection = sqlite3.connect('myDB.db')
    except sqlite3.DatabaseError as error:
        return "Failure: file used for connection is not a database file."
    except:
        return "Failure: could not connect to database."
    cursor = connection.cursor()
    content = request.json
    if content == None:
        try:
            cursor.execute("SELECT * FROM content")
        except sqlite3.OperationalError as error:
            connection.close()
            return "Failure: could not obtain results from database as database does not match the correct pattern for operations."
        except:
            connection.close()
            return "Failure: could not obtain results from database."
    else:
        sql = "SELECT * FROM content WHERE item LIKE ?;"
        try:
            text = content["filter"]
        except:
            return "Failure: unable to obtain value from post argument as JSON data."
        try:
            cursor.execute(sql, (text,))
        except sqlite3.ProgrammingError as error:
            connection.close()
            return "Failure: filter \"" + text + "\" is not appropriate for searching data."
        except:
            connection.close()
            return "Failure: could not obtain results from database."
    info = cursor.fetchall()
    if(len(info) !=0):
        print(info)
        return {"Content":info}
    else:
        return {"Content":[]}

# http://127.0.0.1:5000/update?old=insert here&new=insert there
@app.route('/update')
def update():
    old = request.args.get('old')
    new = request.args.get('new')
    if old == None or new == None:
        return "Failure: arguments incomplete. Must find old item and new item."
    url = 'http://127.0.0.1:5000/DBupdate'
    data = {"old": old, "new": new}
    try:
        r = requests.post(url, verify=False, json=data)
    except:
        return "Failure: unable to execute update process on database."
    return r.text

@app.route('/DBupdate', methods=['GET', 'POST'])
def DBupdate():
    if request.json == None:
        return "Failure: values not obtainable to use with SQL."
    content = request.json
    try:
        connection = sqlite3.connect('myDB.db')
    except sqlite3.DatabaseError as error:
        return "Failure: file used for connection is not a database file."
    except:
        return "Failure: could not connect to database."
    cursor = connection.cursor()
    sql = "UPDATE content SET item = ? WHERE item = ?"
    try:
        text1 = content["new"]
        text2 = content["old"]
    except:
        return "Failure: unable to obtain values from post argument as JSON data."
    try:
        cursor.execute(sql, (text1, text2))
    except sqlite3.OperationalError as error:
        connection.close()
        return "Failed to update \"" + text2 + "\" to \"" + text1 + "\" in database as database does not match the correct pattern for operations."
    except:
        connection.close()
        return "Failed to update \"" + text2 + "\" to \"" + text1 + "\" in database."
    if cursor.rowcount < 1:
        outcome = "Failure: Failed to update \"" + text2 + "\" to \"" + text1 + "\" in database as \"" + text1 + "\" does not exist in database."
    else:
        outcome = "Success: item \"" + text2 + "\" updated to \"" + text1 + "\" in database."
    connection.commit()
    connection.close()
    return outcome

# http://127.0.0.1:5000/delete?item=insert there
@app.route('/delete')
def delete():
    item = request.args.get('item')
    if item == None:
        return "Failure: no item found to delete from URL."
    url = 'http://127.0.0.1:5000/DBdelete'
    data = {"item": item}
    try:
        r = requests.post(url, verify=False, json=data)
    except:
        return "Failure: unable to execute update process on database."
    return r.text
    if r.json() == {"ID": 1}:
        return "Item \"" + item + "\" successfully deleted from database."
    else:
        return "Failure: could not delete \"" + item + "\" from database as item does not exist."

@app.route('/DBdelete', methods=['GET', 'POST'])
def DBdelete():
    if request.json == None:
        return "Failure: value not obtainable to use with SQL."
    content = request.json
    try:
        connection = sqlite3.connect('myDB.db')
    except sqlite3.DatabaseError as error:
        return "Failure: file used for connection is not a database file."
    except:
        return "Failure: could not connect to database."
    cursor = connection.cursor()
    sql = "DELETE FROM content WHERE item = ?"
    try:
        text = content["item"]
    except:
        return "Failure: unable to obtain value from post argument as JSON data."
    try:
        cursor.execute(sql, (text,))
    except sqlite3.OperationalError as error:
        connection.close()
        return "Failure: could not delete \"" + text + "\" from database as database does not match the correct pattern for operations."
    except:
        connection.close()
        return "Failure: could not delete \"" + text + "\" from database."
    if cursor.rowcount < 1:
        outcome = "Failure: could not delete \"" + text + "\" from database as item does not exist."
    else:
        outcome = "Success: Item \"" + text + "\" successfully deleted from database."
    connection.commit()
    connection.close()
    return outcome

# http://127.0.0.1:5000/reset
@app.route('/reset')
def reset():
    try:
        connection = sqlite3.connect('myDB.db')
    except sqlite3.DatabaseError as error:
        return "Failure: file used for connection is not a database file."
    except:
        return "Failure: could not connect to database."
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM content")
    except sqlite3.OperationalError as error:
        connection.close()
        return "Failure: could not execute reset command on database as database does not match the correct pattern for operations."
    except:
        connection.close()
        return "Failure: could not execute reset command on database."
    if cursor.rowcount < 1:
        outcome = "Failure: database not reset as table is already empty."
    else:
        outcome = "Success: database has been reset."
    connection.commit()
    connection.close()
    return outcome

if __name__ == '__main__':
    app.run(debug = True)
    ##app.run(host='0.0.0.0', port=80)
