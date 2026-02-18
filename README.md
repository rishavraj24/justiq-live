# ⚖️ JustiQ: The Next-Gen AI Judicial Assistant
> **"Real-Time Multimodal Intelligence for Indian Courts"**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Gemini](https://img.shields.io/badge/AI-Gemini%201.5%20Flash-orange)
![Flask](https://img.shields.io/badge/Backend-Flask-green)
![Status](https://img.shields.io/badge/Status-Prototype%20v4.0-red)

## 🚀 Overview
**JustiQ** is an agentic AI system designed to solve the **Judicial Backlog Crisis** and **Cognitive Overload** faced by judges. Unlike standard legal search tools, JustiQ listens to live court proceedings, analyzes multimodal evidence (PDFs, CCTV Footage, Crime Scene Photos), and detects contradictions in real-time.

It acts as an intelligent **Co-Counsel**, not just flagging lies but suggesting **"Killer Cross-Examination Questions"** to expose perjury.

---

## 🌟 Key Features (The "Wow" Factors)

### 1. 🧠 Multimodal Reasoning (Text + Vision + Video)
* **📄 Document Intelligence:** Reads 500+ page PDFs (FIRs, Charge Sheets) to find factual contradictions.
* **👁️ Computer Vision:** Analyzes crime scene photos (e.g., "Witness claims car was Blue; Photo shows Red").
* **🎥 CCTV Video Analysis:** Watches video footage frame-by-frame to verify physical actions (e.g., "Witness claims handshake; Video shows punch").

### 2. 🗣️ Native "Hinglish" Support
* Built for Indian courtrooms.
* Understands mixed **Hindi + English** testimony.
* Translates intent instantly to cross-reference against English official records.

### 3. ⚔️ Agentic Cross-Examination
* Doesn't just find the lie—it helps you fight it.
* Generates **3 Aggressive Follow-up Questions** for lawyers to corner a lying witness.

### 4. 🕸️ Live Knowledge Graph
* Visualizes the contradiction using a dynamic **Mermaid.js** graph, connecting the "Lie" to the "Evidence" with a visual link.

### 5. 🔊 The "Judge's Voice" (TTS)
* Uses Text-to-Speech to audibly announce verdicts: *"Objection! Contradiction detected."*

---

## 🛠️ Tech Stack

* **Core AI:** Google Gemini 1.5 Flash (Multimodal capabilities).
* **Backend:** Python (Flask).
* **Frontend:** HTML5, CSS3 (Glassmorphism UI), JavaScript (Web Speech API).
* **Visualization:** Mermaid.js (Real-time graphs).
* **Processing:** `pypdf` (Docs), `Pillow` (Images), `Google Generative AI SDK` (Video).

---

## 📸 Screenshots / Demo Scenarios

### Scenario A: The "Visual Lie" (Computer Vision)
> **Witness:** "The car involved was Blue."
> **Evidence:** Uploaded Photo of a Red Car.
> **Result:** 🔴 **OBJECTION!** AI detects color mismatch.

### Scenario B: The "CCTV Trap" (Video Analysis)
> **Witness:** "We were just talking peacefully."
> **Evidence:** CCTV Video showing a fight.
> **Result:** 🔴 **OBJECTION!** AI cites timestamp 0:04 showing aggression.

### Scenario C: The "Hinglish Budget" (Language)
> **Witness:** "Sir, project ka budget sirf 500 rupay hai."
> **Evidence:** PDF Report showing ₹7,210 Crores.
> **Result:** 🔴 **OBJECTION!** AI understands Hindi and cites the English PDF.

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
    * *(Or hardcode it in app.py for local testing ONLY)*

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

## 🔮 Future Roadmap
* [ ] Integration with ICJS (Inter-operable Criminal Justice System).
* [ ] Blockchain-based evidence tampering detection.
* [ ] Real-time translation for 22+ Indian regional languages.

---

Made with ❤️ for **Justice**.