# 🐾 Mascote de Área de Trabalho Dinâmico (Python)

Este projeto é um widget interativo para Windows que cria um mascote animado (baseado em sprites de Pokémon ou qualquer GIF) que voa pela sua área de trabalho. O diferencial deste projeto é ser **totalmente dinâmico**, permitindo trocar a "skin" do mascote sem necessidade de recompilar o código.

https://github.com/user-attachments/assets/8b6820db-79c4-4d45-90f1-674997b80947

## 🚀 Funcionalidades

- **Animação Fluida:** Suporta GIFs animados com redimensionamento automático de alta qualidade (via Pillow).
- **Movimentação Automática:** O mascote voa sozinho pela tela (da direita para a esquerda).
- **Interatividade:** - **Arrastar:** Clique com o botão esquerdo e segure para posicionar o mascote onde quiser.
  - **Fechar:** Clique com o botão direito para encerrar o aplicativo instantaneamente.
- **Camada Inteligente:** O widget é configurado para ficar atrás de outras janelas abertas, comportando-se como parte do papel de parede.
- **Portabilidade:** Versão executável (.exe) inclusa que dispensa a instalação do Python.

## 🛠️ Tecnologias Utilizadas

- **Python 3.1x**
- **Tkinter:** Para a interface gráfica e manipulação de janelas transparentes.
- **Pillow (PIL):** Para processamento de imagem e suporte a GIFs animados.
- **PyInstaller:** Para compilação do executável autônomo.

## 📥 Como Usar

1. Baixe o arquivo `mascote.exe` na aba [Releases](https://github.com/SeuUsuario/SeuRepo/releases).
2. Coloque o executável em uma pasta de sua preferência.
3. Certifique-se de que existe um arquivo chamado **`mascote.gif`** na mesma pasta.
4. Execute o `mascote.exe`.

## 🎨 Como trocar o Pokémon (Skins)

O motor do aplicativo foi desenvolvido para ser independente da imagem. Para mudar o mascote que aparece na tela:

1. Escolha qualquer arquivo GIF animado.
2. Renomeie o arquivo escolhido para **`mascote.gif`**.
3. Substitua o arquivo antigo na pasta do programa pelo novo.
4. Reinicie o aplicativo.

> **Dica:** Para melhores resultados de transparência, utilize GIFs que tenham o fundo em verde sólido (#00FF00).

## 🔨 Compilação (Opcional)

Se você desejar compilar o seu próprio executável a partir do código fonte:

```bash
pip install Pillow pyinstaller
pyinstaller --noconsole --onefile mascote.py
