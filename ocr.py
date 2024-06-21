import easyocr as ocr  # OCR
import streamlit as st  # Web App
from PIL import Image  # Image Processing
import numpy as np  # Image Processing

import streamlit as st

st.markdown(
    """
    <style>
        div[data-testid="column"]:nth-of-type(3)
        {
            text-align: end;
        } 
    </style>
    """, unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    # Header
    st.subheader("`Massive Project`")

with col3:
    # Header
    st.subheader(":red[IMGS]:grey[can]")


# Title
st.title("Image to Text")
st.header("Optical Character Recognition")

# image uploader
image = st.file_uploader(label="",
                         type=['png', 'jpg', 'jpeg'])


@st.cache_resource
def load_model():
    reader = ocr.Reader(['en'], model_storage_directory='.')
    return reader


reader = load_model()  # load model

if image is not None:

    input_image = Image.open(image)  # read image
    st.image(input_image)  # display image

    with st.spinner("🤖 AI is at Work! "):

        result = reader.readtext(np.array(input_image))

        result_text = []  # empty list for results

        for text in result:
            result_text.append(text[1])

        # Menggabungkan semua elemen dalam result_text menjadi satu string, dipisahkan oleh spasi
        paragraph = ' '.join(result_text)

        # Menampilkan hasil sebagai kalimat atau paragraf
        st.write(paragraph)

        st.write(result_text)

    # st.success("Here you go!")
    st.balloons()
else:
    st.write("Upload Your Image")

st.divider()

# Footer
st.caption(
    "Made with ❤️ by K15 :green[ | Jundi Muhammad Al Fatih | Fatah Muyassar Salim | Adelia Yuli Santika | Eka Bulandary | ]")
