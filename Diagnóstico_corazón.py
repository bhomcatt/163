from tkinter import *
root = Tk()
root.title("Diagnóstico_corazón")
root.geometry("600x600")
root.configure(background="salmon")

question1_radioButton=StringVar(value="0")

Question1=Label(root, text ="¿Experimentas dificultad para respirar durante tus actividades cotidianas?", bg = "salmon",fg= "white")
Question1.place(relx=0.5 ,rely=0.2 ,anchor= CENTER )
question1_r1=Radiobutton(root, text = "sí", variable=question1_radioButton, value="sí",bg ="salmon")
question1_r1.place(relx=0.5 ,rely=0.25 ,anchor= CENTER )
question1_r2=Radiobutton(root, text = "no", variable=question1_radioButton, value="no",bg ="salmon")
question1_r2.place(relx=0.5 ,rely=0.3 ,anchor= CENTER )

question2_radioButton=StringVar(value="0")
Question2=Label(root, text ="¿Presenta hinchazón en los pies/tobillos/piernas (los zapatos te aprietan) o en el abdomen?",bg ="salmon",fg= "white")
Question2.place(relx=0.5 ,rely=0.35 ,anchor= CENTER )
question2_r1=Radiobutton(root, text = "sí", variable=question2_radioButton, value="sí",bg ="salmon")
question2_r1.place(relx=0.5 ,rely=0.4 ,anchor= CENTER )
question2_r2=Radiobutton(root, text = "no", variable=question2_radioButton, value="no",bg ="salmon")
question2_r2.place(relx=0.5 ,rely=0.45 ,anchor= CENTER )

question3_radioButton=StringVar(value="0")
Question3=Label(root, text ="¿Presentas alguno de estos síntomas: confusión, desorientación o pérdida de memoria?",bg ="salmon",fg="white")
Question3.place(relx=0.5 ,rely=0.5 ,anchor= CENTER )
question3_r1=Radiobutton(root, text = "sí", variable=question3_radioButton, value="sí",bg ="salmon")
question3_r1.place(relx=0.5 ,rely=0.55 ,anchor= CENTER )
question3_r2=Radiobutton(root, text = "no", variable=question3_radioButton, value="no",bg ="salmon")
question3_r2.place(relx=0.5 ,rely=0.60 ,anchor= CENTER )


question4_radioButton=StringVar(value="0")
Question4=Label(root, text ="¿Sientes que te falta el aire cuando estás en reposo o acostado?",bg ="salmon",fg= "white")
Question4.place(relx=0.5 ,rely=0.65 ,anchor= CENTER )
question4_r1=Radiobutton(root, text = "sí", variable=question4_radioButton, value="sí",bg ="salmon")
question4_r1.place(relx=0.5 ,rely=0.70 ,anchor= CENTER )
question4_r2=Radiobutton(root, text = "no", variable=question4_radioButton, value="no",bg ="salmon")
question4_r2.place(relx=0.5 ,rely=0.75,anchor= CENTER )

question5_radioButton=StringVar(value="0")
Question5=Label(root, text ="¿Experimentas un silbido o una tos persistente que produce una mucosidad blanca o rosada teñida de sangre?",bg ="salmon",fg= "white")
Question5.place(relx=0.5 ,rely=0.80,anchor= CENTER )
question5_r1=Radiobutton(root, text = "sí", variable=question5_radioButton, value="sí",bg ="salmon")
question5_r1.place(relx=0.5 ,rely=0.85 ,anchor= CENTER )
question5_r2=Radiobutton(root, text = "no", variable=question5_radioButton, value="no",bg ="salmon")
question5_r2.place(relx=0.5 ,rely=0.90 ,anchor= CENTER )

def heart_diagnostic_score():
    score = 0
    if question1_radioButton.get()=="sí":
        score = score+10
        print(score)
    if question2_radioButton.get()=="sí":
        score = score+10
        print(score)
    if question3_radioButton.get()=="sí":
        score = score+10
        print(score)
    if question4_radioButton.get()=="sí":
        score = score+10
        print(score)
    if question5_radioButton.get()=="sí":
        score = score+10
        print(score)
        
    if score <= 10:
        messagebox.showinfo("Reporte","No es necesario que veas a un médico.")
    elif  score > 10 and score <= 30: 
        messagebox.showinfo("Reporte","Es posible que necesites ver a un médico.")
    else :
        messagebox.showinfo("Reporte","Se recomienda visitar a un médico.")
        
btn = Button(root, text= "Haz clic aquí", command= heart_diagnostic_score)
btn.place(relx=0.5 ,rely=0.95 ,anchor= CENTER )

root.mainloop()