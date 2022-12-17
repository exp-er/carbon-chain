

import streamlit as st 
import streamlit.components.v1 as components
import requests

#response = requests.request("GET",url)

def btc():
    st.write("Consensus Algorithnm : Proof of Work (PoW)")
    st.write("Mining Algorithnm : SHA256")
    n='"0"'
    col1, col2, col3 = st.columns(3)
    with col1:
        hashs = st.number_input('Insert your hashrate in MH')
        n='"{}"'.format(hashs)
        x='<a class="minerstat-widget" title="BTC mining calculator" data-coin="BTC" data-algo="SHA-256" data-info="yes" data-style="light" data-color="" data-unit="TH" data-hashrate={} data-width="300" rel="nofollow" href="https://minerstat.com/coin/BTC">Bitcoin mining calculator</a><script async src="https://api.minerstat.com/v2/widgets/coin.js" charset="utf-8"></script>'.format(n)
        components.html(x, width=400, height=800)
    with col3:
        st.write("Carbon Footprint in kgC02e")
        b = st.radio(" Select ", ['Manual', 'CryptoCurrency'])
        if b=="Manual":

            power=st.number_input('Average Power consumption in W')
            times=st.number_input('Running time in hours')
            co2=(power/1000)*times*0.19338
            prices=(co2/1000)*1.08
            st.write("UK Grid : {} kgC02e".format(co2))
            st.write("Offset cost : {} $".format(prices))
        if b=="CryptoCurrency":
            url = "https://api.minerstat.com/v2/coins?list=BTC"
            response = requests.request("GET",url)
            coin=response.json()
            hashs2=coin[0]['network_hashrate']/1000000
            st.write("Hashrate: {} in MH".format(hashs2))
            st.caption('AVG Power consumption: 200')
            st.caption('AVG Hashrate per miner: 25')
            noh=hashs2/25
            co2=(200/1000)*1*0.19338*noh
            prices=(co2/1000)*1.08
            st.write("UK Grid : {} kgC02e per hour".format(co2))
            st.write("Offset cost : {} $ per hour".format(prices))
            st.write("Offset cost : {} $ per hour per Miner".format(prices/noh))
            
def etc():
    st.write("Consensus Algorithnm : Proof of Work (PoW)")
    st.write("Mining Algorithnm : EtcHash")    
    n='"0"'
    col1, col2, col3 = st.columns(3)
    with col1:
        hashs = st.number_input('Insert your hashrate in MH')
        n='"{}"'.format(hashs)
        x='<a class="minerstat-widget" title="ETC mining calculator" data-coin="ETC" data-algo="Etchash" data-info="yes" data-style="light" data-color="" data-unit="MH" data-hashrate={} data-width="300" rel="nofollow" href="https://minerstat.com/coin/ETC">Ethereum Classic mining calculator</a><script async src="https://api.minerstat.com/v2/widgets/coin.js" charset="utf-8"></script>'.format(n)
        components.html(x, width=400, height=400)
    with col3:
        st.write("Carbon Footprint in kgC02e")
        b = st.radio(" Select ", ['Manual', 'CryptoCurrency'])
        if b=="Manual":

            power=st.number_input('Average Power consumption in W')
            times=st.number_input('Running time in hours')
            co2=(power/1000)*times*0.19338
            prices=(co2/1000)*1.08
            st.write("UK Grid : {} kgC02e".format(co2))
            st.write("Offset cost : {} $".format(prices))
        if b=="CryptoCurrency":
            url = "https://api.minerstat.com/v2/coins?list=ETC"
            response = requests.request("GET",url)
            coin=response.json()
            hashs2=coin[0]['network_hashrate']/1000000
            st.write("Hashrate: {} in MH".format(hashs2))
            st.caption('AVG Power consumption: 200')
            st.caption('AVG Hashrate per miner: 25')
            noh=hashs2/25
            co2=(200/1000)*1*0.19338*noh
            prices=(co2/1000)*1.08
            st.write("UK Grid : {} kgC02e per hour".format(co2))
            st.write("Offset cost : {} $ per hour".format(prices))
            st.write("Offset cost : {} $ per hour per Miner".format(prices/noh))
        

def eth():
    st.write("Consensus Algorithnm : Proof of Stake (PoS)")
    st.write("Mining Algorithnm : N/A")
    n='"0"'
    url = "https://digiconomist.net/wp-json/mo/v1/ethereum/stats/20221212"
    response = requests.request("GET",url)
    coin=response.json()
    col1, col2, col3 = st.columns(3)
    with col1:
        x='<script async src="https://static.coinstats.app/widgets/coin-chart-widget.js"></script><coin-stats-chart-widget type="large" coin-id="ethereum" width="400" chart-height="250" currency="USD" locale="en" bg-color="#FFFFFF" text-color="#1C1B1B" status-up-color="#4F8A5B" status-down-color="#FE4747" buttons-color="#FFFFFF" chart-color="#E47103" chart-gradient-from="#FFFFFF" chart-gradient-to="#EFEFEF" chart-label-background="#FFFFFF" candle-grids-color="rgba(0,0,0,0.1)" border-color="rgba(28,27,27,0.15)" font="Roboto, Arial, Helvetica" btc-color="#6DD400" eth-color="#2D73AD"></coin-stats-chart-widget>'
        components.html(x, width=400, height=400)
    with col3:
        st.write("Carbon Footprint in kgC02e")
        b = st.radio(" Select ", ['Manual', 'CryptoCurrency', 'Formula'])
        if b=="Manual":

            stakes=st.number_input('Ethereum Staked', min_value=32, max_value=1000000)
            total=15616893
            per_stakes=(stakes/total)*100
            co2=coin[0]['24hr_kgCO2']
            per_co2=int(co2)*per_stakes
            st.write("24hr CO2 consumption: {} kgCO2e".format(per_co2))
            prices=per_co2*1.08
            st.write("Offset cost : {} $".format(prices))
        if b=="CryptoCurrency":
            power=coin[0]['24hr_kWh']
            st.write("24hr Power consumption: {} kWh".format(power))
            co2=coin[0]['24hr_kgCO2']
            st.write("24hr CO2 consumption: {} kgCO2e".format(co2))
            prices=((int(co2))/24)*1.08
            st.write("Offset cost : {} $ per hour".format(prices))
            
def etpow():
    st.write("Consensus Algorithnm : Proof of Work (PoW)")
    st.write("Mining Algorithnm : Ethash")
    n='"0"'
    col1, col2, col3 = st.columns(3)
    with col1:
        hashs = st.number_input('Insert your hashrate in MH')
        n='"{}"'.format(hashs)
        x='<a class="minerstat-widget" title="ETHW mining calculator" data-coin="ETHW" data-algo="Ethash" data-info="yes" data-style="light" data-color="" data-unit="MH" data-hashrate={} data-width="300" rel="nofollow" href="https://minerstat.com/coin/ETHW">Ethereum PoW mining calculator</a><script async src="https://api.minerstat.com/v2/widgets/coin.js" charset="utf-8"></script>'.format(n)
        components.html(x, width=400, height=400)
    with col3:
        b = st.radio(" Select ", ['Manual', 'CryptoCurrency', 'Formula'])
        if b=="Manual":
            st.write("Carbon Footprint in kgC02e")
            power=st.number_input('Average Power consumption in W')
            times=st.number_input('Running time in hours')
            co2=(power/1000)*times*0.19338
            prices=(co2/1000)*1.08
            st.write("UK Grid : {} kgC02e".format(co2))
            st.write("Offset cost : {} $".format(prices))
        if b=="CryptoCurrency":
            url = "https://api.minerstat.com/v2/coins?list=ETHW"
            response = requests.request("GET",url)
            coin=response.json()
            hashs2=coin[0]['network_hashrate']/1000000
            st.write("Hashrate: {} in MH".format(hashs2))
            st.caption('AVG Power consumption: 200')
            st.caption('AVG Hashrate per miner: 25')
            noh=hashs2/25
            co2=(200/1000)*1*0.19338*noh
            prices=(co2/1000)*1.08
            st.write("UK Grid : {} kgC02e per hour".format(co2))
            st.write("Offset cost : {} $ per hour".format(prices))
            st.write("Offset cost : {} $ per hour per Miner".format(prices/noh))

def xrp():
    st.write("Consensus Algorithnm : Ripple Protocol")
    st.write("Mining Algorithnm : N/A")
    n='"0"'
    col1, col2, col3 = st.columns(3)
    with col1:
        x='<script async src="https://static.coinstats.app/widgets/coin-chart-widget.js"></script><coin-stats-chart-widget type="large" coin-id="ripple" width="400" chart-height="250" currency="USD" locale="en" bg-color="#FFFFFF" text-color="#1C1B1B" status-up-color="#4F8A5B" status-down-color="#FE4747" buttons-color="#FFFFFF" chart-color="#E47103" chart-gradient-from="#FFFFFF" chart-gradient-to="#EFEFEF" chart-label-background="#FFFFFF" candle-grids-color="rgba(0,0,0,0.1)" border-color="rgba(28,27,27,0.15)" font="Roboto, Arial, Helvetica" btc-color="#6DD400" eth-color="#2D73AD"></coin-stats-chart-widget>'
        components.html(x, width=400, height=400)
    with col3:
        st.write("Carbon Footprint in kgC02e")
        b = st.radio(" Select ", ['Manual', 'CryptoCurrency'])
        if b=="Manual":
            power=0.0079*1192639
            co2=(power/24)*0.19338
            prices=(co2)*1.08
            st.write("Negligible transaction unless you are validators")
            st.write("For Validators")
            st.write("Power Consumption : {} kWh".format(power/112))
            st.write("UK Grid : {} kgC02e per hour".format(co2/112))
            st.write("Offset cost : {} $ per hour".format(prices/112))
            
            st.write("")
        if b=="CryptoCurrency":
            power=0.0079*1192639
            co2=(power/24)*0.19338
            prices=(co2)*1.08
            st.write("Power Consumption : {} kWh".format(power))
            st.write("UK Grid : {} kgC02e per hour".format(co2))
            st.write("Offset cost : {} $ per hour".format(prices))
def dg():
    st.write("Consensus Algorithnm : Proof of Work (PoW)")
    st.write("Mining Algorithnm : Scrypt")
    n='"0"'
    col1, col2, col3 = st.columns(3)
    with col1:
        hashs = st.number_input('Insert your hashrate in MH')
        n='"{}"'.format(hashs)
        x='<a class="minerstat-widget" title="DOGE mining calculator" data-coin="DOGE" data-algo="Scrypt" data-info="yes" data-style="light" data-color="" data-unit="MH" data-hashrate={} data-width="300" rel="nofollow" href="https://minerstat.com/coin/DOGE">Dogecoin mining calculator</a><script async src="https://api.minerstat.com/v2/widgets/coin.js" charset="utf-8"></script>'.format(n)
        components.html(x, width=400, height=400)
    with col3:
        b = st.radio(" Select ", ['Manual', 'CryptoCurrency'])
        if b=="Manual":
            st.write("Carbon Footprint in kgC02e")
            power=st.number_input('Average Power consumption in W')
            times=st.number_input('Running time in hours')
            co2=(power/1000)*times*0.19338
            prices=(co2/1000)*1.08
            st.write("UK Grid : {} kgC02e".format(co2))
            st.write("Offset cost : {} $".format(prices))
        if b=="CryptoCurrency":
            url = "https://api.minerstat.com/v2/coins?list=DOGE"
            response = requests.request("GET",url)
            coin=response.json()
            hashs2=coin[0]['network_hashrate']/1000000
            st.write("Hashrate: {} in MH".format(hashs2))
            st.caption('AVG Power consumption: 200')
            st.caption('AVG Hashrate per miner: 25')
            noh=hashs2/25
            co2=(200/1000)*1*0.19338*noh
            prices=(co2/1000)*1.08
            st.write("UK Grid : {} kgC02e per hour".format(co2))
            st.write("Offset cost : {} $ per hour".format(prices))
            st.write("Offset cost : {} $ per hour per Miner".format(prices/noh))
            
def crd():
    st.write("Consensus Algorithnm : Proof of Stake")
    st.write("Mining Algorithnm : N/A")
    url = "https://api.blockchair.com/cardano/stats"
    response = requests.request("GET",url)
    coin=response.json()
    n='"0"'
    col1, col2, col3 = st.columns(3)
    with col1:
        hashs = st.number_input('Insert your hashrate in MH')
        n='"{}"'.format(hashs)
        x='<script async src="https://static.coinstats.app/widgets/coin-chart-widget.js"></script><coin-stats-chart-widget type="large" coin-id="cardano" width="400" chart-height="250" currency="USD" locale="en" bg-color="#FFFFFF" text-color="#1C1B1B" status-up-color="#4F8A5B" status-down-color="#FE4747" buttons-color="#FFFFFF" chart-color="#E47103" chart-gradient-from="#FFFFFF" chart-gradient-to="#EFEFEF" chart-label-background="#FFFFFF" candle-grids-color="rgba(0,0,0,0.1)" border-color="rgba(28,27,27,0.15)" font="Roboto, Arial, Helvetica" btc-color="#6DD400" eth-color="#2D73AD"></coin-stats-chart-widget>'
        components.html(x, width=400, height=400)
    with col3:
        st.write("Carbon Footprint in kgC02e")
        b = st.radio(" Select ", ['Manual', 'CryptoCurrency'])
        if b=="Manual":
            stakes=st.number_input('ADA Staked', min_value=10, max_value=1000000)
            total=coin['data']["circulation"]
            per_stakes=(stakes/total)*100
            co2=16438.3561643836*0.19338
            per_co2=int(co2)*per_stakes
            st.write("24hr CO2 consumption: {} kgCO2e".format(per_co2))
            prices=per_co2*1.08
            st.write("Offset cost : {} $".format(prices))
        if b=="CryptoCurrency":
            st.write("24hr Power consumption: 16438.3561643836 kWh")
            co2=16438.3561643836*0.19338
            st.write("24hr CO2 consumption (UK Grid Electricity): {} kgCO2e".format(co2))
            prices=((co2)/24)*1.08
            st.write("Offset cost : {} $ per hour".format(prices))
            
def mat():
    url = "https://api.minerstat.com/v2/coins?list=ETC"
    response = requests.request("GET",url)
    coin=response.json()
    st.write("Consensus Algorithnm : Proof of Stake")
    st.write("Mining Algorithnm : N/A")
    col1, col2, col3 = st.columns(3)
    with col1:
        x='<script async src="https://static.coinstats.app/widgets/coin-chart-widget.js"></script><coin-stats-chart-widget type="large" coin-id="matic-network" width="400" chart-height="250" currency="USD" locale="en" bg-color="#FFFFFF" text-color="#1C1B1B" status-up-color="#4F8A5B" status-down-color="#FE4747" buttons-color="#FFFFFF" chart-color="#E47103" chart-gradient-from="#FFFFFF" chart-gradient-to="#EFEFEF" chart-label-background="#FFFFFF" candle-grids-color="rgba(0,0,0,0.1)" border-color="rgba(28,27,27,0.15)" font="Roboto, Arial, Helvetica" btc-color="#6DD400" eth-color="#2D73AD"></coin-stats-chart-widget>'
        components.html(x, width=400, height=400)
    with col3:
        st.write("Carbon Footprint in kgC02e")
        b = st.radio(" Select ", ['Manual', 'CryptoCurrency'])
        if b=="Manual":
            stakes=st.number_input('Matic Staked', min_value=10, max_value=100000000)
            total=2929039482.9891/0.8792
            per_stakes=(stakes/total)*100
            co2=(90)*1*0.19338
            per_co2=int(co2)*per_stakes
            st.write("24hr CO2 consumption: {} kgCO2e".format(per_co2))
            prices=per_co2*1.08
            st.write("Offset cost : {} $".format(prices))
        if b=="CryptoCurrency":
            st.write("Power Consumption : 90 kW per hour")
            co2=(90)*1*0.19338
            prices=(co2/1000)*1.08
            st.write("UK Grid : {} kgC02e per hour".format(co2))
            st.write("Offset cost : {} $ per hour".format(prices))