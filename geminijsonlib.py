import google.generativeai as genai

def gemini_json(system_prompt, user_prompt, model_name='gemini-1.5-pro-latest'):
    # Configure the Gemini API key
    api_key = "YOUR_API_KEY_HERE"
    genai.configure(api_key=api_key)

    # Create model instance
    model = genai.GenerativeModel(model_name)

    # Combine system prompt and user prompt
    combined_prompt = f"{system_prompt}\n\n{user_prompt}"

    # Generate content
    try:
        response = model.generate_content(
            combined_prompt,
            generation_config={
                "temperature": 0.9,
                "top_p": 1,
                "top_k": 1,
                "max_output_tokens": 2048,
            },
            safety_settings=[
                {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            ],
            stream=False,
        )
        
        # Print response
        print(response.text)
        return response.text
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
system_prompt = "give me a name, salary mothers origin country fathers origin country."
user_prompt = "top 10 footballers"

result = gemini_json(system_prompt, user_prompt)
