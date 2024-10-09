from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as ggi

ggi.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = ggi.GenerativeModel("gemini-1.5-pro-latest")
chat = model.start_chat()

def LLM_Response(question):
    prompt = f"""Provide a relevant 2-line quote with the author's name along with a concise 3-4 sentence description in response to the following:

    **Prompt:** {question}

    **Answer Format:**

    **Author:** Author Name
    
    **Quote:**
        Quote

    **Description:**
        Concise description

    **Additional Notes:**
        Please ensure the quote and description are directly relevant to the prompt and provide valuable insights.
    """
    response = chat.send_message(
        prompt
    )
    return response

st.title("The Quote Whisperer")

user_quest = st.text_input("Ask me Something?")
btn = st.button("Generate")

if btn and user_quest:
    result = LLM_Response(user_quest)

    # Display response in a more readable way
    st.markdown(''.join([token.text for token in result]))

    # Display metadata
    st.sidebar.title("Metadata")
    st.sidebar.markdown(f"**Prompt Token Count:** {result.usage_metadata.prompt_token_count}")
    st.sidebar.markdown(f"**Candidates Token Count:** {result.usage_metadata.candidates_token_count}")
    st.sidebar.markdown(f"**Total Token Count:** {result.usage_metadata.total_token_count}")

    # Print for debugging
    print(f"Result: {result}")