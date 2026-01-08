# ... (Inside the try block in app.py) ...

            # THE MANUFACTURING KILLER PROMPT
            # THE RUTHLESS MK22 SPECIALIST PROMPT
            prompt = f"""
            You are a Senior Defense Procurement Specialist. 
            You are analyzing the MK22 Motor Tubes Solicitation (N0017426R0002) for a manufacturing client.

            **CONTEXT FROM USER:**
            {company_context}

            **TASK:**
            Using the uploaded PDFs, extract these 'Kill Criteria' to see if the user can actually win:

            1. **AMENDMENT CHECK (0002 & 0003):** - State the NEW closing date from Amendment 0003 (Jan 23, 2026).
               - Explain the Hydrostatic Test clarification from Amendment 0002 (Drawing 525-174-0131 vs 0152).
            
            2. **TECHNICAL REQUIREMENT:** - Identify the "Brown Band" application location from Attachment 1. (Expected: 8.00±.12 inches).
            
            3. **STRATEGY - FIRST ARTICLE TESTING (FAT):**
               - Based on the user's context, are they eligible for a FAT Waiver? 
               - If they are NOT a previous supplier, list the "Offer A" (with FAT) vs "Offer B" (without FAT) pricing requirement.

            4. **REQUIRED DOCUMENTS:**
               - List the CDRLs (Contract Data Requirements List) they must submit (A001-A006).

            **OUTPUT STYLE:**
            Use professional, high-stakes military contractor terminology. Use Bold headers.
            """
