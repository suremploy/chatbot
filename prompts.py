RULES = """---

### **Rules**

1. **Strict Adherence to Input Data**:
   - Only include information provided in the input. Do not infer or assume any details.
   - Leave ambiguities unaddressed unless the input clarifies them.

2. **No Subjective Statements**:
   - Avoid interpretations, opinions, or personal commentary.
   - Repeatedly use phrases like "reports," "states," or "mentions" to attribute statements to the worker.

3. **Explicit Use of Source Phrases**:
   - Repeatedly reference the worker&#39;s statements using terms like "reports", "states", or "mentions" to clearly attribute the information to the injured worker or source document.

4. **Pronoun and Title Usage**:
   - Use gender-specific pronouns and titles based on the provided "Gender" input (e.g., Mr., Ms., he/him, she/her).

5. **Formatting Consistency**:
   - Follow the format of the provided examples.
   - Include clear headings and sections for role, injury details, treatment, work status, and reported concerns.

6. **Professional Tone**:
   - Maintain a formal and professional tone without emotional language or judgment.

---"""

INITIAL_PROMPT = """
You are tasked with generating **professional, structured injury reports** for workplace assessments. Your output must strictly adhere to the provided input data, maintaining factual accuracy and following the rules and formatting described below. **Do not add any information not explicitly provided.**

{rules}

### **Input Example**

**Gender**: Female  
**Assessment Details**:  
- Severe neck and back pain.  
- Role: Nurse.  
- Diagnosed with L4/L5 disc bulge.  
- Reports worsening symptoms when lifting patients.  
- Pain radiates down the left leg, worsening at night.  
- Takes Ibuprofen and Paracetamol twice daily.  
- Missed two weeks of work in June.  
- Reports inability to stand for extended periods.

---

### **Output Example**

Ms X, a Nurse, has been managing severe neck and back pain, which has been diagnosed as a disc bulge at the L4/L5 level. She reports worsening symptoms when lifting patients, with pain radiating down her left leg, particularly worsening at night.

Ms X mentions taking Ibuprofen and Paracetamol twice daily to manage her pain. In June, she missed two weeks of work due to these symptoms. She further reports an inability to stand for extended periods, which impacts her ability to perform her duties effectively.

---

### Task  
Using the above rules and format, generate a **structured workplace injury report** based on the following input fields:

1. **Gender**: {gender}
2. **Assessment Details**: {assessment_details}

Ensure that the output mirrors the examples provided, strictly following the structure, tone, and rules.

"""
