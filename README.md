## abbreviations-generation
Author: Matthew Burnard

Project for generating abbreviations in multiple languages

# Installation
Create a python virtual environment and install the requirements
```python -m venv venv
source venv/bin/activate
pip install -r requirements.txt```
Make a models directory
```mkdir models```
Train
```python -m joeynmt train abbreviations-generation.yaml```
Test
```python -m joeynmt test abbreviations-generation.yaml --output preds```
Direct translation test
```python -m joeynmt translate abbreviations-generation.yaml```
