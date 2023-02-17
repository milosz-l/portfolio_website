import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import base64


# page config
st.set_page_config(page_title="Milosz Lopatto", page_icon="💡", layout="wide")

# load assets
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
data_visualization_lottie = load_lottieurl('https://assets9.lottiefiles.com/private_files/lf30_ps1145pz.json')
mail_lottie = load_lottieurl('https://assets8.lottiefiles.com/packages/lf20_kdx6cani.json')
face_image = Image.open("images/face.jpg")
conti_logo_image = Image.open("images/conti_logo.png")
wut_logo_image = Image.open("images/wut_logo.png")
with open("files/email.txt", "r") as file:
    email = file.read()

# use style.css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")

# header section
with st.container():
    st.subheader("Hi, my name is Milosz :smile:")
    text_column, image_column = st.columns((2, 1))
    with text_column:
        st.title("Computer Science student @ Warsaw University of Technology")
        st.write(
            """
            I am a highly motivated third-year Computer Science student specializing in Artificial Intelligence. I have a strong passion for Machine Learning and Data Science and am constantly seeking new opportunities to apply my knowledge and skills in these areas. With a drive to continuously improve and learn, I am eager to take on new challenges and create impactful solutions in the field of AI.
            """
        )
    with image_column:
        st.image(face_image)

# load lottie
st_lottie(data_visualization_lottie, height=600, key="data_visualization")

# load testimonial pdf
with open("files/testimonial.pdf", "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')
pdf_display_testimonial = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'


# experience
with st.container():
    st.write("---")
    st.header("Experience")
    left_column, right_column = st.columns((2, 1))
    with left_column:
        st.subheader('Data Analytics internship at Continental')
        st.caption('Jul 2022 - Sep 2022, Hanover, Germany')
        st.write(
            """
            - Analysis and improvement of the chatbot and the corresponding NLP Machine Learning model.
                - Performed exploratory analysis of chatbot conversations data. Found an error in database - almost 20% of classifier predictions haven’t been logged in the database.
                - Built a `Power BI` report that allowed for measuring the performance of the NLP Machine Learning model and created detailed documentation in `Confluence`.
                - Presented the results to the management.
                - Retrained the model on new data (improved accuracy by 6%).
                - Created a Sankey diagram with `Python` that shows the flow of users' conversations with the chatbot.
                - Developed an NLP machine learning model to automate manual classification of inputs that the chatbot failed to answer.
            - Supported the `Power BI` reports migration project.
                - Managed reports in `Power BI Service` and optimized their performance.
                - Worked with `Data Vault 2.0` methodology using `Matillion ELT` software.
            - Worked with `Scrum` methodology using `Jira`.
            """
        )
    st.markdown(pdf_display_testimonial, unsafe_allow_html=True)
    with right_column:
        st.image(conti_logo_image)

# education
with st.container():
    st.write("---")
    st.header("Education")
    left_column, right_column = st.columns((2, 1))
    with left_column:
        st.subheader('Warsaw University of Technology')
        st.caption('2020 - Present, Warsaw, Poland')
        st.write(
            """
            - Major in Computer Science (Artificial Intelligence specialization)
            - Current GPA: 4,01 (scale: 2-5)
            - Took first place in a competition during the Artificial Neural Networks course
                - The projects were related to: Convolutional Neural Networks (CNN), Transformers, Generative Adversarial Networks (GAN), Recurrent Neural Networks (RNN) and Natural Language Processing (NLP)
            - Got to know in practice how to build Machine Learning models (including steps like data cleaning, data visualization, feature selection, feature engineering, hyperparameters tuning and more)
            - Currently building an AutoML app in `Streamlit`
            """
        )
    with right_column:
        st.image(wut_logo_image)

# projects
with st.container():
    st.write("---")
    st.header("Projects")
    left_column, right_column = st.columns((2, 1))
    with left_column:
        st.subheader('Predicting the delivery time of packages')
        st.write(
            """
            - [Link to notebook](https://github.com/milosz-l/delivery-time/blob/master/data_analysis.ipynb)
            - Got to know in practice how to build Machine Learning models, including steps like:
                - data cleaning
                - EDA
                - data visualization
                - feature selection
                - feature engineering
                - etc.
            """
        )
        st.subheader('AutoML app in Streamlit')
        st.write(
            """
            - Work in progress as part of an engineering thesis.
            """
        )
        st.subheader('GymNote - workout tracker app in SwiftUI')
        st.write(
            """
            - Work in progress.
            - A hobby project that I intend to release on the App Store at some point.
            """
        )
    with right_column:
        st.empty()

# skills and other
def skills_row(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

with st.container():
    st.write("---")
    st.header("Skills")
    skills_row('Programming', '`Python`, `C`, `C++`, `Swift`, `Git`')
    skills_row('Data processing', '`SQL`, `pandas`, `numpy`')
    skills_row('Data visualization', '`Microsoft Power BI`, `matplotlib`, `seaborn`, `plotly`')
    skills_row('Machine Learning', '`scikit-learn`')
    skills_row('Deep Learning', '`pytorch`, `huggingface`')
    skills_row('Natural Language Processing (NLP)', '`spaCy`')
    skills_row('Model deployment', '`streamlit`')
    skills_row('Web development', '`Django`, `HTML`, `CSS`')
    skills_row('Agile', '`Jira`, `Confluence`')
    skills_row('Languages', '`English`, `Polish (native)`')

# socials
with st.container():
    st.write("---")
    st.header("Socials")
    st.markdown(
        """
        - [linkedin](https://www.linkedin.com/in/milosz-lopatto/)
        - [github](https://github.com/milosz-l)
        """
    )

# contact
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    contact_form = f"""
    <form action="https://formsubmit.co/{email}" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st_lottie(mail_lottie, height=400, key="mail")
