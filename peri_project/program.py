import tkinter
import sqlite3
import time

root = tkinter.Tk()
root.title('Авторизация')
root.geometry('420x600')
root.resizable(False, False)
root.config(bg='#8090a0')


def log_in(user_login, user_password):

    descriptor = sqlite3.connect('DATA.db')
    runner = descriptor.cursor()

    runner.execute("SELECT login, password FROM profiles_data")
    profiles = runner.fetchall()
    check_profile = (user_login, user_password)

    if check_profile in profiles:
        true_login = user_login
        txt_label = tkinter.Label(text='YOU HAVE SUCCESSFULLY LOGGED', width=34, bg='#0f0')
        txt_label.place(x=88.5, y=143)
        time.sleep(2)
        root.destroy()
        new_window()
    else:
        
        txt_label = tkinter.Label(text='INCORRECT USERNAME OR PASSWORD', width=34, bg='red')
        txt_label.place(x=88.5, y=143)

    descriptor.commit()
    runner.close()
    descriptor.close()

def new_window():
    global root2
    root2 = tkinter.Tk()
    root2.title('Меню')
    root2.geometry('420x600')
    root2.resizable(False, False)
    root2.config(bg='#8090a0')





    root2.mainloop()


def registration(new_user_name, new_user_surname, new_user_login, new_user_password):
    if new_user_password == '' or new_user_login == '':
        incorrect_data_text = tkinter.Label(root, text='ENTER THE DATA COMPLETELY', bg='red', width=32)
        incorrect_data_text.place(x=103, y=416)
    else:
        try:
            descriptor = sqlite3.connect('DATA.db')
            runner = descriptor.cursor()

            query = "INSERT INTO profiles_data VALUES (?,?,?,?,?,?,?,?,?)"
            date = 101, new_user_name, new_user_surname, new_user_login, new_user_password, None, None, None, None
            runner.execute(query, date)

            descriptor.commit()
            runner.close()
            descriptor.close()

            sucs_reg = tkinter.Label(root, text='YOU HAVE SUCCESSFULLY REGISTERED', bg='green', width=32)
            sucs_reg.place(x=103, y=416)

        except sqlite3.IntegrityError:
            sqlerror = tkinter.Label(root, text='PLEASE ENTER DATA', bg='red', width=32)
            sqlerror.place(x=103, y=416)

# descriptor = sqlite3.connect('DATA.db')
# runner = descriptor.cursor()

# descriptor.commit()
# runner.close()
# descriptor.close()


def enter_data(user_experience, user_mind, user_diligence, user_discipline, true_login):
    print(true_login)
    descriptor = sqlite3.connect('DATA.db')
    runner = descriptor.cursor()

    query = 'UPDATE profiles_data SET mind=? experience=? diligence=? discipline=? WHERE login=?'
    data = (user_experience, user_mind, user_diligence, user_discipline, true_login)
    runner.execute(query, data)

    descriptor.commit()
    runner.close()
    descriptor.close()


############################################################################

label_login = tkinter.Label(root, text='Login:', bg='#8090a0')
label_login.place(x=148.5, y=20)

entry_login = tkinter.Entry(root)
entry_login.place(x=148.5, y=40)

label_password = tkinter.Label(root, text='Password:', bg='#8090a0')
label_password.place(x=148.5, y=60)

entry_password = tkinter.Entry(root)
entry_password.place(x=148.5, y=80)

btn_log_in = tkinter.Button(root, text='Log in', width=18, bg='red')
btn_log_in.bind('<Button-1>', lambda event: log_in(str(entry_login.get()), str(entry_password.get())))
btn_log_in.place(x=143, y=110)

############################################################################


label_new_name = tkinter.Label(root, text='New name:', bg='#8090a0')
label_new_name.place(x=148.5, y=180)

entry_new_name = tkinter.Entry(root)
entry_new_name.place(x=148.5, y=200)

label_new_sername = tkinter.Label(root, text='New surname:', bg='#8090a0')
label_new_sername.place(x=148.5, y=220)

entry_new_sername = tkinter.Entry(root)
entry_new_sername.place(x=148.5, y=240)

label_new_login = tkinter.Label(root, text='New login:', bg='#8090a0')
label_new_login.place(x=148.5, y=280)

entry_new_login = tkinter.Entry(root)
entry_new_login.place(x=148.5, y=300)

label_new_passw = tkinter.Label(root, text='New password:', bg='#8090a0')
label_new_passw.place(x=148.5, y=330)

entry_new_passw = tkinter.Entry(root)
entry_new_passw.place(x=148.5, y=350)

btn_reg = tkinter.Button(root, text='Register', width=18, bg='red')
btn_reg.bind('<Button-1>', lambda event: registration(entry_new_name.get(), entry_new_sername.get(),
                                                      entry_new_login.get(), entry_new_passw.get()))
btn_reg.place(x=143, y=380)

root.mainloop()

