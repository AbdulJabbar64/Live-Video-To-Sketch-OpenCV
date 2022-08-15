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

st.title("Live Image to Sketch")
#Uploading the dog image
sk_image = st.file_uploader("Choose an image...", type="jpg")
submit = st.button('Make Sketch')
#On predict button click
if submit:
    if sk_image is not None:
        # Convert the file to an opencv image.
        file_bytes = np.asarray(bytearray(sk_image.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        left, right = st.columns(2, gap='large')
        left.write("This Real Video")
        right.write("This Sketch Video")
        # Displaying the image
        left.image(opencv_image, channels="BGR")
        right.image(sketch(opencv_image))
    else:
        st.title("First Upload the Image")
