import streamlit as st 
from Base.equations import *

def supply():
    st.write("Supply Chain")
    st.caption("Please select all the options applicable for your supplychain.")
    st.title("Carbon Footprint Calculator")
    option = st.selectbox('Supply Chain Option',['Choose an Option', 'Personnel Carbon Footprint','Transport Carbon Footprint','Food Carbon Footprint', 'All'])
    if option=="Personnel Carbon Footprint":
            a=personnel()
    elif option=="Transport Carbon Footprint":
            b=transport()
    elif option=="Food Carbon Footprint":
            c=food()
    if option== "All":
        st.write(personnel() + transport() + food())

        
def dex():
    st.write("Decentralized Exchange")
    p=st.radio("Select Blockchain Consensus",['Proof of Work', 'Proof of Stake'])
    if p=="Proof of Work":
        st.write("Carbon Footprint in kgC02e")
        b = st.radio(" Select ", ['Manual', 'CryptoCurrency'])
        if b=="Manual":
            power=st.number_input('Average Power consumption in W', 1)
            times=st.number_input('Running time in hours', 1)
            co2=(power/1000)*times*0.19338
            prices=(co2/1000)*1.08
            st.write("UK Grid : {} kgC02e".format(co2))
            st.write("Offset cost : {} $".format(prices))
        if b=="CryptoCurrency":
            hash=st.number_input('Hashrate of Cryptocurrency',1)
            power=st.number_input('Average Power consumption in kWh', 1)
            miners=st.number_input('Avg hashrate per miner', 1)
            noh=hash/miners
            co2=(power)*1*0.19338*noh
            prices=(co2/1000)*1.08
            st.write("UK Grid : {} kgC02e per hour".format(co2))
            st.write("Offset cost : {} $ per hour".format(prices))
            st.write("Offset cost : {} $ per hour per Miner".format(prices/noh))

    if p=="Proof of Stake":
        st.write("Carbon Footprint in kgC02e")
        staked=st.number_input('Total number of coins staked', 1)
        power=st.number_input('Power Consumption of Blockchain per day', 1)
        b = st.radio(" Select ", ['Manual', 'CryptoCurrency'])
        if b=="Manual":
            stake=st.number_input('Number of coins staked', 1)
            times=st.number_input('Staked time in hours', 1)
            powers=((stake/staked)*100)*power
            st.write("Power Consumption : {}".format(powers))
            co2=(powers)*0.19338
            prices=(co2/1000)*1.08
            st.write("UK Grid : {} kgC02e".format(co2))
            st.write("Offset cost : {} $".format(prices))
        if b=="CryptoCurrency":
            st.write("Power Consumption per day: {}".format(power))
            st.write("Total Coins Staked: {}".format(staked))
            avgstake=st.number_input('Avg Staked coins', 50)
            noh=staked/avgstake
            co2=(power)*1*0.19338*noh
            prices=(co2/1000)*1.08
            st.write("UK Grid : {} kgC02e per hour".format(co2))
            st.write("Offset cost : {} $ per hour".format(prices))
            st.write("Offset cost : {} $ per hour per Miner".format(prices/noh))


def nft():
    st.write("Non Fungible Token")
    p=st.radio("Select Blockchain Consensus",['Proof of Work', 'Proof of Stake'])
    if p=="Proof of Work":
        st.write("Carbon Footprint in kgC02e")
        b = st.radio(" Select ", ['Manual', 'CryptoCurrency'])
        if b=="Manual":
            power=st.number_input('Average Power consumption in W', 1)
            times=st.number_input('Running time in hours', 1)
            co2=(power/1000)*times*0.19338
            prices=(co2/1000)*1.08
            st.write("UK Grid : {} kgC02e".format(co2))
            st.write("Offset cost : {} $".format(prices))
        if b=="CryptoCurrency":
            hash=st.number_input('Hashrate of Cryptocurrency',1)
            power=st.number_input('Average Power consumption in kWh', 1)
            miners=st.number_input('Avg hashrate per miner', 1)
            noh=hash/miners
            co2=(power)*1*0.19338*noh
            prices=(co2/1000)*1.08
            st.write("UK Grid : {} kgC02e per hour".format(co2))
            st.write("Offset cost : {} $ per hour".format(prices))
            st.write("Offset cost : {} $ per hour per Miner".format(prices/noh))

    if p=="Proof of Stake":
        st.write("Carbon Footprint in kgC02e")
        staked=st.number_input('Total number of coins staked', 1)
        power=st.number_input('Power Consumption of Blockchain per day', 1)
        b = st.radio(" Select ", ['Manual', 'CryptoCurrency'])
        if b=="Manual":
            stake=st.number_input('Number of coins staked', 1)
            times=st.number_input('Staked time in hours', 1)
            powers=((stake/staked)*100)*power
            st.write("Power Consumption : {}".format(powers))
            co2=(powers)*0.19338
            prices=(co2/1000)*1.08
            st.write("UK Grid : {} kgC02e".format(co2))
            st.write("Offset cost : {} $".format(prices))
        if b=="CryptoCurrency":
            st.write("Power Consumption per day: {}".format(power))
            st.write("Total Coins Staked: {}".format(staked))
            avgstake=st.number_input('Avg Staked coins', 50)
            noh=staked/avgstake
            co2=(power)*1*0.19338*noh
            prices=(co2/1000)*1.08
            st.write("UK Grid : {} kgC02e per hour".format(co2))
            st.write("Offset cost : {} $ per hour".format(prices))
            st.write("Offset cost : {} $ per hour per Miner".format(prices/noh))
    
def secure():
    st.write("Secure Information")
    st.caption("Secure Information depends on the blockchain used, hence the proof of work and proof of stake, additionally it contains carbon footprint due to verification process and the continous running of the blockchain operation to keep it viable.")
    st.caption("The blockchain footprint is calculated based on proof of work and proof of stake, while the additional carbon footprint due to verification is through averaging the 150000 tonnes of co2 used by legal firms in the UK per year calculated to per minute for processing verficiation of an individual.")
    p=st.radio("Select Blockchain Consensus",['Proof of Work', 'Proof of Stake'])
    if p=="Proof of Work":
        st.write("Carbon Footprint in kgC02e")
        b = st.radio(" Select ", ['Manual', 'CryptoCurrency'])
        if b=="Manual":
            power=st.number_input('Average Power consumption in W', 1)
            times=st.number_input('Running time in hours', 1)

            identity=st.number_input("Fields uploaded for verfication", 1)
            st.caption("Number of fields used for identity (Name/DOB/Tax number/BRP/Passport/etc)")
            add=((((150000/365)/24)/60)/60)*identity
            co2=((power/1000)*times*0.19338) + add
            prices=(co2/1000)*1.08
            st.write("UK Grid : {} kgC02e".format(co2))
            st.write("Offset cost : {} $".format(prices))
        if b=="CryptoCurrency":
            hash=st.number_input('Hashrate of Cryptocurrency',1)
            power=st.number_input('Average Power consumption in kWh', 1)
            miners=st.number_input('Avg hashrate per miner', 1)
            noh=hash/miners
            identity=st.number_input("Fields uploaded for verfication")
            st.caption("Number of fields used for identity (Name/DOB/Tax number/BRP/Passport/etc)")
            add=(((150000/365)/24)/60)*identity
            co2=(power)*1*0.19338*noh + add
            prices=(co2/1000)*1.08
            st.write("UK Grid : {} kgC02e per hour".format(co2))
            st.write("Offset cost : {} $ per hour".format(prices))
            st.write("Offset cost : {} $ per hour per Miner".format(prices/noh))

    if p=="Proof of Stake":
        st.write("Carbon Footprint in kgC02e")
        staked=st.number_input('Total number of coins staked', 1)
        power=st.number_input('Power Consumption of Blockchain per day', 1)
        b = st.radio(" Select ", ['Manual', 'CryptoCurrency'])
        if b=="Manual":
            stake=st.number_input('Number of coins staked', 1)
            times=st.number_input('Staked time in hours', 1)
            powers=((stake/staked)*100)*power
            st.write("Power Consumption : {}".format(powers))
            identity=st.number_input("Fields uploaded for verfication")
            st.caption("Number of fields used for identity (Name/DOB/Tax number/BRP/Passport/etc)")
            add=(((150000/365)/24)/60)*identity
            co2=(powers)*0.19338 + add
            prices=(co2/1000)*1.08
            st.write("UK Grid : {} kgC02e".format(co2))
            st.write("Offset cost : {} $".format(prices))
        if b=="CryptoCurrency":
            st.write("Power Consumption per day: {}".format(power))
            st.write("Total Coins Staked: {}".format(staked))
            avgstake=st.number_input('Avg Staked coins', 50)
            noh=staked/avgstake
            identity=st.number_input("Fields uploaded for verfication")
            st.caption("Number of fields used for identity (Name/DOB/Tax number/BRP/Passport/etc)")
            add=(((150000/365)/24)/60)*identity + add
            co2=(power)*1*0.19338*noh
            prices=(co2/1000)*1.08
            st.write("UK Grid : {} kgC02e per hour".format(co2))
            st.write("Offset cost : {} $ per hour".format(prices))
            st.write("Offset cost : {} $ per hour per Miner".format(prices/noh))
    