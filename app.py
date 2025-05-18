import streamlit as st

def personal_trainer():
    st.title("🏋️ Pallab's Personal Trainer AI")
    st.write("Tell me your fitness goal (e.g., 'I want to lose weight').")

    user_input = st.text_input("You:")

    if user_input:
        if "lose weight" in user_input.lower():
            st.success("Here's a 30-Day Weight Loss Plan:")
            st.markdown("""
            - **Day 1**: Brisk walking, Squats, Push-ups, Plank, Stretching (30 mins)  
            - **Day 2**: Cycling, Lunges, Incline Push-ups, Side Plank, Stretching (30 mins)  
            - **Day 3**: Rest - Light walk or yoga  
            - _...and so on. Add more details as needed._
            """)
        else:
            st.warning("I'm still learning how to help with that goal. Try: 'I want to lose weight'.")

if __name__ == "__main__":
    personal_trainer()
