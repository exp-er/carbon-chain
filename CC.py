

import streamlit as st 
import streamlit.components.v1 as components

x='<a class="minerstat-widget" title="BTC mining calculator" data-coin="BTC" data-algo="SHA-256" data-info="yes" data-style="light" data-color="" data-unit="TH" data-hashrate="100" data-width="300" rel="nofollow" href="https://minerstat.com/coin/BTC">Bitcoin mining calculator</a><script async src="https://api.minerstat.com/v2/widgets/coin.js" charset="utf-8"></script>'
def btec():
    components.html(x, width=400, height=800)
