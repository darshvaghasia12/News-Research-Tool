<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RockyBot: News Research Tool</title>
</head>
<body>
    <h1>RockyBot: News Research Tool</h1>
    <h2>Overview</h2>
    <p>RockyBot is a user-friendly news research tool designed for effortless information retrieval. Users can input article URLs and ask questions to receive relevant insights from the stock market and financial domain.</p>
    <h2>Features</h2>
    <ul>
        <li>Load URLs or upload text files containing URLs to fetch article content.</li>
        <li>Process article content through LangChain's UnstructuredURL Loader.</li>
        <li>Construct an embedding vector using OpenAI's embeddings and leverage FAISS, a powerful similarity search library, to enable swift and effective retrieval of relevant information.</li>
        <li>Interact with the LLM's (ChatGPT) by inputting queries and receiving answers along with source URLs.</li>
    </ul>
    <h2>Installation</h2>
    <ol>
        <li>Clone this repository to your local machine using:</li>
        <code>git clone https://github.com/codebasics/langchain.git</code>
        <li>Navigate to the project directory:</li>
        <code>cd 2_news_research_tool_project</code>
        <li>Install the required dependencies using pip:</li>
        <code>pip install -r requirements.txt</code>
        <li>Set up your OpenAI API key by creating a <code>.env</code> file in the project root and adding your API:</li>
        <code>OPENAI_API_KEY=your_api_key_here</code>
    </ol>
    <h2>Usage/Examples</h2>
    <ol>
        <li>Run the Streamlit app by executing:</li>
        <code>streamlit run main.py</code>
        <li>The web app will open in your browser.</li>
        <li>On the sidebar, you can input URLs directly.</li>
        <li>Initiate the data loading and processing by clicking "Process URLs."</li>
        <li>Observe the system as it performs text splitting, generates embedding vectors, and efficiently indexes them using FAISS.</li>
        <li>The embeddings will be stored and indexed using FAISS, enhancing retrieval speed.</li>
        <li>The FAISS index will be saved in a local file path in pickle format for future use.</li>
        <li>One can now ask a question and get the answer based on those news articles.</li>
    </ol>
    <p>In the video tutorial, we used the following news articles:</p>
    <ul>
        <li><a href="https://www.moneycontrol.com/news/business/tata-motors-mahindra-gain-certificates-for-production-linked-payouts-11281691.html">Article 1</a></li>
        <li><a href="https://www.moneycontrol.com/news/business/tata-motors-launches-punch-icng-price-starts-at-rs-7-1-lakh-11098751.html">Article 2</a></li>
        <li><a href="https://www.moneycontrol.com/news/business/stocks/buy-tata-motors-target-of-rs-743-kr-choksey-11080811.html">Article 3</a></li>
    </ul>
    <h2>Project Structure</h2>
    <ul>
        <li><code>main.py</code>: The main Streamlit application script.</li>
        <li><code>requirements.txt</code>: A list of required Python packages for the project.</li>
        <li><code>faiss_store_openai.pkl</code>: A pickle file to store the FAISS index.</li>
        <li><code>.env</code>: Configuration file for storing your OpenAI API key.</li>
    </ul>

</body>
</html>
