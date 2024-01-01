import streamlit as st
st.set_page_config(page_title='SITE MOZ')
st.title('Aqui encontras os melhores pratos moçambicanos e claro um pouco de tudo.')
st.write('PARA O CANAL DO YOUTUBE [clique aqui](https://youtu.be/hIYlso1RkVg?si=8oRw1tchKiUEN2l0)')
st.write('Para hoje iremos ver a receita de gulabos ')
st.subheader('...................................GULABOS.................................')
st.write('IGREDIENTES PARA PREPARAÇAO DA MASSA:')

col1, col2 = st.columns([1, 3])
with col2:
    st.image("receita.png", caption='receita.png', use_column_width=True)
# Adiciona uma coluna para o texto
with col1:
    st.write('#7 OVOS')
    st.write('#500 g de manteiga')
    st.write('#1 lata de leite condensado')
    st.write('#1 colher de cha de raspa de limao')
    st.write('#2 colheres de cha de custarde')
    st.write('#2 colheres de royal')
    st.write('#1 pacote de coco ralado')
    st.write('#Trigo ate dar o ponto')
with st.container():
    st.write('---')
    st.write('MODO DE PREPARAÇAO')
    st.write('Para a preparaçao deste docinho e necessario seguir os seguintes passos:')
    st.write('PRIMEIRO: Parta os 7 ovos completos(com as  gemas) e adicione a manteiga e as raspas de limao')
    st.write('SEGUNDO: Mexa com uma espatula ate a manteiga se desfazer por completo')
    st.write('TERCEIRO: Adicione a farinha mexendo com a espatula ate dar o ponto')
    st.write('Mais Lina que ponto e esse, aquele ponto em que massa fica meio durinha(nao dura e nem leve')
    st.write('QUARTO: Leve um tabuleiro e comece a fazer rolinhos para fritar')

imagem1 = '1.png'
imagem2 = '2.png'
imagem3 = '3.png'
col1, col2, col3 = st.columns(3)

with col1:
    st.image(imagem1, use_column_width=True)

with col2:
    st.image(imagem2, use_column_width=True)

with col3:
    st.image(imagem3, use_column_width=True)

imagem4 = '4.png'
imagem5 = '5.png'

col4, col5 = st.columns(2)
with col4:
    st.image(imagem4, use_column_width=True)
with col5:
    st.image(imagem5, use_column_width=True)
with st.container():
    st.write('O site ainda esta em desenvolvimento,para mais sugestoes,criticas produtivas por favor contacto 868787572')
    st.write('Se quiser ver mais informaçoes[clique aqui](https://youtube.com/@carolinamorais220?si=28qD3hnxHxGST7ws)')
