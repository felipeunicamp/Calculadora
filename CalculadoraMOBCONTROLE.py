import streamlit as st
import numpy as np
import locale

#st.set_page_config(layout='wide')
#locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8')

def formatar_dinheiro(valor):
    return f"R${valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

st.title('Calculadora - MOB Controle')

aba1, aba2 = st.tabs(['Calculadora MOB CONTROLE', 'Calculadora Loja In Company'])

with aba1:
    st.text('Quantos EPIs são entregues por dia na sua empresa?')
    vl1 = st.number_input('Digite aqui a quantidade de EPIs. Ex:100', min_value=0)
    st.text('Quantos minutos são necessários para entregar um EPI?')
    vl2 = st.number_input('Digite aqui os minutos. Ex: 5', min_value=0)
    st.text('Qual o salário médio na sua empresa?')
    vl3 = st.number_input('Digite aqui o salário médio. Ex: 2400', min_value=0)
    
    botao = st.button('Calcular')
    if botao:
        if vl1 > 0 and vl2 > 0 and vl3 > 0:
            ganho_horas = (((vl1 * vl2 * 60) - (vl1 * 4)) / 60) / 60
            ganho_financeiro_diário = ((vl3 + (vl3 / 2)) / 30) * ganho_horas
            ganho_financeiro_mensal = ganho_financeiro_diário * 30
            ganho_financeiro_anual = ganho_financeiro_mensal * 12
            
            ganho_financeiro_diário_formatado = formatar_dinheiro(ganho_financeiro_diário)
            ganho_financeiro_mensal_formatado = formatar_dinheiro(ganho_financeiro_mensal)
            ganho_financeiro_anual_formatado = formatar_dinheiro(ganho_financeiro_anual)

            st.text(f'Ganho de tempo diário é de {ganho_horas:.2f} horas.')
            st.text(f'Ganho financeiro diário é de {ganho_financeiro_diário_formatado}.')
            st.text(f'Ganho financeiro mensal é de {ganho_financeiro_mensal_formatado}.')
            st.text(f'Ganho financeiro anual é de {ganho_financeiro_anual_formatado}.')    
        else:
            st.text('Por favor, insira valores válidos.')
    else:
        st.text('Por favor, insira valores nos campos acima.')
    
    st.image('MOB_Controle.png')

with aba2:
    st.text('Qual o salário do comprador? Ex: média do mercado é de R$3.367,00.')
    vl4 = st.number_input('Digite aqui o salário. Ex: 3367')
    st.text('Quantas horas mensais são gastas com compras de EPI? Ex: A média mensal é 40 horas.')
    vl5 = st.number_input('Digite aqui a quantidade de horas. Ex: 40')
    st.text('Qual o salário do Técnico de Segurança na sua empresa? Ex: A média no mercado é de R$4.198,00.')
    vl6 = st.number_input('Digite aqui o salário. Ex: 4198')
    st.text('Quantas horas mensais o Técnico de Segurança gasta com o processo de compra de EPI? Ex: A média no mercado é 2 horas.')
    vl7 = st.number_input('Digite quantas horas. Ex: Se forem 2 horas, insira 2')
    st.text('Qual o tamanho do estoque atual em m²?')
    vl8 = st.number_input('Digite aqui a área do estoque. Ex: 10000')
    st.text('Qual a porcentagem do estoque dedicado a EPI?')
    vl9 = st.number_input('A média no mercado é de 5% a 15%. Ex: Se for 10%, inserir 0,1.')
    st.text('Qual o custo mensal do m² do estoque?')
    vl10 = st.number_input('A média no mercado é de 20 a 40 reais. Se for R$30,00, digite 30.')
    st.text('Qual o custo de movimentação de estoque?')
    vl11 = st.number_input('A média no mercado é de "R$3,50". Ex: Se for "R$3,50", digite 3,50')
    st.text('Quantos EPIs são entregues por dia?')
    vl12 = st.number_input('Digite o número de EPIs entregues diariamente. Ex: Se forem 100 EPIs, digite 100')
    st.text('Quanto se perde de EPI por ano devido à deterioração?')
    vl13 = st.number_input('A média no mercado é de 1% a 5% por ano. Ex: Se for 2%, inserir 0,02.')
    st.text('Qual o gasto anual com compras de EPI?')
    vl14 = st.number_input('Digite o valor de compras de EPI anual. Se for R$250.000,00, digite 250000')
    
    botao1 = st.button('Calcular', key='Calcular_aba2')
    if botao1:
        encargos_compras = vl4
        custo_hora_mes_compras = (vl4 + encargos_compras) / 220
        custo_mes_compras = custo_hora_mes_compras * vl5
        encargos_tecseg = vl6
        custo_hora_mes_tecseg = (vl6 + encargos_tecseg) / 220
        custo_mes_tecseg = custo_hora_mes_tecseg * vl7
        custo_total_colaborador_mensal = custo_mes_tecseg + custo_mes_compras
        custo_total_colaborador_mensal_formatado = formatar_dinheiro(custo_total_colaborador_mensal)
        custo_total_colaborador_anual = custo_total_colaborador_mensal * 12
        custo_total_colaborador_anual_formatado = formatar_dinheiro(custo_total_colaborador_anual)

        custo_armazenamento_epi = vl8 * vl9 * vl10
        custo_movimentacao_epi = vl11 * vl12 * 30
        custo_perdas_epi = vl13 * vl14
        custo_total_estoque_ano = (custo_armazenamento_epi * 12) + (custo_movimentacao_epi * 12) + custo_perdas_epi
        custo_total_estoque_ano_formatado = formatar_dinheiro(custo_total_estoque_ano)
        custo_total_empresa_epi = custo_total_colaborador_anual + custo_total_estoque_ano
        custo_total_empresa_epi_formatado = formatar_dinheiro(custo_total_empresa_epi)

        st.text(f'O custo mensal com colaborador é de {custo_total_colaborador_mensal_formatado}.')
        st.text(f'O custo anual com colaborador é de {custo_total_colaborador_anual_formatado}.')
        st.text(f'O custo anual com estoque de EPI é de {custo_total_estoque_ano_formatado}.')
        st.text(f'O custo total anual para compra e armazenamento de EPI é de {custo_total_empresa_epi_formatado}.')
    else:
        st.text('Por favor, insira valores nos campos acima.')
    
    st.image('MOB_Controle.png')
