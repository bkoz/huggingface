"""
A simple HuggingFace/Gradio program.
"""

from transformers import pipeline
import gradio as gr


def predict(prompt: list) -> list:
    """Predict the sentiment
    Args:
        prompt (list): A list of prompts as inputs.

    Returns:
        list: A list positive or negative sentiments and their probabilities.
    """
    return classifier([prompt])

if __name__ == "__main__":

    classifier = pipeline("sentiment-analysis")

    examples = ["The book was well written with an exciting plot."]
    demo = gr.Interface(fn=predict, inputs="text", outputs="text", examples=examples)
    demo.launch()