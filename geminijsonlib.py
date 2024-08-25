import google.generativeai as genai
import json

def gemini_json(system_prompt, user_prompt, model_name='gemini-1.5-pro-latest'):
    # Configure the Gemini API key
    api_key = ""
    genai.configure(api_key=api_key)

    # Create model instance
    model = genai.GenerativeModel(model_name)

    # Combine prompts
    combined_prompt = f"""
    System: {system_prompt}
    User: {user_prompt}
    Instructions: Provide your response as a valid JSON object.
    """

    # Generate content
    try:
        response = model.generate_content(
            combined_prompt,
            generation_config={
                "temperature": 0.7,
                "top_p": 1,
                "top_k": 1,
                "max_output_tokens": 2048,
                "response_mime_type": "application/json"  # This ensures JSON output
            },
            safety_settings=[
                {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            ],
            stream=False,
        )
        
        # The response should already be in JSON format
        json_response = json.loads(response.text)
        return json_response
        
    except json.JSONDecodeError:
        print("The response could not be parsed as JSON. Here's the raw response:")
        print(response.text)
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
system_prompt = "You are a helpful assistant that provides information about footballers."
user_prompt = "Give me information about the top 5 footballers including their name, salary, mother's origin country, and father's origin country."

result = gemini_json(system_prompt, user_prompt)
if result:
    print(json.dumps(result, indent=2))
