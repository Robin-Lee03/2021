import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host= "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()
word = input('Enter a word: ')

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' ") %word  # execute = 執行搜尋結果
if query in con:
    if len(get_close_matches(query,con)) > 0:
        yn = input('Did you mean %s instead ? Enter Y if yes or N if no: ' % get_close_matches(query,con)[0])
        if yn == 'Y':
            return con[get_close_matches(word,query)[0]]

        elif yn == 'N':
            return "The word doesn't exist. please double check it."

results = cursor.fetchall()

for result in results:
    print(result[1])
else:
    print("no word found!")