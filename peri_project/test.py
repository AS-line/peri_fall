import sqlite3

descriptor = sqlite3.connect('DATA.db')
runner = descriptor.cursor()

runner.execute("SELECT * FROM profiles_data")
for row in runner.fetchall():
	print(row)

# runner.execute("DELETE FROM profiles_data WHERE *")


descriptor.commit()
runner.close()
descriptor.close()