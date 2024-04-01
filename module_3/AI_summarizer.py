import google.generativeai as genai


def connect_to_gemini_api(api_key):
    genai.configure(api_key=api_key)

# def send_prompt_to_llm(prompt, article_content):

#     model = genai.GenerativeModel(model_name="gemini-1.0-pro")

#     convo = model.start_chat(history=[])

#     return convo.send_message(prompt + article_content)


def send_prompt_to_llm(prompt, article_content):
    model = genai.GenerativeModel(model_name="gemini-1.0-pro")
    convo = model.start_chat(history=[])
    
    response = convo.send_message(prompt + article_content)
    
    # Extracting the summary text from the response
    summary = response.candidates[0].content.parts[0].text

    return summary




