from tkinter import *
import random
import ttkthemes
from tkinter import ttk

def change_bg(widget):
    widget.config(bg='blue')
    widget.after(100,lambda:widget.config(bg='black'))

root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')

root.geometry('940x735+200+10')
root.resizable(0,0)

main_frame = Frame(root,bd=4) # width='50', height='30',bg='orange'
main_frame.grid()

# first Frame in the main frame ------------
title_frame = Frame(main_frame,bg='orange')
title_frame.grid()
title_lable = Label(title_frame, text="Typing Master",font=('roboto', 20, 'bold'),bg='goldenrod3',fg='white',
                    width=55,bd=10)
title_lable.grid(pady=5)

# paragraph frame start here ---------------------
para_frame = Frame(main_frame)
para_frame.grid(row=1, column=0)

paragraph_list = [
    "Python is a versatile programming language that is widely used for various applications. It is known for its simplicity and readability, making it an excellent choice for beginners and experienced developers alike. With a vast ecosystem of libraries and frameworks, Python empowers developers to build everything from simple scripts to complex web applications. Its syntax emphasizes code readability, and the language supports multiple programming paradigms. Python's community is vibrant and supportive, offering a wealth of resources for learning and collaboration. Whether you're interested in data science, machine learning, web development, or automation, Python has the tools and community to help you succeed.",
    
    "Artificial Intelligence (AI) is transforming industries and reshaping our daily lives. Machine learning, a subset of AI, enables systems to learn from data and improve over time without explicit programming. Python is a popular language for machine learning due to its extensive libraries like TensorFlow and scikit-learn. These libraries provide tools for data analysis, modeling, and deployment of machine learning models. As businesses adopt AI to gain a competitive edge, Python's role in the AI landscape continues to grow. Whether you're a data scientist, engineer, or researcher, proficiency in Python is a valuable skill in the evolving field of artificial intelligence.",
    
    "Web development is a dynamic field that encompasses creating websites and web applications. Python, with frameworks like Django and Flask, offers a powerful and efficient way to build web applications. Django, a high-level web framework, follows the 'Don't Repeat Yourself' (DRY) principle, promoting clean and maintainable code. Flask, a micro-framework, provides flexibility and simplicity for smaller projects. Both frameworks use Python's strengths to streamline the development process, allowing developers to focus on building features rather than dealing with low-level details. Whether you're creating a blog, e-commerce site, or a complex web application, Python's web development tools empower developers to bring their ideas to life.",
    
    "Cybersecurity is a critical concern in our interconnected world, and Python plays a significant role in securing digital systems. Python's simplicity and readability make it an ideal language for developing security tools and scripts. Popular frameworks like Scapy and PyCrypto provide essential tools for network analysis and encryption. Python's extensive standard library includes modules for cryptography, ensuring that developers have the necessary tools to implement secure solutions. As cyber threats evolve, Python's adaptability and the strong community of security professionals contribute to its continued prominence in the field of cybersecurity.",
    
    "Data is a powerful asset in today's information-driven world, and Python is a key player in the field of data science. With libraries like NumPy, Pandas, and Matplotlib, Python provides a comprehensive ecosystem for data manipulation, analysis, and visualization. Jupyter Notebooks, an interactive computing environment, further enhances the data science workflow. Python's simplicity and versatility make it accessible for data scientists, statisticians, and researchers to explore and analyze data efficiently. Whether you're working with structured data in a business context or analyzing complex datasets in a research setting, Python's data science capabilities empower users to derive meaningful insights.",
    
    "Automation is the process of using technology to perform tasks without human intervention. Python is a go-to language for automation due to its readability, versatility, and a rich set of libraries. The 'Pythonic' way of writing code encourages clean and concise scripts, making automation projects more manageable. Whether you're automating repetitive tasks, managing server infrastructure, or orchestrating complex workflows, Python's automation capabilities are well-suited for a wide range of applications. As industries embrace digital transformation, the demand for skilled Python developers proficient in automation is on the rise.",
    
    "Game development is a creative and challenging field that combines art and technology to create immersive experiences. Python, with libraries like Pygame, offers a beginner-friendly approach to game development. Pygame provides tools for handling graphics, input, and sound, simplifying the development process for aspiring game developers. While Python may not be the first choice for high-performance game engines, it excels in educational settings and prototyping. The simplicity of Python allows developers to focus on game design and mechanics, making it an excellent choice for those learning the fundamentals of game development.",
    
    "The Internet of Things (IoT) is a network of interconnected devices that communicate and share data. Python, with its lightweight and versatile nature, is well-suited for IoT development. MicroPython, a version of Python optimized for microcontrollers, enables developers to program IoT devices with ease. With libraries like Adafruit CircuitPython and MicroPython libraries for sensors and actuators, Python simplifies the process of building IoT projects. As IoT applications continue to expand in areas such as smart homes, healthcare, and industrial automation, Python's role in enabling rapid and efficient development for connected devices becomes increasingly significant."
]
random.shuffle(paragraph_list)

para_lable = Label(para_frame,text = paragraph_list[0], wraplength= 912,justify= "left",font=('arial',12,'bold'))
para_lable.grid()



# Text aria Start here ------------------
text_aria_frame = Frame(main_frame)
text_aria_frame.grid(row= 2, column= 0)
text_aria = Text(text_aria_frame, font=('arial',12, 'bold'),width=100, height=4,bd=4, 
                 relief= GROOVE,wrap='word',state= DISABLED)#,state= DISABLED
text_aria.grid()

# output frame start here--------------------------
frame_output = Frame(main_frame)
frame_output.grid(row=3,column=0)

elapsed_time_lable = Label(frame_output, text='Elapsed Time',font=('Tahoma',12,'bold'),fg='red')
elapsed_time_lable.grid(row=0,column=0,padx=5)
elapsed_timer = Label(frame_output, text='0',font=('Tahoma',12,'bold'))
elapsed_timer.grid(row=0,column=1,padx=5)

Remain_time_lable = Label(frame_output, text='Remain Time',font=('Tahoma',12,'bold'),fg='red')
Remain_time_lable.grid(row=0,column=2,padx=5)
remain_timer = Label(frame_output, text='60',font=('Tahoma',12,'bold'))
remain_timer.grid(row=0,column=3,padx=5)

wpm_lable = Label(frame_output, text='WPM',font=('Tahoma',12,'bold'),fg='red')
wpm_lable.grid(row=0,column=4,padx=5)
wpm = Label(frame_output, text='0',font=('Tahoma',12,'bold'))
wpm.grid(row=0,column=5,padx=5)

accuracy_labale = Label(frame_output, text='Accuracy',font=('Tahoma',12,'bold'),fg='red')
accuracy_labale.grid(row=0,column=6,padx=5)
total_word_cnt = Label(frame_output, text='0',font=('Tahoma',12,'bold'))
total_word_cnt.grid(row=0,column=7,padx=5)

total_word_lable = Label(frame_output, text='Total Word',font=('Tahoma',12,'bold'),fg='red')
total_word_lable.grid(row=0,column=8,padx=5)
total_word_cnt = Label(frame_output, text='0',font=('Tahoma',12,'bold'))
total_word_cnt.grid(row=0,column=9,padx=5)

wrong_word_lable = Label(frame_output, text='Wrong Word',font=('Tahoma',12,'bold'),fg='red')
wrong_word_lable.grid(row=0,column=10,padx=5)
wrong_word_cnt = Label(frame_output, text='0',font=('Tahoma',12,'bold'))
wrong_word_cnt.grid(row=0,column=11,padx=5)

# button start here -----------------------
button_frame = Frame(main_frame)
button_frame.grid(row=4,column=0)

start_button = ttk.Button(button_frame, text="Start")
start_button.grid(row=0,column=0, padx= 10)

reset_button = ttk.Button(button_frame, text="Reset",state= DISABLED)
reset_button.grid(row=0,column=1, padx= 10)

exit_button = ttk.Button(button_frame, text="Exit")
exit_button.grid(row=0,column=2, padx= 10)

# keyboard frame start here ------------------
keyboard_frame = Frame(main_frame)
keyboard_frame.grid(row= 5, column= 0)

# 0 to 9 keayboard (first row)-----------------
key_1_0 = Frame(keyboard_frame)
key_1_0.grid(row=0,column=0,pady=3)

lable1 = Label(key_1_0, text= '1' ,bg='black',fg='white',font=('arial',10,'bold'),
               width=5, height=2,bd=10,relief=GROOVE)
lable1.grid(row=0,column= 0,padx=3)

lable2 = Label(key_1_0, text= '2' ,bg='black',fg='white',font=('arial',10,'bold'),
               width=5, height=2,bd=10,relief=GROOVE)
lable2.grid(row=0,column= 1,padx=3)

lable3 = Label(key_1_0, text= '3' ,bg='black',fg='white',font=('arial',10,'bold'),
               width=5, height=2,bd=10,relief=GROOVE)
lable3.grid(row=0,column= 2,padx=3)

lable4 = Label(key_1_0, text= '4' ,bg='black',fg='white',font=('arial',10,'bold'),
               width=5, height=2,bd=10,relief=GROOVE)
lable4.grid(row=0,column= 3,padx=3)

lable5 = Label(key_1_0, text= '5' ,bg='black',fg='white',font=('arial',10,'bold'),
               width=5, height=2,bd=10,relief=GROOVE)
lable5.grid(row=0,column= 4,padx=3)

lable6 = Label(key_1_0, text= '6' ,bg='black',fg='white',font=('arial',10,'bold'),
               width=5, height=2,bd=10,relief=GROOVE)
lable6.grid(row=0,column= 5,padx=3)

lable7 = Label(key_1_0, text= '7' ,bg='black',fg='white',font=('arial',10,'bold'),
               width=5, height=2,bd=10,relief=GROOVE)
lable7.grid(row=0,column= 6,padx=3)

lable8 = Label(key_1_0, text= '8' ,bg='black',fg='white',font=('arial',10,'bold'),
               width=5, height=2,bd=10,relief=GROOVE)
lable8.grid(row=0,column= 7,padx=3)

lable9 = Label(key_1_0, text= '9' ,bg='black',fg='white',font=('arial',10,'bold'),
               width=5, height=2,bd=10,relief=GROOVE)
lable9.grid(row=0,column= 8,padx=3)

lable0 = Label(key_1_0, text= '0' ,bg='black',fg='white',font=('arial',10,'bold'),
                width=5, height=2,bd=10,relief=GROOVE)
lable0.grid(row=0,column= 9,padx=3)

# q to p (second row)----------
key_q_p = Frame(keyboard_frame)
key_q_p.grid(row=1,column=0,pady=3)

lable_q = Label(key_q_p,text='Q',bg='black',fg='white',font=('arial',10,'bold'),
                width=5, height=2,bd=10,relief=GROOVE)
lable_q.grid(row=0,column=0,padx=3)

lable_w = Label(key_q_p,text='W',bg='black',fg='white',font=('arial',10,'bold'),
                width=5, height=2,bd=10,relief=GROOVE)
lable_w.grid(row=0,column=1,padx=3)

lable_e = Label(key_q_p,text='E',bg='black',fg='white',font=('arial',10,'bold'),
                width=5, height=2,bd=10,relief=GROOVE)
lable_e.grid(row=0,column=2,padx=3)

lable_r = Label(key_q_p,text='R',bg='black',fg='white',font=('arial',10,'bold'),
                width=5, height=2,bd=10,relief=GROOVE)
lable_r.grid(row=0,column=3,padx=3)

lable_t = Label(key_q_p,text='T',bg='black',fg='white',font=('arial',10,'bold'),
                width=5, height=2,bd=10,relief=GROOVE)
lable_t.grid(row=0,column=4,padx=3)

lable_y = Label(key_q_p,text='Y',bg='black',fg='white',font=('arial',10,'bold'),
                width=5, height=2,bd=10,relief=GROOVE)
lable_y.grid(row=0,column=5,padx=3)

lable_u = Label(key_q_p,text='U',bg='black',fg='white',font=('arial',10,'bold'),
                width=5, height=2,bd=10,relief=GROOVE)
lable_u.grid(row=0,column=6,padx=3)

lable_i = Label(key_q_p,text='I',bg='black',fg='white',font=('arial',10,'bold'),
                width=5, height=2,bd=10,relief=GROOVE)
lable_i.grid(row=0,column=7,padx=3)

lable_o = Label(key_q_p,text='O',bg='black',fg='white',font=('arial',10,'bold'),
                width=5, height=2,bd=10,relief=GROOVE)
lable_o.grid(row=0,column=8,padx=3)

lable_p = Label(key_q_p,text='P',bg='black',fg='white',font=('arial',10,'bold'),
                width=5, height=2,bd=10,relief=GROOVE)
lable_p.grid(row=0,column=9,padx=3)


# a to l (third row)----------
key_a_l = Frame(keyboard_frame)
key_a_l.grid(row=2,column=0,pady=3)

lable_a = Label(key_a_l,text='A',bg='black',fg='white',font=('arial',10,'bold'),
                width=5, height=2,bd=10,relief=GROOVE)
lable_a.grid(row=0,column=0,padx=3)

lable_s = Label(key_a_l,text='S',bg='black',fg='white',font=('arial',10,'bold'),
                width=5, height=2,bd=10,relief=GROOVE)
lable_s.grid(row=0,column=1,padx=3)

lable_d = Label(key_a_l,text='D',bg='black',fg='white',font=('arial',10,'bold'),
                width=5, height=2,bd=10,relief=GROOVE)
lable_d.grid(row=0,column=2,padx=3)

lable_f = Label(key_a_l,text='F',bg='black',fg='white',font=('arial',10,'bold'),
                width=5, height=2,bd=10,relief=GROOVE)
lable_f.grid(row=0,column=3,padx=3)

lable_g = Label(key_a_l,text='G',bg='black',fg='white',font=('arial',10,'bold'),
                width=5, height=2,bd=10,relief=GROOVE)
lable_g.grid(row=0,column=4,padx=3)

lable_h = Label(key_a_l,text='H',bg='black',fg='white',font=('arial',10,'bold'),
                width=5, height=2,bd=10,relief=GROOVE)
lable_h.grid(row=0,column=5,padx=3)

lable_j = Label(key_a_l,text='J',bg='black',fg='white',font=('arial',10,'bold'),
                width=5, height=2,bd=10,relief=GROOVE)
lable_j.grid(row=0,column=6,padx=3)

lable_k = Label(key_a_l,text='K',bg='black',fg='white',font=('arial',10,'bold'),
                width=5, height=2,bd=10,relief=GROOVE)
lable_k.grid(row=0,column=7,padx=3)

lable_l = Label(key_a_l,text='L',bg='black',fg='white',font=('arial',10,'bold'),
                width=5, height=2,bd=10,relief=GROOVE)
lable_l.grid(row=0,column=8,padx=3)



# z to m (fourth row)----------
key_z_m = Frame(keyboard_frame)
key_z_m.grid(row=3,column=0,pady=3)

lable_z = Label(key_z_m,text='Z',bg='black',fg='white',font=('arial',10,'bold'),
                width=5, height=2,bd=10,relief=GROOVE)
lable_z.grid(row=0,column=0,padx=3)

lable_x = Label(key_z_m,text='X',bg='black',fg='white',font=('arial',10,'bold'),
                width=5, height=2,bd=10,relief=GROOVE)
lable_x.grid(row=0,column=1,padx=3)

lable_c = Label(key_z_m,text='C',bg='black',fg='white',font=('arial',10,'bold'),
                width=5, height=2,bd=10,relief=GROOVE)
lable_c.grid(row=0,column=2,padx=3)

lable_v = Label(key_z_m,text='V',bg='black',fg='white',font=('arial',10,'bold'),
                width=5, height=2,bd=10,relief=GROOVE)
lable_v.grid(row=0,column=3,padx=3)

lable_b = Label(key_z_m,text='B',bg='black',fg='white',font=('arial',10,'bold'),
                width=5, height=2,bd=10,relief=GROOVE)
lable_b.grid(row=0,column=4,padx=3)

lable_n = Label(key_z_m,text='N',bg='black',fg='white',font=('arial',10,'bold'),
                width=5, height=2,bd=10,relief=GROOVE)
lable_n.grid(row=0,column=5,padx=3)

lable_m = Label(key_z_m,text='M',bg='black',fg='white',font=('arial',10,'bold'),
                width=5, height=2,bd=10,relief=GROOVE)
lable_m.grid(row=0,column=6,padx=3)

# Space (fifth row) ----------------
space_frame = Frame(keyboard_frame)
space_frame.grid(row=4,column=0,pady=3)

lable_space = Label(space_frame,text='',bg='black',fg='white',font=('arial',10,'bold'),
                width=40, height=2,bd=10,relief=GROOVE)
lable_space.grid(row=0,column=0,padx=3)

lable_numbers = [lable0,lable1,lable2,lable3,lable4,lable5,lable6,lable7,lable8,lable9]
lable_alphabates = [lable_a,lable_b,lable_c,lable_d,lable_e,lable_f,lable_g,lable_h,lable_i,
                    lable_j,lable_k,lable_l,lable_m,lable_n,lable_o,lable_p,lable_q,lable_r,lable_s,
                    lable_t,lable_u,lable_v,lable_w,lable_x,lable_y,lable_z]

number_binding = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
small_alphabate_bindig = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
capital_alphabate_bindig = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for num in range(10):
    root.bind(number_binding[num], lambda event, lable = lable_numbers[num]:change_bg(lable))

for i in range(26):
    root.bind(small_alphabate_bindig[i], lambda event, lable = lable_alphabates[i]:change_bg(lable))
    root.bind(capital_alphabate_bindig[i], lambda event, lable = lable_alphabates[i]:change_bg(lable))
root.bind('<space>', lambda event, lable = lable_space:change_bg(lable))


root.mainloop()