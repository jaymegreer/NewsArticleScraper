import google.generativeai as genai


def connect_to_gemini_api(api_key): #connects to the ai -- using the configure function from the genai module
    genai.configure(api_key=api_key) #configures the API key to use the AI


def send_prompt_to_llm(prompt, article_content):
    model = genai.GenerativeModel(model_name="gemini-1.0-pro") #creates an instance of the GenerativeModel class from the genai module
    convo = model.start_chat(history=[]) #initiates a conversation with the ai and initializes an empty conversation history
    
    response = convo.send_message(prompt + article_content) #sends the wanted message to the generative model within the conversation

    summary = response.candidates[0].content.parts[0].text #extracts the summary text from the response

    return summary




