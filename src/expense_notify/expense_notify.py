import os
from dotenv import load_dotenv
from expense_notify.data_loader.notiondb_loader import NotionDataLoader
from expense_notify.agent.pandas_agent import DataFrameAnalyzer
from expense_notify.notification.telegram_bot_service import send_telegram_message

# from expense_notify.notification.gmail_service import GmailService

load_dotenv()


def run_expense_notify():
    integration_token = os.getenv("NOTION_API_KEY")
    database_id = os.getenv("NOTION_DB_ID")
    df = NotionDataLoader(
        integration_token=integration_token,
        database_id=database_id,
    ).load_and_process_metadata()

    analyzer = DataFrameAnalyzer(df)

    expense_content = analyzer.analyze()
    send_telegram_message(
        os.getenv("TELEGRAM_TOKEN"), os.getenv("TELEGRAM_CHAT_ID"), expense_content
    )

    # gmail_service = GmailService()
    # gmail_service.send_email("xielusi13@gmail.com", "expenses", expense_content)


# if __name__ == "__main__":
#     main()
