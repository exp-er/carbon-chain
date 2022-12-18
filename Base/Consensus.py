import streamlit as st
def pow():
    st.write("Proof of Work")
    st.caption("Proof of Work is mining based consensus algorithm, Hence the algorithm would depend on")
    st.caption("1. Hashrate ")
    st.caption("2. Number of nodes/miners")
    st.caption("3. Power Consumption")
    st.caption("4. Time(hours)")
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
        noh=hash/25
        co2=(power)*1*0.19338*noh
        prices=(co2/1000)*1.08
        st.write("UK Grid : {} kgC02e per hour".format(co2))
        st.write("Offset cost : {} $ per hour".format(prices))
        st.write("Offset cost : {} $ per hour per Miner".format(prices/noh))
def pos():
    st.write("Proof of Stake")
    st.caption("Proof of Stake is staking based consensus algorithm, Hence the algorithm would depend on")
    st.caption("1. Power of Consumption of Blockchain per day ")
    st.caption("2. Number of coins staked")
    st.caption("3. Number of transactions")
    st.caption("4. Time(hours)")
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
        noh=hash/25
        co2=(power)*1*0.19338*noh
        prices=(co2/1000)*1.08
        st.write("UK Grid : {} kgC02e per hour".format(co2))
        st.write("Offset cost : {} $ per hour".format(prices))
        st.write("Offset cost : {} $ per hour per Miner".format(prices/noh))

def bft():
    st.write("Byzantine Fault Tolerance")
    
    
def poet():
    st.write("Proof of Elapsed Time")