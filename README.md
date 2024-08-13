# 🌐 Azure AI Translator for Arabic

Welcome to the **Azure AI Translator for Arabic** app! This Streamlit application allows you to translate text between English and Arabic using the Microsoft Translator service. It's designed for seamless integration and ease of use, perfect for users needing efficient language translation.

## 🛠 Features

- **Credential Configuration**: Input your Microsoft Translator API credentials through an intuitive sidebar.
- **Language Selection**: Toggle between English and Arabic for both source and target languages.
- **Instant Translation**: Submit your text and receive translations in real-time.

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.8+
- `pip` (Python package installer)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/azure-ai-translator-arabic.git
    cd azure-ai-translator-arabic
    ```

2. **Install Dependencies**:
    ```bash
    pip install streamlit requests uuid
    ```

3. **Run the Application**:
    ```bash
    streamlit run app.py
    ```

## ⚙️ Configuration

Input the following details in the sidebar to configure the translator:

- **Translator Key**: Your unique Microsoft Translator API key.
- **Endpoint**: The API endpoint URL.
- **Location (Region)**: The specific region your API service is located in.

## 📝 Usage

1. **Configure Your API Credentials**: Enter your credentials in the sidebar and press "Process Credentials".
2. **Enter Text**: Input the text you wish to translate in the provided text area.
3. **Select Languages**: Choose the appropriate source and target languages from the dropdown menus.
4. **Translate**: Click on the "Translate" button to view your translated text.

## 🌟 Developer

This application was developed by Shreif Shouman.
