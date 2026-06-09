---
name: Recicle-Já Design System
colors:
  surface: '#f8f9fa'
  surface-dim: '#d9dadb'
  surface-bright: '#f8f9fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f5'
  surface-container: '#edeeef'
  surface-container-high: '#e7e8e9'
  surface-container-highest: '#e1e3e4'
  on-surface: '#191c1d'
  on-surface-variant: '#3e4a3d'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#6e7b6c'
  outline-variant: '#bdcaba'
  surface-tint: '#006e2d'
  primary: '#006b2c'
  on-primary: '#ffffff'
  primary-container: '#00873a'
  on-primary-container: '#f7fff2'
  inverse-primary: '#62df7d'
  secondary: '#5d5f5f'
  on-secondary: '#ffffff'
  secondary-container: '#dfe0e0'
  on-secondary-container: '#616363'
  tertiary: '#525d6c'
  on-tertiary: '#ffffff'
  tertiary-container: '#6b7586'
  on-tertiary-container: '#fdfcff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#7ffc97'
  primary-fixed-dim: '#62df7d'
  on-primary-fixed: '#002109'
  on-primary-fixed-variant: '#005320'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#d9e3f6'
  tertiary-fixed-dim: '#bdc7d9'
  on-tertiary-fixed: '#121c2a'
  on-tertiary-fixed-variant: '#3d4756'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-max: 1200px
  gutter: 24px
---

## Brand & Style

O objetivo deste sistema de design é inspirar ação sustentável através de uma interface clara, otimista e extremamente organizada. A personalidade da marca é **ecológica, eficiente e transparente**. 

A estética adotada é o **Minimalismo Moderno**, priorizando o respiro visual (whitespace) para reduzir a carga cognitiva do usuário. O design evita ornamentos desnecessários, focando em uma hierarquia de informações impecável que reflete a clareza e o propósito de um futuro mais limpo. O foco está na funcionalidade direta, transmitindo confiança e facilidade no processo de reciclagem.

## Colors

A paleta de cores é inspirada na vitalidade da natureza e na limpeza urbana.

*   **Primária (Vibrant Green):** O verde vibrante (#16A34A) é o motor da interface, utilizado para chamadas de ação (CTAs), ícones de sucesso e elementos que indicam progresso ecológico.
*   **Secundária (White):** O branco puro (#FFFFFF) domina as superfícies de fundo, garantindo a estética "clutter-free" e alto contraste.
*   **Terciária (Dark Grey):** O cinza escuro (#1F2937) é reservado para o rodapé e textos de alta hierarquia, ancorando a interface com uma base sólida e profissional.
*   **Neutros:** Tons de cinza ultra-claro (#F9FAFB) são usados para distinguir seções sem comprometer a leveza visual.

## Typography

A tipografia utiliza a família **Plus Jakarta Sans**, escolhida por sua natureza moderna, geométrica e amigável.

1.  **Hierarquia:** Títulos utilizam pesos `700` (Bold) com leve ajuste de espaçamento negativo para um visual editorial.
2.  **Leiturabilidade:** O corpo de texto mantém um `line-height` generoso de 1.6 para garantir conforto visual em descrições de processos de reciclagem.
3.  **Labels:** Rótulos e pequenos textos informativos utilizam peso `600` (Semi-bold) para garantir legibilidade mesmo em tamanhos reduzidos.

## Layout & Spacing

Este sistema utiliza um modelo de **Grid Fixo** centralizado para desktops e um modelo fluido para dispositivos móveis.

*   **Grid:** 12 colunas em desktop com margens laterais seguras de 24px.
*   **Ritmo Vertical:** Baseado em múltiplos de 8px. O espaçamento entre blocos de conteúdo deve ser generoso (48px ou 80px) para manter a sensação de organização.
*   **Mobile:** Breakpoint principal em 768px, onde o grid transiciona para 4 colunas e os espaçamentos `lg` e `xl` são reduzidos em 50%.

## Elevation & Depth

Para manter a interface limpa e "clutter-free", a profundidade é comunicada através de **Camadas Tonais** e sombras ambientais mínimas.

1.  **Superfícies:** Elementos principais (Cards) usam um fundo branco puro contra um fundo de aplicação cinza ultra-claro.
2.  **Sombras:** Evite sombras pesadas. Utilize apenas um "Soft Glow" (difusão de 15px, 4% de opacidade preta) para destacar elementos interativos como cards de feedback ou dropdowns abertos.
3.  **Bordas:** O uso de bordas finas (1px) em cinza muito claro substitui sombras para definir limites de componentes de input de forma discreta.

## Shapes

A linguagem de formas é **amigável e orgânica**, utilizando cantos arredondados para suavizar a interface.

*   **Botões e Inputs:** Utilizam o padrão `rounded-md` (0.5rem) para um toque moderno.
*   **Cards e Blocos de Feedback:** Utilizam `rounded-lg` (1rem) para criar uma diferenciação visual clara entre seções.
*   **Elementos Decorativos:** Pequenos ícones ou avatares podem utilizar formas circulares completas.

## Components

### Botões
*   **Primário:** Fundo verde vibrante (#16A34A), texto em branco bold. Padding horizontal generoso.
*   **Hover:** Escurecimento leve do verde (10%) com transição suave de 200ms.

### Blocos de Feedback
*   **Estilo:** Fundo verde vibrante com texto totalmente branco.
*   **Uso:** Para mensagens de sucesso, confirmação de coleta ou impacto ambiental positivo. Deve usar o arredondamento de 1rem.

### Dropdowns
*   **Design:** Campo de seleção com borda fina cinza, ícone de seta minimalista à direita.
*   **Menu Aberto:** Fundo branco, cantos arredondados (0.5rem), com sombra suave para flutuação. O item selecionado recebe um background verde muito claro (5% de opacidade).

### Cards de Conteúdo
*   Fundo branco puro, borda de 1px cinza claro, padding interno de 24px. Devem ser usados para organizar informações sobre tipos de resíduos.

### Footer (Rodapé)
*   Fundo cinza escuro (#1F2937), texto e links em branco ou cinza médio. Layout simplificado com links de navegação e redes sociais.