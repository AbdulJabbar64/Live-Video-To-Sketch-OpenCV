import cv2
import numpy as np
import streamlit as st

def sketch(image):

    height=int(image.shape[0])
    width=int(image.shape[1])
    dim=(width,height)

    resize=cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
    kernel=np.array([[-1,-1,-1], [-1, 9,-1],[-1,-1,-1]])

    sharp=cv2.filter2D(resize,-1,kernel)
    gray=cv2.cvtColor(sharp,cv2.COLOR_BGR2GRAY)

    inv=255-gray
    blur=cv2.GaussianBlur(src=inv,ksize=(15,15),sigmaX=0,sigmaY=0)

    s=cv2.divide(gray,255-blur,scale=256)
    return s


st.title("Live Video to Sketch")
left, right = st.columns(2)
run = left.button("Open Camera")
run1 = right.button("Close Camera")
real = left.image([])
SketckCam = right.image([])
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
left.write("This Real Video")
right.write("This Sketch Video")
while run:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    real.image(frame)
    SketckCam.image(sketch(frame))

    if run1:
        camera.release()
        camera.destroyAllWindows()
        st.write("Have you Checked Your Sketch")
        break
