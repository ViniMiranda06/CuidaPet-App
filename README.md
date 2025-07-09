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
| `random`       | Gera códigos aleatórios de verificação de 6 dígitos para autenticação              |
| `smtplib`      | Conecta ao servidor SMTP do Gmail para envio de emails                            |
| `email.message.EmailMessage` | Cria e formata a mensagem de email enviada ao usuário               |
  
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
git clone https://github.com/ViniMiranda06/CuidaPet.git
cd CuidaPet
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

⚠️ Atenção: O acesso às funcionalidades administrativas é restrito e só pode ser feito por meio de um recurso secreto acessado após o login.

## 🔐 Como acessar o menu administrativo:
1. Faça login normalmente como qualquer usuário.

2. No Menu Principal, digite 1703 como opção.

3. Isso abrirá o Menu Administrativo, exclusivo para a equipe responsável.

## 🐾 Gestão de Animais
-Cadastro de novos animais
-Edição de informações detalhadas dos pets
-Registro de tratamentos e procedimentos realizados

📄 Gestão de Adoções
-Visualização de todos os pedidos de adoção realizados
    Após os pedidos serem enviados pelos usuários, o administrador poderá visualizá-los.

-Aprovação ou rejeição das solicitações enviadas por usuários

## 👨‍💻 Desenvolvedores
- Vinícius De Oliveira
(https://github.com/ViniMiranda06)
- Igor
(https://github.com/IgordevBR)

## ⚠️ Estado do projeto
O projeto se encontra em estágio de desenvolvimento.

## 📝 Licença
Este é um projeto acadêmico desenvolvido para fins educacionais.
