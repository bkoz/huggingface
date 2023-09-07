from transformers import pipeline
import gradio as gr


def predict(prompt):
    return classifier([prompt])

if __name__ == "__main__":

    classifier = pipeline("sentiment-analysis")

    examples = ["The book was well written with an exciting plot."]
    demo = gr.Interface(fn=predict, inputs="text", outputs="text", examples=examples)
    demo.launch()