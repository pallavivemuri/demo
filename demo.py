import streamlit as st
st.set_page_config(page_title='cats')
st.markdown("Types of cats")
col1,col2=st.columns(2)
with col1:
  st.write("persian Cat")
  st.image("./kitty.jpg")
  st.write("persian cat is cute")
with col2:
  st.write("white Cat")
  st.image("./white cat.jpg")
  st.write("white cats are white")
                   
