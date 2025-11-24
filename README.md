# 🤖 Agentic AI – Multi-Agent System

This project is a multi-agent AI system built using Python, Streamlit, and Groq LLaMA-3.1 models.  
The system takes your input, passes it through multiple agents (Planner, Researcher, Answer, Respond), and gives a final answer.


## 🖥️ UI Screenshot
![App Screenshot](assets/Screenshot%205.pngScreenshot5.png)



### 1️⃣ Create virtual environment

python -m venv venv
venv\Scripts\activate # Windows


### 2️⃣ Install dependencies


pip install -r requirements.txt


### 3️⃣ Add your API key in `.env`


GROQ_API_KEY=your_key_here


### 4️⃣ Run the Streamlit app


streamlit run src/ui/app.py



## 📂 Folder Structure


Agentic-LangGraph-Project/
│
├── src/
│ ├── agents/
│ ├── ui/app.py
│ ├── graph.py
│ ├── rag.py
│
├── assets/
│ └── screenshot.png
│
├── vectorstore/
├── requirements.txt
├── .env
└── README.md




## 📘 Notes
- Uses **Groq LLaMA-3.1** models.