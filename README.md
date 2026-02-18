# ⚖️ JustiQ: The Next-Gen AI Judicial Assistant
> **"Real-Time Multimodal Intelligence for Indian Courts"**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Gemini](https://img.shields.io/badge/AI-Gemini%201.5%20Flash-orange)
![Flask](https://img.shields.io/badge/Backend-Flask-green)
![Status](https://img.shields.io/badge/Status-Prototype%20v4.0-red)

## 🚀 Overview
**JustiQ** is an intelligent AI system designed to solve the **Judicial Backlog Crisis** and **Cognitive Overload** faced by judges. Unlike standard legal search tools, JustiQ listens to live court proceedings, analyzes multimodal evidence (PDFs and Crime Scene Photos), and detects factual contradictions in real-time.

It acts as an intelligent **Judicial Associate**, automatically verifying witness claims against official records and visual evidence.

---

## 🌟 Key Features (The "Wow" Factors)

### 1. 🧠 Multimodal Reasoning (Text + Vision)
* **📄 Document Intelligence:** Reads complex legal documents (FIRs, Charge Sheets, Forensics) page-by-page to find contradictions.
* **👁️ Computer Vision:** "Sees" crime scene photos to verify physical facts (e.g., "Witness claims the car was Blue; Photo evidence clearly shows Red").

### 2. 🗣️ Native "Hinglish" Support
* Built specifically for Indian courtrooms.
* Understands mixed **Hindi + English** testimony.
* Instantly translates intent to cross-reference against English official records.

### 3. 🕸️ Live Knowledge Graph
* Visualizes the contradiction using a dynamic **Mermaid.js** graph, connecting the "Witness Lie" to the "Evidence Truth" with a visual link.

### 4. 🔊 The "Judge's Voice" (TTS)
* Uses Text-to-Speech to audibly announce verdicts: *"Objection! Contradiction detected."*

---

## 🛠️ Tech Stack

* **Core AI:** Google Gemini 1.5 Flash (Multimodal capabilities).
* **Backend:** Python (Flask).
* **Frontend:** HTML5, CSS3 (Glassmorphism UI), JavaScript (Web Speech API).
* **Visualization:** Mermaid.js (Real-time graphs).
* **Processing:** `pypdf` (Docs), `Pillow` (Images).

---

## 📸 Demo Scenarios

### Scenario A: The "Visual Lie" (Computer Vision)
> **Witness:** "Your Honor, the vehicle involved was definitely Blue."
> **Evidence:** Uploaded Photo of a Red Car.
> **Result:** 🔴 **OBJECTION!** AI detects color mismatch between testimony and visual evidence.

### Scenario B: The "Hinglish Budget" (Language + PDF)
> **Witness:** "Sir, is project ka budget sirf 500 rupay hai."
> **Evidence:** Official PDF Report showing ₹7,210 Crores allocation.
> **Result:** 🔴 **OBJECTION!** AI understands Hindi input, reads the English PDF, and cites the specific page number.

### Scenario C: The "Timeline Trap" (Logic)
> **Witness:** "I was arrested at 10 PM."
> **Evidence:** Police Log (PDF) showing arrest time at 8:00 PM.
> **Result:** 🔴 **OBJECTION!** Time contradiction detected.

---

## ⚙️ Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/justiq-live.git](https://github.com/YOUR_USERNAME/justiq-live.git)
    cd justiq-live
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set Up API Key**
    * Create a file named `.env` or export in terminal:
    ```bash
    export GEMINI_API_KEY="your_google_api_key_here"
    ```

4.  **Run the App**
    ```bash
    python app.py
    ```

5.  **Access the Dashboard**
    * Open your browser and go to: `http://127.0.0.1:5000`

---

## 🛡️ Compliance & Ethics
* **BNS 2023 Compliant:** Designed adhering to the new Bharatiya Nyaya Sanhita timelines.
* **Data Privacy:** Can be deployed On-Premise; no data retention on cloud (session-based).

---

Made with ❤️ for **Justice**.