import csv
import requests
class Peticiones:
    def add(self):
        try:
            with open("archivos/Clientes.txt") as f:
                line = csv.reader(f, delimiter=',')
                headers = {"charset": "utf-8", "Content-Type": "application/json"}
                url = "http://localhost:8080/apiv1/clientes/add"
                for bdline in line:
                    data =  {
                            "surname": bdline[0],
                            "firstname": bdline[1],
                            "country": {
                                "name": bdline[2]
                            },
                            "language": {
                                "name": bdline[3]
                            },
                            "airport": {
                                "name": bdline[4]
                            }
                        }
                    r = requests.post(url, json=data, headers=headers)
                    print(r.text)
        except OSError:
            print('Error el archivo no existe')

ejecutar=Peticiones()
ejecutar.add()

