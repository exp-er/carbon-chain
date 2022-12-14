

import streamlit as st 
import streamlit.components.v1 as components
import requests

x='<a class="minerstat-widget" title="ETC mining calculator" data-coin="ETC" data-algo="Etchash" data-info="yes" data-style="light" data-color="" data-unit="MH" data-hashrate="100" data-width="300" rel="nofollow" href="https://minerstat.com/coin/ETC">Ethereum Classic mining calculator</a><script async src="https://api.minerstat.com/v2/widgets/coin.js" charset="utf-8"></script>'
url = "https://api.minerstat.com/v2/coins?list=ETC"
#response = requests.request("GET",url)

def btec():
    col1, col2, col3 = st.columns(3)
    with col1:
        components.html(x, width=400, height=800)
    with col3:
        url = "https://api.minerstat.com/v2/coins?list=ETC"
        response = requests.request("GET",url)
        coin=response.json()
        st.write("Hashrate")
        st.write(coin[0]['network_hashrate']/100000)
        payload = {'url': 'nvidia-rtx-3080'}
        url2 = "https://api.minerstat.com/v2/hardware?brand=nvidia"
        response2=requests.request("GET",url2,params=payload)
        hardware=response2.json()
        i=5
        st.write("ETC Hash for GPU")
        for i in range(10):
            st.write(hardware[i+10]['name'])
            st.write(hardware[i+10]['algorithms']['Etchash'])
            
