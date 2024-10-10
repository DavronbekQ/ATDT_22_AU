from hugchat import hugchat
from hugchat.login import Login

# Log in to huggingface and grant authorization to huggingchat
EMAIL = "xamrayevbek96@gmail.com"
PASSWD = "$alo3laR"
cookie_path_dir = "./cookies/" # NOTE: trailing slash (/) is required to avoid errors
sign = Login(EMAIL, PASSWD)
cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)

# Create your ChatBot
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"
#while True:

# user_input = input("savolni kiriting! :")
# message_result = chatbot.chat(user_input) # note: message_result is a generator, the method will return immediately.
# print(message_result)

def ai_savol(savol):
    message_result = chatbot.chat(savol) # note: message_result is a generator, the method will return immediately.
    return message_result
print(ai_savol("salom"))