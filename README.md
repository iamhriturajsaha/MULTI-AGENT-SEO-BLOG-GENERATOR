# Multi-Agent SEO Blog Generator

## 🚀 Overview

![multi agent blog writer.png](<multi agent blog writer.png>)

The **Multi-Agent SEO Blog Generator** is an innovative project that utilizes cutting-edge technologies to automate the process of creating well-researched, human-like blogs. This system is designed to bridge the gap between AI automation and human creativity by incorporating the latest advancements in **Agentic AI**.

This project features a **multi-agent architecture** that autonomously plans, writes, and edits blog posts, ensuring they are accurate, engaging, and up-to-date with the latest trends.

## 📁 Project Structure

```
HR-Blog-Generator/
├── agents/
│   ├── __init__.py
│   ├── research_agent.py
│   ├── planning_agent.py
│   ├── generation_agent.py
│   ├── seo_agent.py
│   └── review_agent.py
├── config/
│   └── settings.py
├── outputs/
│   ├── blogs/
│   └── temp/
├── tests/
│   └── test_agents.py
├── utils/
│   ├── helpers.py
│   └── seo_tools.py
├── .env
├── requirements.txt
├── blog_generator.py
└── README.md

```
---

## 🌟 Features

- **Automatic Trend Detection**: Pulls latest HR trends from 10+ sources.
- **SEO Score Optimization**: Maintains 8-12% keyword density.
- **Multi-Format Output**: Generates markdown, HTML, and PDF versions.
- **Quality Assurance**: Automated grammar checks and readability scoring.
- **Plagiarism Check**: Integrated Copyscape API (add API key in .env).

---

## ⚙️ Technologies Used

### Backend
- **CREW AI**: For Creating multi agent system.
- **FastAPI**: For serving the AI-powered blog generation API.
- **Python**: For scripting and implementation.
- **LangChain**: For managing multi-agent workflows.
- **Gemini 2.0-Flash-EXP**: As the language model powering the system.
- **Serper Web Search Tool**: To gather real-time data and trends.

### Frontend
- **Next.js**: For building the client-side application.
- **React**: For creating dynamic UI components.
- **Tailwind CSS**: For styling.
- **Shadcn  UI**: Components.

---

## 🛠 Installation

### Backend Setup (FastAPI Server)
1. **Install Dependencies**:
   Ensure Python 3.8+ is installed. Install the required Python libraries:
   ```bash
   pip install -r server/requirements.txt
   ```

2. **Run the FastAPI Server**:
   Open the `crewai.ipynb` notebook and run the cells to start the FastAPI server.
   - **Server URL**: `http://127.0.0.1:8002`

---

### Frontend Setup (Next.js)
1. **Navigate to the Frontend Directory**:
   ```bash
   cd client/bloggpt
   ```

2. **Install Dependencies**:
   ```bash
   npm install
   ```

3. **Start the Development Server**:
   ```bash
   npm run dev
   ```

4. **Frontend URL**: `http://localhost:3000`

---

## 🧠 How It Works

1. **User Input**: The user enters a topic through the Next.js frontend.
2. **API Request**: The frontend sends a POST request to the FastAPI server running at `http://127.0.0.1:8002/generate-blog/`.
3. **Blog Generation**:
   - The FastAPI server processes the request using `crewai.ipynb`.
   - The AI agents (Planner, Writer, Editor) collaboratively generate a polished blog.
4. **Response**: The FastAPI server returns the generated blog in Markdown format.
5. **Frontend Rendering**:
   - The blog is rendered using `ReactMarkdown` with proper Markdown styling.

---

## 🎯 Use Cases

- **Content Marketing**: Automate blog creation for businesses and brands.
- **Research Documentation**: Generate research summaries or articles with minimal effort.
- **Trend Analysis**: Create content based on the latest trends in various domains.

---

## 📝 Future Enhancements

- **Multi-modal Capabilities**: Incorporate image and video generation.
- **Advanced Customization**: Enable user-specific writing styles.
- **Workflow Orchestration**: Add support for managing multiple blogs simultaneously.

---

---

**Elevating AI creativity—one blog at a time! 🌟**

--- 

