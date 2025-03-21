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

To set up the HR Blog Generator project, follow these steps:


1. **Clone the Repository**:

   Open your terminal and clone the repository using Git:

   ```bash
   git clone https://github.com/yourusername/HR-Blog-Generator.git
   cd HR-Blog-Generator

2. **Create a Virtual Environment**:

   It's recommended to create a virtual environment to manage dependencies. You can do this using venv:

   ```bash
   python -m venv venv

3. **Activate the Virtual Environment**:

   **On Windows**:

   ```bash
   venv\Scripts\activate

3. **Install Dependencies**:

   Use pip to install the required packages listed in requirements.txt:

   ```bash
   pip install -r requirements.txt

5. **Set Up Environment Variables**:

   Create a .env file in the root directory of the project and add your API keys:
   
   ```text
   OPENAI_API_KEY=your_openai_key_here
   NEWS_API_KEY=your_newsapi_key_here
   GOOGLE_CSE_ID=your_google_cse_id_here
   GOOGLE_API_KEY=your_google_api_key_here

6. **Run the Blog Generator**:
   
   Execute the main script to generate the blog post:
   
   ```bash
   python blog_generator.py

7. **Check Outputs**:

   After running the script, you will find your generated blog post in markdown format and a PDF file in the outputs/blogs/ directory.

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

**Elevating AI creativity—one blog at a time! 🌟**

--- 

