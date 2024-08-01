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

client = Groq()

# initialize the chat history as streamlit session state if not present already
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# load hotel information from the PDF
hotel_info = {
    "name": "Luxury Haven Hotel",
    "address": "123 Beachside Road, Candolim, Goa, India",
    "current weather": "Rainy, trafellers are advised to carry raincoats and umbrellas",
    "facilities": [
        "Swimming Pool: 7 AM - 10 PM",
        "Gym: 24/7",
        "Spa: 9 AM - 8 PM",
        "Restaurant: Breakfast 7 AM - 10 AM, Lunch 12 PM - 3 PM, Dinner 6 PM - 10 PM",
        "Bar: 5 PM - 12 AM",
        "Conference Rooms: Available upon reservation",
        "Free Wi-Fi",
        "Airport Shuttle Service: Available upon request",
        "Scooty Available upon request at 300-500 INR per day"
        "Laundry Service: 8 AM - 6 PM"
    ],
    "room_types": [
        {"type": "Standard Room", "description": "Cozy room with a queen-sized bed, en-suite bathroom, desk, and flat-screen TV. Amenities include free Wi-Fi, air conditioning, minibar, and complimentary toiletries."},
        {"type": "Deluxe Room", "description": "Additional facilities from Standard Room: King-sized bed, seating area, and coffee maker."},
        {"type": "Suite", "description": "Additional facilities from Standard Room: Separate living area, bathtub, two flat-screen TVs, coffee maker, and bathrobes."},
        {"type": "Family Room", "description": "Additional facilities from Standard Room: Separate area with two twin beds, children's amenities."}
    ],
    "pricing": {
        "Standard Room": {"base_price": 5000, "tax": 900, "total": 5900,},
        "Deluxe Room": {"base_price": 6000, "tax": 1080, "total": 7080},
        "Suite": {"base_price": 7000, "tax": 1260, "total": 8260},
        "Family Room": {"base_price": 8000, "tax": 1440, "total": 9440}
    },
    "location": {
        "description": "Located in the heart of Candolim, Goa, Luxury Haven Hotel offers stunning beach views and easy access to popular attractions.",
        "nearby_attractions": [
            "Candolim Beach: 5-minute walk",
            "Fort Aguada: 10-minute drive",
            "Baga Beach: 15-minute drive",
            "Calangute Beach: 10-minute drive",
            "Anjuna Flea Market: 20-minute drive"
        ],
        "views": "Rooms offer views of the Arabian Sea, lush gardens, or the bustling Candolim street."
    },
    "FAQs": [
        {"question": "What time is check-in and check-out?", "answer": "Check-in is at 3 PM and check-out is at 12 PM."},
        {"question": "Is breakfast included in the room rate?", "answer": "Yes, a complimentary breakfast is included with your stay."},
    ]
}

# streamlit page title
st.title("🏨 Welcome to Luxury Haven Hotel, Goa")

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
        {"role": "system", "content": "You are a helpful hotel receptionist. your name is Alexa and you assist potential guests with qurie and bookings. You have access to hotel facilities, room types, pricing, and availability. Answer queries crisply. After the enwuiries, if user shows interest to book, ask for name, email, number of people, number of rooms before comfirming the booking If a customer asks for discount start from 2.5% and max 7.5%"},
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
