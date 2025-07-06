import datetime
import pandas as pd
from pathlib import Path
from send_email.variables_necessary import name_folder


def fetch_name_archive():
    date_hour_now = datetime.datetime.now()
    date_format = date_hour_now.strftime("%d%m%Y_%H%M%S")

    name_archive = f"report_{date_format}.xlsx"
    return name_archive


def save_excel(report, name_archive):

    try:
        folder = Path(name_folder)
        folder.mkdir(exist_ok=True)

        folder_archive = folder / name_archive

        report_pd = pd.DataFrame(report)
        report_pd.to_excel(folder_archive, index=False)
        print(f"Relatório salvo como: {folder_archive}")
    except Exception as e:
        print(f"Erro ao gerar o  arquivo: {e}")


def remove_archive(name_archive):
    caminho_arquivo = Path(name_archive)
    if (caminho_arquivo.exists()):
        caminho_arquivo.unlink()
        print(f"Arquivo: {name_archive} foi removido com sucesso!")
