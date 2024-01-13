import json , requests , os
from dotenv import load_dotenv

load_dotenv(os.path.join("keys.env"))

OPEN_AI_API_KEY = os.getenv("OPENAI_API_KEY")
QDRANT_URL =  os.getenv("QDRANT_HOST")
COLLECTION_NAME = os.getenv("QD_COLLECTION_NAME")
QDRANT_API_KEY = os.getenv("QDRANT_API")
OPEN_AI_EMBEDDINGS_URL ="https://api.openai.com/v1/embeddings"
#URLs e keys de APIs necessárias


def lambda_handler(event, context)->dict:

    request_parameters:dict = event.get('queryStringParameters', {})
    user_question: str = request_parameters.get("questao", "")   
    num_questions: int = int(request_parameters.get("numero_questoes", -1)) 

    if not user_question:
        raise Exception("Questao solicitada pelo usuário esta vazia")
    
    if num_questions == -1:
        raise Exception("num de questoes solicitada pelo usuário esta vazia")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPEN_AI_API_KEY}"
    }

    data = {
        "input": user_question,
        "model": "text-embedding-ada-002"
    }
    #headers e dados da request para a openAI
    embeddings_response = requests.post(OPEN_AI_EMBEDDINGS_URL, headers=headers, json=data)
    #faz a request com o texto r recebe os embeddings do texto da openAI
    embed_json_result: dict = {}
    if embeddings_response.status_code == 200:
        embed_json_result = embeddings_response.json()
    else:
        raise Exception(f"falha em pegar os embeddings. codigo de status: {embeddings_response.status_code}, resposta: {embeddings_response.text}")

    embeddings : list[float] = embed_json_result.get("data", [])[0].get("embedding", [])
    #pega os embeddings
    
    headers = {
        "Content-Type": "application/json",
        "api-key" : QDRANT_API_KEY
    }

    data = {
        "vector": embeddings,
        "with_payload" : True,
        "limit": num_questions
    }
    #headers e dados para a request pro Qdrant
    qd_url :str= f'{QDRANT_URL}/collections/{COLLECTION_NAME}/points/search'
    qdrant_response = requests.post(qd_url, headers=headers, json=data)
    #faz a request pro qdrant vectorDB e recebe x questões mais similares ao input

    qd_json_result: dict = {}
    if qdrant_response.status_code == 200:
        qd_json_result = qdrant_response.json()
    else:
        raise Exception(f"falhou em pegar respostas do Qdrant. código de status: {qdrant_response.status_code}, resposta: {qdrant_response.text}")
    
    qd_query_result: list[dict] = qd_json_result.get("result", [])
  
    return_list: list[dict] = []

    for question in qd_query_result:
        payload: dict = question.get("payload", {})
        metadata: dict = payload.get("metadata", {})

        question_year: int = metadata.get("ano", 0)
        question_subject: str = metadata.get("materia", "")
        question_text: str = payload.get("page_content", "")

        return_list.append(
            {
             "ano" : question_year,
             "materia": question_subject,
             "questao": question_text
            }  
        )
    #cria uma lista de questões, cada uma um dict, com o texto dela e seus metadados (ano, matéria)
    if not return_list:
        raise Exception("nao foi possivel recuperar a lista de questões")
    
    return {
        'statusCode': 200,
        'body': json.dumps(return_list) #retornar uma lista como JSON
    }

