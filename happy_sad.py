happy_words = ["happy", "joy", "excited", "love", "wonderful",
               "great", "awesome", "smile", "good", "amazing"]

sad_words = ["sad", "cry", "upset", "lonely", "bad",
             "terrible", "angry", "hurt", "unhappy", "depressed"]

sentence = input("Enter a sentence: ").lower()

happy_count = 0
sad_count = 0

words = sentence.split()

for word in words:
    word = word.strip(".,!?")

    if word in happy_words:
        happy_count += 1
    elif word in sad_words:
        sad_count += 1

if happy_count > sad_count:
    print("Prediction: Happy 😊")
elif sad_count > happy_count:
    print("Prediction: Sad 😢")
else:
    print("Prediction: Neutral 😐")
