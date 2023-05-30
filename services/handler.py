def handle_response(text:str) -> str:
    text = text.lower()
    if 'hello' in text:
        return 'Hello There..'
    
    if 'how are you' in text:
        return 'I am good'
    
    return 'I do not understand you.'