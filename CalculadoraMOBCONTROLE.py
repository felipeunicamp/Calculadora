import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Configuração da página
st.set_page_config(
    page_title="MOB Controle - Calculadoras de Ganhos",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado para melhorar a aparência
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
    }

    .main-header h1 {
        color: white !important;
        margin: 0;
        font-size: 2.5rem;
    }

    .main-header p {
        color: white;
        margin: 0.5rem 0 0 0;
        opacity: 0.9;
    }

    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #2a5298;
        margin: 1rem 0;
    }

    .result-positive {
        background: linear-gradient(90deg, #56ab2f 0%, #a8e6cf 100%);
        padding: 1rem;
        border-radius: 8px;
        color: white;
        font-weight: bold;
        margin: 0.5rem 0;
    }

    .input-section {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }

    .stTab > div > div > div > div {
        padding: 2rem 1rem;
    }
</style>
""", unsafe_allow_html=True)


def formatar_dinheiro(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def criar_grafico_economia(valores_dict, titulo):
    """Cria gráfico de barras para mostrar economia"""
    fig = go.Figure()

    categorias = list(valores_dict.keys())
    valores = list(valores_dict.values())

    fig.add_trace(go.Bar(
        x=categorias,
        y=valores,
        marker_color=['#2a5298', '#56ab2f', '#ff6b6b'],
        text=[formatar_dinheiro(v) for v in valores],
        textposition='auto',
    ))

    fig.update_layout(
        title=titulo,
        xaxis_title="Período",
        yaxis_title="Economia (R$)",
        showlegend=False,
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
    )

    return fig


# Header principal
st.markdown("""
<div class="main-header">
    <h1>🏢 MOB Controle - Calculadoras de Ganhos</h1>
    <p>Descubra o potencial de economia da sua empresa com nossas soluções</p>
</div>
""", unsafe_allow_html=True)

# Sidebar com informações
with st.sidebar:
    st.markdown("### 📊 Sobre as Calculadoras")
    st.info("""
    **MOB Controle**: Otimização de entregas de EPI

    **Dispenser Machine**: Automação de distribuição

    **Loja In Company**: Gestão completa de estoque
    """)

    st.markdown("### 💡 Dicas")
    st.success("Use dados reais da sua empresa para obter resultados mais precisos!")

# Tabs principais
aba1, aba2, aba3 = st.tabs(['🎯 MOB Controle', '🤖 Dispenser Machine', '🏪 Loja In Company'])

with aba1:
    st.markdown("## 🎯 Calculadora MOB Controle")
    st.markdown("**Otimize o processo de entrega de EPIs e reduza custos operacionais**")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown('<div class="input-section">', unsafe_allow_html=True)
        st.markdown("### 📝 Dados da sua empresa")

        vl1 = st.number_input(
            '📦 Quantos EPIs são entregues por dia?',
            min_value=0,
            value=100,
            help="Número médio de EPIs distribuídos diariamente"
        )

        vl2 = st.number_input(
            '⏱️ Tempo para entregar um EPI (minutos)',
            min_value=0,
            value=5,
            help="Tempo médio gasto para localizar, registrar e entregar um EPI"
        )

        vl3 = st.number_input(
            '💰 Salário médio mensal (R$)',
            min_value=0,
            value=2400,
            help="Salário médio dos colaboradores responsáveis pela distribuição"
        )

        st.markdown('</div>', unsafe_allow_html=True)

        calcular_mob = st.button('🚀 Calcular Economia', key='mob_calc', type='primary')

    with col2:
        st.markdown("### 📈 Benefícios do MOB Controle")
        st.markdown("""
        - ✅ Redução de 99% no tempo de entrega
        - ✅ Controle total de estoque
        - ✅ Rastreabilidade completa
        - ✅ Redução de custos operacionais
        - ✅ Maior produtividade da equipe
        """)

    if calcular_mob and vl1 > 0 and vl2 > 0 and vl3 > 0:
        # Cálculos
        ganho_horas = (((vl1 * vl2 * 60) - (vl1 * 4)) / 60) / 60
        custo_hora = (vl3 + (vl3 * 0.5)) / (30 * 8)  # Incluindo encargos
        ganho_financeiro_diário = custo_hora * ganho_horas
        ganho_financeiro_mensal = ganho_financeiro_diário * 22  # Dias úteis
        ganho_financeiro_anual = ganho_financeiro_mensal * 12

        # Resultados
        st.markdown("## 📊 Resultados da Análise")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "⏰ Economia Diária",
                f"{ganho_horas:.1f} horas",
                delta=f"{ganho_horas * 60:.0f} min economizados"
            )

        with col2:
            st.metric(
                "💵 Economia Diária",
                formatar_dinheiro(ganho_financeiro_diário),
                delta="Por dia útil"
            )

        with col3:
            st.metric(
                "📅 Economia Mensal",
                formatar_dinheiro(ganho_financeiro_mensal),
                delta=f"{ganho_horas * 22:.0f}h/mês"
            )

        with col4:
            st.metric(
                "🎯 Economia Anual",
                formatar_dinheiro(ganho_financeiro_anual),
                delta="Potencial total"
            )

        # Gráfico
        valores_economia = {
            'Diário': ganho_financeiro_diário,
            'Mensal': ganho_financeiro_mensal,
            'Anual': ganho_financeiro_anual
        }

        fig = criar_grafico_economia(valores_economia, "Economia Financeira - MOB Controle")
        st.plotly_chart(fig, use_container_width=True)


with aba2:
    st.markdown("## 🤖 Calculadora Dispenser Machine")
    st.markdown("**Automatize a distribuição de EPIs e elimine deslocamentos desnecessários**")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown('<div class="input-section">', unsafe_allow_html=True)
        st.markdown("### 📝 Informações operacionais")

        epi = st.number_input(
            '📦 EPIs entregues por dia',
            min_value=0,
            value=50,
            help="Quantidade diária de EPIs distribuídos"
        )

        tempo_almox = st.number_input(
            '🚶 Tempo de deslocamento ao almoxarifado (minutos)',
            min_value=0,
            value=10,
            help="Tempo médio de ida e volta ao almoxarifado"
        )

        salario = st.number_input(
            '💰 Salário médio mensal (R$)',
            min_value=0,
            value=2400,
            help="Salário médio dos colaboradores"
        )

        st.markdown('</div>', unsafe_allow_html=True)

        calcular_dispenser = st.button('🚀 Calcular Economia', key='dispenser_calc', type='primary')

    with col2:
        st.markdown("### 🎯 Vantagens do Dispenser")
        st.markdown("""
        - ⚡ Acesso 24/7 aos EPIs
        - 🎯 Redução de deslocamentos
        - 📊 Controle automático de estoque
        - 🔒 Segurança na distribuição
        - 📱 Interface intuitiva
        """)

    if calcular_dispenser and epi > 0 and tempo_almox > 0 and salario > 0:
        # Cálculos
        salario_hora = (salario * 1.5) / 220  # Incluindo encargos
        economia_horas_dia = epi * (tempo_almox / 60)
        economia_financeira_dia = economia_horas_dia * salario_hora
        economia_mes = economia_financeira_dia * 22
        economia_ano = economia_mes * 12

        # Resultados
        st.markdown("## 📊 Impacto da Automação")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "⏰ Tempo Economizado",
                f"{economia_horas_dia:.1f}h/dia",
                delta=f"{economia_horas_dia * 60:.0f} min/dia"
            )

        with col2:
            st.metric(
                "💵 Economia Diária",
                formatar_dinheiro(economia_financeira_dia),
                delta="Por dia útil"
            )

        with col3:
            st.metric(
                "📅 Economia Mensal",
                formatar_dinheiro(economia_mes),
                delta=f"{economia_horas_dia * 22:.0f}h/mês"
            )

        with col4:
            st.metric(
                "🎯 Economia Anual",
                formatar_dinheiro(economia_ano),
                delta="Potencial total"
            )

        # Gráfico
        valores_economia = {
            'Diário': economia_financeira_dia,
            'Mensal': economia_mes,
            'Anual': economia_ano
        }

        fig = criar_grafico_economia(valores_economia, "Economia com Dispenser Machine")
        st.plotly_chart(fig, use_container_width=True)

with aba3:
    st.markdown("## 🏪 Calculadora Loja In Company")
    st.markdown("**Análise completa de custos operacionais vs. terceirização**")

    # Seção de inputs organizados em colunas
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 👥 Custos com Pessoal")
        vl4 = st.number_input('💼 Salário do comprador (R$)', min_value=0, value=3367)
        vl5 = st.number_input('⏰ Horas mensais em compras de EPI', min_value=0, value=40)
        vl6 = st.number_input('🛡️ Salário do Técnico de Segurança (R$)', min_value=0, value=4198)
        vl7 = st.number_input('⏱️ Horas mensais do Técnico com EPI', min_value=0, value=2)

    with col2:
        st.markdown("### 🏭 Custos Operacionais")
        vl8 = st.number_input('📏 Área do estoque (m²)', min_value=0, value=1000)
        vl9 = st.number_input('📊 % do estoque para EPI (ex: 0.1 = 10%)', min_value=0.0, max_value=1.0, value=0.1,
                              step=0.01)
        vl10 = st.number_input('💰 Custo mensal por m² (R$)', min_value=0, value=30)
        vl11 = st.number_input('📦 Custo de movimentação por EPI (R$)', min_value=0.0, value=3.5, step=0.1)

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("### 📈 Volume e Perdas")
        vl12 = st.number_input('📦 EPIs entregues por dia', min_value=0, value=100)
        vl13 = st.number_input('📉 % de perda anual (ex: 0.02 = 2%)', min_value=0.0, max_value=1.0, value=0.02,
                               step=0.01)

    with col4:
        st.markdown("### 💸 Investimento Total")
        vl14 = st.number_input('🛒 Gasto anual com EPI (R$)', min_value=0, value=250000)

    calcular_loja = st.button('🚀 Calcular Análise Completa', key='loja_calc', type='primary')

    if calcular_loja:
        # Cálculos detalhados
        encargos_rate = 1.5  # 50% de encargos

        # Custos com pessoal
        custo_hora_comprador = (vl4 * encargos_rate) / 220
        custo_mensal_comprador = custo_hora_comprador * vl5

        custo_hora_tecnico = (vl6 * encargos_rate) / 220
        custo_mensal_tecnico = custo_hora_tecnico * vl7

        custo_total_pessoal_mensal = custo_mensal_comprador + custo_mensal_tecnico
        custo_total_pessoal_anual = custo_total_pessoal_mensal * 12

        # Custos operacionais
        custo_armazenamento_mensal = vl8 * vl9 * vl10
        custo_movimentacao_mensal = vl11 * vl12 * 22  # Dias úteis
        custo_perdas_anual = vl13 * vl14

        custo_total_operacional_anual = (custo_armazenamento_mensal * 12) + (
                    custo_movimentacao_mensal * 12) + custo_perdas_anual

        # Custo total
        custo_total_anual = custo_total_pessoal_anual + custo_total_operacional_anual

        # Resultados em dashboard
        st.markdown("## 📊 Dashboard de Custos Operacionais")

        # Métricas principais
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "👥 Custo Pessoal/Mês",
                formatar_dinheiro(custo_total_pessoal_mensal),
                delta=f"{vl5 + vl7}h/mês"
            )

        with col2:
            st.metric(
                "🏭 Custo Operacional/Ano",
                formatar_dinheiro(custo_total_operacional_anual),
                delta=f"{vl8 * vl9:.0f}m² EPI"
            )

        with col3:
            st.metric(
                "💸 Custo Total/Ano",
                formatar_dinheiro(custo_total_anual),
                delta="Custo atual"
            )

        with col4:
            st.metric(
                "📉 Perdas/Ano",
                formatar_dinheiro(custo_perdas_anual),
                delta=f"{vl13 * 100:.1f}% do estoque"
            )

        # Breakdown de custos
        st.markdown("### 📋 Detalhamento de Custos")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### 👥 Custos com Pessoal")
            st.write(f"• **Comprador**: {formatar_dinheiro(custo_mensal_comprador * 12)}/ano")
            st.write(f"• **Técnico de Segurança**: {formatar_dinheiro(custo_mensal_tecnico * 12)}/ano")
            st.write(f"• **Total Pessoal**: {formatar_dinheiro(custo_total_pessoal_anual)}/ano")

        with col2:
            st.markdown("#### 🏭 Custos Operacionais")
            st.write(f"• **Armazenamento**: {formatar_dinheiro(custo_armazenamento_mensal * 12)}/ano")
            st.write(f"• **Movimentação**: {formatar_dinheiro(custo_movimentacao_mensal * 12)}/ano")
            st.write(f"• **Perdas**: {formatar_dinheiro(custo_perdas_anual)}/ano")

        # Gráfico de pizza para distribuição de custos
        fig_pie = go.Figure(data=[go.Pie(
            labels=['Pessoal', 'Armazenamento', 'Movimentação', 'Perdas'],
            values=[
                custo_total_pessoal_anual,
                custo_armazenamento_mensal * 12,
                custo_movimentacao_mensal * 12,
                custo_perdas_anual
            ],
            hole=0.4,
            marker_colors=['#2a5298', '#56ab2f', '#ff6b6b', '#ffa726']
        )])

        fig_pie.update_layout(
            title="Distribuição de Custos Anuais",
            height=400,
            showlegend=True
        )

        st.plotly_chart(fig_pie, use_container_width=True)

        # Proposta de economia
        st.markdown("### 💡 Oportunidade de Economia")
        economia_estimada = custo_total_anual * 0.3  # Estimativa de 30% de economia

        st.success(f"""
        **Economia potencial anual**: {formatar_dinheiro(economia_estimada)}

        **Benefícios adicionais**:
        - Redução de 70% no tempo de gestão
        - Controle total de estoque
        - Compliance automático
        - Relatórios em tempo real
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p>🏢 <strong>MOB Controle</strong> - Soluções inteligentes para gestão de EPIs</p>
    <p>📞 Entre em contato para uma demonstração personalizada -  (11) 9 6479-2134</p>
</div>
""", unsafe_allow_html=True)
