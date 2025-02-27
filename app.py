import streamlit as st
import secrets
import string
import os

# --- APP CONFIGURATION --- #
st.set_page_config(page_title="Password Generator", page_icon="🔑", layout="centered")
st.title("🔑 Custom Password & Passphrase Generator by ZeeJay 🙅‍♂️")

# Initialize session state
if "pw" not in st.session_state:
    st.session_state["pw"] = ""

# --- PASSWORD GENERATOR FUNCTION --- #
def generate_password(length=14):
    """Generate a secure random password with custom length"""
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))

# --- PASSPHRASE GENERATOR FUNCTIONS --- #
def load_word_list(file_path='words.txt'):
    """Load words from a local file"""
    try:
        with open(file_path, 'r') as f:
            return [word.strip() for word in f.readlines()]
    except FileNotFoundError:
        st.error(f"⚠️ Word list file not found at {os.path.abspath(file_path)}")
        return []

def generate_passphrase(num_words=5):
    """Generate a passphrase from local word list"""
    words = load_word_list()
    if not words:
        return "Error: Could not load word list"
    
    return '-'.join(secrets.choice(words) for _ in range(num_words))

# --- UI CONTROLS --- #
col1, col2 = st.columns(2)

with col1:
    st.subheader("Password Settings")
    pw_length = st.slider(
        "Select password length:",
        min_value=8,
        max_value=30,
        value=14,
        help="Recommended minimum is 12 characters"
    )
    if st.button("🔐 Generate Password", key="pw_button"):
        st.session_state.pw = generate_password(pw_length)

with col2:
    st.subheader("Passphrase Settings")
    num_words = st.slider(
        "Select number of words:",
        min_value=3,
        max_value=8,
        value=5,
        help="Recommended minimum is 4 words"
    )
    if st.button("🔠 Generate Passphrase", key="ps_button"):
        st.session_state.pw = generate_passphrase(num_words)

st.divider()

# --- RESULTS DISPLAY --- #
if st.session_state.pw:
    st.subheader("Generated Result:")
    st.code(st.session_state.pw, language="text")

# --- INSTRUCTIONS & SECURITY TIPS --- #
st.divider()
st.markdown("""
### Security Recommendations:
- 🔐 **Passwords**: Use at least 12 characters with mix of letters and numbers
- 🔠 **Passphrases**: Use at least 4 random words (5-6 recommended)
- 🔄 Combine both strategies for maximum security

### How to Use:
1. For passwords: Adjust length slider → Click Generate Password
2. For passphrases: Adjust word count slider → Click Generate Passphrase
3. Copy the generated result using the copy button in the code block
            
""")