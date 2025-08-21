from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
    "AI Chatbot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.BestMatch"
    ],
    tagger_language=None  # 👈 disables spaCy
)

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

while True:
    user_input = input("You: ")
    response = chatbot.get_response(user_input)
    print("Bot:", response)

