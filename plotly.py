import streamlit as st
import plotly.express as px
import openai
import pandas as pd

# Set OpenAI API Key
openai.api_key = "openai_api_key'

# ChatGPT function to generate responses
def get_chatgpt_response(prompt):
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {e}"

# Streamlit page configuration
st.set_page_config(page_title="ChatGPT + Plotly", layout="wide")

# Sidebar with user input
st.sidebar.header("ChatGPT + Plotly App")
user_input = st.sidebar.text_area("Ask ChatGPT:", "Enter your question here.")

# Main content
st.title("Interactive ChatGPT + Plotly Dashboard")

# Load some sample data (you can replace this with your dataset)
df = pd.DataFrame({
    "Fruit": ["Apple", "Banana", "Cherry", "Date", "Elderberry"],
    "Quantity": [10, 15, 7, 12, 5],
    "Price": [1.2, 0.5, 2.5, 3.0, 5.0]
})

# Plotly bar chart for visualization
fig = px.bar(df, x='Fruit', y='Quantity', title="Fruit Quantity")
st.plotly_chart(fig)

# Show the ChatGPT response
if user_input:
    response = get_chatgpt_response(user_input)
    st.write(f"**ChatGPT's Answer:** {response}")
else:
    st.write("Ask a question in the sidebar to interact with ChatGPT.")

# Add some more interactivity (e.g., scatter plot)
fig2 = px.scatter(df, x="Quantity", y="Price", color="Fruit", title="Price vs Quantity")
st.plotly_chart(fig2)

# Footer
st.write("This app uses **ChatGPT** to provide intelligent responses to user questions and **Plotly** to generate interactive charts.")
