# pip install language-tool-python

from textblob import TextBlob
import language_tool_python

def analyze_text(text):
    print("🔹 Original Text:\n", text)
    
    # TextBlob: Sentiment Analysis & Spelling Correction
    blob = TextBlob(text)
    sentiment = blob.sentiment
    corrected_by_textblob = blob.correct()
    
    # LanguageTool: Grammar Correction
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    corrected_by_languagetool = language_tool_python.utils.correct(text, matches)

    # Results
    print("\n🔸 Sentiment Analysis:")
    print(f"  Polarity: {sentiment.polarity} (−1 = negative, +1 = positive)")
    print(f"  Subjectivity: {sentiment.subjectivity} (0 = objective, 1 = subjective)")

    print("\n🔸 TextBlob Spelling Correction:")
    print(corrected_by_textblob)

    print("\n🔸 LanguageTool Grammar Correction:")
    print(corrected_by_languagetool)

# Example usage
sample_text = "I realy like this movy. It was very intresting and have great actor."
analyze_text(sample_text)
