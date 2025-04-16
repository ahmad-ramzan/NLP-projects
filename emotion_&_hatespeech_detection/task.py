# -*- coding: utf-8 -*-
"""practice.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19vZzEMB-fmTEcmrk5Fka98KSgGnuIcfb
"""

!pip install pysentimiento

from pysentimiento import create_analyzer

emotion = create_analyzer(task='emotion',lang='en')
hatespeech = create_analyzer(task='hate_speech', lang='en')

emo = emotion.predict("get out of my sight")
hat = hatespeech.predict("I hate eating apples. that's why i don't want to sit with appple seller")

print(emo.output)
print(hat.probas.items())

text = """I woke up this morning feeling incredibly happy and grateful for the beautiful weather outside.
 The sun was shining, birds were singing, and there was a gentle breeze in the air. It felt like the
 perfect day to go for a long walk in the park."""

emo = emotion.predict(text)
hat = hatespeech.predict(text)

print(emo.output)
print(next(iter(hat.probas.items()),None))