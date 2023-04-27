import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_title,
    search_by_date,
)
from tech_news.analyzer.ratings import top_5_categories


def analyzer_menu():
    try:
        menu = input(
            "Selecione uma das opções a seguir:\n"
            " 0 - Popular o banco com notícias;\n"
            " 1 - Buscar notícias por título;\n"
            " 2 - Buscar notícias por data;\n"
            " 3 - Buscar notícias por categoria;\n"
            " 4 - Listar top 5 categorias;\n"
            " 5 - Sair."
        )

        messages = [
            "Digite quantas notícias serão buscadas: ",
            "Digite o título: ",
            "Digite a data no formato aaaa-mm-dd: ",
            "Digite a categoria: ",
        ]

        result = {
            "0": lambda: get_tech_news(int(input(messages[0]))),
            "1": lambda: search_by_title(input(messages[1])),
            "2": lambda: search_by_date(input(messages[2])),
            "3": lambda: search_by_category(input(messages[3])),
            "4": lambda: top_5_categories(),
            "5": lambda: print("Encerrando script"),
        }

        return result[menu]()
    except KeyError:
        return sys.stderr.write("Opção inválida\n")
