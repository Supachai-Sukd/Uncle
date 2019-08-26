from tkinter import *
from tkinter import ttk,filedialog

from selenium import webdriver
import time
import csv

def read(): #function ต้องมีการ get ค่า string มะกี้

	filename = openfile.get()

	data = []
	with open(filename,newline='',encoding='utf-8')as file:
		fr = csv.reader(file)
		for dt in fr:
			#print(dt)
			data.append(dt)
	return data
def report(room,title,detail):
	elem_name = driver.find_element_by_id('room') #Id ต่างๆเหล่านี้หาได้จากคลิกขวาดูใน chrome
	elem_name.clear()
	elem_name.send_keys(room) #ในนี้เราก็ไม่ต้องใส่ค่าอะไรลงไปให้เราใส่ตัว Values ไปเหมือนทำ function อื่นๆ

	elem_title = driver.find_element_by_id('title')
	elem_title.clear()
	elem_title.send_keys(title)

	elem_detail = driver.find_element_by_id('detail')
	elem_detail.clear()
	elem_detail.send_keys(detail)


	time.sleep(2)

	driver.find_element_by_id('submitBtn').click()


###############################################################		
def runbot():
	global driver
	driver = webdriver.Chrome()
	driver.get('http://cons-robotics.com/bot/selenium')

	time.sleep(3)

	driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") #เป็นคำสั่ง Script ให้ Scrolldown ลง
	#driver.execute_script("window.scrollTo(0,10);") #Scrolldown ลง 10 Pixel



	alldata = read()

	for dt in alldata:
		#print(dt[0],dt[1],dt[2])

		print('Room: {} Problem: {} Detail: {}'.format(dt[0],dt[1],dt[2])) #เหมือนกับ print ในภาษา c ที่ต้องใส่ %s %d และตัวแปรข้างหลัง
		print('################################')#ข้างบนนี้นำ dt มาใส่มันเป็น loop
		report(dt[0],dt[1],dt[2])
	driver.get('http://cons-robotics.com/bot/selenium/view')
	#Step program นี้คร่าวๆเปิด ใช้ function read ที่โดนกำกับโดย alldata
	#และ Show messege ด้านล่าง
	#และใช้ฟังชั่น report เพื่อส่งข้อมูลขึ้นเว็ปโดยใช้ loop ที่เรากำหนดไว้

gui = Tk()
gui.geometry('500x500+100+100')
gui.title('Program Mia')



def bot():
	print('Hello bot')

#Insert image
bg = PhotoImage(file='botsend.png')

background = ttk.Label(gui,image=bg)
background.place(x=50,y=10)

f1 = Frame(gui)
f1.place(x=20,y=200) #เป็นการกำหนดเฟรม เฟรมมันเหมือนกรอบ

bbot = ttk.Button(f1,text='Auto Bot',command=runbot) #ttk คือ theme ของ gui
bbot.pack(ipady=30,ipadx=30) #Button เรียก f1 เพราะต้องการอยู่ใน frame

#StringVar ฟังชั่นตัวนึงของ gui ไว้เก็บข้อความที่เปลี่ยนค่าได้ตลอด
openfile = StringVar() #ตั้งเพื่อให้เป็นตัวแปรไว้รับค่าส่งค่า
openfile.set('-----please select csv file-------- ')

showfile = ttk.Label(gui,textvariable=openfile)
showfile.place(x=5,y=5)

def select():
	#คำสั่งนี้จะได้ file path เพื่อเอาไป link กับ function เปิดไฟล์
	#askopenfile คือเป็น popup ให้เราเลือก  open file
	filename = filedialog.askopenfilename(title='select file',
		filetypes=(("CSV File","*.csv"),("All files","*.*")))
	print(filename) #คือ function เปิดไฟล์
	openfile.set(filename) #สั่งให้ตัวแปรที่ตั้งไว้มีค่าเท่ากับ filename ที่เราดึงมาได้

selectfile = ttk.Button(gui,text='Selectfile',command=select) #ttk คือ theme ของ gui
selectfile.place(x=5,y=20) #Button เรียก f1 เพราะต้องการอยู่ใน frame

gui.mainloop()
