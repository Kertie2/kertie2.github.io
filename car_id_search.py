import requests
import signal
import sys
import datetime
import json
import os
import html

print("\033[91m💻 Bienvenue sur le script de recherche de Numéro d’identification du véhicule, De la Marque, Du modèle, de la Carrosserie, Et du nombre de portes. 💻\033[0m")
print("\033[91m💻 Ce script a été fait par Kertie2_ et Le script utilise l'api de Carglass France via l'url : apigateway.carglass.fr. 💻\033[0m")


def search_car():
    def signal_handler(signal, frame):
        print("\n\n\033[91m🔴 Fermeture du programme. 🔴\033[0m")
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    running = True

    while running:
        try:
            plaque = input("🚗 Veuillez entrer la plaque d'immatriculation de la voiture. ( Ou appuyez sur CTRL + C pour fermer le programme ) ( Tapez clean pour supprimer les logs. ) : 🚗  ")

            if plaque.lower() == "clean":
                os.system("python clean_all.py")
                continue

            if "-" in plaque:
                plaque_convertie = plaque.upper().strip()  # Convertir en majuscules
            else:
                plaque_formattee = plaque.upper().strip()
                plaque_convertie = "-".join([plaque_formattee[:2], plaque_formattee[2:5], plaque_formattee[5:]])

            url = f"https://apigateway.carglass.fr/rest/v1/olb-diagnostics/vehicle/{plaque_convertie}?jobType=02&alreadyBooked=true&remainingDays=10"

            headers = {
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
                "Content-Type": "application/json",
                "Cookie": "didomi_token=eyJ1c2VyX2lkIjoiMTg4ZDUxMzYtY2E2MC02NzZkLWE3MGQtM2ZiYjE2MjNiZmM4IiwiY3JlYXRlZCI6IjIwMjMtMDYtMTlUMTk6MTM6MjEuNDM0WiIsInVwZGF0ZWQiOiIyMDIzLTA2LTE5VDE5OjEzOjIxLjQzNFoiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsiYzplenB1Ymxpc2gtSmZyR2JNR2MiLCJjOmNvbnRlbnRzcS1xdzIyNmJhRCIsImM6Y2FyZ2xhc3MtZFczTmM3blUiLCJjOnR2dHktRXBZYk5YVjgiLCJjOm9wdGltaXplbHktQnBSQjM3SkQiLCJjOmRvdWJsZWNsaS05dENWUFZSaiIsImM6Z29vZ2xlYWRzLTdqTGtoSlFSIiwiYzpxdWFsYXJvby04bWpLQWEyTiIsImM6ZmFjZWJvb2stZDJieGdVREciLCJjOmdvb2dsZWFuYS1MZ3FRRXBhZiIsImM6bWF1dGljLWhrTGk4N2U5IiwiYzpnb29nbGVhbmEtOHh0M0ZpTm4iLCJjOmJpbmctY1VGQzJQdFAiLCJjOnNuYXBjaGF0LUNnSmYySzNtIiwiYzpxd2FtcGxpZnktTFhGVnFkZEgiXX0sInB1cnBvc2VzIjp7ImVuYWJsZWQiOlsiInB1YmxpY2l0ZS1oOGJiYkh5NCIsInB1YmxpY2l0ZS1oYzR2bHJWViIsInJlc2VhdXhzby1YM2hEbk5yUiJdfSwidmVyc2lvbiI6Mn0=",
                "Origin": "https://www.carglass.fr",
                "Referer": "https://www.carglass.fr/",
                "Sec-Ch-Ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": '"Windows"',
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
                "X-Journey-Id": "519f4af2-302c-5a75-8671-82360852212c",
                "X-Origin": "connect",
                "X-Record-Id": "0149e7ea-bdd5-559d-9885-3fcb8257762c"
            }

            response = requests.get(url, headers=headers)

            if response.status_code == 404 or response.status_code == 403:
                print("\033[91m❗ L'adresse de l'API n'est plus utilisable ! ❗\033[0m")
                log_message = f"[{datetime.datetime.now()}] 🚗 Requête pour la plaque : {plaque_convertie} 🚗\n"
                log_message += f"🔗 URL : {url} 🔗²\n"
                log_message += f"\033[91m🔴 Status : ERROR 🔴</span>\n"
                log_message += f"\033[91m❗ ERROR : Error 404 : The requested URL was not found on this server. or Error 403 : We are sorry, but you do not have access to this page or ressource. ❗\033[0m\n\n"
                running = False

            elif response.status_code == 200:
                data = response.json()
                vehicle_info = data.get("response", {}).get("vehicle", {})
                status_request = data.get("status")
                vin = vehicle_info.get("vin")
                make = vehicle_info.get("make")
                model = vehicle_info.get("model")
                body = vehicle_info.get("body")
                doors_count = vehicle_info.get("doorsCount")
                color = vehicle_info.get("color")

                log_message = f"[{datetime.datetime.now()}] 🚗 Requête pour la plaque : {plaque_convertie} 🚗\n"
                log_message += f"🔗 URL : {url} 🔗\n"
                log_message += f'<span style="color: green">🟢 Status : {status_request} 🟢</span>\n'
                log_message += f"🚗 Numéro d’identification du véhicule : {vin} 🚗\n"
                log_message += f"🚗 Marque : {make} 🚗\n"
                log_message += f"🚗 Modèle : {model} 🚗\n"
                log_message += f"🚗 Carrosserie : {body} 🚗\n"
                log_message += f"🚗 Nombre de portes : {doors_count} 🚗\n"
                log_message += f"🚗 Couleur D'Usine De Véhicules : {color} 🚗\n"
                log_message += f'<span style="color: green">✅ Code Réponse : {response} ✅</span>\n\n'

                with open("log.txt", "a", encoding='utf-8') as file:
                    file.write(html.escape(log_message))

                json_response = f"[{datetime.datetime.now()}] 🚗 Requête pour la plaque : {plaque_convertie} 🚗\n"
                json_response += f"🔗 URL : {url} 🔗\n"
                json_response += f"💻 Réponse JSON : {json.dumps(data, indent=4)} 💻\n\n"

                with open("json_request.txt", "a", encoding='utf-8') as file:
                    file.write(json_response)

                print("\n\n🚗 Résultat via l'api : apigateway.carglass.fr : 🚗")
                print("🔗 URL : ", url, " 🔗")
                print("\033[92m🟢 Status : \033[0m", status_request, " 🟢")
                print("🚗 Numéro d’identification du véhicule : ", vin, " 🚗")
                print("🚗 Marque :", make, " 🚗")
                print("🚗 Modèle :", model, " 🚗")
                print("🚗 Carrosserie :", body, " 🚗")
                print("🚗 Nombre de portes :", doors_count, " 🚗")
                print("🚗 Couleur D'Usine De Véhicules : ", color, " 🚗")
                print("\033[92m✅ Code Réponse : \033[0m", response, " ✅")
                print("💻 Réponse JSON : Dans le fichier json_response.txt. 💻\n\n")
            else:
                print(f"\n\033[91m ❗ La plaque d'immatriculation {plaque_convertie} est incorrecte ou n'est pas disponible dans la base de données ! ❗ \033[0m")
                log_message = f"[{datetime.datetime.now()}] 🚗 Requête pour la plaque : {plaque} 🚗\n"
                log_message += f"🔗 URL : {url} 🔗\n"
                log_message += f"\033[91m🔴 Status : ERROR 🔴\033[0m\n"
                log_message += f"\033[91m❗ ERROR : The requested URL was not found on this server. ❗\033[0m\n\n"
                with open("log.txt", "a", encoding='utf-8') as file:
                    file.write(html.escape(log_message))

        except KeyboardInterrupt:
            print("\n\n\033[91m🔴 Fermeture du programme. 🔴\033[0m\n")
            running = False


search_car()
