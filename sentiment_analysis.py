"""
A simple HuggingFace/Gradio program.
"""

from transformers import pipeline
import gradio as gr


def predict(prompt: str) -> list:
    """Predict the sentiment
    Args:
        prompt (str): The input prompt.

    Returns:
        list: A list of positive or negative sentiments and their probabilities.
    """
    return classifier([prompt])


if __name__ == "__main__":
    classifier = pipeline("sentiment-analysis")

    examples = [
        "The book was well written with an exciting plot.",
        "I could barely stay awake as I read the first chapter.",
    ]
    demo = gr.Interface(fn=predict, inputs="text", outputs="text", examples=examples)
    demo.launch()
