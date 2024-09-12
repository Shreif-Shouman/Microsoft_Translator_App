import streamlit as st
import requests, uuid


custom_html = """
            <div style="text-align: center;">
                <div style="display: inline-block; overflow: hidden; height: auto; width: 50%; max-width: 300px; background-color: #f0f0f0; border-radius: 20px; border: 1px solid gray; margin-bottom: 20px;">
                    <img src="https://raw.githubusercontent.com/Shreif-Shouman/Mistral-VDB-Chat/main/banner.jpg" style="width: 100%; height: auto; object-fit: contain; border-radius: 20px;">
                </div>
                <h1 style="text-align: center; font-size: 28px; font-weight: bold; color: #333;">Azure AI Arabic Translator</h1>
                <p style='text-align: center; font-size: small; color: gray;'>Powered by © Microsoft Translator Service.</p>
            </div>
            """
st.markdown(custom_html, unsafe_allow_html=True)


st.sidebar.title("Microsoft Translator")
translator_key = st.sidebar.text_input("Translator Key")
endpoint = st.sidebar.text_input("Endpoint")
location = st.sidebar.text_input("Location (Region)")

if st.sidebar.button("Process Credentials"):
    if translator_key and endpoint and location:
        st.sidebar.success("Configuration looks good!")
    else:
        st.sidebar.warning("Please fill in all configuration fields.")
st.sidebar.markdown("""
## About This App

Welcome to the Text Translator app!\n\nThis tool leverages the power of **Azure AI Translation Service** to provide instant translations between English and Arabic.\n\nSimply enter your text, select the source and target languages, and get your translation in seconds.\n\n**Developed by the Innovation Team\nDeveloper: Shreif Shouman**
""")



if translator_key and endpoint and location:
    text_to_translate = st.text_area("Enter text to translate:")
    
    source_language = st.selectbox("Select source language:", ["en", "ar"])
    target_language = st.selectbox("Select target language:", ["ar", "en"])

    if st.button("Translate"):
        path = '/translate'
        constructed_url = endpoint + path

        params = {
            'api-version': '3.0',
            'from': source_language,
            'to': [target_language]
        }

        headers = {
            'Ocp-Apim-Subscription-Key': translator_key,
            'Ocp-Apim-Subscription-Region': location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        body = [{
            'text': text_to_translate
        }]

        try:
            request = requests.post(constructed_url, params=params, headers=headers, json=body)
            response = request.json()

            if "error" in response:
                st.error(f"Error: {response['error']['message']}")
            else:
                translated_text = response[0]['translations'][0]['text']
                if target_language == 'ar':
                    st.markdown(f"<div dir='rtl'>{translated_text}</div>", unsafe_allow_html=True)
                else:
                    st.write(translated_text)

        except Exception as e:
            st.error(f"Translation failed: {e}")

else:
    st.warning("Please configure the translator in the sidebar first.")
