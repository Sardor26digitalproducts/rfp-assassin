import streamlit as st
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

# 1. CONFIGURE THE BEAST
# Get this from https://aistudio.google.com/app/apikey
# In Streamlit Cloud, go to App Settings -> Secrets and add: GOOGLE_API_KEY = "your_key"
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# 2. MODEL SETUP (Ruthless Config)
generation_config = {
  "temperature": 0.2, # Low temp = precise, compliant answers. High temp = hallucinations.
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 65536, # Huge output for full proposals
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp", # Use Flash for the App (Speed). Use Pro in Studio for analysis.
  generation_config=generation_config,
  # Turn off safety filters that block legitimate business text (e.g. "attack strategy")
  safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    }
)

# 3. THE INTERFACE (Clean & Corporate)
st.set_page_config(page_title="RFP Assassin", layout="wide")
st.title("⚡ RFP Assassin: The Bid Winner")
st.markdown("### Upload the Tender. Win the Contract.")

# Two columns: Inputs vs Outputs
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("1. The Target (Tender)")
    uploaded_file = st.file_uploader("Upload RFP PDF", type=['pdf', 'txt'])
    
    st.subheader("2. The Ammo (Your Company Info)")
    company_context = st.text_area("Paste your 'About Us', Case Studies, or Past Wins here.", height=200)
    
    generate_btn = st.button("🚀 Draft Winning Proposal", type="primary")

with col2:
    st.subheader("3. The Output")
    output_container = st.empty()

# 4. THE LOGIC
if generate_btn and uploaded_file and company_context:
    with st.spinner("Reading 100 pages... Analyzing competitors... Drafting..."):
        try:
            # Process the PDF (Gemini can read files directly in 2.0/1.5)
            # Note: For simplest code, we treat it as a file part.
            file_data = {"mime_type": uploaded_file.type, "data": uploaded_file.getvalue()}

            # The Prompt that sells
            prompt = f"""
            You are a ruthlessly effective Bid Writer. 
            
            **CONTEXT:**
            Here is the RFP (Request for Proposal) document: [Attached]
            Here is the Company Context (Who we are): {company_context}
            
            **TASK:**
            Write a compliant, persuasive Executive Summary and Scope of Work response.
            
            **RULES:**
            1. Use the EXACT terminology found in the RFP.
            2. Map every client requirement to a specific strength in the Company Context.
            3. If the Company Context is missing a requirement, flag it as [RISK: MISSING CAPABILITY].
            4. Structure:
               - Executive Summary (The "Hook")
               - Understanding of Requirements (The "Proof")
               - Proposed Solution (The "How")
               - Why Us (The "Kill")
            """

            # Stream the response so it looks cool
            response_stream = model.generate_content_stream([prompt, file_data])
            
            full_text = ""
            for chunk in response_stream:
                full_text += chunk.text
                output_container.markdown(full_text + "▌") # The "typing" cursor effect
            
            output_container.markdown(full_text) # Final render
            
            st.success("Proposal Generated. Now go close the deal.")

        except Exception as e:
            st.error(f"System Failure: {e}")
