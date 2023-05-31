# Zadanie 1:
```
#!/usr/bin/env python3

# Import potrzebnych bibliotek:
import http.server
import socketserver
import datetime
import socket

# Pobranie nazwy hosta:
hostname = socket.gethostname()

# Pobranie adresu IP hosta:
ip_address = socket.gethostbyname(hostname)

# Pobranie aktualnej daty i godziny:
current_time = datetime.datetime.now()

# Port serwera:
port = 8000

# Zapisanie informacji do logów:
log_message = f"Autor: Damian Kosidlo\nUruchomiono serwer z adresu IP {ip_address} i portu {port}"
print(log_message)
text_file = open("logs.txt",mode='a')
text_file.write(log_message)
text_file.close()

# Tworzenie klasy obsługującej żądania HTTP:
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Pobranie adresu IP klienta
        client_ip = self.client_address[0]
        # Pobranie aktualnej daty i godziny w strefie czasowej klienta
        client_time = datetime.datetime.now(datetime.timezone.utc).astimezone()
        # Tworzenie odpowiedzi dla klienta
        response_content = f"Klient o adresie IP {client_ip} polaczyl sie {client_time}"
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(response_content.encode())

# Uruchomienie serwera na wybranym porcie:
with socketserver.TCPServer(("", port), MyHttpRequestHandler) as httpd:
    httpd.serve_forever()
```
# Zadanie 2:
```# Damian Kosidlo
FROM python:latest
COPY main.py /
CMD [ "python", "./main.py" ]
```
# Zadanie 3:
## A. Budowa obrazu kontenera:
```
sudo docker build -t serwer .
```
## B. Uruchomienie kontenera:
```
sudo docker run serwer
```
## C. Dostanie się do pliku logs.txt:
```
# Sprawdzić nazwę uruchomionego kontenera
sudo docker ps
# Dostanie się do plików kontenera
sudo docker exec -it Nazwa_Kontenera bash
# Plik z logs.txt znajduję się w głównym folderze, wystarczy tylko odczytać plik
cat logs.txt
```
![image](https://github.com/INeedEstus/docker_laboratorium/assets/79727495/a19de98c-9ef3-4498-ab8f-8905323bfe8f)
## D. Ilość warstw zbudowanego obrazu:
```
sudo docker history -q serwer | wc -l
```
# Ze względu na duże rozmiary obrazów z zadania dodatkowego, zostały one przesłane pod adresem https://drive.google.com/file/d/1YkiCFTzLHU21puhgAdDHSfuHvQBQXN1d/view?usp=sharing

# Jak dostać się do strony:
## Wyświetlić uruchomione kontenery:
```
sudo docker ps
```
## Wyświetlić adres IP kontenera:
```
sudo docker container inspect ID_Kontenera | grep -i IPAddress
```
## Na koniec należy wpisać "Adres_IP_Kontenera:Port" w przeglądarce (przypisany kod w porcie to 8000):
![image](https://github.com/INeedEstus/docker_laboratorium/assets/79727495/752f7d4d-6626-4064-b908-7f02f35a1a77)
