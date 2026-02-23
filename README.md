
<div align="center">
  <h1><b>AI-focused Software Engineer</b></h1>
  <p>Building practical AI systems with strong backend foundations, 
while exploring methods to advance model capability and reasoning.</p>
</div>

<!-- QUOTE_START -->
<div align="center">

<br/>
<br/>

*******<br><hr>

<br/>

*“Give me a place to stand, and I will move the earth.”*

<br/>

— *Archimedes* —

<br/>

<hr><br>*****

<br/>
<br/>

</div>
<!-- QUOTE_END -->


<br/>

## 👨‍💻 About Me

AI-focused software engineering student with hands-on experience in computer vision, LLM system integration, and memory-augmented agent design. 

I am particularly interested in representation learning, optimization in deep models, and building efficient AI systems that balance reasoning capability with practical constraints.

## 🛠 Technical Skills

| Domain | Skills |
|:---:|:---|
| **Programming** | Python (primary), C/C++ (excellent), Julia (preferred), Java (hated but really good at it) |
| **AI / ML** | Supervised & Unsupervised Learning, Reinforcement Learning, Hyperparameters tuning, Model selection & evaluation, Cross-Validation variants |
| **Deep & Representation Learning** | Feedforward Neural Networks, Graph Neural Networks, Dense embedding & similarity systems |
| **Generative & Probabilistic Models** | Diffusion Models, Restricted Boltzmann Machines, Transformer architectures |
| **LLM Systems & AI Agents** | llama.cpp (local inference), Prompt engineering, Parameter-efficient fine-tuning (LoRA), Model orchestration, Agent frameworks (Langchain), Retrieval-Augmented Generation (RAG), Quantization |
| **Mathematics for AI** | Non-convex optimization, Gradient Descent variants, L1/L2 Regularization, Matrix decomposition, Probability & Statistical Modeling |

## 🚀 Projects

### 1. [IoT Face Recognition Attendance System (AI Module)](https://github.com/antialberteinstein/PBL5)
*Note: This project is currently in progress. The description will be expanded as development continues.*
*   **Face Recognition Pipeline:** Developed a highly accurate face recognition pipeline utilizing InsightFace embeddings.
*   **Classification:** Implemented adaptive online classification—orchestrating multiple ML models—with hyperparameter tuning to maximize **precision**.
*   **Integration:** Exposed a robust inference API via Flask for seamless integration into IoT hardware systems.

### 2. [ChatToExplore (Java + llama.cpp)](https://github.com/antialberteinstein/ChatToExplore)
*   **Overview:** A web application that allows users to discover Vietnamese historical figures through an interactive timeline UI. Users can chat with an embedded AI assistant to learn about these figures, and even ask the bot to autonomously research and add new figures to the timeline.
*   **Local Inference:** Integrated local LLM inference directly into a Java Servlet backend.
*   **Async Architecture:** Designed a robust job queue for long-running AI tasks to ensure computation persists beyond standard HTTP session lifecycles. Background processes run independently until completion, allowing users to safely close their browsers or log out without interrupting the task.
*   **Agent Logic:** Developed a custom, lightweight agent framework from scratch—without relying on heavy external libraries. This agent supports dynamic actions such as web searching and autonomous data saving.

### 3. [Hybrid AI Agent (Python)](https://github.com/antialberteinstein/HybridAIAgent)
*   **Overview:** A custom agent framework (conceptually similar to LangChain) designed to significantly enhance the accuracy and multi-step decision-making capabilities of Small Language Models (SLMs).
*   **Background:** SLMs often struggle with complex decision-making, frequently resulting in hallucinations or logical errors. To address this, rather than blindly leaving action generation solely to a "next-word prediction machine", I augmented this traditional approach with lightweight Machine Learning algorithms to filter and guide the action selection process. This keeps the system highly efficient while allowing the SLM to make the final, informed determination.
*   **Mechanism:** Think of the SLM as a football referee who occasionally makes mistakes without assistance. In this architecture, the ML algorithms act as a Video Assistant Referee (VAR). The framework maintains a "notebook" of available actions (acting as a few-shot prompt). Since SLMs struggle to reliably search large contexts, the ML algorithms pre-filter this notebook to narrow down the action space, making it much easier for the SLM to select the correct action. This drastically reduces hallucinations. I also implemented supplementary techniques to boost accuracy, such as dynamically scaling the number of few-shot examples based on ML confidence scores and randomly re-injecting historical successes.
*   **Teacher Mode:** To dynamically expand the framework's capabilities, users can toggle "Teacher Mode," where a stronger, external LLM generates and appends new action knowledge to the system's notebook.


---