train_data = [
    ("I got full marks in the test today!", "Happy"),
    ("We won the college cricket match", "Happy"),
    ("My friends planned a surprise party for me", "Happy"),
    ("The food in the canteen was really tasty", "Happy"),
    ("I am so excited for the weekend trip", "Happy"),
    ("Our project got selected for the exhibition", "Happy"),
    ("I finally learned how to ride a bicycle", "Happy"),
    ("Mom made my favourite sweets today", "Happy"),
    ("I lost my phone on the bus", "Sad"),
    ("I failed in the mathematics exam", "Sad"),
    ("My best friend is moving to another city", "Sad"),
    ("It rained and our picnic was cancelled", "Sad"),
    ("I missed the last bus and felt very upset", "Sad"),
    ("My laptop stopped working before the submission", "Sad"),
    ("I felt lonely during the long holidays", "Sad"),
]
def count_moods(data):
    happy_count = 0
    sad_count = 0

    for sentence, mood in data:
        if mood == "Happy":
            happy_count += 1
        elif mood == "Sad":
            sad_count += 1

    return happy_count, sad_count


print("LEVEL 1: COUNT THE MOODS")
print("Mood Count:", count_moods(train_data))
happy_words = ["marks", "won", "surprise", "tasty", "excited"]
sad_words = ["lost", "failed", "moving", "cancelled", "upset"]


def clean_sentence(sentence):
    cleaned = ""

    for char in sentence.lower():
        if char.isalnum() or char.isspace():
            cleaned += char
        else:
            cleaned += " "

    return cleaned.split()


def guess_mood(sentence):
    words = clean_sentence(sentence)

    happy_score = 0
    sad_score = 0

    for word in words:
        if word in happy_words:
            happy_score += 1

        if word in sad_words:
            sad_score += 1

    if happy_score > sad_score:
        return "Happy"
    elif sad_score > happy_score:
        return "Sad"
    else:
        return "Sad"

practice_data = [
    ("I won a medal in the sports meet", "Happy"),
    ("I lost my notebook before the exam", "Sad"),
    ("My friends gave me a lovely surprise", "Happy"),
    ("The train waslate and I felt upset", "Sad"),
    ("Today was a great day", "Happy"),
]

print("\nLEVEL 2: MOOD PREDICTIONS")

correct = 0

for sentence, actual_mood in practice_data:
    predicted_mood = guess_mood(sentence)

    print("\nSentence:", sentence)
    print("Actual Mood:", actual_mood)
    print("Predicted Mood:", predicted_mood)

    if predicted_mood == actual_mood:
        correct += 1

accuracy = (correct / len(practice_data)) * 100

print("\nLEVEL 3: TEST RESULTS")
print("Correct Predictions:", correct)
print("Total Sentences:", len(practice_data))
print("Accuracy:", accuracy, "%")

def learn_scores(data):
    scores = {}

    for sentence, mood in data:
        words = clean_sentence(sentence)

        for word in words:
            if word not in scores:
                scores[word] = 0

            if mood == "Happy":
                scores[word] += 1
            elif mood == "Sad":
                scores[word] -= 1

    return scores


def guess_mood_learned(sentence):
    scores = learn_scores(train_data)

    total_score = 0

    for word in clean_sentence(sentence):
        total_score += scores.get(word, 0)

    if total_score > 0:
        return "Happy"
    else:
        return "Sad"

learned_correct = 0

print("\nBONUS: LEARNED MOOD PREDICTIONS")

for sentence, actual_mood in practice_data:
    predicted = guess_mood_learned(sentence)

    print("\nSentence:", sentence)
    print("Actual Mood:", actual_mood)
    print("Learned Prediction:", predicted)

    if predicted == actual_mood:
        learned_correct += 1

learned_accuracy = (
    learned_correct / len(practice_data)
) * 100

print("\nLEARNED MODEL ACCURACY:", learned_accuracy, "%")

print("\nCOMPARISON")
print("Level 2 Accuracy:", accuracy, "%")
print("Learned Model Accuracy:", learned_accuracy, "%")


