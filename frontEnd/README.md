# Alura Album - Copa do Mundo Tech

O **Alura Album** é uma aplicação web interativa inspirada nos clássicos álbuns de figurinhas físicos (como o da Copa do Mundo), mas adaptado para o universo da tecnologia. O objetivo principal do projeto é celebrar e homenagear grandes nomes e marcos da computação, divididos em categorias temáticas.

O álbum conta com um efeito visual premium de virada de páginas em 3D, efeitos sonoros realistas de papel gerados dinamicamente via código, suporte a gestos de arraste e integração com uma API backend para colar automaticamente as figurinhas colecionáveis nos slots corretos.

---

## 🚀 Funcionalidades Principais

*   **Efeito Flip-Book 3D:** Transição realista de virada de página ao arrastar com o mouse/toque ou usar os botões de navegação.
*   **Áudio Procedural:** Geração sintética do som de página virando utilizando a **Web Audio API** do navegador (sem necessidade de carregar arquivos `.mp3` ou `.wav` externos).
*   **Integração Dinâmica com API:** Busca automática das informações e imagens das figurinhas a partir de um servidor backend e as renderiza nos slots correspondentes em tempo real.
*   **Navegação Híbrida:** Suporta cliques nas setas laterais, teclas do teclado (`Seta Esquerda` e `Seta Direita`) e arraste na tela (Mouse/Touch).
*   **Design Responsivo e Premium:** Visual moderno com gradientes e estilo cyberpunk (efeitos de glitch e sombras realistas para simular a lombada física do livro).

---

## 📁 Estrutura e Função dos Arquivos

O projeto é composto por três arquivos essenciais no frontend:

### 1. [index.html](file:///c:/Users/gil_c/OneDrive/Documentos/Projetos%20TI/i-arq-ia-alura-album-main/index.html)
Define toda a estrutura semântica do álbum de figurinhas.
*   **Estrutura de Páginas:** Contém as marcações das páginas (Capa, Páginas de Conteúdo de #1 a #6 e Contracapa).
*   **Categorias Temáticas:**
    *   **IA (Pág. 1):** Pioneiros da Inteligência Artificial (ex: Alan Turing, John McCarthy, Sam Altman).
    *   **PYTHON (Pág. 2):** Arquitetos da Simplicidade (ex: Guido van Rossum, Tim Peters, Wes McKinney).
    *   **BANCO DE DADOS (Pág. 3):** Arquitetos de Bancos de Dados (ex: Edgar F. Codd, Michael Widenius, Salvatore Sanfilippo).
    *   **SISTEMAS OPERACIONAIS (Pág. 4):** Arquitetos da Computação Moderna (ex: Linus Torvalds, Dennis Ritchie, Steve Jobs).
    *   **BRASIL (Págs. 5 e 6):** Celebridades e educadores tech do Brasil (ex: Paulo Silveira, Guilherme Silveira, Gustavo Guanabara).
*   **Slots de Figurinhas:** Cada página possui slots demarcados (`.sticker-slot`) com um número identificador (ex: `#01`) e metadados básicos.
*   **Controles de Interface:** Botões de som (`#sound-toggle`) e setas de navegação lateral (`#btn-prev` e `#btn-next`).

### 2. [style.css](file:///c:/Users/gil_c/OneDrive/Documentos/Projetos%20TI/i-arq-ia-alura-album-main/style.css)
Responsável pelo visual moderno, animações e responsividade.
*   **Identidade Visual:** Paleta de cores baseada em tons de azul escuro espacial, preto e branco nevado, estilizado com gradientes circulares.
*   **Efeito Glitch & Brilhos:** Efeitos cyberpunk para a capa, incluindo textos com efeito glitch e um elemento central animado em 3D (Tech Sphere).
*   **Simulação Realista:** Sombreamentos dinâmicos nas bordas das páginas (`.page-content::after`) para simular a curvatura e a dobra física do álbum aberto.
*   **Animação ao "Colar":** Transição suave de escala e opacidade (`@keyframes sticker-aparecer`) para dar o efeito de figurinha sendo colada no slot assim que a imagem é carregada com sucesso do backend.

### 3. [app.js](file:///c:/Users/gil_c/OneDrive/Documentos/Projetos%20TI/i-arq-ia-alura-album-main/app.js)
Controla a lógica de comportamento e a interatividade da aplicação.
*   **Conexão com API:** Contém a função [preencherFigurinhas](file:///c:/Users/gil_c/OneDrive/Documentos/Projetos%20TI/i-arq-ia-alura-album-main/app.js#L12) que realiza uma requisição assíncrona (`fetch`) para a API local (`http://localhost:8000/figurinhas`) para obter os dados das figurinhas. Se disponível, as imagens são renderizadas nos slots correspondentes dinamicamente.
*   **Inicialização do PageFlip:** Configura as propriedades da biblioteca `St.PageFlip` (largura, altura, tempos de transição de 800ms, desativação de cliques acidentais e suporte a dispositivos móveis).
*   **Controle de Arraste (Drag):** Gerencia eventos de mouse (`mousedown`, `mousemove`, `mouseup`) e toque (`touchstart`, `touchmove`, `touchend`) para criar uma transição de dobra suave.
*   **Síntese de Som:** Contém a função [playPaperTurnSound](file:///c:/Users/gil_c/OneDrive/Documentos/Projetos%20TI/i-arq-ia-alura-album-main/app.js#L215) que utiliza a **Web Audio API** para gerar de forma procedural o ruído branco do papel e aplicar filtros dinâmicos de frequência (varredura exponencial de 1500Hz para 350Hz) simulando o som físico de uma folha sendo folheada.
*   **Navegação e Som:** Configura os atalhos de teclado, atualiza o estado de mute da aplicação e esconde/mostra setas de navegação de acordo com a página ativa.

---

## 🛠️ Como Executar o Projeto

### Pré-requisitos
1. Um servidor web local para rodar o frontend (ex: extensão **Live Server** do VS Code ou comando Python/Node).
2. Um backend ativo para servir as imagens das figurinhas.

### Passo a Passo

1. **Iniciar o Backend (Opcional - necessário para carregar as imagens das figurinhas):**
   * Se você tiver a pasta do backend configurada, execute:
     ```bash
     cd backend/dia-3
     uvicorn main:app --reload
     ```
   * O backend rodará por padrão em `http://localhost:8000`.

2. **Rodar o Frontend:**
   * Abra o arquivo [index.html](file:///c:/Users/gil_c/OneDrive/Documentos/Projetos%20TI/i-arq-ia-alura-album-main/index.html) e inicie a extensão **Live Server** do VS Code.
   * Alternativamente, você pode usar um servidor simples via CLI:
     ```bash
     python -m http.server 3000
     ```
     E abrir `http://localhost:3000` no seu navegador.
