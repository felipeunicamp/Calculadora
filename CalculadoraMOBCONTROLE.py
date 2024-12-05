import streamlit as st
import numpy as np
import locale

#st.set_page_config(layout='wide')
locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8')
st.title('Calculadora - MOB Controle')


st.text('Quantos EPIs são entregues por dia na sua empresa?')
vl1 = st.number_input('Digite aqui a quantidade de EPIs. Ex:100',min_value=0)
st.text('Quantos minutos são necessários para entregar um EPI?')
vl2 = st.number_input('Digite aqui os minutos. Ex: 5',min_value=0)
st.text('Qual o salário médio na sua empresa?')
vl3 = st.number_input('Digite aqui o salário médio. Ex: 2400',min_value=0)
botao = st.button('Calcular')
if botao:
    if vl1 > 0 and vl2 >0 and vl3 >0:
        ganho_horas = (((vl1 * vl2 * 60) - (vl1 * 4)) / 60) / 60
        ganho_financeiro_diário = ((vl3 + (vl3 / 2)) / 30) * ganho_horas
        ganho_financeiro_mensal = ganho_financeiro_diário * 30
        ganho_financeiro_anual = ganho_financeiro_mensal * 12
        ganho_horas_formatado = locale.format_string('%d', ganho_horas, grouping=True)
        ganho_financeiro_diário_formatado = locale.format_string('%d', ganho_financeiro_diário, grouping=True)
        ganho_financeiro_mensal_formatado = locale.format_string('%d', ganho_financeiro_mensal, grouping=True)
        ganho_financeiro_anual_formatado = locale.format_string('%d', ganho_financeiro_anual, grouping=True)

        st.text(f'Ganho de tempo diário é de {ganho_horas:.2f} horas.')
        st.text(f'Ganho financeiro diário é de R${ganho_financeiro_diário_formatado}.')
        st.text(f'Ganho financeiro mensal é de R${ganho_financeiro_mensal_formatado}.')
        st.text(f'Ganho financeiro anual é de R${ganho_financeiro_anual_formatado}.')
    else:
        st.text('Por favor, insira valores válidos.')
else:
    st.text('Por favor, insira valores nos campos acima.')
st.image(r'C:\Users\felipe.goncalves\PycharmProjects\opencv\.venv\MOB_Controle.png')