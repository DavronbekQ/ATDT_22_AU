import openai
import os

# Set up the OpenAI API key
openai.api_key = "YOUR_API_KEY"

def get_cybersecurity_assistance(query):
    """
    Function to get assistance from the AI chatbot for cybersecurity related tasks.
    :param query: The user's query or request for assistance.
    :return: The AI chatbot's response with assistance.
    """
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Provide cybersecurity assistance for the following query: {query}\n\nAssistance:",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Main program loop
while True:
    query = input("Ask me for cybersecurity assistance or type 'quit' to exit: ")
    if query.lower() == 'quit':
        break
    
    assistance = get_cybersecurity_assistance(query)
    print("Assistance:", assistance)``