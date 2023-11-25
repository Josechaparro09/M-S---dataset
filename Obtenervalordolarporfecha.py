import tkinter as tk
from tkcalendar import DateEntry
import requests
from datetime import datetime

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Consulta de API")
        self.geometry("400x200")

        self.inicializar_interfaz()

    def inicializar_interfaz(self):
        self.calendario = DateEntry(self, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.calendario.pack(pady=10)

        btn_consultar = tk.Button(self, text="Consultar", command=self.consultar_api)
        btn_consultar.pack(pady=10)

    def consultar_api(self):
        fecha_seleccionada = self.calendario.get_date()

        fecha_formateada = datetime.strptime(str(fecha_seleccionada), '%Y-%m-%d').strftime('%Y-%m-%dT%H:%M:%S.000')

        url_api = "https://www.datos.gov.co/resource/mcec-87by.json"  # Reemplaza esto con la URL de tu API
        parametros = {"vigenciadesde": fecha_formateada}

        try:
            respuesta = requests.get(url_api, params=parametros)
            datos_api = respuesta.json()
            datos=datos_api[0]
            print(datos["valor"])
        except requests.RequestException as e:
            print(f"Error al consultar la API: {e}")

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()