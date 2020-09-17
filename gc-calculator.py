import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt



st.write("""
# GC Content Calculator App

This app calculate the guanin-citosin content in given data

""")



st.sidebar.header("File Input")


uploaded_file = st.sidebar.file_uploader("asjhg", type=["csv","fasta"])




try:
    with open(str(uploaded_file)) as input:
        if st.checkbox('Show the genome'):
            st.subheader('Genome')
            st.text(input.read())
except FileNotFoundError:
    st.error("File Not Found")

gene = uploaded_file

def gc_content(gene):
    

    try:

        gene = open(str(uploaded_file), 'r')

        gene.readline()

        g = 0
        a = 0
        t = 0
        c = 0
        
        for line in gene:
            line = line.lower()
            for char in line:
                if char == "g":
                    g += 1
                if char == "a":
                    a += 1
                if char == "c":
                    c += 1
                if char == "t":
                    t += 1

        st.write("The number of **Guanin**: " + str(g))
        st.write("The number of **Cytosin**: " + str(c))
        st.write("The number of **Adenin**: " + str(a))
        st.write("The number of **Timin**: " + str(t))

        g_content = g
        c_content = c
        a_content = a
        t_content = t


        gc = (g+c+0.)/(a+g+t+c+0.)

        st.write("**GC content**: " + str(gc))

        
        nucleotides = ["Guanin", "Cytosin", "Adenin", "Timin"]
        numbers = [g_content, c_content, a_content, t_content]

        df = pd.DataFrame(numbers, index=nucleotides)
        plt.bar(nucleotides, numbers, label="Nucleotides", width=.2)

        st.pyplot()
        if st.checkbox('Show the table'):
            st.subheader('Table')
            st.write(df)
    except FileNotFoundError:
        st.error("Please give the path of your data")
    

    
    
    

gc_content(gene)






