# CuidaPet

O crescimento significativo do número de maus tratos à animais em nosso país é uma problemática preocupante nos últimos anos. Junto à falta de canais acessíveis para denúncias, tais barreiras representam um entrave à proteção efetiva da fauna brasileira. O projeto CuidaPet surge como resposta a essa demanda, oferecendo um aplicativo gratuito que facilita um canal efetivo de denúncias e encaminhamento desses animais a órgãos de tratamento. Desenvolvido com foco em simplicidade e acessibilidade, o nosso sistema permite que qualquer pessoa realize denúncias de forma rápida e prática.

## 🧑‍💻 Fluxograma do Projeto
Disponíveis no seguinte link do Google Drive:
        https://drive.google.com/drive/folders/1iSLQePa_2zy8PUJ-Ys6y1j3dXj4Qr47d
        
## 🚀 Tecnologia Utilizada
- Python 3.12.4

 ## 📚 Bibliotecas:

  ***JSON*** (Uso de listas e dicionários, salvar e carregar os dados em .json)
  
  ***Pillow*** (manipulação de imagens)

  ***TKInter*** (Interface Gráfica)

  ### ⚙️ Módulos e para que servem

| Módulo         | Função no Projeto                                                                 |
|----------------|------------------------------------------------------------------------------------|
| `os`           | Limpa o terminal com `os.system('cls' ou 'clear')` para manter o visual limpo     |
  
### 💻 Estruturas utilizadas:

 ***if*** = executa um bloco se uma condição for verdadeira
  
 ***elif*** = executa outra condição se a anterior for falsa
 
 ***else*** = executa caso todas as condições anteriores sejam falsas
 
 ***while*** = repete um bloco enquanto a condição for verdadeira
 
 ***for*** = percorre itens de uma sequência (lista, string, etc)
 
 ***try*** = tenta executar um bloco e trata erros com except se algo falhar

## 🔧 Instalação e Execução

1. Clone o repositório:
```bash
git clone https://github.com/ViniMiranda06/CuidaPet-App.git
cd CuidaPet-App
```

2. Execute o programa:
```bash
main.py
```

## 👤 Funcionalidades para Usuários Comuns

### Visualização 
- Fazer um pedido de adoção:
    Permite que o usuário faça uma solitação de adoção de um pet, o pedido será enviado a equipe administrativa, que entrará em contato com quem fez o pedido

- Visualização de animais em tratamento
    Permite que o funcionário visualise os animais em tratamento, posteriormente haverá um patreon para os animais onde o usuário será redirecionado para o patreon

- Detalhes completos de cada animal

### Gerenciamento de Conta
- Edição de informações pessoais
- Alteração de senha
- Logout

👑 Funcionalidades para Administradores

⚠️ Atenção: O acesso às funcionalidades administrativas é restrito e só pode ser feito por meio de uma 'etiqueta' atribuida ao usuário.

## 🔐 Como acessar o menu administrativo:
Será necessário ter a categoria "Administrador" atrelada ao seu usuário cadastrado. assim, ao abrir a aplicação abrirá diretamente no menu administrativo
Para atribuir essa categória ao usuário você deve:
1.localizar o usuário cadastrado no json correspondente ao armazenamento de cadastros
2.verificar a situação do usuário (Deve estar descrito como 'usuário')
3.Mudar para Administrador
4.Salve e tente entrar novamente na aplicação!

## 🐾 Gestão de Animais
-Cadastro de novos animais
-Edição de informações detalhadas dos pets
-Registro de tratamentos e procedimentos realizados

📄 Gestão de Adoções
-Visualização de todos os pedidos de adoção realizados
    Após os pedidos serem enviados pelos usuários, o administrador poderá visualizá-los.

-Aprovação ou rejeição das solicitações enviadas por usuários

📄 Gerenciamento de Denúncias.
-Recebe Denúncias relacionadas a maus tratos de animais, que serão posteriormente movidos para tratamento e adoção. fomentando o Resgate desses seres.

## 👨‍💻 Desenvolvedores
- Vinícius De Oliveira
(https://github.com/ViniMiranda06)
- Igor
(https://github.com/IgordevBR)


## 📦 Release 3.0 — Melhorias e funcionalidades ##

A terceira entrega do CuidaPet tem como foco o refinamento técnico, com foco em robustez nos cadastros, usabilidade nas denúncias e valorização da experiência do usuário. A Release 3.0 foi construída com base em conceitos sólidos vistos ao longo da disciplina, como:

- **Tratamento de strings e dados de entrada**
- **Uso de estruturas condicionais e repetição**
- **Criação de funções reutilizáveis e especializadas**
- **Manipulação de listas e dicionários para armazenamento**
- **Organização modular com Programação Orientada a Objetos (POO)**

### ✅ Melhorias implementadas

1. **Validação de nome no cadastro de usuários**  
   O sistema agora impede o cadastro caso o campo de nome esteja vazio. Isso foi possível por meio de funções específicas de validação de strings, garantindo integridade nos dados desde o primeiro uso.

2. **Validação de e-mail com formato obrigatório (@ e .)**  
   O campo de e-mail passou a ser verificado com base em padrões mínimos de formatação. O código utiliza funções de verificação com operadores de presença (`in`) e estrutura condicional para garantir que o e-mail seja aceito apenas se tiver os elementos básicos de um endereço válido.

3. **Validação de senha com mínimo de 6 caracteres**  
   A segurança do sistema foi aprimorada com a exigência de senhas mais fortes. A verificação é feita através de uma função de análise de comprimento de strings, impedindo que o cadastro avance com senhas frágeis.

4. **Validação de telefone com 11 dígitos (padrão nacional)**  
   Por meio da conversão e validação de caracteres numéricos com `.isdigit()` e `len()`, o sistema assegura que apenas números no padrão brasileiro (com DDD) sejam aceitos. Isso evita cadastros inconsistentes e falhas em comunicações futuras.

5. **Interrupção completa do cadastro em caso de erro**  
   Todas as validações são agora interligadas: se qualquer campo estiver inválido, o sistema exibe uma mensagem clara e impede o salvamento do usuário. Isso foi feito por meio de funções especializadas e estruturas de decisão aninhadas.

6. **Melhorias visuais e refinamento da identidade do sistema**  
   A interface gráfica passou por melhorias importantes, incluindo:
   - **Adição da logo** da plataforma no menu principal do usuário;
   - **Ajustes de proporção e clareza em fontes e tamanhos de texto**, para facilitar a leitura;
   - Alterações visuais que reforçam a **identidade do projeto**.

### ✨ Funcionalidades adicionadas

1. **📨 Sistema de denúncias com confirmação, registro e status**  
   Os usuários agora podem registrar denúncias de maus-tratos de forma mais completa. O sistema:
   - Solicita **confirmação antes do envio**;
   - **Registra a data e o horário exatos** com a biblioteca `datetime`;
   - Salva a denúncia em um arquivo `.json`, **mantendo um histórico completo**;
   - Exibe o **status atual** da denúncia, facilitando a comunicação entre o administrador e o denunciante.

   Essa funcionalidade foi pensada para garantir **transparência e rastreabilidade**, utilizando dicionários para armazenar os dados e listas para organizá-los em arquivos persistentes. Além disso, o uso de estruturas de repetição permite exibir o histórico sempre que necessário.

2. **🚨 Tela dedicada para contato com autoridades legais**  
   Agora, ao fazer uma denúncia, o usuário tem acesso a uma aba com três opções principais de contato:
   - Polícia Militar (casos emergenciais),
   - Disque denúncia para denúncias ambientais anônimas,
   - **IBAMA**, para denúncias relacionadas a **animais silvestres**.

   A interface foi desenvolvida para oferecer **praticidade máxima**: o usuário pode simplesmente **copiar e colar os dados** de contato conforme o caso. A separação em três categorias claras torna a tomada de decisão mais simples e eficaz.  
   Internamente, essa funcionalidade é implementada com separação de classes (POO), uso de `LabelFrame` no Tkinter e estrutura modular para facilitar manutenção futura.

3. **❗ Confirmação de saída em todos os menus principais**  
   Implementamos caixas de diálogo de confirmação em todos os pontos sensíveis, como menus do usuário e administrador. Essa funcionalidade evita saídas acidentais, reforçando a navegabilidade do app.  
   O comportamento foi implementado com `messagebox.askyesno()` e **laços de repetição** que aguardam a resposta do usuário.

4. **🧠 Modularização das validações em funções reutilizáveis**  
   As validações dos campos (nome, e-mail, senha e telefone) foram extraídas em funções específicas que podem ser reutilizadas em diferentes partes do sistema.  
   Esse refatoramento melhora a legibilidade do código, evita redundância e aplica diretamente o conceito de **abstração e encapsulamento** da Programação Orientada a Objetos.
