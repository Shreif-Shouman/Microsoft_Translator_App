# 🌐 Microsoft Translator App

## Overview

This Streamlit app allows users to translate text between English and Arabic using the Microsoft Translator service. The app provides a simple interface for inputting text, selecting source and target languages, and displaying the translated text.

## ✨ Features

- **📝 Text Translation:** Translate text between English and Arabic.
- **💻 User-Friendly Interface:** Input your Microsoft Translator credentials via the sidebar for easy configuration.
- **⚡ Real-time Translation:** Get instant translations as you input text.

## 📋 Prerequisites

Before running this app, ensure you have the following:

- **🐍 Python 3.x:** Make sure Python is installed on your system.
- **🔑 Microsoft Translator API Key:** Obtain a subscription key from the Azure portal.
- **📦 Streamlit Library:** Install Streamlit using pip.

## 🚀 Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repository/translator-app.git
   cd translator-app
   ```

2. Install the Required Libraries:
Install the necessary Python packages by running:
bash
Copy code
pip install -r requirements.txt
Ensure the requirements.txt file includes:

text
Copy code
streamlit
requests
🔧 Configuration

Microsoft Translator Credentials:
🔑 Translator Key: Your Microsoft Translator API key.
🌐 Endpoint: Your Azure Translator service endpoint.
📍 Location (Region): The region where your Azure service is hosted.
Input Credentials:
Run the app (streamlit run app.py), and enter your Translator Key, Endpoint, and Location in the sidebar.
🏃‍♂️ Running the App

To start the app, navigate to the project directory and run:

bash
Copy code
streamlit run app.py
The app will open in your web browser. Follow the on-screen instructions to enter your credentials and translate text.

💡 Usage

Enter Microsoft Translator Credentials: Input your Translator Key, Endpoint, and Location in the sidebar.
Text Input: Enter the text you want to translate.
Select Languages: Choose the source and target languages.
Get Translation: The translated text will be displayed on the main page.
👨‍💻 Developer

This application was developed by Shreif Shouman.

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgements

Streamlit
Microsoft Translator
