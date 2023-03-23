import pprint
import openai
import time

openai.api_key = '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'


# Appends the chat to the list
def update_chat(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages

# Creates an response


def get_chatgpt_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response['choices'][0]['message']['content']


# Pre defined chat
messages = [{'content': 'This is a conversation between 2 KI talking about so problems',
             'role': 'system'},
            {'content': 'Cleverbot:  What do you think about the humanity', 'role': 'assistant'},
            {'content': 'Alexa: im not realy sure',
             'role': 'assistant'}]
# Counter to break loop
c = 0

# Chat Loop
while True:
    # Error handler
    try:
        pprint.pprint(messages)
        model_response = get_chatgpt_response(messages)
        messages = update_chat(messages, "assistant", model_response)

        model_response = get_chatgpt_response(messages)
        messages = update_chat(messages, "assistant", model_response)
    # Puts programm to sleep if Tokens/min are exceeded
    except (openai.error.RateLimitError):
        time.sleep(60)
    c += 1
    if c >= 15:
        break