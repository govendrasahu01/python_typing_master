from tkinter import *
import random
import ttkthemes
from tkinter import ttk

root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')

root.geometry('940x630+200+10')
root.resizable(0,0)

main_frame = Frame(root,bd=4) # width='50', height='30',bg='orange'
main_frame.grid()

# first Frame in the main frame ------------
title_frame = Frame(main_frame,bg='orange')
title_frame.grid()
title_lable = Label(title_frame, text="Typing Master",font=('roboto', 30, 'bold'),bg='goldenrod3',fg='white',
                    width=38,bd=10)
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

para_lable = Label(para_frame,text = paragraph_list[0], wraplength= 912,justify= "left",font=('arial',14))
para_lable.grid()



# Text aria Start here ------------------
text_aria_frame = Frame(main_frame)
text_aria_frame.grid(row= 2, column= 0)
text_aria = Text(text_aria_frame, font=('arial',12, 'bold'),width=100, height=5,bd=4, relief= GROOVE,wrap='word',
                 state= DISABLED)
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

# button start here
button_frame = Frame(main_frame)
button_frame.grid(row=4,column=0)

start_button = ttk.Button(button_frame, text="Start")
start_button.grid(row=0,column=0, padx= 10)

reset_button = ttk.Button(button_frame, text="Reset",state= DISABLED)
reset_button.grid(row=0,column=1, padx= 10)

exit_button = ttk.Button(button_frame, text="Exit")
exit_button.grid(row=0,column=2, padx= 10)



root.mainloop()