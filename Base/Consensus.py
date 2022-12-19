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
        noh=hash/miners
        co2=(power)*1*0.19338*noh
        prices=(co2/1000)*1.08
        st.write("UK Grid : {} kgC02e per hour".format(co2))
        st.write("Offset cost : {} $ per hour".format(prices))
        st.write("Offset cost : {} $ per hour per Miner".format(prices/noh))
def pos():
    st.write("Proof of Stake")
    st.caption("Proof of Stake is staking based consensus algorithm, Hence the algorithm would depend on")
    st.caption("1. Power of Consumption of Blockchain per day ")
    st.caption("2. Total Number of Coins Skated on Blockchain")
    st.caption("3. Total Number of transactions on Blockchain")
    st.caption("4. Time(hours)")
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

def bft():
    st.write("Byzantine Fault Tolerance")
    st.caption("Byzantine Fault Tolerance is based on voting mechanism for consensus, Hence the algorithm would depend on")
    st.caption("1. Number of participants for voting")
    st.caption("2. Required number of votes for approving block")
    st.caption("3. Power consumption per voter")
    st.write("Carbon Footprint in kgC02e")
    voters=st.number_input('Total number of voters', 1)
    power=st.number_input('Power Consumption of voters', 1)
    b = st.radio(" Select ", ['Manual', 'CryptoCurrency'])
    if b=="Manual":
        time=st.number_input('Avg Waiting time', 1)
        powers=((1/voters)*100)*power*time
        st.write("Power Consumption : {}".format(powers))
        co2=(powers)*0.19338
        prices=(co2/1000)*1.08
        st.write("UK Grid : {} kgC02e".format(co2))
        st.write("Offset cost : {} $".format(prices))
    if b=="CryptoCurrency":
        st.write("Power Consumption: {}".format(power))
        st.write("Total Number of Voters: {}".format(voters))
        avgtime=st.number_input('Avg Idle Time in hours', 10)
        co2=(power)*1*0.19338*voters*avgtime
        prices=(co2/1000)*1.08
        st.write("UK Grid : {} kgC02e per hour".format(co2))
        st.write("Offset cost : {} $ per hour".format(prices))
        st.write("Offset cost : {} $ per hour per Miner".format(prices/voters))
    
def poet():
    st.write("Proof of Elapsed Time")
    st.caption("Proof of Elapsesd Time is based on reandom selection mechanism for selecting miner, Hence the algorithm would depend on")
    st.caption("1. Number of Participants/Nodes ")
    st.caption("2. Average waiting time of Miners")
    st.caption("3. Power consumption per minute")
    st.caption("4. Time(hours)")
    st.write("Carbon Footprint in kgC02e")
    nodes=st.number_input('Total number of Nodes', 1)
    power=st.number_input('Power Consumption per Minute', 1)
    b = st.radio(" Select ", ['Manual', 'CryptoCurrency'])
    if b=="Manual":
        times=st.number_input('Avg Idle time in Minutes', 1)
        powers=times*power
        st.write("Power Consumption : {}".format(powers))
        co2=(powers)*0.19338
        prices=(co2/1000)*1.08
        st.write("UK Grid : {} kgC02e".format(co2))
        st.write("Offset cost : {} $".format(prices))
    if b=="CryptoCurrency":
        st.write("Power Consumption per day: {} ".format(power))
        st.write("Total number of nodes : {}".format(nodes))
        times=st.number_input('Avg Idle time in Minutes', 1)
        co2=(power)*1*nodes*0.19338
        prices=(co2/1000)*1.08
        st.write("UK Grid : {} kgC02e per hour".format(co2))
        st.write("Offset cost : {} $ per hour".format(prices))
        st.write("Offset cost : {} $ per hour per Node".format(prices/nodes))