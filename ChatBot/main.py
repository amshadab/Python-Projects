from hugchat import hugchat

def chatBot(query):
    try:
        user_input = query.lower()
        chatbot = hugchat.ChatBot(cookie_path="cookies.json")
        conversation_id = chatbot.new_conversation()
        chatbot.change_conversation(conversation_id)
        response = chatbot.chat(user_input)
        return response
    except Exception as e:
        return f"An error occurred: {e}"
    

if __name__=="__main__":
    user=input("You: ")
    
    r=chatBot(user)
    print("Bot: ",r)
    