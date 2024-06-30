import pandas as pd
from typing import List, Dict, Any
from langchain_community.document_loaders import NotionDBLoader


class NotionDataLoader:
    def __init__(
        self, integration_token: str, database_id: str, request_timeout_sec: int = 30
    ):
        self.integration_token = integration_token
        self.database_id = database_id
        self.request_timeout_sec = request_timeout_sec
        self.docs = []

    def load_metadata(self) -> List[Dict[str, Any]]:
        """Call NotionDBLoader to load metadata
        from Notion database

        Returns:
            List[Dict[str, Any]]: A list of dictionaries
        """
        loader = NotionDBLoader(
            integration_token=self.integration_token,
            database_id=self.database_id,
            request_timeout_sec=self.request_timeout_sec,
        )
        return loader.load()

    def process_metadata(self, docs: List[Dict[str, Any]]) -> pd.DataFrame:
        """Process the metadata for each row and return
        a Pandas DataFrame

        Args:
            docs (List[Dict[str, Any]]): A list of dictionaries

        Returns:
            pd.DataFrame: A cleaned DataFrame
        """
        lst = []
        for doc in docs:
            metadata = doc.metadata
            metadata.update(metadata.pop("date"))
            metadata["category"] = ", ".join(metadata["category"])
            for key in ["id", "end", "time_zone"]:
                metadata.pop(key, None)
            lst.append(metadata)

        return pd.DataFrame(lst)

    def load_and_process_metadata(self):
        docs = self.load_metadata()
        return self.process_metadata(docs)


# sample usage

if __name__ == "__main__":
    notiondbloader = NotionDataLoader(
        integration_token="xxx",
        database_id="xxx",
        request_timeout_sec=30,
    )

    df = notiondbloader.load_and_process_metadata()

    print(df.head())

    df.to_csv("./data/sample_data.csv", index=False)
