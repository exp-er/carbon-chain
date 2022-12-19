import streamlit as st

def personnel():
    noofmembers=st.number_input("Enter Number of Personnel in Supply Chain",min_value=1)
    electricity=st.number_input("Enter the kWh of Electricity Used")
    naturalgas=st.number_input("Enter kWh of Natural Gas Used ")
    heatingoil=st.number_input("Enter Litres of Heating Oil Used")
    coal=st.number_input("Enter Metric Tons of Coal Used")
    lpg=st.number_input("Enter Litres of LPG Used")
    propane=st.number_input("Enter Litres of Propane Used")
    woodenpellets=st.number_input("Enter Metric Tons of Wooden Pellets Used")
    f_electicity=((electricity/1000)*0.7080)
    f_naturalgas=((naturalgas/100)*0.02)
    f_heatingoil=((heatingoil/100)*0.27)
    f_coal=(coal*2.88)
    f_lpg=((lpg/100)*0.17)
    f_propane=((propane/100)*0.16)
    f_woodenpellets=(woodenpellets*0.07)
    total=(f_electicity+f_coal+f_heatingoil+f_lpg+f_naturalgas+f_propane+f_woodenpellets)/(noofmembers)
    st.title('Your Carbon Footprint is'+" "+str(total)+" "+"Metric Tonnes")
    st.write("Offset Cost : {} $".format(total*3.54))
    return total
    
    
def transport():
    mileage = st.selectbox(
    'Enter Average Mileage in transport',
    ('35 MPG', '46 MPG','52 MPG','Enter Custom mpg'))
    miles = st.selectbox(
    'Miles Travelled',
    ('Choose an Option','Low (6,000 miles)', 'Average (9,000 miles)','High (12,000 miles)','Enter Custom miles'))
    
    if mileage=='35 MPG':
        size=35
    if mileage=='46 MPG':
        size=46
    if mileage=='52 MPG':
        size=52
    if mileage=='Enter Custom mpg':
        size=st.number_input("Enter Mileage",1)
    if miles=='Choose an Option':
        mileage=0
    if miles=='Low (6,000 miles)':
        mileage=6000
    if miles=='Average (9,000 miles)':
        mileage=9000
    if miles=='High (12,000 miles)':
        mileage=12000
    if miles=='Enter Custom miles':
        mileage=st.number_input('Enter miles',1)
        
    total3=(((((mileage/size)*14.3)/1000)*0.907185)/1)
    st.title('Your Carbon Footprint is'+" "+str(total3)+" "+"Metric Tonnes")
    st.write("Offset Cost : {} $".format(total3*3.54))
    return total3

def food():
    food1 = st.selectbox(
    'How much of the food that you export is organic?',
    ('None','Some', 'Most','All'))
    food2 = st.selectbox(
    'How much meat/dairy do you export?',
    ('Above-average meat/dairy','Average meat/dairy', 'Below-average meat/dairy','Lacto-vegetarian','Vegan'))
    food3 = st.selectbox(
    'How much of the food is produced locally?',
    ('Very little (much foreign / out of season food)','Average', 'Above average','Almost all'))
    food4 = st.selectbox(
    'How much of the food is packaged or processed?',
    ('Above average','Average', 'Below average','Very little'))
    food5 = st.selectbox(
    'How much do you compost leftover and unused food?',
    ('None','Some','All'))

    if food1=='None':
        organic=0.7
    if food1=='Some':
        organic=0.5
    if food1=='Most':
        organic=0.2
    if food1=='All':
        organic=0

    if food2=='Above-average meat/dairy':
        meat=0.6
    if food2=='Average meat/dairy':
        meat=0.4
    if food2=='Below-average meat/dairy':
        meat=0.25
    if food2=='Lacto-vegetarian':
        meat=0.1
    if food2=='Vegan':
        meat=0

    if food3=='Very little (much foreign / out of season food)':
       foodmiles=0.5
    if food3=='Average':
       foodmiles=0.3
    if food3=='Above average':
       foodmiles=0.2
    if food3=='Almost all':
       foodmiles=0.1
        
    if food4=='Above average':
        package=0.6
    if food4=='Average':
        package=0.4
    if food4=='Below average':
        package=0.2
    if food4=='Very little':
        package=0.05
        
    if food5=='None':
        composting=0.2
    if food5=='Some':
        composting=0.1
    if food5=='All':
        composting=0
    
    total=(organic+meat+foodmiles+package+composting)
    st.title('Your Carbon Footprint is'+" "+str(total)+" "+"Tonnes")
    st.write("Offset Cost : {} $".format(total*3.54))
    return total
    
    
    
