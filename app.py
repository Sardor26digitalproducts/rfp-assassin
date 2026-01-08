import streamlit as st
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

# 1. CONFIGURE THE BEAST
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# 2. MODEL SETUP
generation_config = {
    "temperature": 0.2,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 65536,
}

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
)

# 3. THE INTERFACE
st.set_page_config(page_title="RFP Assassin", layout="wide")
st.title("⚡ RFP Assassin: MK22 Defense Edition")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("1. The Target (Tender PDFs)")
    uploaded_files = st.file_uploader("Upload MK22 Solicitation & Amendments", type=['pdf'], accept_multiple_files=True)
    
    st.subheader("2. The Ammo (Your Company Info)")
    company_context = st.text_area("Paste your Shop Capabilities/Experience here.", height=200)
    
    generate_btn = st.button("🚀 Run Compliance & Draft", type="primary")

with col2:
    st.subheader("3. Analysis & Strategy")
    output_container = st.empty()

# 4. THE LOGIC (Perfectly Indented)
if generate_btn and uploaded_files and company_context:
    with st.spinner("Analyzing Navy Requirements..."):
        try:
            # Convert uploaded files for Gemini
            processed_files = []
            for f in uploaded_files:
                processed_files.append({"mime_type": f.type, "data": f.getvalue()})

            prompt = f"""
            You are a Senior Defense Procurement Specialist. 
            You are analyzing the MK22 Motor Tubes Solicitation (N0017426R0002) for a manufacturing client.

            **CONTEXT FROM USER:**
            {company_context}

            **TASK:**
            Using the uploaded PDFs, extract these 'Kill Criteria' to see if the user can actually win:

            1. **AMENDMENT CHECK (0002 & 0003):** - State the NEW closing date from Amendment 0003.
               - Explain the Hydrostatic Test clarification from Amendment 0002.
            
            2. **TECHNICAL REQUIREMENT:** - Identify the "Brown Band" application location from the attachments.
            
            3. **STRATEGY - FIRST ARTICLE TESTING (FAT):**
               - Based on the user's context, are they eligible for a FAT Waiver? 
               - If they are NOT a previous supplier, list the "Offer A" (with FAT) vs "Offer B" (without FAT) pricing requirement.

            4. **REQUIRED DOCUMENTS:**
               - List the CDRLs (Contract Data Requirements List) they must submit.

            **OUTPUT STYLE:**
            Use professional, high-stakes military contractor terminology. Use Bold headers.
            """

            response_stream = model.generate_content([prompt] + processed_files, stream=True)
            
            full_text = ""
            for chunk in response_stream:
                full_text += chunk.text
                output_container.markdown(full_text + "▌")
            
            output_container.markdown(full_text)

        except Exception as e:
            st.error(f"Error: {e}")
