import sqlite3

desriptor = sqlite3.connect('DATA.db')
runner = desriptor.cursor()

runner.execute("""CREATE TABLE profiles_data (
	id NUMBER,
	name VARCHAR(30),
	sername VARCHAR(50),
	login VARCHAR(20) PRIMARY KEY,
	password VARCHAR(20),
	experience NUMBER,
	mind NUMBER,
	diligence NUMBER,
	discipline NUMBER
	)""")

desriptor.commit()
runner.close()
desriptor.close()
