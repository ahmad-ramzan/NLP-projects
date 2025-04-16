import spacy

# Load the pre-trained model for English
nlp = spacy.load("en_core_web_sm")

# Sample text
text = """
Apple Inc., one of the world’s leading technology companies, announced in a press release today that it is planning to acquire a small but promising startup based in the United Kingdom. The acquisition, worth a staggering $1 billion, is expected to close by the end of the year. Tim Cook, the CEO of Apple, mentioned in a statement that the company sees significant potential in the startup’s innovative technologies.

The acquisition will add to Apple’s expanding portfolio of AI-driven solutions, which includes products such as the iPhone, iPad, and Apple Watch. Apple, headquartered in Cupertino, California, has been actively investing in artificial intelligence, machine learning, and augmented reality in recent years.

Tim Cook further emphasized that the deal was part of Apple’s long-term strategy to enhance its services and hardware offerings. In the same statement, Cook also discussed the company’s efforts to reduce its carbon footprint, with plans to make all of its operations carbon neutral by 2030.

The United States tech industry is closely watching this acquisition, as it could mark a major shift in how large tech companies are acquiring smaller, innovative startups. Investors are particularly focused on the potential impact this will have on the stock market. Analysts expect that the deal will significantly strengthen Apple’s position in the tech sector globally.

The announcement comes just days after the release of the latest iPhone 13, which was unveiled at a highly anticipated event in Cupertino. This new model features advanced camera systems, a more powerful chip, and improved battery life. Many are speculating that the startup’s technology will be integrated into the next generation of Apple products.
"""

# Process the text using spaCy pipeline
doc = nlp(text)

# Extract entities
for entity in doc.ents:
    print(f"{entity.text} => {entity.label_}")
