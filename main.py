from api import fetch_users
from api import fetch_posts
from processor import group_posts_by_user
from processor import calculate_average_characters
from report import save_excel
from send_email.send_email import sending_email
from report import fetch_name_archive
from report import remove_archive
from send_email.send_email import name_folder


def start():
    users = fetch_users()
    posts = fetch_posts()
    if (users == [] or posts == []):
        print("Error, list empty")
        return

    grouped_posts = group_posts_by_user(posts)

    report_xlsx = calculate_average_characters(users, grouped_posts)

    name_arquive = fetch_name_archive()
    save_excel(report_xlsx, name_arquive)

    if (save_excel is None):
        print("Erro ao salvar o relatório.")
        return

    send_email_confirm = input(
        "Gostaria de enviar o relatório via e-mail? [ Y/N ] ")
    if send_email_confirm in ['Y', 'y']:
        confirmation_send_email = sending_email(name_arquive)

        if (confirmation_send_email):
            print("E-mail enviado com sucesso! ")
        else:
            print("Houve um erro, e-mail não foi enviado")

    elif send_email_confirm in ['N', 'n']:
        print("Relatório gerado! E-mail não enviado! ")

    remove_archive_in_folder = input(
        "Gostaria de apagar o arquivo? [ Y/N ] ")

    if remove_archive_in_folder in ['Y', 'y']:
        remove_archive(f"{name_folder}/{name_arquive}")
        return
    else:
        return


if __name__ == "__main__":
    start()
