import streamlit as st
import cv2 
import time

def facereco(color_new, minNeighbors, scaleFactor):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') 

    cap = cv2.VideoCapture(0)

    frame_placeholder= st.empty() 
    while True: 
        ret, frame = cap.read() 

        if not ret:
            st.write("fales to detect frame") 
            break


        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
            
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor, minNeighbors)

        for (x, y, w, h) in faces:
             cv2.rectangle(frame, (x,y), (x+w, y+h), color_new, 2) 

        rgb_frame =cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 

        if len (faces) > 0:
            cv2.imwrite("detectedfaces.png") 
            time.sleep(1) 

        frame_placeholder.image(rgb_frame, channels="RGB", use_container_width=True)

        if cv2.waitKey(1) | 0xFF == ord('q'):
            break

    cap.release() 




def main():
    st.title("Face Recognition")
    st.text("instruction: ensure that your physical privacy cover is enabled, click on detect face button to relaunch the application" ) 
    color = st.color_picker('choose a color', "#06CE56")

    #rouge = int(color[1:3], 16)
    #vert = int(color[3:5], 16)
    #bleu = int([5:2], 16)
    #color_tuple = (bleu, vert, rouge)"""
    color_new = tuple(int(color[i:i+2],16) for i in (5,3,1))
    minNeighbors = st.slider("select minimum neighbors", min_value=0, max_value=10, step=1) 
    scaleFactor =st.slider("select scaleFactor;",min_value=1.0,max_value=2.0, step=0.1, value=1.3)
    if st.button('Detect Face'):
        facereco(color_new, minNeighbors, scaleFactor)



if __name__=="__main__":
    main()
    
