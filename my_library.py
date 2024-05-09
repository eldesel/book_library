#
import os
import json
from tkinter import *
from tkinter import messagebox
from some_constants import *
import test_func as ts
#
letters = ['ا','ب','ت','ج','ح','خ','د','ذ','ر','ز','س','ش','ص','ض','ط','ظ','ع','غ','ف','ق','ك','ل','م','ن','ه','و','ي','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
writers = []
num_books = 0
mian_dict_ids_books = {}
ROOT_COLR = '#0A706B'
ENTRY_COLR = '#DED3BA'
FONT_COLR = '#C4AF82'
COLR ='#AA6131'
WHITE_MOOD = (ROOT_COLR,FONT_COLR,ENTRY_COLR,COLR)
BOOKS = 'books.txt'
#
def ready():
    global num_books
    if os.path.exists(BOOKS):
        mian_dict_ids_books.clear()
        with open(BOOKS,'r') as f:
            data = json.load(f)
            num_books = len(data)
            for writer in data:
                if writer[1] not in writers:
                     writers.append(writer[1])
            for book , id in zip(data,range(1,len(data)+1)):
                mian_dict_ids_books[id] = book[0]
            
                
    else:
        with open(BOOKS,'w') as f:
            json.dump([],f)
ready()
def calu(big,rate):
    n1 = big * rate
    final = n1 // 100
    return final

def change_yview(event=0):
    if len(main_canves.find_all()) == 1:
        return
    elif event.delta !=0:
        if event.delta > 0:
            main_canves.yview('scroll',-1,'units')
        else:
            main_canves.yview('scroll',1,'units')

def put_books(let = None,writer = None):
    for dele in main_canves.find_all():
        main_canves.delete(dele)
    main_dict = {}
    main_list = []
    y_b= 0
    tit = True
    state = True
    if let != None:
        for i in main_canves.find_all():
            main_canves.delete(i)
        with open(BOOKS,'r') as f:
            data = json.load(f)
        for letter in letters:
            for name in data:
                if name[0][0] == letter:
                    if tit == True: 
                        main_canves.create_text(150,y_b+15,text=f'_________________{letter}_________________')
                        y_b +=10
                    for id,book in mian_dict_ids_books.items():
                        if name[0] == book:
                            main_canves.create_text(295,y_b+20,text=f'{name[0]} // {name[1]} // {name[2]} // {name[-1]} // ({id}) ',anchor=E)
                            tit = False
                            y_b +=20
            else:
                tit = True
                main_canves.config(scrollregion=main_canves.bbox('all')) 
    
    elif writer != None:
        with open(BOOKS,'r') as f:
            data_ = json.load(f)
        for wirter_ in writers:
            main_dict[wirter_] = []
        for key,value in main_dict.items():
            for item_w in data_:
                if item_w[1] == key:
                    value.append(item_w)
        for value in main_dict.values():
            main_list.append(value)
        else:
            ts.sort_ar(main_list)
        for books in main_list:
            for key,value in main_dict.items():
                if value == books:
                    for i in value:
                        for id,book in mian_dict_ids_books.items():
                            if state == True:
                                main_canves.create_text(150,y_b+15,text=f'________________{key}________________')
                                state = False
                                y_b +=18
                            if i[0] == book:
                                main_canves.create_text(293,y_b+20,text=f'{i[0]}//{i[-1]}//{i[2]} ({id})  ',anchor=E)
                                y_b +=20
                    else:
                        state = True
                        main_canves.config(scrollregion=main_canves.bbox('all')) 
    
    else:
        with open(BOOKS,'r') as f:
            data = json.load(f)
        for i in data:
            for id,book in mian_dict_ids_books.items():
                if book == i[0]:
                    main_canves.create_text(300,y_b,text=f'{i[0]}  // {i[1]}  // {i[-1]}  // ({id})  \n{i[2]} ',anchor=E)
                    y_b += 40
        else:
            main_canves.config(scrollregion=main_canves.bbox('all')) 

def close(event):
    global num_books
    root.state('zoomed')
    '''
    with open(BOOKS,'r') as f:
        data = json.load(f)
        num_books = len(data)
        if len(data) != 0:
            for writer in data:
                if writer[1] not in writers:
                     writers.append(writer[1])
    '''

def add_books():
    def add_book():
        for lb in s_root.children.values():
            name = type(lb).__name__
            if name == 'Label':
                if lb.cget('text') == 'add a books.':
                    pass
                else:
                     lb.config(fg='black')

        if entry_name.get() == '':
            messagebox.showerror('Erorr','please enter name of the book')
            labe_name.config(fg='#6B0F0F')
        elif entry_writer.get() == '':
            messagebox.showerror('Erorr','please enter name the writer')
            labe_writer.config(fg='#6B0F0F')
        elif entry_size.get() == '':
            messagebox.showerror('Erorr','please enter contact of the book')
            labe_size.config(fg='#6B0F0F')
        elif entry_type.get() =='':
            messagebox.showerror('Erorr','please enter type of book (Book classification)')
            labe_type.config(fg='#6B0F0F')
        else:
            with open(BOOKS,'r') as f:
                data = json.load(f) 
            data.append([entry_name.get().lower(),entry_writer.get().lower(),entry_type.get().lower(),entry_size.get().lower()])
            with open(BOOKS,'w') as f:
                json.dump(data,f)
            messagebox.showinfo('Successful','Added has been successful')
            ready()
            sort()
            num_of_books.config(text=f' this is a numbers of books exists now: {num_books}')

    x_en = main_width-216
    x_lb = main_width-366
    root.state('iconic')
    s_root = Tk()
    s_root.config(bg=ROOT_COLR)
    s_root.state('zoomed')
    s_root.bind(DESTROY,close)

    #
    main_but = Button(s_root,bg=WHITE_MOOD[3],width=int(calu(1366,1.3)),text='Add a book.',command=add_book)
    main_but.pack()
    entry_name  = Entry(s_root,bg=WHITE_MOOD[2])
    entry_name.place(x=x_en,y=main_height-258)
    entry_writer  = Entry(s_root,bg=WHITE_MOOD[2])
    entry_writer.place(x=x_en,y=main_height-228)
    entry_size = Entry(s_root,bg=WHITE_MOOD[2])
    entry_size.place(x=x_en,y=main_height-198)
    entry_type    = Entry(s_root,bg=WHITE_MOOD[2])
    entry_type.place(x=x_en,y=main_height-168)
    #
    main_labal  = Label(s_root,bg=WHITE_MOOD[0],fg=WHITE_MOOD[1],font=['bold',int(calu(1366,4))],text='add a books.')
    main_labal.pack(pady=50)
    labe_name   = Label(s_root,bg=WHITE_MOOD[0],fg='black',text='Enter name of the book:')
    labe_name.place(x=x_lb,y=main_height-258)
    labe_writer = Label(s_root,bg=WHITE_MOOD[0],fg='black',text='Enter name the writer:')
    labe_writer.place(x=x_lb,y=main_height-228)
    labe_size = Label(s_root,bg=WHITE_MOOD[0],fg='black',text='Enetr size of the book:')
    labe_size.place(x=x_lb,y=main_height-198)
    labe_type   = Label(s_root,bg=WHITE_MOOD[0],fg='black',text='Enter his type:')
    labe_type.place(x=x_lb,y=main_height-168)

def sort():
    if var_alp.get() == 1:
        put_books(let=0)
    elif var_wir.get() == 1:
        put_books(writer=0)
    else:
        put_books()

def serach(event):
    find = False
    if serach_entry.get():
        for i in main_canves.find_all():
            main_canves.delete(i)
        with open(BOOKS,'r') as f:
            data = json.load(f)
        for book in data:
            if serach_entry.get().strip().lower() == book[0]:
                for id,book_ in mian_dict_ids_books.items():
                    if serach_entry.get().strip().lower() == book_ :
                        main_canves.create_text(300,5,text=f'{book[0]} //{book[1]} //{book[2]} //{book[3]} // ({id})',anchor=E)
                        find = True
                        main_canves.config(scrollregion=main_canves.bbox('all'))
        for id_ ,_book_ in mian_dict_ids_books.items():
            if serach_entry.get().strip().lower() == str(id_):
                for book_n in data:
                    if book_n[0] == _book_:
                        main_canves.create_text(300,5,text=f'{book_n[0]} //{book_n[1]} //{book_n[2]} //{book_n[3]} // ({id_})',anchor=E)
                        find = True
                        main_canves.config(scrollregion=main_canves.bbox('all'))
                        
        else:
            if find == False:
                messagebox.showinfo('INFO..',"this book is not available")
                sort()
    else:
        messagebox.showerror('Error',"Pls enter book name")
        sort()

def edit(event):
    def edit_():
        find = False
        laabel0.config(fg=WHITE_MOOD[1])
        with open(BOOKS,'r') as f:
            data = json.load(f)
        if name_entry.get():
            for book in data:
                if book[0] == name_entry.get():
                    find = True
                    if name_e_entry.get():
                        book[0] = name_e_entry.get()
                    if writer_e_entry.get():
                        book[1] = writer_e_entry.get()
                    if size_e_entry.get():
                        book[2] = size_e_entry.get()
                    if type_e_entry.get():
                        book[-1] = type_e_entry.get()
                        pass
            else:
                if find == True:
                    with open(BOOKS,'w') as f:
                        json.dump(data,f)
                    sort()
                    messagebox.showinfo('INFO','edit has been successful')
                    root_2.destroy()
                else:
                    messagebox.showerror('Error','this book its not availabel')
                    laabel0.config(fg='red')

        else:
            messagebox.showerror('Error','Pls put an book you want to edit it')
            laabel0.config(fg='red')
    root_2 = Tk()
    root_2.title('Edit an book')
    root_2.geometry(f'350x250+{calu(main_width,36)}+{calu(main_height,28)}')
    root_2.resizable(False,False)
    root_2.config(bg=WHITE_MOOD[0])
    line = Label(root_2,bg=WHITE_MOOD[-1],height=200).pack()
    name_entry = Entry(root_2,bg=WHITE_MOOD[2])
    #
    name_e_entry = Entry(root_2,bg=WHITE_MOOD[2])
    writer_e_entry = Entry(root_2,bg=WHITE_MOOD[2])
    size_e_entry = Entry(root_2,bg=WHITE_MOOD[2])
    type_e_entry = Entry(root_2,bg=WHITE_MOOD[2])
    #
    laabel0 = Label(root_2,bg=WHITE_MOOD[0],fg=WHITE_MOOD[1],text='Put book name')
    laabel1 = Label(root_2,bg=WHITE_MOOD[0],fg=WHITE_MOOD[1],text='Put a new name')
    laabel2 = Label(root_2,bg=WHITE_MOOD[0],fg=WHITE_MOOD[1],text='Put a new writer')
    laabel3 = Label(root_2,bg=WHITE_MOOD[0],fg=WHITE_MOOD[1],text='Put a new size')
    laabel4 = Label(root_2,bg=WHITE_MOOD[0],fg=WHITE_MOOD[1],text='put a new type')

    btn = Button(root_2,width=8,text='Save',command=edit_)
    btn.place(x=250,y=200)
    name_entry.place(x=220,y=30)
    name_e_entry.place(x=5,y=30)
    writer_e_entry.place(x=5,y=70)
    size_e_entry.place(x=5,y=110)
    type_e_entry.place(x=5,y=150)
    laabel0.place(x=220,y=5)
    laabel1.place(x=5,y=10)
    laabel2.place(x=5,y=50)
    laabel3.place(x=5,y=90)
    laabel4.place(x=5,y=130)

#
root = Tk()
root.title('Library')
root.config(bg=WHITE_MOOD[0])
root.state('zoomed')
root.bind('<Control-e>',edit)

main_height = root.winfo_screenheight()
main_width = root.winfo_screenwidth()
#
var_alp = IntVar()
var_wir = IntVar()
title = Label(root,bg=WHITE_MOOD[0],fg=WHITE_MOOD[1],text='My library',font=['bold',50])
dev_label = Label(root,bg=WHITE_MOOD[0],fg=WHITE_MOOD[1],text='developer:\n youssef khaled',font='italic')
num_of_books = Label(root ,bg=WHITE_MOOD[0],fg=WHITE_MOOD[1],text=f' this is a numbers of books exists now: {num_books} ' , font=['times',int(calu(1366,1.1))])
lane = Label(root,height=main_height,bg=WHITE_MOOD[1])
but_add = Button(root,text='add a new book',bg=COLR,width=int(calu(main_width,1.25)),height=int(calu(768,0.42)),activebackground='white',command=add_books)
sort_books = Button(root,text='sort books',bg=COLR,width=int(calu(main_width,1.25)),height=int(calu(768,0.42)),command=sort)
main_frame = Frame(root)
main_canves = Canvas(main_frame,bg=WHITE_MOOD[2],width=int(calu(main_width,27)),height=int(calu(main_height,79)))
can_scrollbar = Scrollbar(main_frame,command=main_canves.yview)
label_chek_alp = Label(root,bg=WHITE_MOOD[0],fg=WHITE_MOOD[1],text='Sort by letters->').place(x=main_width-(main_width-1050),y=main_height-(main_height-480))
label_chek_wirters = Label(root,bg=WHITE_MOOD[0],fg=WHITE_MOOD[1],text='Sort by wirters->').place(x=main_width-(main_width-1208),y=main_height-(main_height-480))
chek_b_alp = Checkbutton(root,variable=var_alp,bg=WHITE_MOOD[0],activebackground=WHITE_MOOD[1],cursor='hand2')
chek_b_wirter = Checkbutton(root,variable=var_wir,bg=WHITE_MOOD[0],activebackground=WHITE_MOOD[1],cursor='hand2')
serach_entry = Entry(root,bg=WHITE_MOOD[2])
label_serach_entrey = Label(bg=WHITE_MOOD[0],fg=WHITE_MOOD[1],font=['bold',int(calu(main_width,1))],text='serach bar->')
main_canves.config(yscrollcommand=can_scrollbar.set)
main_canves.bind('<Configure>',lambda e:main_canves.config(scrollregion=main_canves.bbox('all')))
main_canves.bind(MOUS_WHEEL,change_yview)
serach_entry.bind('<Return>',serach)
#
title.place(x=main_width-316,y=main_height-718) # x = 1050 y= 50
dev_label.place(x=main_width-111,y=main_height-111) # x = 1255 y=657
num_of_books.place(x=main_width-1370,y=main_height-758) # x = 30 y=10
lane.place(x=main_width-346) # x = 1020 y = null
but_add.place(x=main_width-228,y=main_height-168) # x = 1138 , y=600
sort_books.place(x=main_width-228,y=main_height-248)# x = 1138 , y = 520
main_frame.place(x=main_width-1361,y=main_height-728) # x = 5 , y = 40
main_canves.pack(side=LEFT)
can_scrollbar.pack(side=RIGHT,fill=Y)
chek_b_alp.place(x=main_width-226,y=main_height-288) # x = 1140, y=480
chek_b_wirter.place(x=main_width-66,y=main_height-288) # x= 1300,y=480
serach_entry.place(x=main_width-476,y=main_height-763)# x = 890 , y=5
label_serach_entrey.place(x=main_width-576,y = main_height-763) # x = 800 , y = 5
put_books()
root.mainloop()