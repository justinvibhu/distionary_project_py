import mysql.connector

from difflib import get_close_matches

con = mysql.connector.connect(

    user="root",
    password="",
    host="127.0.0.1",
    database="entries"
)
cursor = con.cursor()
word = input("enter The Word ")
word =word.lower()
query = cursor.execute("SELECT * from entries WHERE word ='%s'" % word)
results = cursor.fetchall()
if results:
    for result in results:
        print(result[1])
elif len(get_close_matches(word, cursor)) > 0:
    yn = input("Did you mean %s instead ? Enter Y for YES or N for NO " % get_close_matches(w, data.keys())[0])

else:
    print( "no word found ")

