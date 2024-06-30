import pandas as pd
from dotenv import load_dotenv
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI

load_dotenv()


class DataFrameAnalyzer:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def initialize_agent(self):
        agent = create_pandas_dataframe_agent(
            ChatOpenAI(temperature=0, model="gpt-3.5-turbo"),
            self.df,
            verbose=True,
            agent_type=AgentType.OPENAI_FUNCTIONS,
            allow_dangerous_code=True,
        )
        return agent

    def analyze(self):
        agent = self.initialize_agent()
        result = agent.invoke(
            """Analyze the expenses for the past 7 days. Provide the total expenses and expenses by category
            and what are the big ticket items relative to the total expenses."""
        )
        return result["output"]


# sample usage

# if __name__ == "__main__":
#     df = pd.read_csv("./data/sample_data.csv")
#     analyzer = DataFrameAnalyzer(df)
#     analyzer.analyze()
