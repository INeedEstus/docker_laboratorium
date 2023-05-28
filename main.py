#!/usr/bin/env python3

# Import potrzebnych bibliotek
import http.server
import socketserver
import datetime
import socket

# Pobranie nazwy hosta
hostname = socket.gethostname()

# Pobranie adresu IP hosta
ip_address = socket.gethostbyname(hostname)

# Pobranie aktualnej daty i godziny
current_time = datetime.datetime.now()

# Port serwera
port = 8000

# Zapisanie informacji do logów
log = f"Autor: Damian Kosidlo\nUruchomiono serwer z adresu IP {ip_address} i portu {port}"
print(log)
text_file = open("logs.txt",mode='a')
text_file.write(log)
text_file.close()

# Tworzenie klasy obsługującej żądania HTTP
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

# Uruchomienie serwera na wybranym porcie
with socketserver.TCPServer(("", port), MyHttpRequestHandler) as httpd:
    httpd.serve_forever()
