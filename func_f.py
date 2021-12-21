import pandas as pd
import numpy as np
from datetime import date, datetime

def formatear_para_usuario_fact(tabla):
    cambios_nombres = {
        "Sociedad PA": "Sociedad",
        "Importe en moneda local BANCO": "Importe en moneda local",
        "Moneda local BANCO": "Moneda local",
        "Texto BANCO": "Texto",
        "Nº factura BANCO": "Nº factura",
        "Asignación PA": "Asignación",
        "Referencia PA": "Referencia",
        "Importe en moneda doc. PA": "Importe en moneda doc.",
        "Moneda del documento PA": "Moneda del documento",
        "Fecha nueva cont. BANCO": "Fecha contabilización",
    }
    
    columnas = [
        "Correlativo",
        "Sociedad",
        "Nº documento BANCO",
        "Clase de documento BANCO",
        "Importe en moneda local",
        "Moneda local",
        "Texto",
        "Nº factura",
        "Asignación",
        "Nº documento PA",
        "Referencia",
        "Clase de documento PA",
        "Importe en moneda doc.",
        "Moneda del documento",
    ]

    tabla = tabla.copy()
    tabla = tabla.rename(columns=cambios_nombres)
    return tabla[columnas].copy()


def formatear_para_usuario_id(tabla):
    cambios_nombres = {
        "Sociedad PA": "Sociedad",
        "Importe en moneda local BANCO": "Importe en moneda local",
        "Moneda local BANCO": "Moneda local",
        "Texto BANCO": "Texto",
        "Cliente BANCO": "Cliente",
        "Nº ident.fis.1 BANCO": "Nº ident.fis.1",
        "Nombre 1 BANCO": "Nombre 1",
        "Asignación PA": "Asignación",
        "Referencia PA": "Referencia",
        "Importe en moneda doc. PA": "Importe en moneda doc.",
        "Moneda del documento PA": "Moneda del documento",
    }
    
    columnas = [
        "Correlativo",
        "Sociedad",
        "Nº documento BANCO",
        "Clase de documento BANCO",
        "Importe en moneda local",
        "Moneda local",
        "Texto",
        "Cliente",
        "Nº ident.fis.1",
        "Nombre 1",
        "Asignación",
        "Nº documento PA",
        "Referencia",
        "Clase de documento PA",
        "Importe en moneda doc.",
        "Moneda del documento",
    ]

    tabla = tabla.copy()
    tabla = tabla.rename(columns=cambios_nombres)
    return tabla[columnas].copy()

def formatear_para_exportar(tabla):
    cambios_nombres = {
        "Correlativo": "CORR",
        "Fecha nueva cont. BANCO": "BUDAT",
        "Fecha valor BANCO": "VALUT",
        "Sociedad PA": "BUKRS",
        "Moneda local BANCO": "WAERS",
        "Cuenta de mayor BANCO": "KONTO",
        "Importe en moneda local BANCO": "WRBTR",
        "Cuenta PA": "AGKON",
        "Texto BANCO": "SGTXT",
        "Nº documento PA": "BELNR",
    }

    columnas = [
        "CORR",
        "BLDAT",
        "BUDAT",
        "VALUT",
        "BLART",
        "BUKRS",
        "WAERS",
        "XBLNR",
        "BKTXT",
        "KONTO",
        "WRBTR",
        "AGKON",
        "AGUMS",
        "KOART",
        "AUGTX",
        "SGTXT",
        "BELNR",
    ]
                           
    if len(tabla) == 0:
        return pd.DataFrame(columns=columnas)
    
    tabla = tabla.copy()

    # Agregar algunas columnas
    tabla["BLART"] = "DZ"
    
    string = input("XBLNR (referencia): ")
    while len(string) > 16:
        string = input("Debe ingresar un string de no más de 16 caracteres de largo: ")
    tabla["XBLNR"] = string

    string = input("BKTXT (texto): ")
    while len(string) > 10:
        string = input("Debe ingresar un string de no más de 10 caracteres de largo: ")
    tabla["BKTXT"] = string
    
    tabla["AGUMS"] = ""
    tabla["KOART"] = "D"

    string = input("AUGTX (texto): ")
    while len(string) > 18:
        string = input("Debe ingresar un string de no más de 18 caracteres de largo: ")
    tabla["AUGTX"] = string

    # Renombrar columnas   
    tabla = tabla.rename(columns=cambios_nombres)

    # Cambiar el formato de la fecha de valor
    tabla["VALUT"] = tabla["VALUT"].dt.strftime("%d.%m.%Y")

    # Agregar una fecha
    tabla["BLDAT"] = tabla["BUDAT"]

    # Sacar valor absoluto de los montos
    tabla["WRBTR"] = tabla["WRBTR"].abs()

    # Seleccionar columnas
    return tabla[columnas].copy()
