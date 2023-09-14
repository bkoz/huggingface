# Experiment with HuggingFace in Openshift DevSpaces

- Create a [Red Hat Developer Sandbox](https://developers.redhat.com)
- Login to Openshift and open the DevSpaces Dashboard (see the 3x3 menu in the upper right).
- Create a new workspace by importing this repo.
- Run the task to create a new Python virtual environment:
  - View => Command Pallette => run task => devfile => Configure Python.
  - Add the Microsoft Itellisense (Pylance) extension for Python to vscode.
  - Open the example Gradio Python client and run it.
  - A dialog should appear to port-forward port 7860.
