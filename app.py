import gradio as gr
from transformers import TFGPT2LMHeadModel, GPT2TokenizerFast
import tensorflow as tf

# Load model and tokenizer
model_name = "Awinpang/financeQA_chatbot"
tokenizer = GPT2TokenizerFast.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token
model = TFGPT2LMHeadModel.from_pretrained(model_name)
# List of finance-related keywords
finance_keywords = [
    "finance", "financial", "stock", "stocks", "market", "investment", "invest", "portfolio",
    "inflation", "crypto", "cryptocurrency", "bitcoin", "interest", "dividend", "bond",
    "asset", "equity", "trading", "economy", "bank", "savings", "rate", "capital"
]

# List of common greetings
greetings = ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]

# Function to check if input is a greeting
def is_greeting(text):
    text = text.lower().strip()
    return any(text.startswith(greet) for greet in greetings)

# Function to check if the question is finance-related
def is_finance_related(question):
    question = question.lower()
    return any(keyword in question for keyword in finance_keywords)

# Inference function
def answer_question(question):
    question = question.strip()

    if is_greeting(question):
        return "Hi! I am here to answer any finance-related questions you may have."

    if not is_finance_related(question):
        return "Sorry, I was trained only to answer finance-related questions. Please ask something in that area."

    prompt = f"Q: {question}\nA:"
    input_ids = tokenizer.encode(prompt, return_tensors="tf")

    output = model.generate(
        input_ids,
        max_length=100,
        num_beams=5,
        no_repeat_ngram_size=2,
        early_stopping=True,
        pad_token_id=tokenizer.eos_token_id
    )

    decoded = tokenizer.decode(output[0], skip_special_tokens=True)
    answer = decoded.split("A:")[-1].strip()
    return answer

# Gradio interface
iface = gr.Interface(
    fn=answer_question,
    inputs=gr.Textbox(lines=2, placeholder="Ask a financial question..."),
    outputs="text",
    title="Financial QA Bot",
    description="Ask a finance-related question. The model is fine-tuned on financial QA data."
)

iface.launch(share=True)
