import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('progress_bar')
'start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.02)

'Done!!'

left_colum, right_column = st.columns(2)
button = left_colum.button('output in the right')
if button:
    right_column.write('here is right_column')

expander1 = st.expander('inquiry1')
expander1.write('write inquiry 1')
expander2 = st.expander('inquiry2')
expander2.write('write inquiries 2')
expander3 = st.expander('inquiry3')
expander3.write('write inquiries3')




# text = st.text_input('What is your hobby?')
# condition = st.slider('How are your', 0, 100, 50)
#
# 'Your hobby is', text
# 'condition', condition
#
#
# # if st.checkbox('Show Image'):
#     img = Image.open('02_b.png')
#     st.image(img, caption = 'test_shiesuta', use_column_width=True)

#
# img = Image.open('02_b.png')
# st.image(img, caption = 'test_shiesuta', use_column_width=True)

# #/
# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.85, 139.71],
#     columns = ['lat','lon']
#                 )
# df
#
# #st.table(df.style.highlight_max(axis=0))
# #st.bar_chart(df)
# st.map(df)
# /#