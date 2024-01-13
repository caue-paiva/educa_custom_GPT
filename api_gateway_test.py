import requests


def make_api_gateway_request()->dict:
    json = {
        "queryStringParameters":{
        "questao": "geografia fisica",
       "numero_questoes": 1
        }
    }

    lambda_api_url: str = "url da API"
    answer = requests.get(lambda_api_url, json=json)

    if answer.status_code == 200:
        return answer.json()
    else:
        raise Exception(f"Failed to fetch embeddings. Status code: {answer.status_code}, Response: {answer.text}")


def privacy_api_request()->None:
    answer = requests.get("url da API")
    print(answer)
    if answer.status_code == 200:
        return answer.json()
    else:
        raise Exception(f"Failed to fetch embeddings. Status code: {answer.status_code}, Response: {answer.text}")

print(privacy_api_request())