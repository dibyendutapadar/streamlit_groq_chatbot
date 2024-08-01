# 🏨 Hotel Chatbot using groq and streamlit

This project is designed to create an interactive and informative chatbot for the Luxury Haven Hotel using Streamlit and Groq.

## 📋 Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## 🎉 Introduction

The  chatbot is a user-friendly application that helps potential guests inquire about hotel facilities, room types, pricing, availability, and make bookings. The chatbot provides crisp, concise responses and is designed to enhance the user experience.

## 🌟 Features

- Answer queries regarding hotel information including facilities, room types, and pricing.
- Answer frequently asked questions.
- Assist users in making room bookings.
- Maintain chat history for a seamless conversation experience.

## 🛠️ Installation

To get started with the Luxury Haven Hotel chatbot, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone <repo>
    cd hotel-chatbot
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up Streamlit secrets**:
    Create a `.streamlit/secrets.toml` file with the following content:
    ```toml
    [groq]
    api_key = "your_groq_api_key"
    ```

## 🚀 Usage

To run the chatbot application, use the following command:

```bash
streamlit run main.py
