import time
from gpt4all import GPT4All

model = GPT4All(model_name="Meta-Llama-3-8B-Instruct.Q4_0.gguf") # downloads / loads a 4.66GB LLM
tokens = 20
words_in_answer = 10
prompt_snippet = "Answer in " + str(words_in_answer) + " words or less."

wake_word_gpt = "GPT"

def gpt():
    with model.chat_session():
        prompt = input("Prompt: ")
        start = time.time()
        print(model.generate(prompt + prompt_snippet, max_tokens=tokens))
        end = time.time()
        print("Generation took " + str(end-start) + " seconds.")

def main():
    while(True):
        wake_word = input("Waiting for wake-word...\n")
        if(wake_word == wake_word_gpt):
            gpt()
        else:
            print("That's no wake-word.")

main()