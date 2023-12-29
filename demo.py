import streamlit as st
st.set_page_config(page_title='cats')
st.markdown("Types of cats")
col1,col2=st.columns(2)
with col1:
  st.write("persian Cat")
  st.image("./kitty.jpg",caption="Persian Cat",width=300,use_column_width=True))
  st.write("persian cat is cute")
with col2:
  st.write("white Cat")
  st.image("./white cat.jpg",caption="White kitten",width=300,use_column_width=True)
  st.write("white cats are white")
                   
