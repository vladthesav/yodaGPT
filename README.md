# YodaGPT - ChatGPT Powered Yoda Chatbot

YodaGPT is an advanced chatbot powered by ChatGPT. It is designed to simulate conversations with users, providing helpful responses and engaging interactions. This README file provides instructions for running YodaGPT locally or with Docker.

## Usage

### Running Locally 

To run YodaGPT locally, follow the steps below:

1. Install the required packages:
   ```bash
   pip3 install -r requirements.txt
   ```

2. Set your OpenAI API key as an environment variable:
   ```bash
   export OPENAI_API_KEY="YOUR_API_KEY"
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

4. Connect to YodaGPT by opening your web browser and navigating to:
   ```
   http://localhost:8501/
   ```

### Running with Docker

To run YodaGPT using Docker, follow the steps below:

1. Build the Docker container:
   ```bash
   docker build -t yoda_gpt:latest .
   ```

2. Run the Docker container with your API key as an environment variable:
   ```bash
   docker run -d -p 8501:8501 --env OPENAI_API_KEY="YOUR_API_KEY" yoda_gpt:latest
   ```

3. Connect to YodaGPT by opening your web browser and navigating to:
   ```
   http://localhost:8501/
   ```