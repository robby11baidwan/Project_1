import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

df = pd.read_csv("Admission_Predict.csv")
st.title("Admission Predictor")
st.image(
    "https://images.unsplash.com/flagged/photo-1554473675-d0904f3cbf38?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTF8fGNvbGxlZ2V8ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
    width=700)

st.header("Predicting the admission chance in Colleges.")

st.write("This is a project created to compute the chances of admission to colleges w.r.t"
         " to certain parameters.")
st.write("The dataset can be acccessed at https://www.kaggle.com/mohansacharya/graduate-admissions")

st.text("")
st.text("")
st.write("A peek at the data we are gonna use :")
df = df.drop(["Serial No."], axis=1)

col_names = df.columns.tolist()
st.dataframe(df[st.multiselect("Columns to display", col_names, default = col_names)])

st.text("")
st.text("")
st.header("Data Visualization")


X = st.selectbox('X value', col_names)
Y = st.selectbox('Y value', col_names)


st.text("")
st.text("")

plt.rcParams['axes.facecolor'] = '#31333f'
fig2, ax2 = plt.subplots()
plt.xlabel(X)
plt.ylabel(Y)

fig2.patch.set_alpha(0)

ax2.tick_params(axis='x', colors='white')
ax2.tick_params(axis='y', colors='white')

ax2.yaxis.label.set_color('white')
ax2.xaxis.label.set_color('white')

ax2 = plt.scatter(x=df[X], y=df[Y])
ax2.set_facecolor("#f43464")
sns.despine()
st.pyplot(fig2)

st.sidebar.header("User Input Parameters")


def get_user_input():
    GRE_Score = st.sidebar.slider("GRE Score:", 0, 340, step=1)
    TOEFL_Score = st.sidebar.slider("TOEFL Score:", 0, 120, step=1)
    University_Rating = st.sidebar.slider("University Rating:", 1, 5, step=1)
    SOP = st.sidebar.slider("SOP:", 0.0, 5.0, step=0.5)

    LOR = st.sidebar.slider("LOR:", 0, 5, step=1)

    CGPA = st.sidebar.slider("CGPA:", 0.0, 10.0, step=0.1)

    Research = st.sidebar.slider("Research (0 - No / 1- yes):", 0, 1, step=1)

    features = pd.DataFrame({"GRE Score": GRE_Score,
                             "TOEFL Score": TOEFL_Score,
                             "University Rating": University_Rating,
                             "SOP": SOP,
                             "LOR": LOR,
                             "CGPA": CGPA,
                             "Research": Research}, index=[0])
    return features


lr_model = pickle.load(open("Proj_model2.pkl", "rb"))
input1 = get_user_input()
prediction = ml_model.predict(input1)

st.text("")
st.text("")

st.header("Prediction")
st.write("Tune the parameter on the side-bar by accessing the top left button on screen.")
st.write("**The Chance Of Admission is ", "0" if (round(prediction[0], 2) < 0) else (
    str(round(prediction[0], 2) * 100) if (round(prediction[0], 2) < 1) else "100"), "percent.**")



def credits(content):
    st.markdown(
        f'<p style="color:{"#f63366"};">{content}</p>',
        unsafe_allow_html=True)


st.text("")
st.text("")
credits("Made By:")
credits("Brijeshwar Singh")
credits("101803170")
credits("COE-9")
