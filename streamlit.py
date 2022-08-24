import pickle
import sklearn
import streamlit as st

# loading the trained model
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

@st.cache()

# defining the function which will make the prediction using the data which the user inputs
def prediction(race_B, Most_Improved_Player, Most_Valuable_Player, Finals_MVP,
       All_Rookie_Second_Team, All_NBA_First_Team, All_NBA_Second_Team,
       All_Rookie_First_Team):

       # Making predictions
       prediction = classifier.predict(
       [[race_B, Most_Improved_Player, Most_Valuable_Player, Finals_MVP,
              All_Rookie_Second_Team, All_NBA_First_Team, All_NBA_Second_Team,
              All_Rookie_First_Team]])
       if prediction == 0:
            pred = 'Not Awarded'
       else:
            pred = 'Awarded'#
       return pred

# This is the main function where we define the webpage
def main():
    # front end elements of the webpage
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Hall of Fame Awards</h1>
    </div>
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True)

    # The following lines create boxes in which user can enter data required to make predictions
    race_B = st.selectbox('Number', ("0", "1"))
    Most_Improved_Player = st.selectbox('Number', ("0.0", "1.0"))
    Most_Valuable_Player = st.selectbox('Number', ("0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0"))
    Finals_MVP = st.selectbox('Number', ("0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0"))
    All_Rookie_Second_Team = st.selectbox('Number', ("0.0", "1.0"))
    All_NBA_First_Team = st.selectbox('Number', ("0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0", "10.0", "11.0"))
    All_NBA_Second_Team = st.selectbox('Number', ("0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0"))
    All_Rookie_First_Team = st.selectbox('Number', ("0.0", "1.0"))
    result =""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        result = prediction(race_B, Most_Improved_Player, Most_Valuable_Player, Finals_MVP,
               All_Rookie_Second_Team, All_NBA_First_Team, All_NBA_Second_Team,
               All_Rookie_First_Team)
        st.success('This player is {}'.format(result))


    if __name__=='__main__':
        main()
