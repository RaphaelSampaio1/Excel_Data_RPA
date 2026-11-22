from src.google_forms import GoogleForms
from loguru import logger
import pandas as pd


if __name__ == "__main__":
    bot = GoogleForms()
    n_registered = 1
    
    try:
        logger.success("Bot started!")
        #bot.fill_form(coin = "Euro", price ="1000", country="brasil")

        df = pd.read_csv("dados.csv")
        logger.success(f"Dataframe Readed")

        for i, row in df.iterrows():
            nome = row["Nome"]
            email = row["Email"]
            nacionalidade = row['Nacionalidade']

            bot.fill_form(coin = nome,
                            price = email,
                            country= nacionalidade)
            
            bot.submit_form()
            logger.success(f"{nome} - Records filled: {n_registered}")
            n_registered += 1
            
            



        input("=================================")
    except Exception as e:
        logger.error(f"Error: {e}\n")