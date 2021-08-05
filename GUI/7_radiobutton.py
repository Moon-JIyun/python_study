from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")  # "가로 x 세로 + x좌표 + y좌표"
root.resizable(True, True)

label1 = Label(root, text = "메뉴를 선택하세요 ").pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root, text ="햄버거", value=1, variable = burger_var)
btn_burger1.select()

btn_burger2 = Radiobutton(root, text ="치즈버거", value=2, variable = burger_var)
btn_burger3 = Radiobutton(root, text ="치킨버거", value=3, variable = burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

label1 = Label(root, text = "음료를 선택하세요 ").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text = "coke", value='coke', variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text = "cider", value='cider', variable=drink_var)
btn_drink3 = Radiobutton(root, text = "beer", value='beer', variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

def btncmd():
    print(burger_var.get()) # 햄버거중 선택된 라디오 항목의 값을 출력
    print(drink_var.get())



btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()