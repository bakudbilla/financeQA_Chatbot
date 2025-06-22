# financeQA_Chatbot
This project develops a domain-specific Finance QA chatbot powered by the GPT-2 language model, fine-tuned on the Financial-QA-10k dataset from Hugging Face. The dataset contains 10,000 question-answer pairs extracted from company 10-K financial reports, covering a broad spectrum of topics related to financial analysis, company operations, and strategic insights. Each entry includes the question, answer, context, company stock ticker, and filing year, providing rich, domain-specific information. By training GPT-2 on this dataset, the chatbot generates coherent and contextually relevant responses, enabling it to effectively assist users with complex financial queries and improve access to financial knowledge.

The project’s goals were to preprocess the Financial-QA-10k dataset for GPT-2 fine-tuning, train the model to generate accurate and coherent financial responses, and deploy it through an easy-to-use Streamlit interface. Model performance was evaluated quantitatively using perplexity (~2.61) to measure syntactic and semantic accuracy, alongside qualitative assessments based on sample user interactions.

![Image](https://github.com/user-attachments/assets/0898b8ee-463a-406d-b036-6e60be117a98)

# Dataset Structure 
Rows: 7000
Columns: 5
question: The financial or operational question asked.
answer: The specific answer to the question.
context: The textual context extracted from the 10-K filing, providing additional information.
ticker: The stock ticker symbol of the company.
filing: The year of the 10-K filing from which the question and answer are derived.

# How to Run the Chatbot
You can interact with the model in two ways:

Option 1: Hugging Face Spaces (Gradio)
Live Demo: https://huggingface.co/spaces/Awinpang/financeQA_chatbot

The Hugging Face Model can also be found here: https://huggingface.co/Awinpang/financeQA_chatbot

No installation needed — just visit the link and start chatting.

Option 2: Run Locally
Clone this repo:
```
git clone https://huggingface.co/spaces/Awinpang/financeQA_chatbot
cd financeQA_chatbot

```
Install requirements:
```
pip install -r requirements.txt

```
Launch the app:
```
python app.py
```
# Sample Conversations
**Q:** What is the role of cryptocurrency in modern finance?  
**A:** Digital currencies are used to facilitate transactions, facilitate payments, and facilitate the exchange of assets and liabilities. They are also used by financial institutions to protect against fraud and other risks.

---

**Q:** Why is the stock market affected by inflation?  
**A:** The inflationary impact of inflation on the U.S. dollar is primarily due to higher interest rates, higher commodity prices, and higher foreign exchange rates.

---

**Q:** Define what a stock means in simple terms.  
**A:** A stock refers to a company's financial condition and results of operations.

---

**Q:** What are the benefits of investing in bonds?  
**A:** Bonds are a diversified portfolio of assets that can be invested in various types of investments, including bonds, notes, and options. They can also be sold or repurchased.

---

**Q:** How does interest rate affect loan repayments?  
**A:** Interest rate is influenced by factors such as interest rates, the timing of interest payments, and the maturity date of the loan.

