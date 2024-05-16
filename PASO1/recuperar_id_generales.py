import requests

# Configuración inicial
url = "http://190.11.243.226/app/marcas.aspx"
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "ASP.NET_SessionId=pvdbo5qr2q22suh0a5fo5wef",
    "Host": "190.11.243.226",
    "Origin": "http://190.11.243.226",
    "Referer": "http://190.11.243.226/app/marcas.aspx?_dc=1715716181515&",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "X-Ext.Net": "delta=true,staticmethod=true",
    "X-Requested-With": "XMLHttpRequest"
}

# Crear el archivo donde se guardarán las respuestas
file_path = "PASO1\\response_data5.txt"
with open(file_path, "w", encoding='utf-8') as file:
    # Loop sobre el rango de id deseados
    for expediente_id in range(57914, 60501):  # Cambiar 60501 por el número máximo + 1
        payload = {
            "jsonObject": '{"ClienteIdPais":0,"ClienteNombre":"","ClienteId":null,"ClienteContacto":"","TramitanteNombre":"","TramitanteIdPais":0,"PropietarioIdPais":0,"PropietarioId":null,"PropietarioNombre":"","IdPais":0,"TipoMarca":"","Denominacion":"","Clase":"","Cobertura":"","ExpedienteCodigo":' + str(expediente_id) + ',"RefInterna":"","RefCliente":"","SolicitudNro":"","RegistroNro":"","Comentarios":"","IncluirAnexos":false,"SolicitudFechaDesde":"","SolicitudFechaHasta":"","VigenciaFechaDesde":"","VigenciaFechaHasta":"","FechaCreacionDesde":"","FechaCreacionHasta":"","FechaModificacionDesde":"","FechaModificacionHasta":"","PruebaUsoFechaDesde":"","PruebaUsoFechaHasta":"","RegistroFechaDesde":"","RegistroFechaHasta":"","IdEstado":"0","IdBoletin":"0","IdTipoPublicacion":"0","IdTipoEvento":"0","EventoFechaDesde":"","EventoFechaHasta":"","CreadoPor":"","ModificadoPor":"","FuenteDatos":1,"Archivo":3,"IdAbogado":"0"}',
            "_methodName_": "BuscarMarcas"
        }

        response = requests.post(url, headers=headers, data=payload)
        file.write(f"ExpedienteCodigo {expediente_id}: {response.text}\n\n")
        print(f"Completed {expediente_id}")

print("All requests completed and data saved to file.")
