from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import pandas as pd
from itertools import product

model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

prompt = "In the future, artificial intelligence will"

param_grid = {
    "temperature": [0.2, 0.5, 0.8, 1.2],
    "top_k": [10, 30, 50, 100],
    "max_length": [50, 100, 150]
}

results = []
for temp, top_k, max_len in product(param_grid["temperature"], param_grid["top_k"], param_grid["max_length"]):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    output = model.generate(input_ids, max_length=max_len, temperature=temp, top_k=top_k, do_sample=True, 
                            pad_token_id=tokenizer.eos_token_id)
    
    generated_text = tokenizer.decode(output[0], skip_speacial_tokens=True)

    results.append({"temperature": temp, "top_k": top_k, "max_length": max_len, "output": generated_text})

df = pd.DataFrame(results)
print(df[["temperature", "top_k", "max_length", "output"]].head())

df.to_csv('generation_experiments.csv', index=False)
print("\nSaved results to 'generation_experiments.csv'")