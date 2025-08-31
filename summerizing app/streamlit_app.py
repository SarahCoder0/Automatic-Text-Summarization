import streamlit as st

# Must be the first Streamlit command
st.set_page_config(page_title="Text Summarization System", layout="centered")

from transformers import pipeline

# Load summarization model
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_summarizer()

# UI Interface
st.title("📝 Text Summarization App")
st.markdown("Enter a long text to get an AI-powered summary.")

# Text input
text_input = st.text_area("Enter text here:", 
                         height=300, 
                         placeholder="Paste your article or long text here...")

# On button click
if st.button("Summarize"):
    if text_input.strip():
        with st.spinner("Summarizing..."):
            summary = summarizer(text_input, 
                                max_length=150, 
                                min_length=40, 
                                do_sample=False)[0]['summary_text']
        st.success("✅ Summary:")
        st.write(summary)
    else:
        st.warning("Please enter text before summarizing.")