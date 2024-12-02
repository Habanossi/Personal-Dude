from gpt4all import GPT4All
import time

model = GPT4All(model_name="Meta-Llama-3-8B-Instruct.Q4_0.gguf") # downloads / loads a 4.66GB LLM
tokens = 20
words_in_answer = 10
prompt_snippet = "Answer in " + str(words_in_answer) + " words or less."

with model.chat_session():
    while(True):
        start = time.time()
        print(model.generate(input("Prompt: ") + prompt_snippet, max_tokens=tokens))
        end = time.time()
        print("Generation took " + str(end-start) + " seconds.")
