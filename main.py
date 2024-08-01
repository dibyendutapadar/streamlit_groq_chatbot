import os
import json
import streamlit as st
from groq import Groq

# streamlit page configuration
st.set_page_config(
    page_title="Luxury Haven Hotel",
    page_icon="🏨",
    layout="centered"
)

working_dir = os.path.dirname(os.path.abspath(__file__))


# Load configuration and secrets
GROQ_API_KEY = st.secrets["groq"]["api_key"]
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# initialize the chat history as streamlit session state if not present already
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# load hotel information from the PDF
hotel_info = {
    "name": "Luxury Haven Hotel",
    "facilities": [
        "Swimming Pool: 7 AM - 10 PM",
        "Gym: 24/7",
        "Spa: 9 AM - 8 PM",
        "Restaurant: Breakfast 7 AM - 10 AM, Lunch 12 PM - 3 PM, Dinner 6 PM - 10 PM",
        "Bar: 5 PM - 12 AM",
        "Conference Rooms: Available upon reservation",
        "Free Wi-Fi",
        "Airport Shuttle Service: Available upon request",
        "Laundry Service: 8 AM - 6 PM"
    ],
    "room_types": [
        {"type": "Standard Room", "description": "Cozy room with a queen-sized bed, en-suite bathroom, desk, and flat-screen TV. Amenities include free Wi-Fi, air conditioning, minibar, and complimentary toiletries."},
        {"type": "Deluxe Room", "description": "Spacious room with a king-sized bed, en-suite bathroom, seating area, and flat-screen TV. Amenities include free Wi-Fi, air conditioning, minibar, coffee maker, and complimentary toiletries."},
        {"type": "Suite", "description": "Large suite with a separate living area, king-sized bed, en-suite bathroom with a bathtub, and two flat-screen TVs. Amenities include free Wi-Fi, air conditioning, minibar, coffee maker, complimentary toiletries, and bathrobes."},
        {"type": "Family Room", "description": "Room designed for families, includes a king-sized bed and a separate area with two twin beds, en-suite bathroom, and flat-screen TV. Amenities include free Wi-Fi, air conditioning, minibar, coffee maker, complimentary toiletries, and children's amenities."}
    ],
    "pricing": {
        "Standard Room": "$150 - $160",
        "Deluxe Room": "$200 - $210",
        "Suite": "$350 - $360",
        "Family Room": "$250 - $260"
    }
}

# streamlit page title
st.title("🏨 Welcome to Luxury Haven Hotel")

# display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# input field for user's message:
user_prompt = st.chat_input("Ask about rooms, facilities, or make a booking...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # create messages list with hotel context
    messages = [
        {"role": "system", "content": "You are a helpful hotel receptionist. You have access to hotel facilities, room types, pricing, and availability. Answer queries crisply and assist with bookings.Before completing booking make sure you get the name and email id from user"},
        {"role": "system", "content": f"Hotel Information: {hotel_info}"}
    ]
    messages.extend(st.session_state.chat_history)

    # send user's message to the LLM and get a response
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )

    assistant_response = response.choices[0].message.content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    # display the LLM's response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
