:us:

## CustomGPTs with AWS lambda APIs

# About the project

This project is for the API implementation of the tools for a **customGPT focused on helping brazilian students to prepare for university admittance standardized tests(ENEM)** trough active study and question answering

The **chatbot is available for openAI premium users** [here](https://chat.openai.com/g/g-lTKGDJhnR-professor-particular-para-o-enem)

Around the last quarter of 2023, **OpenAI enabled premium users to create their own custom GPTs**, with custom prompts, dataset and actions (tools or API calls). This went well with my other [project](https://github.com/caue-paiva/educa_gpt_publico) for building an educational chatbot and i wanted to try this new feature and how it could help my project.

However through experimentation i found that uploading files to your custom GPT becomes unfeasible when the data is too large, as it tends to become too slow and innacurate to retrieve such info and this was very bad for my use case, where i needed to do retrieval over hundreds of test questions and over 10k lines of text.

Thats when i decided to create an **action/tool for my custom GPT** that enabled it to do **semantic query on a vectorDB (Qdrant)**, with hundreds of questions and get as many questions as the input required. For that i needed an API, so i decided to use **AWS lambda for the code logic** of chaining API calls (first to openAI for embeddings and then to qdrant for the semantic search) and **AWS APIgateway for managing the APIs** and their resources/paths

customGPT actions also requires openAPI specifications to operate , thankfully **AWS APIgateway allows you to build an API by uploading an openAPI specs file** (open_api_json_schema.json) so i did just that

<br>
<br>
<br>

:brazil:

Este projeto é para a implementação da API das ferramentas para um **customGPT focado em ajudar estudantes brasileiros a se prepararem para o exame nacional do ensino médio (ENEM)** através de estudo ativo e resolução de questões.

O **chatbot está disponível para usuários premium da OpenAI** [aqui](https://chat.openai.com/g/g-lTKGDJhnR-professor-particular-para-o-enem).

Por volta do último trimestre de 2023, a **OpenAI permitiu que usuários premium criassem seus próprios GPTs personalizados**, com prompts, conjunto de dados e ações personalizadas (ferramentas ou chamadas de API). Isso se alinhou bem com meu [outro projeto](https://github.com/caue-paiva/educa_gpt_publico) para **construir um chatbot educacional** e eu queria experimentar essa nova funcionalidade e como ela poderia ajudar meu projeto.

No entanto, através de experimentação, **descobri que fazer upload de arquivos para o seu GPT personalizado fica inviável quando os dados são muito grandes**, pois ele tende a se tornar **muito lento e impreciso para recuperar tais informações** e isso foi muito ruim para o meu caso de uso, onde eu precisava fazer recuperação de centenas de questões de teste e mais de 10 mil linhas de texto.

Foi então que decidi **criar uma ação/ferramenta para o meu GPT personalizado** que o permitisse a fazer **consulta semântica em um vectorDB (Qdrant)**, com centenas de questões e obter tantas perguntas quanto a entrada requeria. Para isso, eu precisava de uma API, então decidi usar **AWS Lambda para a lógica do código** de encadear chamadas de API (primeiro para a OpenAI para os embeddings e depois para o Qdrant para a pesquisa semântica) e **AWS API Gateway para gerenciar as APIs** e seus recursos/caminhos.

Ações do customGPT também requerem especificações da OpenAPI para operar, felizmente **AWS API Gateway permite que você construa uma API fazendo upload de um arquivo de especificações da OpenAPI** (open_api_json_schema.json), então foi exatamente isso que fiz."