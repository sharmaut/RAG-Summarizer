# Medical Information Retrieval & Summarization Tool

This project is an AI-powered tool designed to help users understand complex medical information. It retrieves data from trusted sources like PubMed and clinical guidelines, then uses a Retrieval-Augmented Generation (RAG) model to generate concise, reliable, and easy-to-understand summaries.

## Description

Navigating medical literature can be daunting for patients and even for healthcare professionals looking for quick summaries. This application bridges that gap by providing a simple interface to query complex medical topics. The backend pipeline uses Playwright to scrape up-to-date documents, which are then indexed in a PostgreSQL database. When a user submits a query, a Hugging Face RAG model retrieves the most relevant information and generates a context-aware summary, complete with citations and safety disclaimers.

## Key Features

- **Trusted Data Retrieval:** Gathers documents from reliable medical sources like PubMed and clinical news sites using Playwright for web automation.
- **RAG-Powered Summarization:** Integrates a Retrieval-Augmented Generation (RAG) model from Hugging Face Transformers to produce accurate, context-aware summaries.
- **Built-in Safety Guardrails:** Automatically appends disclaimers to all generated content, ensuring users understand that the information is not a substitute for professional medical advice.
- **FastAPI Backend:** A robust RESTful API built with FastAPI handles user queries and orchestrates the entire retrieval and summarization pipeline.
- **Interactive Dashboard:** A user-friendly frontend developed with React and Material-UI allows users to enter queries and view the generated summaries and data visualizations.
- **Cloud-Native Architecture:** Deployed for scalability, with the frontend on Netlify and backend services utilizing AWS.

## Technologies Used

- **Backend:** Python, FastAPI, Hugging Face Transformers, Playwright
- **Frontend:** React.js, Chart.js, Material-UI
- **Database:** PostgreSQL
- **Deployment:** AWS S3, Netlify, Git
