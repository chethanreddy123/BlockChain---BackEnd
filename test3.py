import streamlit as st
import time

st.set_page_config(layout="wide")
st.title('Logging in Text Box')

# creating a placeholder for the fixed sized textbox
logtxtbox = st.empty()
logtxt = 'start'
logtxtbox.text_area("Logging: ",logtxt, height = 500)

end_of_loop = False
counter = 1

while (end_of_loop==False):

    logtxt += 'Counter [' + str(counter) + '] \n'
    logtxtbox.text_area("Logging: ", logtxt, height=500)

    counter += 1
    if (counter > 10):
        end_of_loop = True

    time.sleep(0.2)