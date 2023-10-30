import pickle
import streamlit as st

# membaca model
water_model = pickle.load(open("water_model.sav", "rb"))

# judul web
st.title("Data Mining Prediksi Air")

# membagi kolom
col1, col2, col3, col4 = st.columns(4)

with col1:
    aluminium = st.text_input("Input nilai Aluminium")
    if aluminium == "":
        st.warning("Inputan tidak boleh kosong!")

with col2:
    ammonia = st.text_input("input nilai Amomonia")
    if ammonia == "":
        st.warning("Inputan tidak boleh kosong!")

with col3:
    arsenic = st.text_input("input nilai Arsenic")
    if arsenic == "":
        st.warning("Inputan tidak boleh kosong!")

with col4:
    barium = st.text_input("input nilai Skin Barium")
    if barium == "":
        st.warning("Inputan tidak boleh kosong!")

with col1:
    cadmium = st.text_input("input nilai Cadmium")
    if cadmium == "":
        st.warning("Inputan tidak boleh kosong!")

with col2:
    chloramine = st.text_input("input Chloramine")
    if chloramine == "":
        st.warning("Inputan tidak boleh kosong!")

with col3:
    chromium = st.text_input("input nilai Chromium")
    if chromium == "":
        st.warning("Inputan tidak boleh kosong!")

with col4:
    copper = st.text_input("input nilai Chopper")
    if copper == "":
        st.warning("Inputan tidak boleh kosong!")

with col1:
    flouride = st.text_input("input nilai Flouride")
    if flouride == "":
        st.warning("Inputan tidak boleh kosong!")

with col2:
    bacteria = st.text_input("input nilai Bacteria")
    if bacteria == "":
        st.warning("Inputan tidak boleh kosong!")

with col3:
    viruses = st.text_input("input nilai Viruses")
    if viruses == "":
        st.warning("Inputan tidak boleh kosong!")

with col4:
    lead = st.text_input("input nilai Lead")
    if lead == "":
        st.warning("Inputan tidak boleh kosong!")

with col1:
    nitrates = st.text_input("input nilai Nitrates")
    if nitrates == "":
        st.warning("Inputan tidak boleh kosong!")

with col2:
    nitrites = st.text_input("input nilai Nitrites")
    if nitrites == "":
        st.warning("Inputan tidak boleh kosong!")

with col3:
    mercury = st.text_input("input nilai Mercury")
    if mercury == "":
        st.warning("Inputan tidak boleh kosong!")

with col4:
    perchlorate = st.text_input("input nilai Perchlorate")
    if perchlorate == "":
        st.warning("Inputan tidak boleh kosong!")

with col1:
    radium = st.text_input("input nilai Radium")
    if radium == "":
        st.warning("Inputan tidak boleh kosong!")

with col2:
    selenium = st.text_input("input nilai Selenium")
    if selenium == "":
        st.warning("Inputan tidak boleh kosong!")

with col3:
    silver = st.text_input("input nilai Silver")
    if silver == "":
        st.warning("Inputan tidak boleh kosong!")

with col4:
    uranium = st.text_input("input nilai Uranium")
    if uranium == "":
        st.warning("Inputan tidak boleh kosong!")

# code untuk prediksi
wq_diagnosis = ""

# membuat tombol untuk prediksi
if st.button("Test Prediksi Kualitas Air"):
    wq_prediction = water_model.predict(
        [
            [
                aluminium,
                ammonia,
                arsenic,
                barium,
                cadmium,
                chloramine,
                chromium,
                copper,
                flouride,
                bacteria,
                viruses,
                lead,
                nitrates,
                nitrites,
                mercury,
                perchlorate,
                radium,
                selenium,
                silver,
                uranium,
            ]
        ]
    )

    if wq_prediction[0] == 1:
        wq_diagnosis = (
            "<span style='color:green;font-size:24px'>Air Aman untuk diminum/span>"
        )
    else:
        wq_diagnosis = "<span style='color: red; font-size: 24px; text-align:center;'>Air tidak Aman untuk diminum</span>"
    st.markdown(wq_diagnosis, unsafe_allow_html=True)
