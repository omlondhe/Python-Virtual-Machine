from tkinter import *
import os
from tkinter.filedialog import askopenfilename, asksaveasfilename
from subprocess import call
import tkinter.messagebox as msg
import tkinter.font as tkf


fontoption = "lucida"
fontstyle = "normal"
fontsize = 12


def save():
    global file
    if file is None:
        file = asksaveasfilename(initialfile="Untitled", defaultextension=".c",
                                 filetypes=[("C programing file", "*.c")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(txt.get(1.0, END))
            f.close()
    else:
        f = open(file, "w")
        f.write(txt.get(1.0, END))
        f.close()


def save_as():
    global file
    file = "Untitled"
    file = asksaveasfilename(initialfile=f"{file}", filetypes=[("C programming file", "*.c")],
                             defaultextension=".c")
    f = open(file, "w")
    f.write(txt.get(1.0, END))
    f.close()


def stdio():
    txt.delete("%s-1c" % INSERT, INSERT)
    txt.insert(INSERT, "#include<stdio.h>\n", "RED")


def co_nio():
    txt.delete("%s-1c" % INSERT, INSERT)
    txt.insert(INSERT, "#include<conio.h>\n", "RED")


def math():
    txt.delete("%s-1c" % INSERT, INSERT)
    txt.insert(INSERT, "#include<math.h>\n", "RED")


def string():
    txt.delete("%s-1c" % INSERT, INSERT)
    txt.insert(INSERT, "#include<string.h>\n", "RED")


def time():
    txt.delete("%s-1c" % INSERT, INSERT)
    txt.insert(INSERT, "#include<time.h>\n", "RED")


def stdlib():
    txt.delete("%s-1c" % INSERT, INSERT)
    txt.insert(INSERT, "#include<stdlib.h>\n", "RED")


def ass():
    txt.delete("%s-1c" % INSERT, INSERT)
    txt.insert(INSERT, "#include<assert.h>\n", "RED")


def comp():
    txt.delete("%s-1c" % INSERT, INSERT)
    txt.insert(INSERT, "#include<comp.h>\n", "RED")


def c_type():
    txt.delete("%s-1c" % INSERT, INSERT)
    txt.insert(INSERT, "#include<ctype.h>\n", "RED")


def err_no():
    txt.delete("%s-1c" % INSERT, INSERT)
    txt.insert(INSERT, "#include<errno.h>\n", "RED")


def f_env():
    txt.delete("%s-1c" % INSERT, INSERT)
    txt.insert(INSERT, "#include<fenv.h>\n", "RED")


def flo():
    txt.delete("%s-1c" % INSERT, INSERT)
    txt.insert(INSERT, "#include<float.h>\n", "RED")


def int_types():
    txt.delete("%s-1c" % INSERT, INSERT)
    txt.insert(INSERT, "#include<inttypes.h>\n", "RED")


def iso646():
    txt.delete("%s-1c" % INSERT, INSERT)
    txt.insert(INSERT, "#include<iso646.h>\n", "RED")


def limits():
    txt.delete("%s-1c" % INSERT, INSERT)
    txt.insert(INSERT, "#include<limits.h>\n", "RED")


def local():
    txt.delete("%s-1c" % INSERT, INSERT)
    txt.insert(INSERT, "#include<locale.h>\n", "RED")


def set_jmp():
    txt.delete("%s-1c" % INSERT, INSERT)
    txt.insert(INSERT, "#include<setjmp.h>\n", "RED")


def signal():
    txt.delete("%s-1c" % INSERT, INSERT)
    txt.insert(INSERT, "#include<signal.h>\n", "RED")


def std_align():
    txt.delete("%s-1c" % INSERT, INSERT)
    txt.insert(INSERT, "#include<stdalign.h>\n", "RED")


def std_arg():
    txt.delete("%s-1c" % INSERT, INSERT)
    txt.insert(INSERT, "#include<std_arg.h>\n", "RED")


def std_atomic():
    txt.delete("%s-1c" % INSERT, INSERT)
    txt.insert(INSERT, "#include<stdatomic.h>\n", "RED")


def std_bool():
    txt.delete("%s-1c" % INSERT, INSERT)
    txt.insert(INSERT, "#include<stdbool.h>\n", "RED")


def std_def():
    txt.delete("%s-1c" % INSERT, INSERT)
    txt.insert(INSERT, "#include<stddef.h>\n", "RED")


def std_int():
    txt.delete("%s-1c" % INSERT, INSERT)
    txt.insert(INSERT, "#include<stdint.h>\n", "RED")


def std_no_return():
    txt.insert(INSERT, "#include<stdnoreturn.h>\n", "RED")


def tg_math():
    txt.delete("%s-1c" % INSERT, INSERT)
    txt.insert(INSERT, "#include<tgmath.h>\n", "RED")


def thread():
    txt.delete("%s-1c" % INSERT, INSERT)
    txt.insert(INSERT, "#include<thread.h>\n", "RED")


def uchar():
    txt.delete("%s-1c" % INSERT, INSERT)
    txt.insert(INSERT, "#include<uchar.h>\n", "RED")


def wchar():
    txt.delete("%s-1c" % INSERT, INSERT)
    txt.insert(INSERT, "#include<wchar.h>\n", "RED")


def wc_types():
    txt.delete("%s-1c" % INSERT, INSERT)
    txt.insert(INSERT, "#include<wctypes.h>\n", "RED")


def void_main():
    txt.delete("%s-3c" % INSERT, INSERT)
    txt.insert(INSERT, "void main()\n {\n   \n }", "BLUE")
    cur = txt.index(INSERT)
    print(cur)
    txt.mark_set(INSERT, float("%s" % cur)-1.0)


def gen_if():
    txt.delete("%s-2c" % INSERT, INSERT)
    txt.insert(INSERT, "if( )\n {\n   \n }\nelse\n {\n  \n }\n\n", "ORANGE")
    cur = txt.index(INSERT)
    print(cur)
    txt.mark_set(INSERT, float("%s" % cur) - 8.1)


def el_if():
    txt.delete("%s-2c" % INSERT, INSERT)
    txt.insert(INSERT, "if( )\n {\n   \n }\nelse if ()\n {\n   \n }\nelse\n {\n  \n }\n\n", "ORANGE")
    cur = txt.index(INSERT)
    print(cur)
    txt.mark_set(INSERT, float("%s" % cur) - 12.7)


def for_l():
    txt.delete("%s-3c" % INSERT, INSERT)
    txt.insert(INSERT, "for ( int i =  ; i <=  ; i++)\n {\n   \n }\n\n", "VIOLET")
    cur = txt.index(INSERT)
    print(cur)
    txt.mark_set(INSERT, float("%s" % cur) - 4.3)


def w_loop():
    txt.delete("%s-3c" % INSERT, INSERT)
    txt.insert(INSERT, "while ( )\n {\n   \n }\n\n", "VIOLET")
    cur = txt.index(INSERT)
    print(cur)
    txt.mark_set(INSERT, float("%s" % cur) - 4.3)


def do_loop():
    txt.delete("%s-2c" % INSERT, INSERT)
    txt.insert(INSERT, "do\n {\n   \n } while ( );\n\n", "VIOLET")
    cur = txt.index(INSERT)
    print(cur)
    txt.mark_set(INSERT, float("%s" % cur) - 2.3)


def switch_case():
    txt.delete("%s-3c" % INSERT, INSERT)
    txt.insert(INSERT, "switch ( choice )\n {\n  case  :\n\t\n\t\n\tbreak;  \n  default:\n\t \n}\n\n", "ORANGE")
    cur = txt.index(INSERT)
    print(cur)
    txt.mark_set(INSERT, float("%s" % cur) - 2.3)


def structure():
    txt.delete("%s-4c" % INSERT, INSERT)
    txt.insert(INSERT, "struct Structure\n {\n   \n };\n", "ORANGE")
    cur = txt.index(INSERT)
    print(cur)
    txt.mark_set(INSERT, float("%s" % cur) - 2.0)


def print_f():
    txt.delete("%s-3c" % INSERT, INSERT)
    txt.insert(INSERT, "printf (\" \");", "GREEN")


def scan_f():
    txt.delete("%s-3c" % INSERT, INSERT)
    txt.insert(INSERT, "scanf (\"% \", &);", "GREEN")


def str_cat():
    txt.insert(INSERT, "cat();")


def str_len():
    txt.insert(INSERT, "len();")


def str_rev():
    txt.insert(INSERT, "rev();")


def str_cmp():
    txt.insert(INSERT, "cmp();")


def str_cpy():
    txt.insert(INSERT, "cpy();")


def str_chr():
    txt.insert(INSERT, "chr();")


def undo():
    txt.event_generate("<<Undo>>")


def redo():
    try:
        txt.edit_redo()
    except:
        pass


def select_all():
    txt.tag_add("sel", 1.0, END)


def cut():
    txt.event_generate("<<Cut>>")


def copy():
    txt.event_generate("<<Copy>>")


def paste():
    txt.event_generate("<<Paste>>")


def delete():
    txt.delete(1.0, END)


# def f_print():
#     if file is None:
#         save()
#         os.startfile(file.replace(".c", ".txt"), "print")
#     else:
#         os.startfile(file.replace(".c", ".txt"), "print")


def new():
    global file
    root.title("C Editor")
    txt.delete(1.0, END)


def new_p():
    call(["python", "C Editor.py"])


def f_open():
    global file
    file = askopenfilename(defaultextension=".c", filetypes=[("C programming Files", "*.c")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file))
        txt.delete(1.0, END)
        f = open(file, "r")
        txt.insert(1.0, f.read)
        f.close()


def stop():
    global file
    if file is None:
        e = msg.askyesno("Exit ", "Do you want to Save you File ?")
        if e == YES:
            save()
            exit()
        else:
            exit()
    else:
        exit()


def font():
    font_ls = list(tkf.families())

    def set_op():
        txt.config(font=f"{font_ls[font.curselection()[0]]} {fontsize} {fontstyle}")

    font_root = Toplevel(root)
    font_root.title("Font")
    font_root.geometry("250x300")

    font_label = Label(font_root, text="Font\n\n", font="ariel 21")
    font_label.place(x=21, y=3)

    scroll_y = Scrollbar(font_root)
    font = Listbox(font_root, font="lucida 11", yscrollcommand=scroll_y.set)
    font.place(x=21, y=51)
    scroll_y.pack(fill=Y, side=RIGHT)
    scroll_y.config(command=font.yview)

    for i in tkf.families():
        font.insert(END, i)

    Button(font_root, text="Ok", font="lucida 11", command=set_op, width=7).place(x=111, y=251)

    font_root.mainloop()


def style():
    style_ls = ["normal", "bold", "italic", "roman", "underline"]

    def set_style():
        txt.config(font=f"{fontstyle} {fontsize} {style_ls[style.curselection()[0]]}")

    style_root = Toplevel(root)
    style_root.title("Style")
    style_root.geometry("250x300")

    style_label = Label(style_root, text="Font Style\n\n", font="ariel 21")
    style_label.place(x=21, y=3)

    style = Listbox(style_root, font="lucida 11")
    style.place(x=21, y=51)

    style.insert(END, "normal")
    style.insert(END, "bold")
    style.insert(END, "italic")
    style.insert(END, "roman")
    style.insert(END, "underline")

    Button(style_root, text="Ok", font="lucida 11", command=set_style, width=7).place(x=111, y=251)
    style_root.mainloop()


def size():
    size_ls = list(range(8, 73))

    def set_size():
        txt.config(font=f"{fontoption} {size_ls[size.curselection()[0]]} {fontstyle}")

    size_root = Toplevel(root)
    size_root.title("Size")
    size_root.geometry("250x360")

    size_label = Label(size_root, text="Font Size\n\n", font="ariel 21")
    size_label.place(x=21, y=3)

    scroll_y = Scrollbar(size_root)
    size = Listbox(size_root, font="lucida 11", yscrollcommand=scroll_y.set)
    size.place(x=21, y=51)
    scroll_y.pack(fill=Y, side=RIGHT)
    scroll_y.config(command=size.yview)

    for i in range(8, 73):
        size.insert(END, i)

    Button(size_root, text="Ok", font="lucida 11", command=set_size, width=7).place(x=111, y=251)
    size_root.mainloop()


def f_help():
    msg.showinfo("C Editor",
                 "1) You can Write the C program in the text area \n"
                 "2) The option to Save , Make new file is available in the File menu section \n"
                 "3) You can Exit whenever you want to Exit and we will ask you if any problem or warning is there \n"
                 "4) Fonts option is also available in th is Version to personalize the Editor settings \n"
                 "5) If you have some queries Visit Contact Us section in the Help menu\n")


def contact():
    msg.showinfo("C Editor",
                 "Creator : Om Londhe, Ajay Rathod\n"
                 "Contact no. : 7276594467\n"
                 "E-mail id : oplondhe@gmaiil.com, rathodajay1202@gmail.com\n")


def about():
    msg.showinfo("C Editor",
                 "This is the C Editor .\n"
                 "It is made by Om Londhe and Ajay Rathod using the tKinter package in the Python for Graphical User "
                 "Interface(GUI) purpose......\n"
                 "The version of Python used is the Python 3.7.4\n")


def com():
    save_as()
    # print(file)
    os.system(f'start cmd /k "gcc {file}"')


def run():
    if file is None:
        save()
    else:
        pass
    # print(file)
    os.system(f'start cmd /k "a"')


file = None
root = Tk()
root.title("C Editor")

txt_scroll_x = Scrollbar(root, orient=HORIZONTAL)
txt_scroll_x.pack(side=BOTTOM, fill=X)

txt_scroll_y = Scrollbar(root)
txt_scroll_y.pack(side=RIGHT, fill=Y)

txt = Text(root, undo=True, font=f"{fontoption} {fontsize} {fontstyle}", xscrollcommand=txt_scroll_x.set,
           yscrollcommand=txt_scroll_y.set)
txt.pack(fill=BOTH, expand=True)

txt_scroll_x.config(command=txt.xview)
txt_scroll_y.config(command=txt.yview)

m = Menu(root)
m1 = Menu(m, tearoff=0)
m1.add_command(label="New", command=new)
m1.add_command(label="New Window", command=new_p)
m1.add_separator()
m1.add_command(label="Open", command=f_open)
m1.add_separator()
m1.add_command(label="Save", command=save)
m1.add_command(label="Save as", command=save_as)
# m1.add_command(label="Print", command=f_print)
m1.add_separator()
m1.add_command(label="Exit", command=stop)
root.config(menu=m)
m.add_cascade(label="File", menu=m1)

m1 = Menu(m, tearoff=0)
m1.add_command(label="Undo", command=undo)
m1.add_command(label="Redo", command=redo)
m1.add_command(label="Select all", command=select_all)
m1.add_separator()
m1.add_command(label="Cut", command=cut)
m1.add_command(label="Copy", command=copy)
m1.add_command(label="Paste", command=paste)
m1.add_command(label="Delete", command=delete)
root.config(menu=m)
m.add_cascade(label="Edit", menu=m1)


m1 = Menu(m, tearoff=0)
m1.add_command(label="Compile", command=com)
m1.add_command(label="Run", command=run)
root.config(menu=m)
m.add_cascade(label="Build", menu=m1)

m1 = Menu(m, tearoff=0)
m1.add_checkbutton(label="Wordwrap")
fm = Menu(m1, tearoff=0)
fm.add_command(label="Font", command=font)
fm.add_command(label="Font Style", command=style)
fm.add_command(label="Text Size", command=size)
m1.add_cascade(label="Font", menu=fm)
root.config(menu=m)
m.add_cascade(label="Format", menu=m1)

m1 = Menu(m, tearoff=0)
m1.add_command(label="View Help", command=f_help)
m1.add_command(label="Contact Us", command=contact)
m1.add_separator()
m1.add_command(label="About", command=about)
root.config(menu=m)
m.add_cascade(label="Help", menu=m1)


header_files = Menu(root, tearoff=0, font="lucida 11")
header_files.add_command(label="#include<stdio.h>", command=stdio)
header_files.add_command(label="#include<conio.h>", command=co_nio)
header_files.add_command(label="#include<math.h>", command=math)
header_files.add_command(label="#include<string.h>", command=string)
header_files.add_command(label="#include<time.h>", command=time)
header_files.add_command(label="#include<stdlib.h>", command=stdlib)
header_files.add_command(label="#include<assert.h>", command=ass)
header_files.add_command(label="#include<complex.h>", command=comp)
header_files.add_command(label="#include<ctype.h>", command=c_type)
header_files.add_command(label="#include<errno.h>", command=err_no)
header_files.add_command(label="#include<fenv.h>", command=f_env)
header_files.add_command(label="#include<float.h>", command=flo)
header_files.add_command(label="#include<inttypes.h>", command=int_types)
header_files.add_command(label="#include<iso646.h>", command=iso646)
header_files.add_command(label="#include<limits.h>", command=limits)
header_files.add_command(label="#include<locale.h>", command=local)
header_files.add_command(label="#include<setjmp.h>", command=set_jmp)
header_files.add_command(label="#include<signal.h>", command=signal)
header_files.add_command(label="#include<stdalign.h>", command=std_align)
header_files.add_command(label="#include<stdarg.h>", command=std_arg)
header_files.add_command(label="#include<stdatomic.h>", command=std_atomic)
header_files.add_command(label="#include<stdbool.h>", command=std_bool)
header_files.add_command(label="#include<stddef.h>", command=std_def)
header_files.add_command(label="#include<stdint.h>", command=std_int)
header_files.add_command(label="#include<stdnoreturn.h>", command=std_no_return)
header_files.add_command(label="#include<tgmath.h> ", command=tg_math)
header_files.add_command(label="#include<threads.h>", command=thread)
header_files.add_command(label="#include<uchar.h>", command=uchar)
header_files.add_command(label="#include<wchar.h>", command=wchar)
header_files.add_command(label="#include<wctype.h>", command=wc_types)


quick_options = Menu(root, tearoff=0, font="lucida 11")
quick_options.add_command(label="Copy", command=copy)
quick_options.add_command(label="Cut", command=cut)
quick_options.add_command(label="Paste", command=paste)
quick_options.add_command(label="Select All", command=select_all)
quick_options.add_separator()
quick_options.add_command(label="Compile", command=com)
quick_options.add_command(label="Run", command=run)
quick_options.add_separator()
quick_options.add_command(label="Undo", command=undo)
quick_options.add_command(label="Redo", command=redo)
quick_options.add_command(label="Delete All", command=delete)
quick_options.add_separator()
# quick_options.add_command(label="Print", command=f_print)


void = Menu(root, tearoff=0, font="lucida 11")
void.add_command(label="void main()...", command=void_main)


if_statement = Menu(root, tearoff=0, font="lucida 11")
if_statement.add_command(label="if () { }...else {}", command=gen_if)
if_statement.add_command(label="if () { }...lse if () { }...else { }", command=el_if)


for_loop = Menu(root, tearoff=0, font="lucida 11")
for_loop.add_command(label="for ()", command=for_l)


wh_loop = Menu(root, tearoff=0, font="lucida 11")
wh_loop.add_command(label="while ( )", command=w_loop)


do = Menu(root, tearoff=0, font="lucida 11")
do.add_command(label="do ... while ( )", command=do_loop)


switch = Menu(root, tearoff=0, font="lucida 11")
switch.add_command(label="switch ( ) ... case no", command=switch_case)


struct = Menu(root, tearoff=0, font="lucida 11")
struct.add_command(label="struct Structure {  };", command=structure)


pri = Menu(root, tearoff=0, font="lucida 11")
pri.add_command(label="printf ( \" \" );", command=print_f)

sc = Menu(root, tearoff=0, font="lucida 11")
sc.add_command(label="scanf ( \" \", & );", command=scan_f)


str_fun = Menu(root, tearoff=0, font="lucida 11")
str_fun.add_command(label="strlen();", command=str_len)
str_fun.add_command(label="concat();", command=str_cat)
str_fun.add_command(label="strchr();", command=str_chr)
str_fun.add_command(label="strcmp();", command=str_cmp)
str_fun.add_command(label="strcmp();", command=str_cpy)
str_fun.add_command(label="strrev();", command=str_rev)


def show_header_files(event):
    try:
        header_files.tk_popup(event.x_root, event.y_root, 0)
    finally:
        header_files.grab_release()


def show_quick_options(right_click):
    try:
        quick_options.tk_popup(right_click.x_root, right_click.y_root, 0)
    finally:
        quick_options.grab_release()


def logic(fun):
    pos = txt.index(INSERT)

    if "void main" not in txt.get(1.0, END):
        if txt.get("%s-3c" % pos, pos) == "voi":
            try:
                void.tk_popup(fun.x_root, fun.y_root, 0)
            finally:
                void.grab_release()

    elif txt.get("%s-2c" % pos, pos) == "if":
        try:
            if_statement.tk_popup(fun.x_root, fun.y_root, 0)
        finally:
            if_statement.grab_release()

    elif txt.get("%s-3c" % pos, pos) == "for":
        try:
            for_loop.tk_popup(fun.x_root, fun.y_root, 0)
        finally:
            for_loop.grab_release()

    elif txt.get("%s-3c" % pos, pos) == "whi":
        try:
            wh_loop.tk_popup(fun.x_root, fun.y_root, 0)
        finally:
            wh_loop.grab_release()

    elif txt.get("%s-2c" % pos, pos) == "do":
        try:
            do.tk_popup(fun.x_root, fun.y_root, 0)
        finally:
            do.grab_release()

    elif txt.get("%s-3c" % pos, pos) == "swi":
        try:
            switch.tk_popup(fun.x_root, fun.y_root, 0)
        finally:
            switch.grab_release()

    elif txt.get("%s-3c" %pos, pos) == "pri":
        try:
            pri.tk_popup(fun.x_root, fun.y_root, 0)
        finally:
            pri.grab_release()

    elif txt.get("%s-3c" % pos, pos) == "sca":
        try:
            sc.tk_popup(fun.x_root, fun.y_root, 0)
        finally:
            sc.grab_release()

    elif "#include<string.h>" in txt.get(1.0, END):
        if txt.get("%s-3c" % pos, pos) == "str":
            try:
                str_fun.tk_popup(fun.x_root, fun.y_root, 0)
            finally:
                str_fun.grab_release()

    if txt.get("%s-4c" % pos, pos) == "stru":
        try:
            struct.tk_popup(fun.x_root, fun.y_root, 0)
        finally:
            struct.grab_release()


txt.bind("<Shift-numbersign>", show_header_files)
txt.bind("<KeyRelease>", logic)
txt.bind("<Button-3>", show_quick_options)
txt.focus_set()
txt.tag_config('RED', foreground='red')
txt.tag_config('BLUE', foreground='blue')
txt.tag_config('ORANGE', foreground='orange')
txt.tag_config('PURPLE', foreground='purple')
txt.tag_config('VIOLET', foreground='violet')
txt.tag_config('YELLOW', foreground='yellow')
txt.tag_config('GREEN', foreground='green')
root.mainloop()
