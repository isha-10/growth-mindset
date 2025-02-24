

import streamlit as st
from datetime import date

st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱", layout="centered")

st.title("🌱 Growth Mindset Challenge")

st.write("A growth mindset is the belief that your abilities and intelligence can be developed through hard work, perseverance, and learning from mistakes. Popularized by psychologist Carol Dweck, this mindset encourages us to see every challenge as a chance to learn and grow.")


st.header("💡 Today's Growth Mindset Quote?")
st.write("''success is a final, failure is not fatal: it is courage to continue that counts.''-winston churchill")


st.header( "💫  what's your challenge today?")
user_input = st.text_input("Describe a challenge you are facing:")

if user_input:
    st.success(f" you are facing:{user_input}.keep pushing forward towards your goals!")

else:
    st.warning("Tell us about your challenge to get started!")


st.header("📝 Reflect on Your Challenges")
reflection = st.text_area("Share a recent challenge you faced and what you learned from it:")
if reflection:
    st.success("Great reflection! Remember, every challenge is a learning opportunity.")
else:
    st.info("share your difficulties!")

st.header("🎯 Set Your Growth Goals")
goal = st.text_input("What is one learning goal you want to achieve this week?")
date_set = st.date_input("When do you plan to achieve this goal?", value=date.today())
if goal:
    st.info(f"Goal set: **{goal}** by **{date_set}**. Stay determined!")


st.header("📊 Growth Mindset Poll")
adopt_mindset = st.radio("Are you willing to adopt a growth mindset?", ("Yes", "Maybe", "Not yet"))
if adopt_mindset == "Yes":
    st.balloons()
    st.success("Fantastic! You're on the path to continuous growth.")
elif adopt_mindset == "Maybe":
    st.warning("Consider taking small steps to embrace a growth mindset.")
else:
    st.info("It's okay to take your time. Stay curious and open to growth.")


st.write("- - -")
("🚀 Remember, your educational journey is about developing your intelligence, not just proving it. Embrace your potential and never stop striving to be better!")
st.write("**created bi Isha khan**")
