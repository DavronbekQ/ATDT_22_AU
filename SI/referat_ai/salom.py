from huggingface_hub import InferenceClient

client = InferenceClient(api_key="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")

messages = [
	{ "role": "user", "content": "qayerdansiz" }
]

output = client.chat.completions.create(
    model="meta-llama/Llama-3.1-8B-Instruct", 
	messages=messages, 
	stream=False, 
	temperature=0.5,
	max_tokens=1024,
	top_p=0.7
)

for chunk in output:
    print(chunk.choices[0].delta.content)