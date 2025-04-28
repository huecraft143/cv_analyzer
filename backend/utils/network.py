from gradio_client import Client

def contact_api(message):
    client = Client("huecraft143/cv_analyzer")
    result = client.predict(
            message,
            system_message="You are a friendly Chatbot.",
            max_tokens=2048,
            temperature=0.7,
            top_p=0.95,
            api_name="/chat"
    )
    return result