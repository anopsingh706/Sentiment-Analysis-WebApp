
import streamlit as st 
from textblob import TextBlob 


from streamlit_extras.let_it_rain import rain 

st.title("A Sentiment Analysis WebApp .") 
st.text('developed by Anop Singh')

message = st.text_area("Please Enter your text") 
blob = TextBlob(message)

result = blob.sentiment


if st.button("Analyze the Sentiment"):
    blob = TextBlob(message)
    result = blob.sentiment
    polarity = result.polarity
    subjectivity = result.subjectivity

    if polarity < 0:
        st.warning("The entered text has negative sentiments associated with it: " + str(polarity))
        rain(
            emoji="😥",  # Replace with your desired emoji
            font_size=25,
            falling_speed=3,
            animation_length="infinite"
        )
    else:
        st.success("The entered text has positive sentiments associated with it: " + str(polarity))
        rain(
            emoji="😍",  # Replace with your desired emoji
            font_size=25,
            falling_speed=3,
            animation_length="infinite"
        )

st.success(result)

