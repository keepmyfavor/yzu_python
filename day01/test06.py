import tkinter as tk
import tkinter.messagebox
import datetime as dt

def onOK():
    print("購買日期, {}.".format(buyDate.get()))
    print("離職日期, {}.".format(quitDate.get()))
    print("補助金額, {}.".format(companyPay.get()))
    tkinter.messagebox.showinfo(title = "試算結果",
                                message = buyDate.get())

windows = tk.Tk()
windows.title("筆電補助計算")
windows.geometry("300x200+250+150")
# buyDate = tk.Entry(windows,
#                  width = 20)


buyDate = dt.datetime.strptime(str(tk.Entry(windows, width = 20)), "%Y-%m-%d").date()
buyDate.pack()

quitDate = tk.Entry(windows,
                 width = 20)
quitDate.pack()
companyPay = tk.Entry(windows,
                 width = 20)
companyPay.pack()




button = tk.Button(windows, text = "OK", command = onOK)
button.pack()
windows.mainloop()
