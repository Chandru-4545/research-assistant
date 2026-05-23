import gradio as gr
from ingest import ingest_pdf
from query import ask_question

def handle_upload(file):
    ingest_pdf(file.name)
    return "✅ Document uploaded and processed!"

def handle_query(question):
    return ask_question(question)

with gr.Blocks(title="Research Assistant") as demo:
    gr.Markdown("# 📄 AI Research Assistant")
    with gr.Row():
        upload = gr.File(label="Upload PDF")
        upload_btn = gr.Button("Process Document")
    status = gr.Textbox(label="Status")
    upload_btn.click(handle_upload, inputs=upload, outputs=status)

    gr.Markdown("### Ask a Question")
    question = gr.Textbox(label="Your Question")
    answer = gr.Textbox(label="Answer")
    ask_btn = gr.Button("Ask")
    ask_btn.click(handle_query, inputs=question, outputs=answer)

demo.launch()