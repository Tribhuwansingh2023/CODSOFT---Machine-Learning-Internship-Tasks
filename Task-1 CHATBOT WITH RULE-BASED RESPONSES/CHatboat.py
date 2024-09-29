# Rule-based Chatbot Function  
def chatbot_response(user_input):  
    user_input = user_input.lower()  # Convert to lowercase for matching  
    
    # Define responses based on user input
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a program, but thanks for asking! How can I assist you?"
    elif "what is your name" in user_input:
        return "I am a simple rule-based chatbot. You can call me ChatBot!"
    elif "help" in user_input:
        return "Sure! I can help with general information or answer any questions you might have."
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    elif "what can you do" in user_input:
        return "I can assist with general information, answer questions, and provide basic conversation."
    elif "who created you" in user_input:
        return "I was created by a developer to assist with basic tasks and provide information."
    elif "what is your purpose" in user_input:
        return "My purpose is to assist users with general information and provide basic conversation."
    elif "can you tell me a joke" in user_input:
        return "Why was the math book sad? Because it had too many problems."
    elif "what is the capital of france" in user_input:
        return "The capital of France is Paris."
    elif "what is the largest planet in our solar system" in user_input:
        return "The largest planet in our solar system is Jupiter."
    elif "what is the smallest country in the world" in user_input:
        return "The smallest country in the world is Vatican City."
    elif "what is the largest living thing on earth" in user_input:
        return "The largest living thing on earth is a fungus called Armillaria ostoyae."
    elif "what is the highest mountain in the world" in user_input:
        return "The highest mountain in the world is Mount Everest, located in the Himalayas."
    elif "what is the deepest ocean" in user_input:
        return "The deepest ocean is the Pacific Ocean, with a maximum depth of about 36,000 feet."
    elif "what is the longest river in the world" in user_input:
        return "The longest river in the world is the Nile River, located in northeastern Africa."
    elif "what is the largest mammal on earth" in user_input:
        return "The largest mammal on earth is the blue whale."
    elif "what is the fastest land animal" in user_input:
        return "The fastest land animal is the cheetah, which can reach speeds of up to 70 mph."
    elif "what is the largest bird in the world" in user_input:
        return "The largest bird in the world is the ostrich."
    elif "what is the smallest bird in the world" in user_input:
        return "The smallest bird in the world is the bee hummingbird."
    elif "what is the longest word in the english language" in user_input:
        return "The longest word in the English language is pneumonoultramicroscopicsilicovolcanoconiosis."
    elif "what is the shortest word in the english language" in user_input:
        return "The shortest word in the English language is 'a'."
    elif "what is the most spoken language in the world" in user_input:
        return "The most spoken language in the world is Mandarin Chinese."
    elif "what is the most widely used programming language" in user_input:
        return "The most widely used programming language is JavaScript."
    elif "what is the most popular social media platform" in user_input:
        return "The most popular social media platform is Facebook."
    elif "what is the most popular search engine" in user_input:
        return "The most popular search engine is Google."
    elif "what is the most popular web browser" in user_input:
        return "The most popular web browser is Google Chrome."
    elif "what is the most popular operating system" in user_input:
        return "The most popular operating system is Windows."
    elif "what is the most popular database management system" in user_input:
        return "The most popular database management system is MySQL."
    elif "what is the most popular framework for building web applications" in user_input:
        return "The most popular framework for building web applications is React."
    elif "what is the most popular framework for building mobile applications" in user_input:
        return "The most popular framework for building mobile applications is React Native."
    elif "what is the most popular language for building artificial intelligence" in user_input:
        return "The most popular language for building artificial intelligence is Python."
    elif "what is the most popular platform for building machine learning models" in user_input:
        return "The most popular platform for building machine learning models is TensorFlow."
    elif "what is the most popular platform for building natural language processing models" in user_input:
        return "The most popular platform for building natural language processing models is NLTK."
    elif "what is the most popular platform for building computer vision models" in user_input:
        return "The most popular platform for building computer vision models is OpenCV."
    elif "what is the most popular platform for building robotics" in user_input:
        return "The most popular platform for building robotics is ROS."
    elif "what is the most popular platform for building internet of things" in user_input:
        return "The most popular platform for building internet of things is Arduino."
    elif "what is the most popular platform for building cloud computing" in user_input:
        return "The most popular platform for building cloud computing is AWS."
    elif "what is the most popular platform for building cybersecurity" in user_input:
        return "The most popular platform for building cybersecurity is Kali Linux."
    elif "what is the most popular platform for building data science" in user_input:
        return "The most popular platform for building data science is pandas."
    elif "what is the most popular platform for building business intelligence" in user_input:
        return "The most popular platform for building business intelligence is Tableau."
    elif "what is the most popular platform for building customer relationship management" in user_input:
        return "The most popular platform for building customer relationship management is Salesforce."
    elif "what is the most popular platform for building enterprise resource planning" in user_input:
        return "The most popular platform for building enterprise resource planning is SAP."
    elif "what is the most popular platform for building human resource management" in user_input:
        return "The most popular platform for building human resource management is Workday."
    elif "what is the most popular platform for building supply chain management" in user_input:
        return "The most popular platform for building supply chain management is Oracle."
    elif "what is the most popular platform for building marketing automation" in user_input:
        return "The most popular platform for building marketing automation is Marketo."
    elif "what is the most popular platform for building sales automation" in user_input:
        return "The most popular platform for building sales automation is HubSpot."
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Chat Loop
def chat():
    print("Welcome to the ChatBot! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")  # Get input from the user
        response = chatbot_response(user_input)  # Get the chatbot's response
        print("ChatBot:", response)  # Print the response

        if "bye" in user_input.lower():
            break  # Exit the loop if the user says bye

# Start the chatbot
chat()