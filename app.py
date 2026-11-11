
import streamlit as st
#1 Page configuration
st.set_page_config(
    page_title="Faith Hongo| Data Scientist",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded"    
)
st.markdown("""
    <style>
    .main { background-color: #f9f9f9;}
    h1 { color: #1a1a1a: font-weight: 700; }
    h2 { color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 5px; }
    .stButton>button { background-color: #3498db; color: white; border-radius: 5px; }
    <style>
    """, unsafe_allow_html=True)

#2. hero section
st.title("Hi, I'm Faith Hongo")
st.markdown("""
### Data scientist turning complex data into actionable insights and production ready ML solutions.
# I bridge the gap between raw data and business value, building end-to-end data solutions from exploratory analysis to interactive dashboards.
""")
st.markdown("[LinkedIn](https://www.linkedin.com/in/faithhongo) | [GitHub](https://github.com/faithongo)")
st.markdown("---")

#3. Tech track
st.header("What I build & My stack")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    -**PredictiveModelling:** Building and turning ML models for classification and regression. \n
    -**Data Pipelines:** Cleaning, transforming and automating data workflows. \n
    -**Interactive Dashboards:** Creating intuitive UIs for stakeholders to explore data and insights. \n
    """)

with col2:
    st.markdown("""
    -**Languages:** Pythong, SQL, R, Bash \n
    -**ML/AI:** Scikit-learn, TensorFlow, PyTorch, pandas, NumPy, NLP \n
    -**Tools:** Git, Docker, Jupyter \n
    -**Visualisation:** Streamlit, Matplotlib, Seaborn, Plotly, powerBI \n
    """)

st.markdown("---")


# 4. Featured Projects
st.header("Featured Projects")


with st.expander("Project 1: Actuarial Modeling for Kenya's NHIF to SHIF Transition", expanded=True):
    st.markdown("""
    - **Problem:** The new SHIF 2.75% premium with a KES 300 floor poses affordability risks for low-income households, threatening fund solvency.
    - **Solution:** Developed R-based actuarial models, including an ARIMA forecast for claims (2025–2029) and a logistic regression model to predict household default risk based on income volatility.
    - **Impact:** Identified the KES 10,909 break-even income threshold and recommended an Adjusted Progressive Premium Model (APPM) to inform sustainable policy design.
    - **Stack:** R, ggplot2, ARIMA Forecasting, Logistic Regression, Git
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"[View My GitHub Repo](https://github.com/faithongo/nhif-shif-actuarial-models-r)")
    with col2:
        st.markdown("[View Project Presentation](https://jessywaweru.github.io/FINAL-YR-PRESENTATION/)")

with st.expander("Project 2: Real-Estate Price Explorer & Predictor"):
    st.markdown("""
    - **Problem:** Homebuyers lack transparent, data-driven tools to estimate fair market value.
    - **Solution:** Scraped real estate data, cleaned it and built a multiple linear regression model. Created a dashboard where users input features to get instant price estimates.
    - **Impact:** Model achieved an R-squared of 0.85. Dashboard receives consistent traffic from local real estate groups.
    - **Stack:** Python, BeautifulSoup, Statsmodels, Plotly, Streamlit
    """)
    #col1, col2 = st.columns(2)
    #with col1:
     #   st.markdown("[🔗 View GitHub Repo](https://github.com/yourusername/project2)")
    #with col2:
     #   st.markdown("[🌐 Live Demo](https://yourproject2.streamlit.app)")

st.markdown("---")

# 5. Experience & Education
st.header("Experience & Education")

st.markdown("""
**Data Science Trainee** | **ALX Africa** \n
*March 2025 - August 2026*  
- Completed intensive, project based training in Python, SQL, Machine Learning, and Data Visualization.
- Collaborated with peers on agile sprints, practicing version control with Git and GitHub.
- Built end-to-end capstone projects focusing on real world business problems.

**Bsc. Actuarial Science** | **University of Nairobi** \n
*September 2022 -September 2026*  
-  Conducted research on the actuarial implications of the transition from NHIF to SHA, examining affordability,
 contribution structures, risk pooling and long term financial sustainability.
 - Developed an understanding of financial risk, probability modelling and quantitative decision making.
""")

st.markdown("---")

# 6. Contact Section
st.header("Let's Connect")
st.markdown("I'm currently open to Data Scientist and Machine Learning Engineer roles." \
"Let's build something impactful together.")

st.markdown("**Email:** faithongo414@gmail.com")
st.markdown("**LinkedIn:** https://linkedin.com/in/faithhongo")
st.markdown("**GitHub:** https://github.com/faithongo")
