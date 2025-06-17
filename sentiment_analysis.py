import streamlit as st
import pandas as pd
from textblob import TextBlob


from streamlit_extras.let_it_rain import rain

st.title("Reviews Sentiment Analysis For Amazon Fine Food App.")

message = st.text_area("Please Enter your text")

if st.button("Analyze the Sentiment"):
  blob = TextBlob(message)
  result = blob.sentiment
  polarity = result.polarity
  subjectivity = result.subjectivity
  if polarity < 0:
    st.warning("The entered text has negative sentiments associated with it"+str(polarity))
    rain(
    emoji="????",
    font_size=20,  # the size of emoji
    falling_speed=3,  # speed of raining
    animation_length="infinite",  # for how much time the animation will happen
)
  if polarity >= 0:
    st.success("The entered text has positive sentiments associated with it."+str(polarity))
    rain(
    emoji="????",
    font_size=20,  # the size of emoji
    falling_speed=3,  # speed of raining
    animation_length="infinite",  # for how much time the animation will happen
    )
  st.success(result)

with st.expander('Analyze CSV'):
  upl = st.file_uploader('Upload file')


  def score(x):
      blob1 = TextBlob(x)
      return blob1.sentiment.polarity

  def analyze(x):
      if x >= 0.5:
        return 'Positive'
      elif x <= -0.5:
        return 'Negative'
      else:
        return 'Neutral'


    #
  if upl:
      df = pd.read_excel(upl)
      del df['Unnamed: 0']
      df['score'] = df['tweets'].apply(score)
      df['analysis'] = df['score'].apply(analyze)
      st.write(df.head(10))


      @st.cache
      def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
          return df.to_csv().encode('utf-8')


      csv = convert_df(df)

      st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='sentiment.csv',
        mime='text/csv',
      )