import streamlit as st
import datetime
import pytz

# Page config
st.set_page_config(page_title="NeoFuture Login Console", layout="wide")

# CSS futuristic styling
st.markdown("""
    <style>
    .futuristic {
        font-family: "Lucida Console", Monaco, monospace;
        color: #00FFAA;
        text-shadow: 0 0 10px #00FFAA;
        font-size: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='futuristic'>🕒 " + datetime.datetime.now(pytz.UTC).strftime('%H:%M:%S UTC') + "</div>", unsafe_allow_html=True)

st.title("🚀 Future Login Console")

# Login form
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    st.markdown("<div class='futuristic'>❌ Non registered user</div>", unsafe_allow_html=True)

    with st.expander("Would you like to register at OpenAI.com?"):
        if st.button("🔗 Yes, take me there"):
            st.markdown('<meta http-equiv="refresh" content="0;url=https://openai.com">', unsafe_allow_html=True)
        else:
            st.write("You chose not to register at this time.")

    st.write("---")
    st.markdown("<div class='futuristic'>📺 Streaming YouTube below</div>", unsafe_allow_html=True)

    # Embed YouTube
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # Classic rickroll :)

else:
    st.markdown("<div class='futuristic'>🔒 Please enter your credentials to continue.</div>", unsafe_allow_html=True)
