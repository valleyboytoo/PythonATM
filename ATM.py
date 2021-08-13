import tkinter as tk
import tkinter.messagebox
import os
import matplotlib.pyplot as plt

records = {}
fr = open('C:/Users/Hansang/Desktop/myPython/users.txt', 'r')
for line in fr:
    for i in range(len(line)):
        if line[i] == ':':
            key = line[0:i]
            break
    records[key] = eval(line[i + 1:])


def behind_the_scene_create_account():
    global records
    x = enter_name_entry.get()
    y = password_entry.get()
    if len(y) == 4:
        f = open('C:/Users/Hansang/Desktop/myPython/users.txt', 'a+')
        z = x[0::2] + x[:0:-1]
        if z in records.keys():
            answer_1 = tkinter.messagebox.askretrycancel("ERROR", "Same user name exists")
            if answer_1 == True:
                create_account()
            else:
                admin()
        else:
            fp = open(z + '.txt', 'a+')
            records[z] = [x[0::2] + x[:0:-1], x, 0, y]
            f.write("%s:%s" % (z, records[z]))
            fp.write("%s:%s" % (z, records[z]))
            f.write("\n")
            fp.write('\n')
            f.close()
            fp.close()
            answer = tkinter.messagebox.askyesno("INFO", "Account created successfully")
            if answer == True or answer == False:
                main_window()
            else:
                admin()
    else:
        tkinter.messagebox.showerror("ERROR", "Enter 4 digit password")


def behind_the_scene_delete_account():
    global records
    x = enter_name_entry.get()
    f = open('C:/Users/Hansang/Desktop/myPython/users.txt', 'a+')
    z = x[0::2] + x[:0:-1]
    if z in records.keys():
        del records[z]
        f.truncate(0)
        for k, v in records.items():
            f.write(str(k).replace("'", "") + ':'+ str(v) + '\n\n')
        f.close()
        os.remove(z + '.txt')
        answer = tkinter.messagebox.askyesno("INFO", x.upper() + " account deleted successfully")
        if answer == True or answer == False:
            delete_account()
        else:
            admin()

    else:
        answer_2 = tkinter.messagebox.askretrycancel("ERROR", "The user doesn't exist")
        if answer_2 == True or answer_2 == False:
            delete_account()
        else:
            admin()


def logout():
    login()


def back():
    main_window()


def withdraw():
    def amount_withdrawn():
        try:
            if int(withdraw_entry.get())>=0:
                if int(withdraw_entry.get())%10==0:
                    fr = open(z + '.txt', 'r')
                    all_lines = fr.readlines()
                    last_line = all_lines[-1]
                    temp_data = {}
                    temp_data[z] = eval(last_line[len(z) + 1:])
                    fr.close()
                    if temp_data[z][2] >= int(withdraw_entry.get()):
                        temp_data[z][2] = temp_data[z][2] - int(withdraw_entry.get())
                        file_update = open(z + '.txt', 'a+')
                        file_update.write("%s:%s" % (z, temp_data[z]))
                        file_update.write('\n')
                        file_update.close()
                        user()
                    else:
                        answer_1 = tkinter.messagebox.askretrycancel("ERROR", "YOU DO NO HAVE SUFFICIENT BALANCE")
                        if answer_1 == True:
                            withdraw()
                        else:
                            user()
                else:
                    answer_2 = tkinter.messagebox.askretrycancel("ERROR", "ENTER A MULTIPLE OF  $10")
                    if answer_2 == True:
                        withdraw()
                    else:
                        user()
            else:
                tkinter.messagebox.showerror("ERROR", "ENTER A VALID AMOUNT")
        except:
            tkinter.messagebox.showerror("ERROR", "ENTER A VALID AMOUNT")

    withdraw_frame = tk.Frame(display_frame, width=900, height=400)
    withdraw_frame.place(x=0, y=0)
    withdraw_frame.tkraise()
    withdraw_label = tk.Label(withdraw_frame, text="ENTER THE AMOUNT YOU WANT TO WITHDRAW")
    withdraw_label.place(x=350, y=100)
    withdraw_entry = tk.Entry(withdraw_frame)
    withdraw_entry.place(x=400, y=200)
    withdraw_button = tk.Button(withdraw_frame, text='withdraw', command=amount_withdrawn)
    withdraw_button.place(x=400, y=300)


def deposit():
    def amount_deposited():
        try:
            if int(deposit_entry.get())>=0:
                fr = open(z + '.txt', 'r')
                all_lines = fr.readlines()
                last_line = all_lines[-1]
                temp_data = {}
                temp_data[z] = eval(last_line[len(z) + 1:])
                fr.close()
                temp_data[z][2] = temp_data[z][2] + int(deposit_entry.get())
                file_update = open(z + '.txt', 'a+')
                file_update.write("%s:%s" % (z, temp_data[z]))
                file_update.write('\n')
                file_update.close()
                user()
            else:
                tkinter.messagebox.showerror("ERROR", "ENTER A VALID AMOUNT")
        except:
            tkinter.messagebox.showerror("ERROR","ENTER A VALID AMOUNT")

    deposit_frame = tk.Frame(display_frame, width=900, height=400)
    deposit_frame.place(x=0, y=0)
    deposit_frame.tkraise()
    deposit_label = tk.Label(deposit_frame, text="ENTER THE AMOUNT YOU WANT TO DEPOSIT")
    deposit_label.place(x=350, y=100)
    deposit_entry = tk.Entry(deposit_frame)
    deposit_entry.place(x=400, y=200)
    deposit_button = tk.Button(deposit_frame, text='Deposit', command=amount_deposited)
    deposit_button.place(x=400, y=300)


def view_account():
    view_account_frame = tk.Frame(display_frame, width=900, height=400)
    view_account_frame.place(x=0, y=0)
    view_account_frame.tkraise()
    fr = open(z + '.txt', 'r')
    all_lines = fr.readlines()
    last_line = all_lines[-1]
    temp_data = {}
    temp_data[z] = eval(last_line[len(z) + 1:])
    fr.close()
    account_name = tk.Label(view_account_frame, text='ACCOUNT NAME: ' + records[z][1])
    account_name.place(x=400, y=100)
    account_code = tk.Label(view_account_frame, text='CODE NAME: ' + records[z][0])
    account_code.place(x=400, y=200)
    account_amount = tk.Label(view_account_frame, text='CURRENT AMOUNT: ' + str(temp_data[z][2]))
    account_amount.place(x=400, y=300)


def plot_account():
    plt.title('Balance by account(CDI BANK)')
    plt.xlabel('Account')
    plt.ylabel('Balance')
    plot_dic = records.copy()
    for key in plot_dic:
        fr = open(key + '.txt', 'r')
        all_lines = fr.readlines()
        last_line = all_lines[-1]
        temp_data = {}
        temp_data[key] = eval(last_line[len(key) + 1:])
        fr.close()
        plot_dic[key] = int(temp_data[key][2])
    keys = plot_dic.keys()
    values = plot_dic.values()
    plt.bar(keys, values, color=('r', 'g', 'b', 'y', 'b', 'c'))

    plt.show()


display_frame = None


def user():
    dasboard_frame = tk.Frame(login_frame, width=900, height=100, bg='black')
    dasboard_frame.place(x=0, y=0)
    dasboard_frame.tkraise()
    dasboard_button_1 = tk.Button(dasboard_frame, text='BALANCE', command=view_account)
    dasboard_button_1.place(x=100, y=50)
    dasboard_button_2 = tk.Button(dasboard_frame, text='DEPOSIT', command=deposit)
    dasboard_button_2.place(x=300, y=50)
    dasboard_button_3 = tk.Button(dasboard_frame, text='WITHDRAW', command=withdraw)
    dasboard_button_3.place(x=500, y=50)
    dasboard_button_4 = tk.Button(dasboard_frame, text='LOGOUT', command=logout)
    dasboard_button_4.place(x=700, y=50)
    global display_frame
    display_frame = tk.Frame(login_frame, width=900, height=400, bg='white')
    display_frame.place(x=0, y=100)
    display_frame.tkraise()
    user_logo=tk.Label(display_frame,image=img1,bg='white')
    user_logo.place(x=150,y=0)

def admin():
    dasboard_frame = tk.Frame(login_frame, width=900, height=100, bg='black')
    dasboard_frame.place(x=0, y=0)
    dasboard_frame.tkraise()
    dasboard_button_1 = tk.Button(login_create_frame, text='CREATE ACCOUNT', command=create_account)
    dasboard_button_1.place(x=100, y=50)
    dasboard_button_2 = tk.Button(dasboard_frame, text='DELETE ACCOUNT', command=delete_account)
    dasboard_button_2.place(x=300, y=50)
    dasboard_button_3 = tk.Button(dasboard_frame, text='PLOT ACCOUNT', command=plot_account)
    dasboard_button_3.place(x=500, y=50)
    dasboard_button_4 = tk.Button(dasboard_frame, text='LOGOUT', command=logout)
    dasboard_button_4.place(x=700, y=50)
    global display_frame
    display_frame = tk.Frame(login_frame, width=900, height=400, bg='white')
    display_frame.place(x=0, y=100)
    display_frame.tkraise()
    user_logo=tk.Label(display_frame,image=img1,bg='white')
    user_logo.place(x=150,y=0)

x = ''
z = ''

count = 3
def behind_the_scene_login():
    global count
    global x
    global z
    x = enter_username_entry.get()
    z = x[0::2] + x[:0:-1]
    if z in records.keys():
        if login_password_entry.get() == records[z][3]:
            if x == 'SysAdmin':
                tkinter.messagebox.showinfo("Successful", "ADMIN login Successful")
                admin()
            else:
                tkinter.messagebox.showinfo("Successful", "USER login Successful")
                user()
        else:
            a = tkinter.messagebox.askretrycancel("ERROR", "Invalid Username or Password" + "\n   Attempts left: " + str(count - 1))
            if a == True:
                count -= 1
                login()
            else:
                main_window()
    else:
        b = tkinter.messagebox.askretrycancel("ERROR", "Invalid Username or Password" + "\n   Attempts left: " + str(count - 1))
        if b == True:
            count -= 1
            login()
        else:
            main_window()
    if count == 0:
        tkinter.messagebox.showerror("ERROR", "You have tried 3 times. Check Username and Password." + "\nLogin Failed")
        count = 3
        main_window()



enter_username_entry = None
login_password_entry = None
login_frame = None


def login():
    global login_frame
    login_frame = tk.Frame(login_create_frame, width=900, height=500)
    login_frame.place(x=0, y=0)
    login_frame.tkraise()
    enter_username_label = tk.Label(login_frame, text="Enter User Name: ")
    enter_username_label.place(x=300, y=100)
    global enter_username_entry
    enter_username_entry = tk.Entry(login_frame)
    enter_username_entry.place(x=400, y=100)
    login_password_label = tk.Label(login_frame, text="Enter Password: ")
    login_password_label.place(x=300, y=200)
    global login_password_entry
    login_password_entry = tk.Entry(login_frame, show='●')
    login_password_entry.place(x=400, y=200)
    login_button = tk.Button(login_frame, text='LOGIN', command=behind_the_scene_login)
    login_button.place(x=300, y=300)
    back_button = tk.Button(login_frame, text='BACK', command=back)
    back_button.place(x=500, y=300)


enter_name_entry = None
password_entry = None


def create_account():
    create_account_frame = tk.Frame(login_create_frame, width=900, height=500)
    create_account_frame.place(x=0, y=0)
    create_account_frame.tkraise()
    enter_name_label = tk.Label(create_account_frame, text="Enter Name: ")
    enter_name_label.place(x=300, y=100)
    global enter_name_entry
    enter_name_entry = tk.Entry(create_account_frame)
    enter_name_entry.place(x=400, y=100)
    password_label = tk.Label(create_account_frame, text="Enter Password: ")
    password_label.place(x=300, y=200)
    global password_entry
    password_entry = tk.Entry(create_account_frame)
    password_entry.place(x=400, y=200)
    create_account_button = tk.Button(create_account_frame, text='CREATE', command=behind_the_scene_create_account)
    create_account_button.place(x=300, y=300)
    back_button = tk.Button(create_account_frame, text='BACK', command=back)
    back_button.place(x=500, y=300)


def delete_account():
    create_account_frame = tk.Frame(login_create_frame, width=900, height=500)
    create_account_frame.place(x=0, y=0)
    create_account_frame.tkraise()
    enter_name_label = tk.Label(create_account_frame, text="Enter Name: ")
    enter_name_label.place(x=300, y=100)
    global enter_name_entry
    enter_name_entry = tk.Entry(create_account_frame)
    enter_name_entry.place(x=400, y=100)
    delete_account_button = tk.Button(create_account_frame, text='DELETE', command=behind_the_scene_delete_account)
    delete_account_button.place(x=300, y=300)
    back_button = tk.Button(create_account_frame, text='BACK', command=back)
    back_button.place(x=500, y=300)


login_create_frame = None


def main_window():
    global login_create_frame
    login_create_frame = tk.Frame(root, width=900, height=500)
    login_create_frame.place(x=0, y=0)
    main_logo = tk.Label(login_create_frame,image=img2)
    main_logo.place(x=150,y=10)
    login_button = tk.Button(login_create_frame, text='LOGIN', command=login)
    login_button.place(x=400, y=400)


root = tk.Tk()
root.geometry("900x500")
root.title("CDI ATM")
img1 = tk.PhotoImage(file='C:/Users/Hansang/Desktop/myPython/menu_logo.png')
img2 = tk.PhotoImage(file='C:/Users/Hansang/Desktop/myPython/main_logo.png')
main_window()
root.mainloop()