from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from pypdf import PdfReader
from PIL import Image
import io

app = Flask(__name__)

# ---------------------------------------------------------
# 🔴 CONFIGURATION: PASTE YOUR API KEY BELOW 🔴
# ---------------------------------------------------------
MY_API_KEY = ""  # <--- PASTE YOUR KEY INSIDE THESE QUOTES

genai.configure(api_key=MY_API_KEY)

# --- SMART MODEL SELECTOR ---
# We prefer 'gemini-1.5-flash' because it is Multimodal (sees images) and Fast.
def get_working_model():
    try:
        # Check available models
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                if 'flash' in m.name: return genai.GenerativeModel(m.name)
        # Fallback
        return genai.GenerativeModel('gemini-1.5-flash')
    except:
        return genai.GenerativeModel('gemini-1.5-flash')

model = get_working_model()

# --- ROUTES ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        witness = request.form.get('witness')
        context_data = ""
        image_part = None
        has_visual_evidence = False

        # 1. HANDLE FILE UPLOADS (PDF OR IMAGES)
        if 'file' in request.files and request.files['file'].filename != '':
            file = request.files['file']
            filename = file.filename.lower()

            # A. Handle PDF (Text Evidence)
            if filename.endswith('.pdf'):
                pdf_reader = PdfReader(file)
                for i, page in enumerate(pdf_reader.pages):
                    text = page.extract_text()
                    if text: 
                        context_data += f"[PAGE {i+1} RECORD]: {text}\n---\n"
            
            # B. Handle Images (Visual Evidence)
            elif filename.endswith(('.png', '.jpg', '.jpeg', '.webp')):
                # Read image bytes for Gemini
                image_data = file.read()
                image_part = {'mime_type': file.mimetype, 'data': image_data}
                context_data += "[VISUAL EVIDENCE ATTACHED: Crime Scene Photo]"
                has_visual_evidence = True

        else:
            # Fallback to manual text context
            context_data = request.form.get('context')

        # Validation
        if not context_data and not image_part:
            return jsonify({"error": "No Evidence Uploaded! Please upload a PDF or Image."})
        if not witness:
            return jsonify({"error": "No Witness Testimony! Please speak into the mic."})

        # 2. CONSTRUCT THE "GOD PROMPT"
        # This prompt forces Gemini to act as a Judge, handle Hinglish, and output HTML.
        prompt_text = f"""
        Act as JustiQ, the Supreme AI Judge Associate.
        
        OFFICIAL EVIDENCE RECORD:
        {context_data[:15000]} 
        
        LIVE WITNESS TESTIMONY (Listen carefully):
        "{witness}"
        
        TASK:
        1. LANGUAGE: If the witness speaks Hindi/Hinglish, translate it internally to English context.
        2. ANALYSIS: Compare the testimony against the provided Evidence (Text OR Image).
           - If an Image is provided: Look at it. Does the witness description match the visual reality? (Colors, Objects, Damage).
           - If Text is provided: Check for factual contradictions (Time, Dates, Locations, Status).
        
        OUTPUT FORMAT (Strict HTML):
        Return a valid HTML block matching this specific structure. Do not use Markdown.
        
        <div class='alert-card [STATUS]'>
            <div class='alert-header'>
                <i class='fas [ICON]'></i> [TITLE]
            </div>
            <div class='comparison-grid'>
                <div class='comp-box witness'>
                    <small>WITNESS CLAIM</small>
                    <p>[Quote the specific lie/claim]</p>
                </div>
                <div class='comp-box record'>
                    <small>EVIDENCE TRUTH</small>
                    <p>[What the Text/Image actually shows]</p>
                    <span class='citation-badge'><i class='fas fa-book'></i> [Source: Page # OR Visual Analysis]</span>
                </div>
            </div>
            <div class='reasoning'>
                <strong>VERDICT:</strong> [Brief, punchy explanation of the conflict]
            </div>
            <div id='tts-text' style='display:none;'>Objection! [Short Spoken Verdict for the Judge]</div>
        </div>

        RULES FOR VARIABLES:
        - If Contradiction Found:
          [STATUS] = 'danger'
          [ICON] = 'fa-gavel'
          [TITLE] = 'OBJECTION! CONTRADICTION DETECTED'
        
        - If Testimony Verified/Consistent:
          [STATUS] = 'success'
          [ICON] = 'fa-check-circle'
          [TITLE] = 'TESTIMONY VERIFIED'
        """
        
        # 3. SEND TO GEMINI (Handling Multimodal Inputs)
        inputs = [prompt_text]
        if image_part:
            inputs.append(image_part) # Add the image to the request
            
        response = model.generate_content(inputs)
        
        # 4. RETURN RESULT
        return jsonify({"result": response.text})

    except Exception as e:
        print(f"Server Error: {e}")
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)