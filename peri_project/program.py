import tkinter
import sqlite3
import time
import issues

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

    if user_login == '' or user_password == '':
        txt_label = tkinter.Label(text='Заполните поля', width=34, bg='#0f0')
        txt_label.place(x=88.5, y=143 + 20)

    if check_profile in profiles:
        true_login = user_login
        root.destroy()
        menu(true_login)
    else:
        txt_label = tkinter.Label(text='Неправильный логин или пароль', width=34, bg='red')
        txt_label.place(x=88.5, y=143 + 20)

    descriptor.commit()
    runner.close()
    descriptor.close()


def menu(login):
    global root2
    root2 = tkinter.Tk()
    root2.title('Меню')
    root2.geometry('420x630')
    root2.resizable(False, False)
    root2.config(bg='#8090a0')

    txt_label = tkinter.Label(text='Успешная авторизация', width=34, bg='#0f0')
    txt_label.place(x=88, y=10)

    menu_btn = tkinter.Button(root2, text='Пройти тест', width=18, bg='red')
    menu_btn.bind('<Button-1>', lambda event: new_window(login))
    menu_btn.place(x=64, y=50)

    menu_btn2 = tkinter.Button(root2, text='Выход', width=18, bg='red')
    menu_btn2.bind('<Button-1>', lambda event: root2.destroy())
    menu_btn2.place(x=30 + 64 + 136 + 20, y=50)

    root2.mainloop()


def new_window(login):
    global root3
    root2.destroy()
    root3 = tkinter.Tk()
    root3.title('Тест')
    root3.geometry('700x1000')
    root3.resizable(False, False)
    root3.config(bg='#8090a0')
    q = issues.issues()
    
    ques1 = tkinter.Label(root3, text='1)'+q[1], bg='#8090a0')
    ques1.place(x=0, y=0)
    tr1 = tkinter.Radiobutton(root3, text='Это относится ко мне', value=True, bg='#8090a0')
    tr1.place(x=100, y=20)
    fa1 = tkinter.Radiobutton(root3, text='Это не относится ко мне', value=False, bg='#8090a0')
    fa1.place(x=250, y=20)


    ques2 = tkinter.Label(root3, text='2)'+q[2], bg='#8090a0')
    ques2.place(x=0, y=60)
    tr2 = tkinter.Radiobutton(root3, text='Это относится ко мне', value=1, bg='#8090a0')
    tr2.place(x=100, y=100)
    fa2 = tkinter.Radiobutton(root3, text='Это не относится ко мне', value=2, bg='#8090a0')
    fa2.place(x=250, y=100)


    root3.mainloop()


def registration(new_user_name, new_user_surname, new_user_login, new_user_password):
    if new_user_password == '' or new_user_login == '' or new_user_name == '' or new_user_surname == '':
        incorrect_data_text = tkinter.Label(root, text='Введите данные полностью', bg='red', width=32)
        incorrect_data_text.place(x=103, y=416 + 20)
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

            sucs_reg = tkinter.Label(root, text='Успешная регистрация', bg='#0f0', width=32)
            sucs_reg.place(x=103, y=416 + 20)

        except sqlite3.IntegrityError:
            sqlerror = tkinter.Label(root, text='Введите данные полностью', bg='red', width=32)
            sqlerror.place(x=103, y=416 + 20)


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

label_login = tkinter.Label(root, text='Логин:', bg='#8090a0')
label_login.place(x=148.5, y=20 + 20)

entry_login = tkinter.Entry(root)
entry_login.place(x=148.5, y=40 + 20)

label_password = tkinter.Label(root, text='Пароль:', bg='#8090a0')
label_password.place(x=148.5, y=60 + 20)

entry_password = tkinter.Entry(root)
entry_password.place(x=148.5, y=80 + 20)

btn_log_in = tkinter.Button(root, text='Войти', width=18, bg='red')
btn_log_in.bind('<Button-1>', lambda event: log_in(str(entry_login.get()), str(entry_password.get())))
btn_log_in.place(x=143, y=110 + 20)

############################################################################


label_new_name = tkinter.Label(root, text='Имя:', bg='#8090a0')
label_new_name.place(x=148.5, y=180 + 20)

entry_new_name = tkinter.Entry(root)
entry_new_name.place(x=148.5, y=200 + 20)

label_new_sername = tkinter.Label(root, text='Фамилия:', bg='#8090a0')
label_new_sername.place(x=148.5, y=220 + 20)

entry_new_sername = tkinter.Entry(root)
entry_new_sername.place(x=148.5, y=240 + 20)

label_new_login = tkinter.Label(root, text='Логин:', bg='#8090a0')
label_new_login.place(x=148.5, y=280 + 20)

entry_new_login = tkinter.Entry(root)
entry_new_login.place(x=148.5, y=300 + 20)

label_new_passw = tkinter.Label(root, text='Пароль:', bg='#8090a0')
label_new_passw.place(x=148.5, y=330 + 20)

entry_new_passw = tkinter.Entry(root)
entry_new_passw.place(x=148.5, y=350 + 20)

btn_reg = tkinter.Button(root, text='Зарегистрироваться', width=18, bg='red')
btn_reg.bind('<Button-1>', lambda event: registration(entry_new_name.get(), entry_new_sername.get(),
                                                      entry_new_login.get(), entry_new_passw.get()))
btn_reg.place(x=143, y=380 + 20)

root.mainloop()
