#!/usr/bin/python
# -*- coding: utf-8 -*-


import numpy as np
import sys
if "Tkinter" not in sys.modules:
    from tkinter import *
from tkinter import *
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename
import cv2
import os
import tkinter as tk
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import imutils
import pickle
import time
import subprocess
from subprocess import Popen
import argparse


from subprocess import Popen,PIPE,STDOUT,call





ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", type=str,
	help="path to output video")
ap.add_argument("-y", "--display", type=int, default=1,
	help="whether or not to display output frame to screen")
args = vars(ap.parse_args())



#data = pickle.loads(open('C:\\Python_CV\\Python37\\FACE_RECOGNITION_PROJECTS\\In a Live VideoPicture\\face-recognition-opencv\\encodings.pickle', "rb").read())




class Test():

    def __init__(self):
        
        self.root = Tk()
        self.root.title('Lisecnce Plate Vision System')
        self.root.geometry('850x567+0+0')
        #self.root.attributes("-fullscreen", True)



        def Camera():
            vid = askopenfilename(initialdir="C:/",filetypes =(("Video File", "*.mp4"),("All Files","*.*")),title = "Choose a file.")
            stream = cv2.VideoCapture(vid)
            writer = None
            while True:
                (grabbed, frame) = stream.read()
                if not grabbed:
                    break
                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                rgb = imutils.resize(frame, width=750)
                r = frame.shape[1] / float(rgb.shape[1])

                boxes = face_recognition.face_locations(rgb,model='hog')
                encodings = face_recognition.face_encodings(rgb, boxes)
                names = []

                for encoding in encodings:
                    matches = face_recognition.compare_faces(data["encodings"],encoding)
                    name = "Unknown"
                    if True in matches:
                        matchedIndxs = [i for (i, b) in enumerate(matches) if b]
                        counts = {}
                        for i in matchedIndxs:
                            name = data["names"][i]
                            counts[name] = counts.get(name, 0) + 1

                        name = max(counts, key=counts.get)
                        
                    names.append(name)


                for ((top, right, bottom, left), name) in zip(boxes, names):
                    top = int(top * r)
                    right = int(right * r)
                    bottom = int(bottom * r)
                    left = int(left * r)

                    cv2.rectangle(frame, (left, top), (right, bottom),(0, 255, 0), 2)
                    y = top - 15 if top - 15 > 15 else top + 15
                    cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,0.75, (0, 255, 0), 2)

                if writer is None and args["output"] is not None:
                    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
                    writer = cv2.VideoWriter(args["output"], fourcc, 24,(frame.shape[1], frame.shape[0]), True)

                
                if writer is not None:
                    writer.write(frame)

                if args["display"] > 0:
                    cv2.imshow("Press Q to Quit Window", frame)
                    key = cv2.waitKey(1) & 0xFF

                    if key == ord("q"):
                        cv2.destroyAllWindows()
                        break
                    

            stream.release()
            
            if writer is not None:
                writer.release()   

            
        def select_image():

            name = askopenfilename(initialdir="C:/Work_CV/Office_Codes/spectrum/",filetypes =(("Image File", "*.jpg"),("All Files","*.*")),title = "Choose a file.")



            image = cv2.imread(name)

            print(name)
            top0 = tk.Toplevel()
            top0.title("Number Plate Extracted")
            top0.geometry("300x150+440+200")
            small = Canvas(top0, bg="white", height=150, width=300)
            small.pack()

            
            small.create_text(52,12, text="Plates Database", font=('Times New Roman', '20', 'bold italic'), fill="black", anchor='nw')





            



            apna = "alpr "+name+ " --c pk -n 1"

            proc=Popen(apna, stdout=PIPE, shell=True)
            output=proc.communicate()[0]
            b = (str(output))


            plate= (b[29:35])

            
            plate = (plate.replace("\\",""))

            print(plate)


            small.create_text(90,60, text=plate, font=('Times New Roman', '28', 'bold underline'), fill="black", anchor='nw')

            

            
        def about():
            top = tk.Toplevel()
            top.title("Guidance For Execution")
            top.geometry("400x200+180+200")
            t_lbl = tk.Label(top, text="\n\n1. Select the Image and wait for process...")
            t_lbl.pack()


            t_lbl2 = tk.Label(top, text="\n\n2. Select the Video and wait for process...")
            t_lbl2.pack()


            t_lbl3 = tk.Label(top, text="\n\n3. For Real TIme Video Connect Webcam ...")
            t_lbl3.pack()


        def live_cam():
            vs = VideoStream(src=0).start()
            writer = None
            time.sleep(2.0)
            while True:
                frame = vs.read()
                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                rgb = imutils.resize(frame, width=750)
                r = frame.shape[1] / float(rgb.shape[1])
                boxes = face_recognition.face_locations(rgb,model='hog')
                encodings = face_recognition.face_encodings(rgb, boxes)
                names = []
                for encoding in encodings:
                    matches = face_recognition.compare_faces(data["encodings"],encoding)
                    name = "Unknown"
                    if True in matches:
                        matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                        counts = {}
                        for i in matchedIdxs:
                            name = data["names"][i]
                            counts[name] = counts.get(name, 0) + 1
                        name = max(counts, key=counts.get)
                    names.append(name)
                for ((top, right, bottom, left), name) in zip(boxes, names):
                    top = int(top * r)
                    right = int(right * r)
                    bottom = int(bottom * r)
                    left = int(left * r)
                    cv2.rectangle(frame, (left, top), (right, bottom),(0, 255, 0), 2)
                    y = top - 15 if top - 15 > 15 else top + 15
                    cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,0.75, (0, 255, 0), 2)
                if writer is None and args["output"] is not None:
                    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
                    writer = cv2.VideoWriter(args["output"], fourcc, 20,(frame.shape[1], frame.shape[0]), True)


                if writer is not None:
                    writer.write(frame)

                if args["display"] > 0:
                    cv2.imshow("Press Q to Quit Window", frame)
                    key = cv2.waitKey(1) & 0xFF
                    if key == ord("q"):
                        cv2.destroyAllWindows()
                        break
            vs.stop()
            cv2.destroyAllWindows()
            
            if writer is not None:
                writer.release()   

        C = Canvas(self.root, bg="blue", height=850, width=567)
        filename = PhotoImage(file = "C:\\Work_CV\\Office_Codes\\spectrum\\back.png")
        C.create_image(0, 0, image=filename, anchor='nw')

        

        C.create_text(285,50, text="Lisence Plates Database", font=('Times New Roman', '35', 'bold'), fill="white")
        C.pack(fill=BOTH, expand=1)




        button1 = Button(C, text = "Saved Execute", font=('Times', '14', 'bold italic'), borderwidth=4, highlightthickness=4, highlightcolor="#37d3ff", highlightbackground="#37d3ff",relief=RAISED,command=Camera)
        button1.configure(width=15, activebackground = "#33B5E5")
        button1.place(x=180, y=100)


        button2 = Button(C, text = "Image Analysis", font=('Times', '14', 'bold italic'), borderwidth=4, highlightthickness=4, highlightcolor="#37d3ff", highlightbackground="#37d3ff",relief=RAISED, command =select_image)
        button2.configure(width=15, activebackground = "#33B5E5")
        button2.place(x=180, y=180)
        

        button3 = Button(C, text = "Webcam Video", font=('Times', '14', 'bold italic'),borderwidth=4, highlightthickness=4, highlightcolor="#37d3ff", highlightbackground="#37d3ff",relief=RAISED, command =live_cam)
        button3.configure(width=15, activebackground = "#33B5E5")
        button3.place(x=180, y=260)


        button4 = Button(C, text = "App Details", font=('Times', '14', 'bold italic'), borderwidth=4, highlightthickness=4, highlightcolor="#37d3ff", highlightbackground="#37d3ff",relief=RAISED, command =about)
        button4.configure(width=15, activebackground = "#33B5E5")
        button4.place(x=180, y=340)

        button5 = Button(C, text = "Closing All", font=('Times', '14', 'bold italic'), borderwidth=4, highlightthickness=4, highlightcolor="#37d3ff", highlightbackground="#37d3ff",relief=RAISED, command=self.quit)
        button5.configure(width=15, activebackground = "#33B5E5")
        button5.place(x=180, y=420)





        

##
##        self.about = Button(C, text="Saved Video Execution", width="30",font=('Helvetica', '12', 'italic'), command=Camera)
##        self.about.pack(padx=5, pady=40)
##
##        self.about_1 = Button(C, text="Image Analysis", width="30", font=('Helvetica', '12', 'italic'), command=select_image)
##        self.about_1.pack(padx=5, pady=45)
##
##        self.about = Button(C, text="Live Webcam Video", width="30",font=('Helvetica', '12', 'italic'), command=live_cam)
##        self.about.pack(padx=5, pady=50)
##
##        self.about = Button(C, text="About Application", width="30", font=('Helvetica', '12', 'italic'),command=about)
##        self.about.pack(padx=5, pady=55)
##
##        good = Button(C, text="Closing the Window", width="30",font=('Helvetica', '12', 'italic'), command=self.quit)
##        good.pack(padx=5, pady=60)

        

        
        


        self.root.mainloop()

    def quit(self):
        self.root.destroy()


app = Test()



