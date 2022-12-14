import streamlit as st 
from hashlib import sha256
import matplotlib.pyplot as plt
import pandas as pd

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

if __name__=='__main__':
    transactions='''
    Akshat->Theo->10,
    X->Y->20
    A->B->10
    '''

    timer=[0]
    nonces=[0]
    for i in range(5):

        difficulty=i
        nonces.append(i)
     # try changing this to higher number and you will see it will take more time for mining as difficulty increases
        import time
        start = time.time()
        new_hash = mine(5,transactions,'0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty)
        total_time = str((time.time() - start))
        timer.append(total_time*1000000)
    



    data= pd.DataFrame(timer, columns = ['time_taken'])
    st.dataframe(data)
    