# End-to-End QA Chatbot

This repository provides an end-to-end QA (Question-Answering) Chatbot that integrates multiple state-of-the-art technologies. The chatbot can scrape websites using BeautifulSoup (bs4), retrieve relevant documents via vector retrieval, and maintain conversation history to provide context-aware responses. It leverages advanced tools and models including **Groq**, **Huggingface**, **OpenAI**, and **Ollama models**, and uses prompt templates to structure queries.

## Overview

The project demonstrates how to:

- Build a conversational chatbot that interacts with websites and answers questions contextually.
- Scrape websites using **BeautifulSoup (bs4)**.
- Retrieve context-relevant documents using **vector retrieval** techniques.
- Maintain conversation history to provide context-aware responses.
- Use prompt templates for effective query structuring.
- Integrate multiple models including **Groq**, **Huggingface**, **OpenAI**, and **Ollama models**.

## Features

- **Groq Integration:**  
  Efficient querying with the Groq API for language model inference.

- **Huggingface Models:**  
  Leverage state-of-the-art NLP models and utilities from Huggingface.

- **Web Scraping with BeautifulSoup (bs4):**  
  Extract and process content from websites to support conversational queries.

- **Conversational Chatbot:**  
  Maintains conversation history for context-aware answers.

- **Vector Retrieval:**  
  Uses vector-based methods to index and retrieve relevant documents.

- **Prompt Templating:**  
  Structures queries for effective interaction with language models.

- **Multiple Model Integrations:**  
  Combines capabilities from **OpenAI** and **Ollama models**.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/EniolaAdemola/End-to-End-QA-Chatbot.git
   cd End-to-End-QA-Chatbot

   ```

2. **Create and activate a virtual environment (optional but recommended) for me i used conda:**

   ```bash
   conda create -p venv python==3.10 -y
   ```

   ```bash
   conda activate venv

   ```

3. **Install the required libraries:**

   ```bash
   pip install -r requirements.txt

   ```

4. **Set up environment variables:**
   Create a .env file in the root directory with the following keys:
   ```bash
   GROQ_API_KEY=your_groq_api_key
   HF_TOKEN=your_hf_token
   ```

---

### Run the bot

To start the streamlit application, you can run either ollama-bot.py or openai-bot.py:

```bash
streamlit run openai-qa-chatbot\openai-bot.py

```

## 🤝 Contributing

Contributions are welcome! Feel free to submit a PR or open an issue.

## 📞 Contact

For inquiries, reach out to [Eniola Ademola](https://github.com/EniolaAdemola).

---
