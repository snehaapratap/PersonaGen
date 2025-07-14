# PersonaGen: Reddit User Persona Generator

## 🚀 Overview

**PersonaGen** is an AI-powered tool that generates a detailed, visually appealing user persona from any public Reddit profile.  
It scrapes both posts and comments, analyzes them using a Large Language Model (LLM), and outputs:
- A structured, human-readable persona **text file** (with citations for each trait)
- A beautiful, downloadable **persona image** (like a UX persona card)
- An interactive **Streamlit web app** for easy use

---

## ✨ Features

- **Reddit Scraper**: Collects both posts and comments from any Reddit user.
- **LLM Persona Builder**: Uses advanced LLMs to infer age, occupation, motivations, habits, frustrations, and more.
- **Citation for Each Trait**: Every persona characteristic is backed by a specific post or comment (with reference).
- **Persona Image Generator**: Creates a modern, two-column persona card image (16:9, auto-sized for long personas).
- **Downloadable Outputs**: Instantly download both the persona text and image.

- **Streamlit UI**: User-friendly web interface for non-technical users.
- **PEP-8 Compliant**: Clean, readable, and well-documented code.
---

## 🧠 How It Works

1. **Scraping**: Collects up to 100 recent posts and comments from the user.
2. **LLM Prompting**: Sends the data to an LLM with a carefully crafted prompt to extract persona traits and cite sources.
3. **Formatting**: Outputs a clean text file and generates a persona image using Pillow.
4. **Web UI**: Streamlit app ties it all together for easy use.

---

## 🖥️ Demo


<img width="1303" height="779" alt="Screenshot 2025-07-14 at 12 12 50" src="https://github.com/user-attachments/assets/617a1d2c-ce44-4f2c-9f33-bb9b77bf07bf" />
<img width="1352" height="714" alt="Screenshot 2025-07-14 at 12 13 13" src="https://github.com/user-attachments/assets/ea8ad85a-5b93-431b-b589-6de4357322af" />




---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/snehaapratap/PersonaGen.git
cd PersonaGen
```

### 2. Install Dependencies

We recommend using a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Set Up API Keys

- **LLM API**: Set your LLM API key (e.g., GROQ_API_KEY) as an environment variable or in a `.env` file:
  ```
  GROQ_API_KEY=your_groq_api_key_here
  ```
## OR

### 4. Run the Streamlit App with the API key

```bash
export GROQ_API_KEY=your_groq_api_key_here
streamlit run app.py
```

---

## ⚡ Usage

### **Web App (Recommended)**

1. Open the Streamlit app in your browser.
2. Enter any Reddit user’s profile URL (e.g., `https://www.reddit.com/user/kojied/`).
3. Click **Generate Persona**.
4. View the generated persona, download the text file (with citations), and download the persona image.

### **Command-Line (Optional)**

You can also run the script directly for batch processing:

```bash
python main.py https://www.reddit.com/user/kojied/
```
- Output will be saved in the `output/` directory.

---

## 📄 Output Format

### **Persona Text File Example**

```
Name: Kojied
Age: Late 20s/Early 30s  [Cited: Comment #3]
Occupation: Software Developer/Remote Worker  [Cited: Post #1]
...
Motivations:
- Convenience  [Cited: Comment #7]
...
```

### **Persona Image Example**

- Modern, two-column card with all persona details, ready for presentations or UX research.

---


## 📝 Sample Outputs

- See `output/kojied_persona.txt` and `output/kojied_persona.png` for examples.

---

## 🧑‍💻 Code Quality

- Follows PEP-8 guidelines.
- Modular, well-commented, and easy to extend.
- Includes error handling for API/network issues.

---
## Contact
For any queries , contact me @sneha.prem918@gmail.com
