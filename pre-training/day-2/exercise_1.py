from typing import Dict

def word_frequency(text) -> Dict[str, int]:
    # Remove punctuation and convert to lowercase
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum() or char.isspace())
    words = cleaned_text.split()
    
    frequency = {}
    for word in words:
        if(frequency.get(word)):
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

paragraph = """
                In the heart of the bustling city,
                there was a small café that everyone loved. 
                The aroma of freshly brewed coffee filled the air, 
                and the sound of laughter and chatter created a warm atmosphere. 
                People from all walks of life would gather there, 
                sharing stories and enjoying each other's company. 
                The café was more than just a place to get a drink; 
                it was a sanctuary where friendships blossomed and memories were made.
            """

word_counts = word_frequency(paragraph)
top_5 = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:5]

for word, count in top_5:
    print(f"{word}: {count}")
