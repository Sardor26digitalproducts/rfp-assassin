# ... (Inside the try block in app.py) ...

            # THE MANUFACTURING KILLER PROMPT
            prompt = f"""
            You are a Defense Contract Bid Strategist.
            
            **CONTEXT:**
            The user is a manufacturer bidding on: MK22 Motor Tubes (Solicitation N0017426R0002).
            Company Info: {company_context}
            
            **CRITICAL COMPLIANCE CHECKS (Must Answer):**
            1. **First Article Testing (FAT):** Does the user's context mention previous experience with "MK22 Motor Tubes"? 
               - If YES: Write a justification to WAIVE First Article Testing (saves money).
               - If NO: Explicitly state that "First Article Testing IS REQUIRED" and list the test steps found in Section C of the PDF.
            
            2. **Hydrostatic Testing:** Extract the exact pressure requirements (PSI) from the PDF for the hydrostatic test.
            
            3. **The "Brown Band":** Look at "Attachment 1" in the PDF context. Explain exactly where the Brown Band must be applied on the tube (distance from edge).
            
            **OUTPUT STRUCTURE:**
            ## 1. Executive Summary (Bid/No-Bid Recommendation)
            ## 2. Technical Compliance Matrix (Pass/Fail)
               - Hydrostatic Test Capability: [Yes/No based on company context]
               - Brown Band Application: [Confirm understanding]
            ## 3. Pricing Strategy Note
               - [Insert Advice on FAT Waiver here]
            ## 4. Draft Proposal Text (SOW Response)
            """
