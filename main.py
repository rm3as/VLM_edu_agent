import streamlit as st
from PIL import Image

st.title("Image Interaction App")

# upload image
uploaded_file = st.file_uploader('upload image.', type=['jpg', 'png',])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='uploaded image', use_column_width=True)

    # ユーザーの自然言語指示
    instruction = st.text_input('How can I help you?(ex. "Highlight C pass")')
    if st.button('Start analysis.'):
        """
        ここでCLIP呼び出す
        """
        answer = ...
        caption = ...
        st.write(f'Bot:{answer}')
        st.image('output_example.jpeg', caption=caption, use_column_width=True)
        