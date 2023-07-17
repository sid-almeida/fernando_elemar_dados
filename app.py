import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl
# load the data
data = pd.read_csv('https://raw.githubusercontent.com/sid-almeida/fernando_elemar_dados/main/fernanddo.csv?token=GHSAT0AAAAAACEWO6QOTOF2TKL2W73HMRXOZFVTTXA', encoding='cp1258', index_col=0)

with st.sidebar:
    st.image("https://github.com/sid-almeida/fernando_elemar_dados/blob/d8bcb49ffca0bafc2ff29b132d9de2049c107928/Brainize%20Tech%20(1).png", width=250)
    st.title("Dashboard de Alunos")
    choice = option_menu(
        None, ["Sobre", "DataSet", "Dashboard"],
    icons=["file-person-fill", "table", "bar-chart-fill", "telephone-fill"])

    st.info('**Nota:** Esta aplicação foi desenvolvida com base em dados específicos e destina-se apenas a esse propósito. Por favor, evite utilizá-la para outros fins.')

if choice == "Sobre":
    st.write("""
        # Dashboard de Alunos
        Utilizando as bibliotecas Streamlit, Dash e Plotly. Neste aplicativo, criamos uma plataforma interativa que serve como uma referência visual aos dados dos alunos do Professor Fernando..
        """)
    st.write('---')
    st.write('**Sobre o App:**')
    st.write("""
        Ao utilizar o Streamlit, conseguimos construir uma interface web simples e intuitiva, permitindo uma experiência de uso fluida e acessível. Com o Dash, conseguimos adicionar recursos de criação de painéis interativos, possibilitando uma visualização dinâmica dos dados.
O grande destaque do aplicativo é o uso da biblioteca Plotly, que oferece uma ampla variedade de gráficos interativos e personalizáveis. Com o Plotly, podemos criar gráficos de linha, barras, dispersão, mapas de calor e muito mais, garantindo uma apresentação visualmente atraente e informativa dos dados dos alunos.
A combinação dessas bibliotecas nos permitiu desenvolver um aplicativo rico em recursos, fornecendo uma interface amigável para explorar e analisar os dados dos alunos do Professor Fernando. Esperamos que essa ferramenta seja uma fonte valiosa de informações e insights para melhorar o acompanhamento e a tomada de decisões relacionadas aos alunos.
        """)
    st.info(
        '**Note:** Please be aware that this application is intended solely for educational purposes. It is strongly advised against utilizing this tool for making any financial decisions.')
    st.write('---')

if choice == "DataSet":
    # Criei uma dashboard com o streamlit, dash e plotly
    st.title("DataSet de Alunos")
    st.write('---')
    st.write('**DataSet:**')
    st.write(data)
    st.write('---')
    st.info('**Nota:** Esta aplicação foi desenvolvida com base em dados específicos e destina-se apenas a esse propósito. Por favor, evite utilizá-la para outros fins.')

if choice == "Dashboard":
    st.title("Dashboard de Alunos")
    st.write('---')
    dashboard = st.selectbox("Selecione a Visualização Desejada", ["Supervisionados (Sim/Não) por Curso", "Alunos Orientados por Modalidade", "Alunos Orientados por Agente Integrador",
                                                                   "Supervisionados (Sim/Não) por Status", "Status por Curso", "Status por Concedente", "Encoding & Correlação (Mapa de Calor)"])
    if dashboard == "Supervisionados (Sim/Não) por Curso":
        # Gráfico de Barras (Supervisionados) com sns
        st.write('**Gráfico de Barras (Supervisionados):**')
        sns.set_style('darkgrid')
        fig1, ax = plt.subplots(figsize=(15, 12))
        sns.countplot(x='Curso', hue='Supervisor', data=data)
        plt.style.use('ggplot')
        plt.title('Gráfico de Barras (Supervisionados)')
        plt.xlabel('Curso')
        plt.ylabel('Supervisor')
        novas_labels = ['Não', 'Sim']
        plt.legend(loc='upper right', labels=novas_labels)
        st.pyplot(fig1)
        st.write('---')

    if dashboard == "Alunos Orientados por Modalidade":
        st.write('**Gráfico de Barras (Orientados por Modalidade):**')
        sns.set_style('darkgrid')
        fig2, ax = plt.subplots(figsize=(15, 12))
        sns.countplot(x='Modalidade', data=data)
        plt.style.use('ggplot')
        plt.title('Gráfico de Barras (Orientados por Modalidade)')
        plt.xlabel('Modalidade')
        plt.ylabel('Orientados')
        st.pyplot(fig2)
        st.write('---')

    if dashboard == "Alunos Orientados por Agente Integrador":
        st.write('**Gráfico de Barras (Orientados por Agente Integrador):**')
        sns.set_style('darkgrid')
        fig3, ax = plt.subplots(figsize=(15,12))
        sns.countplot(x='Agente Integrador', data=data)
        plt.style.use('ggplot')
        plt.title('Gráfico de Barras (Orientados por Agente Integrador)')
        plt.xlabel('Agente Integrador')
        plt.ylabel('Orientados')
        st.pyplot(fig3)
        st.write('---')

    if dashboard == "Supervisionados (Sim/Não) por Status":
        st.write('**Gráfico de Barras (Supervisionados por Status):**')
        sns.set_style('darkgrid')
        fig4, ax = plt.subplots(figsize=(15,12))
        sns.countplot(x='Status', hue='Supervisor', data=data)
        plt.style.use('ggplot')
        plt.title('Gráfico de Barras (Supervisionados por Status)')
        plt.xlabel('Status')
        plt.ylabel('Supervisor')
        novas_labels = ['Não', 'Sim']
        plt.legend(loc='upper right', labels=novas_labels)
        st.pyplot(fig4)
        st.write('---')

    if dashboard == "Status por Curso":
        st.write('**Gráfico de Barras (Status por Curso):**')
        sns.set_style('darkgrid')
        fig5, ax = plt.subplots(figsize=(15,12))
        sns.countplot(x='Curso', hue='Status', data=data)
        plt.style.use('ggplot')
        plt.title('Gráfico de Barras (Status por Curso)')
        plt.xlabel('Curso')
        plt.ylabel('Status')
        novas_labels = ['Concluído', 'Indeferido', 'Encerrado', 'Em Andamento']
        plt.legend(loc='upper right', labels=novas_labels)
        st.pyplot(fig5)
        st.write('---')

    if dashboard == "Status por Concedente":
        # criei uma pivot table da quantidade de alunos em cada classe de status por concedente
        pivot_conc = data.pivot_table(index='Concedente', columns='Status', aggfunc='size')
        # criei um gráfico de barras empilhadas com a pivot table
        fig6, ax = plt.subplots(figsize=(20,12))
        pivot_conc.plot(kind='bar', stacked=True, ax=ax)
        plt.style.use('ggplot')
        plt.title('Gráfico de Barras Empilhadas (Status por Concedente)')
        plt.xlabel('Concedente')
        plt.ylabel('Status')
        st.pyplot(fig6)
        st.info('**Nota:** Para melhorar a visibilidade, favor utilizar o botão de FullScreen no canto superior direito.')
        st.write('---')

    if dashboard == "Encoding & Correlação (Mapa de Calor)":
        st.info('**Nota:** Esta é uma opção avançada que utiliza machine learning para encodar as variáveis categóricas e gerar uma matriz de correlação. Encodar dados que não representam categorias (como datas por exemplo) poderá acarretar em interpretações equivocadas sobre os dados. Utilize com cuidado.')
        # Selecione as colunas que serão encodadas
        colunas = st.multiselect('Selecione as colunas que serão encodadas', data.columns)
        # Criei um dataframe com as colunas selecionadas
        data_encoded = data[colunas]
        # Encodei as colunas selecionadas com o LabelEncoder via botão
        if st.button('Encode'):
            from sklearn.preprocessing import LabelEncoder
            le = LabelEncoder()
            for col in colunas:
                data_encoded[col] = le.fit_transform(data_encoded[col])
            # Criei uma matriz de correlação utilizando o método de Pearson
            corr = data_encoded.corr(method='pearson')
            # Criei um mapa de calor com a matriz de correlação
            fig7, ax = plt.subplots(figsize=(35,20))
            sns.heatmap(corr, annot=True, ax=ax, cmap='coolwarm')
            plt.style.use('ggplot')
            plt.title('Mapa de Calor (Correlação)')
            st.pyplot(fig7)
            st.info('**Nota:** Para melhorar a visibilidade, favor utilizar o botão de FullScreen no canto superior direito.')
            st.write('---')

st.write('Made with ❤️ by [Sidnei Almeida](https://www.linkedin.com/in/saaelmeida93/)')
