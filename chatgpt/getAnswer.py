from config import API_KEY
import pandas
import openai

def GetAnswer(question: str):

    df = pandas.read_csv('data/sample.csv')
    data_top = df.head() 
    data_table_name = "employee_score"
    
    openai.api_key = API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a Data Scientist"},
                {"role": "system", "content": f"data frame {data_top}, table name {data_table_name}"},
                {"role": "user", "content": f"{question}"},
            ]
    )

    result = ''
    for choice in response.choices:
        result += choice.message.content

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a Data Scientist"},
                {"role": "system", "content": f"data frame {data_top}, table name {data_table_name}"},
                {"role": "user", "content": f"run this query {result} in the dataset above, bring me the results"},
            ]
    )

    result_2 = ''
    for choice in response.choices:
        result_2 += choice.message.content

    return result_2