from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.response_selection import get_first_response

bot = ChatBot(
    "Coco",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database="./dbBrain.sqlite3",
    input_adapter="chatterbot.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.output.OutputAdapter",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "response_selection_method": get_first_response
        }
    ]
)


with open("C:/Users/jonat/Desktop/work/Coco BOT/training.txt") as f:
    conversation = f.readlines()
    trainer = ListTrainer(bot)
    trainer.train(conversation)


while True:
    try:
        user_input = input("Tu: ")
        response = bot.get_response(user_input)
        print("Coco: ", response)
    except(KeyboardInterrupt, SystemExit):
        print("A presto!")
        break
