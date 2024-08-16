import streamlit as st
from pdf import setPdf
import datetime as dt

form_data = {}
start_date = dt.datetime(1900, 1, 1)
end_date = dt.datetime(2100, 12, 31)

title_cols = st.columns([1, 2, 1])
with title_cols[1]:
    st.title("Thawani Airlines")
# Create 5 columns
cols = st.columns(4)

# Place an input in each column
with cols[0]:
    form_data["Departure City"] = st.text_input(label="", placeholder="Departure City")
with cols[1]:
    form_data["Arrival City"] = st.text_input(label="", placeholder="Arrival City")
with cols[2]:
    form_data["Departure Date"] = st.date_input(label="Departure Date", min_value=start_date, max_value=end_date)
# with cols[3]:
#     st.text_input(label="", placeholder="Add return", key="return")
with cols[3]:
    form_data["Seating Class"] = st.selectbox(label="", options=("Economy", "Premium Economy", "Business"))
    # st.text_input(label="", placeholder="Travellers & Cabin Class", key="5")

radio_col = st.columns(4)
with radio_col[0]:
    st.markdown("""
                    <style>
                    .big-font {
                        font-size:38px !important;
                    }
                    </style>
                    """, unsafe_allow_html=True)
    st.markdown('<p class="big-font">Special Fares</p>', unsafe_allow_html=True)
    # st.write("Special Fares(optional)")

with radio_col[1]:
    form_data["Special Status"] = st.radio("", ("Armed Forces", "Student", "Senior Citizen", "Friends & Family", "None"))
with radio_col[2]:
    st.markdown("""
                        <style>
                        .big-font {
                            font-size:36px !important;
                        }
                        </style>
                        """, unsafe_allow_html=True)
    st.markdown('<p class="big-font">Seat <br> Preference</p>', unsafe_allow_html=True)
    # st.write("Special Fares(optional)")
with radio_col[3]:
    form_data["Seat Preference"] = st.radio("", ("Window", "Aisle", "No preference"))

personal_info = st.columns(5)

# Place an input in each column
with personal_info[0]:
    form_data["First name"] = st.text_input(label="", placeholder="First Name")
with personal_info[1]:
    form_data["Last Name"] = st.text_input(label="", placeholder="Last Name")
with personal_info[2]:
    form_data["Date of Birth"] = st.date_input(label="Date of Birth", min_value=start_date, max_value=end_date)
with personal_info[3]:
    form_data["Phone"] = st.text_input(label="", placeholder="Phone")
with personal_info[4]:
    form_data["Email ID"] = st.text_input(label="", placeholder="Email ID")

final_cols = st.columns([2, 2])
with final_cols[0]:
    form_data["Departure Time"] = st.time_input(label="Departure Time")
with final_cols[1]:
    form_data["Arrival Time"] = st.time_input(label="Arrival Time")

button_cols = st.columns([1, 2, 1])
with button_cols[1]:
    st.markdown("""
            <style>
            div.stButton > button {
                width: 100%;
                height: 50px;
                font-size: 18px;
            }
            </style>
        """, unsafe_allow_html=True)
    buttons = st.button("Book")

    if buttons:
        # st.write("Form data:")
        setPdf(form_data)
        # for key, value in form_data.items():
        #     st.write(f"{key}: {value}")
# st.write('<meta http-equiv="refresh" content="0">', unsafe_allow_html=True)