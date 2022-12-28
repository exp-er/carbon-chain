import streamlit as st 
from hashlib import sha256
import pandas as pd
import time
import altair as alt

import pyscrypt
import math, random, sys
from decimal import Decimal as dml
import binascii
import pycryptonight

MAX_NONCE = 100000000000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            return new_hash

    raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")


def sha256fun():
    
    transactions='''
    Akshat->Theo->10,
    X->Y->20
    A->B->10
    '''
    first_hash= SHA256("Akshat Pande | 2153363")
    

    timer=[]
    nonces=[]

    n= st.slider('Nonce', 0, 10, 1)
    st.caption('Nonces till 5-6 require less amount of time, easy to verify. Nonces over 6 may require extended periods for running!')
    

    for i in range(n):

        difficulty=i+1
        nonces.append(i+1)
        start = time.time()
        new_hash = mine(5,transactions,first_hash, difficulty)
        total_time = (time.time() - start) 
        timer.append(total_time)


    df=pd.DataFrame(nonces, columns=['Nonces'])
    df['Time Taken']=timer
    energ=pd.read_csv('result.csv', sep=';')
    energ.columns= ['timestamp','tag','duration','avg energy']
    energ.pop('timestamp')
    energ.pop('tag')

    bars = alt.Chart(df).mark_bar().encode(
    x='Nonces',
    y="Time Taken"
    )

    lines= alt.Chart(df).mark_line(point=True).encode(
    alt.X('Nonces', scale=alt.Scale(zero=False)),
    alt.Y('Time Taken', scale=alt.Scale(zero=False))
    )
    col1,col2,col3=st.columns(3)
    with col1:
    #st.altair_chart(bars+text)
        st.altair_chart(lines+bars)
    
    with col3:
        st.caption('time taken to run for each nonce')
        st.dataframe(df)
        st.caption('energy consumption to mine each nonce except the first (negligible)')
        st.dataframe(energ)


def ethash():
    st.error("Ethash development has been deprecated and was unable to be simulated for now. Will be updated in the future. The carbon footprint for currencies using ethash can be evaluated through other mediums using their hashrate and power consumption etc. Use proof of work in consensus algorithm to calcualte your carbon footprint after entering the details")

def scrypt():
    col1,col2,col3=st.columns(3)
    n=11
    timer=0
    counter=0
    with col1:
        salt = random.randint(0, 10).to_bytes(2, 'big')
        st.write('Salt for random interger: {}'.format(salt))
        passwd = b'Akshat@2153363'
        st.write('Given Password: {}'.format(passwd))
        key = pyscrypt.hash(passwd, salt, 2048, 8, 1, 32)
        key.hex()
        answer=key.hex()
        st.write('OG Key Generated: {}'.format(answer))
    with col3:
        for i in range(n):
            start = time.time()
            salt2 = i.to_bytes(2, 'big')
            st.write('Iteration : {}'.format(i))
            st.write(salt2)
            key2 = pyscrypt.hash(passwd, salt2, 2048, 8, 1, 32)
            test=key2.hex()
            st.write(test)
            if test == answer:
                counter=i
                with col1:

                    total_time = (time.time() - start) 
                    st.write('----Scrypt Solved-------')
                    st.write("Iterations taken: {}".format(counter))
                    st.write("Time Taken: {}".format(total_time))
                break

    

def equil():
    
    people = st.slider("Please enter how many random 'people' you'd like to simulate: ", 1, 365,10)
    trial = []
    timer=[]
    matches = 0
    nomatches = 0



    for i in range(1,200,10):

        trials=i
        total_trials=trials
        start = time.time()
        def findmatches( numbers ):
            s = set()
            ans = False
            for number in numbers:
                if numbers.count(number) > 1:
                    s.add(number)
                    ans = True
            return ans, s
        while trials > 0:
            
            trials -= 1
            
            random.seed()

            numbers = [random.randrange(1,366) for i in range(people)]

            a,b = findmatches(numbers)
            
            if a == True:
                matches += 1

        result = dml(matches) / dml(total_trials) * 100
        expected =  (1 - dml(math.factorial(365)) / ( 365**people * math.factorial(365-people)))*100
        if result != 0:
            trial.append(i)
            pe = abs( (expected - dml(result) ) / dml(result)) * 100
            total_time = (time.time() - start)
            timer.append(total_time)
        else:
            trial.append(i)
            timer.append(0)
    
    df=pd.DataFrame(trial, columns=['Trials'])
    df['Time Taken']=timer
    
    bars = alt.Chart(df).mark_bar().encode(
    x='Trials',
    y="Time Taken"
    )

    lines= alt.Chart(df).mark_line(point=True).encode(
    alt.X('Trials', scale=alt.Scale(zero=False)),
    alt.Y('Time Taken', scale=alt.Scale(zero=False))
    )
    col1,col2,col3=st.columns(3)
    with col1:
    #st.altair_chart(bars+text)
        st.altair_chart(lines+bars)
    
    with col3:
        st.caption('time taken to run for each Trial')
        st.dataframe(df)
        st.write("Number of successful trials: {}".format(matches))
        st.write("Percent of successful trials: {}".format(round(result,4)))
        st.write("Expected percent of number of successful trials: {}".format(round(expected,4)))
        st.write("Percent of error: {}".format(round(pe,4)))
        
        
def crynight():
    timers=[]
    timerf=[]
    hashed=[]
    n=10
    for i in range(n):
        hashed.append(i)
        start = time.time()
        alts = i.to_bytes(2, 'big')
        pycryptonight.cn_fast_hash(alts).hex()
        total_time = (time.time() - start)
        timerf.append(total_time)
        
    
    for i in range(n):
        start = time.time()
        alts = i.to_bytes(2, 'big')
        pycryptonight.cn_slow_hash(alts).hex()
        total_time = (time.time() - start)
        timers.append(total_time)
    
    
    df=pd.DataFrame(hashed, columns=['HashedValue'])
    df['Fast Time Taken']=timerf
    df['Slow Time Taken']=timers
    
    barf = alt.Chart(df).mark_bar().encode(
    x='HashedValue',
    y="Fast Time Taken"
    )   
    
    bars = alt.Chart(df).mark_bar().encode(
    x='HashedValue',
    y="Slow Time Taken"
    )   

    st.altair_chart(bars)
    st.altair_chart(barf)
    st.dataframe(df)
