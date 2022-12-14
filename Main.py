import streamlit as st 
from streamlit_option_menu import option_menu
from Title import *
from Document import *
from CC import *

def streamlit_menu(menu):
    if menu == 2:
        # 2. horizontal menu w/o custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home","Project", "Document", "Contact"],  # required
            icons=["house"," ", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        return selected



selected = streamlit_menu(menu=2)
if selected == "Home":
    simpledata();
if selected == "Project":
    st.sidebar.title("")
    st.sidebar.title("Carbon Footprint")
    y=st.sidebar.radio(' ', ['Cryptocurrency','Consensus Algorithm','Mining Algorithm','Use Case', 'Smart Contract'])
    st.sidebar.title("Carbon Credit")
    z=st.sidebar.radio(' ', ['Evaluation', 'Smart Contract'])
    st.sidebar.title("Carbon Index")
    p=st.sidebar.radio(' ', ['Carbon Footprint', 'Carbon Credit','Carbon Ratio'])
    if y=="Cryptocurrency":
        btec();
    if z=="Evaluation":
        simpledata();
if selected == "Document":
    st.sidebar.title("Document")
    x=st.sidebar.radio(' ', ['Abstract', 'Contextual Background', 'Technical Background', 'Aim, Objectives and Questions', 'Motivation','Research Methodology', 'Project Implementation and Execution', 'Analysis', 'Results', 'Future Scope', 'Recommendation', 'Conclusion', 'References'])
    if x=="Abstract":
        abstract();
    if x=="Contextual Background":
        context();
    if x=="Technical Background":
        technical();
    if x=="Aim, Objectives and Questions":
        AOO();
    if x=="Motivation":
        motivation();
    if x=="Research Methodology":
        researchmethod();
    if x=="Project Implementation and Execution":
        project();
    if x=="Analysis":
        analysis();
    if x=="Results":
        result();
    if x=="Future Scope":
        future();
    if x=="Recommendation":
        recommend();
    if x=="Conclusion":
        conclusion();
    if x=="References":
        references();
if selected == "Contact":
    simpledata();

    
    
    
