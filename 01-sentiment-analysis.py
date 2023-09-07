from transformers import pipeline
import gradio as gr

classifier = pipeline("sentiment-analysis")

def predict(prompt):
    return classifier([prompt])

examples = ["The book was well written with an exciting plot."]
demo = gr.Interface(fn=predict, inputs="text", outputs="text", examples=examples)
demo.launch()