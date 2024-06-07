from langchain_openai import ChatOpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
import pandas as pd

def query_agent(data, query):
    # Parse the CSV file and create a DataFrame from its contents
    df = pd.read_csv(data)
    
    llm = ChatOpenAI()  # Corrected to use ChatOpenAI
    
    # Create a Pandas DataFrame agent with verbosity set to False to suppress intermediate outputs
    agent = create_pandas_dataframe_agent(llm, df, verbose=False)
    
    # Execute the query and get the result
    result = agent.invoke(query)
    
    # Extract only the final answer from the result
    final_answer = result['output'] if 'output' in result else result

    return final_answer