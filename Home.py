import streamlit as st
from PIL import Image

st.set_page_config(
    page_title = 'Home',
    layout='wide'
)

image = Image.open('logo.png')
st.sidebar.image(image, width=120)

# ===============================
# Barra Lateral no Streamlit
# ===============================

st.sidebar.markdown('# Curry Company')
st.sidebar.markdown('## Fastest Delivery in Town')
st.sidebar.markdown("""---""")

st.write('# Curry Company Growth Dashboard')

st.markdown(
    """
    Growth Dashboard foi construído para acompanhar as métricas de crescimento dos Entregadores e Restaurantes;
    ### Como utilizar esse Growth Dashboard?
    - Visão Empresa:
        - Visão Gerencial: Métricas gerais de comportamento.
        - Visão Tática: Indicadores semanais de crescimento;
        - Visão Geográfica: Insights de localização.
    - Visão Entregador:
        - Acompanhamento dos indicadores semanais de crescimento.
    - Visão Restaurantes:
        - Indicadores semanais de crescimento de restaurantes.
    ### Ask for Help
    - Time de Data Science no Discord
        -@meigarom
    """
)



st.sidebar.markdown("""---""")
st.sidebar.markdown('### Powered by Comunidade DS')