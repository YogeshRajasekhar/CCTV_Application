from tkinter import *
import cv2
import tkinter.font as font
import datetime as dt
import numpy as np
from PIL import Image,ImageTk
import screeninfo



u1,u2,p1,p2='0','1','2','3'
text=open(r'pluggins.txt','r+')
list=text.readlines()
tuple=list[0].split()[-2::]
user__id,pass__word=tuple
pd_bol,ud_bol=False,False
date=str(dt.date.today())
screen=screeninfo.get_monitors()
w,h=screen[0].width,screen[0].height-80


root = Tk()
ip1,ip2,ip3,ip4='0','0','0','0'
pager_run=False
video_run=False
rec=False


class menubtn():
    def userst():
        usid = Tk()
        def usvd():
            global u1, u2, user__id
            u1 = str(newuid_entry.get())
            u2 = str(newuid2_entry.get())

            if u1 == u2:
                try:
                    errlabel.grid_forget()
                except:
                    pass
                user__id = u1
                crrlabel.grid(column=2,row=3)
            else:
                try:
                    crrlabel.grid_forget()
                except:
                    pass
                errlabel.grid(column=2, row=3)
            return user__id

        usid.title('Change User Id')
        usid.geometry('650x330')
        newuid_label = Label(usid, text='Enter a new User Id : ')
        newuid2_label = Label(usid, text='Enter a new User Id again : ')
        newuid_label.grid(column=1, row=1)
        newuid2_label.grid(column=1, row=2)
        newuid_entry = Entry(usid, width=30)
        newuid_entry.grid(column=2, row=1)
        newuid2_entry = Entry(usid, width=30)
        newuid2_entry.grid(column=2, row=2)

        errlabel = Label(usid, text="Entered text is not same ", foreground='red')
        crrlabel = Label(usid, text="User Id saved successfully ", foreground='green')

        cbtn = Button(usid, text='    save    ',bd=3 ,command=usvd)
        cbtn.grid(column=1, row=4)
        dbtn = Button(usid, text='    next    ',bd=3 ,command=usid.destroy)
        dbtn.grid(column=2, row=4)
        usid.mainloop()
        saver=' '+user__id+' '+pass__word
        text.write(saver)
        return user__id,saver

    def pwdst():

        def psvd():
            global p1, p2, pass__word
            p1 = str(newpwd_entry.get())
            p2 = str(newpwd2_entry.get())

            if p1 == p2:
                try:
                    errlabel.grid_forget()
                except:
                    pass
                pass__word = p1
                prrlabel.grid(column=2,row=3)
            else:
                try:
                    prrlabel.grid_forget()
                except:
                    pass
                errlabel.grid(column=2, row=3)

            return pass__word

        pswd = Tk()
        pswd.title('Change Password ')
        pswd.geometry('650x330')
        newpwd_label = Label(pswd, text='Enter a new Password : ')
        newpwd2_label = Label(pswd, text='Enter a new Password again : ')
        newpwd_label.grid(column=1, row=1)
        newpwd2_label.grid(column=1, row=2)
        newpwd_entry = Entry(pswd, width=30)
        newpwd_entry.grid(column=2, row=1)
        newpwd2_entry = Entry(pswd, width=30)
        newpwd2_entry.grid(column=2, row=2)

        errlabel = Label(pswd, text="Entered text is not same ", foreground='red')
        prrlabel = Label(pswd, text="Password Saved Successfully ", foreground='green')

        abtn = Button(pswd, text='    save    ',bd=3, command=psvd)
        abtn.grid(column=1, row=4)
        bbtn = Button(pswd, text='    next    ',bd=3, command=pswd.destroy)
        bbtn.grid(column=2, row=4)

        pswd.mainloop()
        saver = ' ' + user__id + ' ' + pass__word
        text.write(saver)
        return pass__word,saver

def quit_the():
    global ip1,ip2,ip3,ip4,video_run,name,rec_name
    ip1, ip2, ip3, ip4 = str(Ip1_entry.get()), str(Ip2_entry.get()), str(Ip3_entry.get()), str(Ip4_entry.get())
    name=name_entry.get()
    rec_name=str(rec_name.get())
    video_run=True
    page.destroy()
    return ip1, ip2, ip3, ip4,video_run,name,rec_name

def check():
    global pager_run
    userid = entry_user_id.get()
    password = password_entry.get()
    if userid == user__id and password == pass__word:
        pager_run=True
        root.destroy()
        return pager_run
    else:
        tryagain = Label(fil,foreground='red', text='Oops seems userid or password is incorrect try again ')
        tryagain.grid(column=2, row=6)
        pass


root.title('CCTV Details')
root.geometry('%dx%d+0+0'%(w,h))
img=Image.open('images/bg01.jpg')
img2= img.resize((w,h))
image=ImageTk.PhotoImage(img2)
l1 = Label(image=image)
l1.image = image
l1.place(x=0, y=0)

fil=Frame(root,height=199,width=300,highlightbackground='black',highlightthickness=3)
fil.place(relx=0.314159,rely=0.4)

menubar=Menu(root,bd=2)
uid=Menu(menubar,tearoff=0)
uid.add_command(label="Change userid",command=menubtn.userst)
menubar.add_cascade(label='User Id',menu=uid)

pwd=Menu(menubar,tearoff=0)
pwd.add_command(label="Change password",command=menubtn.pwdst)
menubar.add_cascade(label='Password',menu=pwd)

root.config(menu=menubar)


text=open(r'pluggins.txt','r+')
list=text.readlines()
tuple=list[0].split()[-2::]
user__id,pass__word=tuple


a=Label(fil,text='Enter the details to proceed',foreground='#000099',font=('Arial',20))
a.grid(column=2,row=1)

user_id_label=Label(fil,text='Enter the user id : ',font=('Arial',15))
space2=Label(fil,text='        ',font=('Arial',15))
space2.grid(row=1,column=3)
user_id_label.grid(column=1,row=3)
entry_user_id=Entry(fil,width=30,font=('Arial',12))
entry_user_id.grid(column=2,row=3)

password_label=Label(fil,text='Enter the password : ',font=('Arial',15))
password_label.grid(column=1,row=4)
password_entry=Entry(fil,width=30,font=('Arial',12))
password_entry.grid(column=2,row=4)

proceed_button=Button(fil,text='proceed',command=check,font=('Arial',12))
proceed_button.grid(column=2,row=5)

root.mainloop()

if pager_run==True:
    page = Tk()
    page.title('Entry details : ')
    page.geometry('%dx%d+0+0'%(w,h))
    bgimg=Image.open(r'images/bg02.jpg')
    bgimage=bgimg.resize((round(w),round(h)))
    bg=ImageTk.PhotoImage(bgimage)
    l1 = Label(image=bg)
    l1.image = bg
    l1.place(x=0, y=0)
    file = Frame(page, height=500, width=500, highlightbackground='black', highlightthickness=3,bg='black')
    file.place(relx=0.34, rely=0.38)

    name_label = Label(file, text='Name : ',font=('Arial',15),fg='white',bg='black')
    name_label.grid(column=2, row=3)
    name_entry = Entry(file, width=30,font=('Arial',12))
    name_entry.grid(column=3, row=3)

    Ip1_label = Label(file, text='Ip1 : ',font=('Arial',15),fg='white',bg='black')
    Ip1_label.grid(column=2, row=5)
    Ip1_entry = Entry(file, width=30,font=('Arial',12))
    Ip1_entry.grid(column=3, row=5)

    Ip2_label = Label(file, text='Ip2 : ',font=('Arial',15),fg='white',bg='black')
    Ip2_label.grid(column=2, row=6)
    Ip2_entry = Entry(file, width=30,font=('Arial',12))
    Ip2_entry.grid(column=3, row=6)

    Ip3_label = Label(file, text='Ip3 : ',font=('Arial',15),fg='white',bg='black')
    Ip3_label.grid(column=2, row=7)
    Ip3_entry = Entry(file, width=30,font=('Arial',12))
    Ip3_entry.grid(column=3, row=7)

    Ip4_label = Label(file, text='Ip4 : ',font=('Arial',15),fg='white',bg='black')
    Ip4_label.grid(column=2, row=8)
    Ip4_entry = Entry(file, width=30,font=('Arial',12))
    Ip4_entry.grid(column=3, row=8)

    rec_name_label=Label(file,text='Name for recording : ',font=('Arial',15),fg='white',bg='black')
    rec_name_label.grid(column=2,row=9)
    rec_name=Entry(file,width=30,font=('Arial',12))
    rec_name.grid(column=3,row=9)

    proceed_button = Button(file, text='proceed', command=quit_the,font=('Arial',12))
    proceed_button.grid(column=2, row=11)

    page.mainloop()


if video_run==True:
    ip_1=r''+ip1+'/video'
    ip_2=r''+ip2+'/video'
    ip_3=r''+ip3+'/video'
    ip_4=r''+ip4+'/video'

    if ip1==0:
        ip_1=''
    elif ip2==0:
        ip_2=''
    elif ip3==0:
        ip_3=''
    elif ip4==0:
        ip_4=''
    else:
        pass

    screen = screeninfo.get_monitors()
    w, h = int(screen[0].width-10), int(screen[0].height-80)

    vid_01=cv2.VideoCapture(ip_1)
    vid_02=cv2.VideoCapture(ip_2)
    vid_03=cv2.VideoCapture(ip_3)
    vid_04=cv2.VideoCapture(ip_4)
    rec__name='video/'+rec_name+' '+date+'.avi'

    eph=cv2.imread('images/error.png')
    eph=cv2.resize(eph,(650,330))

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(rec__name, fourcc, 20.0, (w,h))

    cv2.namedWindow(name + ' Recordings',cv2.WINDOW_FREERATIO)
    cv2.moveWindow(name + ' Recordings', 0,0)
    cv2.resizeWindow(name+' Recordings',w,h)


    run=True

    while run:
        if vid_01.isOpened():
            ret_01,frame_01=vid_01.read()
            frame_01=cv2.resize(frame_01,(650,330))
        else:
            frame_01=eph
            ret_01=True
            frame_01 = cv2.resize(frame_01, (650, 330))

        if vid_02.isOpened():
            ret_02, frame_02 = vid_02.read()
            frame_02 = cv2.resize(frame_02, (650, 330))
        else:
            frame_02 = eph
            ret_02 = True
            frame_02 = cv2.resize(frame_02, (650, 330))

        if vid_03.isOpened():
            ret_03,frame_03=vid_03.read()
            frame_03 = cv2.resize(frame_03, (650, 330))
        else:
            frame_03=eph
            ret_03=True
            frame_03 = cv2.resize(frame_03, (650, 330))

        if vid_04.isOpened():
            ret_04,frame_04=vid_04.read()
            frame_04 = cv2.resize(frame_04, (650, 330))
        else:
            frame_04=eph
            ret_04=True
            frame_04 = cv2.resize(frame_04, (650, 330))


        f_01=cv2.hconcat([frame_01,frame_02])
        f_02=cv2.hconcat([frame_03,frame_04])

        final=cv2.vconcat([f_01,f_02])

        final=cv2.line(final,(650,0),(650,660),(255,255,255),2)
        final=cv2.line(final,(0,330),(1300,330),(255,255,255),2)
        final=cv2.resize(final,(w,h))


        if rec==True:
            final = cv2.circle(final, (round(w/2)-10, round(h/2)-10), 7, (0, 0, 255), -1)
            final = cv2.circle(final, (round(w)-10, round(h/2)-10), 7, (0, 0, 255), -1)
            final = cv2.circle(final, (round(w/2)-10, round(h)-10), 7, (0, 0, 255), -1)
            final = cv2.circle(final, (round(w)-10, round(h)-10), 7, (0, 0, 255), -1)
            out.write(final)
        final=cv2.resize(final,(w,h))
        cv2.imshow(name+' Recordings', final)

        key=cv2.waitKey(1)

        if key & 0xFF==ord('q'):
            break
        if key & 0xFF==ord('r'):
            rec=True
        if key & 0xFF==ord('s'):
            rec=False
        if cv2.getWindowProperty(name+' Recordings',cv2.WND_PROP_VISIBLE)<1:
            break
        if key & 0xFF==27:
            break


    vid_01.release()
    vid_02.release()
    vid_03.release()
    vid_04.release()
    out.release()
    cv2.destroyAllWindows()
text.close()



