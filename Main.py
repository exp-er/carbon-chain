import streamlit as st 
from streamlit_option_menu import option_menu
from Base.Title import * #Title Page
from Base.Document import * #Document Page
from Base.CC import *  #Project Cryptocurrency Page
from Base.Mining import * #Project Mining Algo Page
from Base.Consensus import * #Project Consensus Page
from Base.uses import * #Project Use Case Page
from Base.equations import *
from Base.index import *
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
    y=st.sidebar.radio(' ', ['Cryptocurrency','Consensus Algorithm','Mining Algorithm','Use Case', 'Smart Contract Footprint', 'Smart Contract Credit', 'Carbon Index'])
    if y=="Cryptocurrency":
        st.sidebar.title("Cryptocurrency")
        a=st.sidebar.radio('Select Cryptocurrency', ['Bitcoin','Ethereum','Ethereum POW','Ethereum Classic','XRP','Doge','Cardano','Polygon'])
        if a=='Bitcoin':
            btc();
        if a=='Ethereum':
            eth();
        if a=='Ethereum POW':
            etpow();
        if a=='Ethereum Classic':
            etc();
        if a=='XRP':
            xrp();
        if a=='Doge':
            dg();
        if a=='Cardano':
            crd();
        if a=='Polygon':
            mat();
    if y=="Consensus Algorithm":
        st.sidebar.title("Consensus Algorithm")
        a=st.sidebar.radio('Select Consensus Algorithm', ['Proof of Work','Proof of Stake','Proof of Elapsed Time','Byzantine Fault Tolerance'])
        if a=='Proof of Work':
            pow();
        if a=='Proof of Stake':
            pos();
        if a=='Proof of Elapsed Time':
            poet();
        if a=='Byzantine Fault Tolerance':
            bft();
    if y=="Use Case":
        st.sidebar.title("Usecase")
        a=st.sidebar.radio('Select UseCase', ['Supply-Chain','Decentralized Exchange','NFT Marketplace','Secure Information'])
        if a=='Supply-Chain':
            supply();
        if a=='Decentralized Exchange':
            dex();
        if a=='NFT Marketplace':
            nft();
        if a=='Secure Information':
            secure();
    if y=="Mining Algorithm":
        st.sidebar.title("Mining Algorithm")
        a=st.sidebar.radio('Select Algorithm', ['SHA256','Ethash', 'Scrypt', 'Equilhash','CryptoNight'])
        if a=='SHA256':
            sha256fun(); 
        if a=="Scrypt":
            scrypt();
        if a=="Equilhash":
            equil();
        if a=="CryptoNight":
            crynight();
        if a=="Ethash":
            ethash();
    if y=="Carbon Index":
        st.sidebar.title("Carbon Index")
        st.write("All values to simulate index are through the calculations done in Cryptocurrency section and averages or made-up values.")
        st.caption("Average values: Hashrate = 30 | Staked coin = 50")
        st.caption("Made-up: Offsetting currently")
        a=st.sidebar.selectbox('Select Index', ['Footprint','Credit', 'Ratio'])
        if a=="Footprint":
            foot()
        if a=="Credit":
            cred()
        if a=="Ratio":
            ratio()
    if y=="Smart Contract Footprint":
        st.write("Smart Contract Footprint")
    if y=="Smart Contract Credit":
        st.write("Smart Contract Credit")
if selected == "Document":
    st.sidebar.title("Document")
    x=st.sidebar.radio(' ', ['Abstract', 'Contextual Background', 'Technical Background', 'Aim, Objectives and Questions', 'Motivation','Research Methodology', 'Project Implementation and Execution', 'Analysis', 'Results', 'Recommendation', 'Conclusion', 'References'])
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
    if x=="Recommendation":
        recommend();
    if x=="Conclusion":
        conclusion();
    if x=="References":
        references();
if selected == "Contact":
    simpledata();

    
    
    
