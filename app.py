import streamlit as st
st.title ("DO YOU EVER FEEL LIKE A PLASTIC BAG")
st.header("la mejor cancion de Katty Perry")
from PIL import Image
image=Image.open("katty.jpg")
st.image(image,caption="WOOOOOO")
texto=st.text_input("Ingresa Texto","Texto Inicial")
st.write("El texto que haz escrito", texto)
if st.button("presiona el boton"):
  st.write("haz presionado")
