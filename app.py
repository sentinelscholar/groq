import os
import streamlit as st
from groq import Groq 

# Initialize your Groq client with the appropriate API key
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def main():
    st.title('Graduate School Recommendation App')

    # Get user preferences
    research_interests = st.text_input('What are your research interests?')
    sub_field = st.text_input('Specify any sub-field or technology you are particularly interested in:')
    university_attributes = st.selectbox('Select preferred attributes for universities:', ['High research activity', 'Strong industry connections', 'Internationally renowned', 'Small cohort sizes'])

    preferred_location = st.selectbox('Preferred location for graduate studies?', 
                                      ['Any', 'USA', 'Europe', 'Asia', 'Other'])
    degree_type = st.selectbox('Type of degree', ['Masters', 'PhD', 'Post Baccalaureate'])
    field_of_study = st.text_input('Field of study?')
    other_preferences = st.text_input('Any other preferences (e.g., faculty-to-student ratio, collaboration opportunities):')


    if st.button('Get Recommendations'):
        if research_interests and field_of_study:
            # Enhanced query with more detail
            query = f"Please provide detailed information about {degree_type} programs in {field_of_study}, with a specific focus on {research_interests}. I am particularly interested in programs that excel in areas such as {sub_field}. I am looking at universities located in {preferred_location}, preferably those known for {university_attributes} in the field of {field_of_study}. Additional considerations include {other_preferences}. Please also provide information about the program duration, tuition, and notable alumni."

            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": query}],
                model="llama3-70b-8192",  # Ensure you specify the correct model
            )

            # Display the response from the Groq API
            if chat_completion and chat_completion.choices:
                response = chat_completion.choices[0].message.content
                st.subheader("Faculty Recommendations")
                st.text_area("Details", value=response, height=300)
            else:
                st.error('No recommendations found. Please try different preferences.')
        else:
            st.warning('Please enter all required fields to get recommendations.')

if __name__ == '__main__':
    main()
