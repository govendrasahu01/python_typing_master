import threading
from tkinter import *
import random
import ttkthemes
from tkinter import ttk
from time import sleep

def change_bg(widget):
    widget.config(bg='Blue')
    widget.after(100,lambda:widget.config(bg='black'))

total_time = 60
time = 0
wrong_words = 0
elapsed_time_in_minut = 0

def start_timer():
    start_button.config(state=DISABLED)
    global time
    text_aria.config(state= NORMAL)
    text_aria.focus()

    # elaps timer increasing and remain time decreasing
    for time in range(1,total_time+1):
        elapsed_timer.config(text=time)
        remain_timer.config(text= total_time-time)
        sleep(1)
        root.update()
    text_aria.config(state= DISABLED)
    reset_button.config(state=NORMAL)

def count():
    global wrong_words
    global elapsed_time_in_minut 

    while time != total_time:
        entered_data = text_aria.get(1.0,END).split()
        total_words = len(entered_data)

    total_word_cnt.config(text=total_words)

    given_data = para_lable['text'].split()
    for pair in list(zip(entered_data,given_data)):
        if pair[0] != pair[1]:
            wrong_words +=1

    wrong_word_cnt.config(text= wrong_words)
    elapsed_time_in_minut = time/60
    wpm = (total_words - wrong_words)/elapsed_time_in_minut
    wpm_cnt.config(text= wpm)

    gross_wpm =(total_words/elapsed_time_in_minut)
    accuracy = round(wpm/gross_wpm * 100)
    accuracy_cnt.config(text=str(accuracy)+'%')

def start():
    t1 = threading.Thread(target=start_timer)
    t1.start()

    t2 = threading.Thread(target=count)
    t2.start()

def reset():
    global time
    global elapsed_time_in_minut
    global wrong_words 

    start_button.config(state=NORMAL)
    reset_button.config(state=DISABLED)
    text_aria.config(state=NORMAL)
    text_aria.delete(1.0,END)
    text_aria.config(state=DISABLED)

    para_lable.config(text=paragraph_list[random.randint(0,len(paragraph_list)-1)])
    elapsed_timer.config(text='0')
    remain_timer.config(text=0)
    wpm_cnt.config(text=0)
    accuracy_cnt.config(text= 0)
    total_word_cnt.config(text=0)
    wrong_word_cnt.config(text=0)
    time = 0
    elapsed_time_in_minut = 0
    wrong_words = 0

# =============================================================================
root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')

root.geometry('940x735+200+10')
root.resizable(0,0)
root.overrideredirect(True)

main_frame = Frame(root,bd=4) # width='50', height='30',bg='orange'
main_frame.grid()

# first Frame in the main frame ------------
title_frame = Frame(main_frame,bg='orange')
title_frame.grid()
title_lable = Label(title_frame, text="Typing Master",font=('roboto', 20, 'bold'),bg='goldenrod3',fg='white',
                    width=54,bd=10)
title_lable.grid(pady=5)

# paragraph frame start here ---------------------
para_frame = Frame(main_frame)
para_frame.grid(row=1, column=0)

paragraph_list = [
    "As the sun dips below the horizon, casting a warm glow on the distant mountains, the tranquil valley undergoes a breathtaking transformation. The symphony of nature crescendos as birds return to their nests, their melodic calls blending with the rustle of leaves. Day gracefully yields to night, and the world, bathed in twilight hues, surrenders to a serene quietude. The fading sunlight paints a portrait of tranquility, inviting reflection on the beauty of endings and the promise of new beginnings in the canvas of the evening sky.",
    
    "In the ever-evolving landscape of technology, artificial intelligence stands as a beacon of innovation. From virtual assistants streamlining daily tasks to self-driving cars navigating intricate urban landscapes, AI's influence is pervasive. Algorithms, constantly refined, unlock new frontiers of machine learning. As machines become more adept at understanding human behavior and context, the possibilities for advancement seem limitless. The evolving symbiosis between human ingenuity and artificial intelligence heralds a future where technological breakthroughs reshape the fabric of our lives.",
    
    "Spring unfurls its magic, coaxing life back into the dormant earth. Delicate blossoms adorn trees like jewels, and the air carries the sweet perfume of blooming flowers. A palette of vibrant colors emerges, painting the landscape in hues of pink, yellow, and green. The renewal of nature is a symphony of sights and scents, a testament to the cyclical rhythm of life. Each petal, each leaf, whispers the promise of growth and rejuvenation as the world awakens from the winter slumber.",
    
    "Embarking on the cosmic journey, humanity's exploration of space has transcended the limits of our terrestrial abode. Space agencies launch missions to distant planets, rovers traverse alien landscapes, and telescopes capture the breathtaking beauty of distant galaxies. The mysteries of the universe unfold, unveiling celestial wonders that spark wonder and curiosity. From the intricacies of black holes to the discovery of exoplanets, our quest for knowledge propels us into the cosmic frontier, where the vastness of space beckons us to explore the unknown.",
    
    "Diversity, the tapestry of human existence, weaves together the threads of cultures, beliefs, and experiences. Embracing this rich mosaic fosters unity amid differences. In understanding and appreciating diversity, society becomes a harmonious blend of perspectives. It is through the celebration of uniqueness that the human spirit flourishes. The symphony of voices, each contributing its distinct note, creates a melody of inclusivity. In a world where diversity is honored, individuals find strength in their differences, forming a resilient and interconnected global community.",
    
    "Culinary exploration is a gastronomic journey that transcends borders. From the aromatic spices of Indian cuisine to the delicate flavors of Japanese sushi, each dish tells a tale of tradition and innovation. Culinary artistry is a celebration of diversity, a fusion of ingredients that captivates the palate. Exploring global flavors not only satiates hunger but also serves as a passport to cultural understanding. It is in the shared experience of savoring a meal that people connect, transcending linguistic barriers and forging bonds through the universal language of food.",
    
    "Raindrops cascade from the heavens, tapping on windowpanes like a gentle melody. The rhythmic percussion of rain creates a soothing ambiance, a lullaby for the Earth. Droplets cling to leaves and flowers, transforming the world into a glistening spectacle. The air is cool and crisp, carrying the scent of damp earth. It's a symphony of senses, where sight, sound, and smell converge. Rainy days offer a reprieve, inviting introspection and tranquility amid the rhythmic dance of water droplets on nature's stage.",
    
    "Education, the cornerstone of progress, empowers individuals to shape their destinies. The pursuit of knowledge opens doors to a world of possibilities. From classrooms to virtual learning platforms, education is the catalyst for personal and societal transformation. It equips minds with the tools to navigate the complexities of life, fostering critical thinking and creativity. As the beacon of enlightenment, education illuminates the path to a brighter future, where informed minds contribute to a global society marked by understanding, collaboration, and the pursuit of excellence.",
    
    "In the digital age's fast-paced landscape, cybersecurity emerges as the guardian of the virtual realm. With the increasing reliance on technology, protecting sensitive information becomes paramount. Cybersecurity measures, from firewalls to encryption, stand as bulwarks against malicious intent. Safeguarding personal data, financial information, and critical infrastructure ensures the integrity of digital interactions. As technology evolves, the cybersecurity frontier expands, requiring constant vigilance to defend against cyber threats. It is through the fortification of digital landscapes that a secure and resilient digital future is forged.",
    
    "Art, a timeless expression of human creativity, transcends the boundaries of time and culture. From classical masterpieces that adorn museum walls to contemporary installations that challenge societal norms, art is a mirror reflecting the human experience. It evokes emotion, prompts introspection, and fosters connection. In the strokes of a painting, the notes of a melody, or the lines of a sculpture, the artist communicates a narrative that transcends language. The appreciation of art is a journey of exploration, where each encounter broadens one's perspective and enriches the tapestry of human expression."
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
wpm_cnt = Label(frame_output, text='0',font=('Tahoma',12,'bold'))
wpm_cnt.grid(row=0,column=5,padx=5)

accuracy_labale = Label(frame_output, text='Accuracy',font=('Tahoma',12,'bold'),fg='red')
accuracy_labale.grid(row=0,column=6,padx=5)
accuracy_cnt = Label(frame_output, text='0',font=('Tahoma',12,'bold'))
accuracy_cnt.grid(row=0,column=7,padx=5)

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

start_button = ttk.Button(button_frame, text="Start",command=start)
start_button.grid(row=0,column=0, padx= 10)

reset_button = ttk.Button(button_frame, text="Reset",state= DISABLED,command=reset)
reset_button.grid(row=0,column=1, padx= 10)

exit_button = ttk.Button(button_frame, text="Exit",command=root.destroy)
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

lable_space = Label(space_frame,text='Govendra cap01_009',bg='black',fg='white',font=('arial',10,'bold'),
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