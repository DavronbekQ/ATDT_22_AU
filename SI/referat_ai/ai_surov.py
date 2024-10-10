# from hugchat import hugchat
# from hugchat.login import Login

# # Log in to huggingface and grant authorization to huggingchat

from g4f.client import Client

def gpt_surov(referat_mavzu):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"{referat_mavzu} - mavzusida maqola yoz, maqola o'zbek tilida bo;'lsin"}],
    )
    javob = response.choices[0].message.content
    return javob 
print(gpt_surov("Alisher Navoiy"))