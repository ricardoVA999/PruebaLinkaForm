

var columnsData = [
  {"headerFilter": "input", "title": "Area Operativa", "frozen": false, "hozAlign": "left", "field": "area_operativa", "with": 150},
  {"headerFilter": "input", "title": "Compañia", "frozen": false, "hozAlign": "left", "field": "compania", "with": 150},
  {"title": "Mes de Cierre",  "field": "mes_cierre", "frozen": false, "hozAlign": "center", "with": 75},
  {"title": "Placa",  "field": "placa", "frozen": false, "hozAlign": "center", "with": 75},
  {"title": "No Hoja",  "field": "no_hoja", "frozen": false, "hozAlign": "center", "with": 75},
  {"title": "Fecha Hora Salida",  "field": "salida", "frozen": false, "hozAlign": "center", "with": 75},
  {"title": "Fecha Hora Entrada",  "field": "entrada", "frozen": false, "hozAlign": "center", "with": 75},
  {"title": "Dias Arrendamiento",  "field": "d_arrendamiento", "frozen": false, "hozAlign": "center", "with": 25},
  {"title": "Total Arrendamiento",  "field": "t_arrendamiento", "frozen": false, "hozAlign": "center",  "formatter": "money", "with":25,
    "formatterParams": {"symbol": "Q ", "symbolAfter": "", "decimal": ".", "thousand": ",", "precision": 2 }},
  {"title": "Divsion",  "field": "division", "frozen": false, "hozAlign": "center", "with": 75},
  {"headerFilter": "input", "title": "Pilotos",  "field": "piloto", "frozen": false, "hozAlign": "center", "with": 75},
  {"title": "Proyecto ODT",  "field": "proyecto_odt", "frozen": false, "hozAlign": "center", "with": 75},
  {"title": "Lugar Destino",  "field": "destino", "frozen": false, "hozAlign": "center", "with": 75},
]


/*var dataTable1 = [
 {id:1, plant_name:"Oli Bob", gender:"female", actuals202238:"12", col:"red", dob:""},
 {id:2, plant_name:"Mary May", actuals202238:"1", col:"blue", dob:"14/05/1982"},
 {id:3, plant_name:"Christine Lobowski", actuals202238:"42", col:"green", dob:"22/05/1982"},
 {id:4, plant_name:"Brendon Philips", actuals202238:"125", col:"orange", dob:"01/08/1980"},
 {id:5, plant_name:"Margret Marmajuke", actuals202238:"16", col:"yellow", dob:"31/01/1999"},
];
*/

var dataTable1 = [
  {
    "area_operativa":"PLANTA INTERNA/EXTERNA", "compania":"SELECOM NETWORKS. S.A", "mes_cierre":"AGOSTO",
    "placa":"049HSR", "salida":"2021-08-02 09:00:35", "entrada":"2021-08-04 12:00:35", "d_arrendamiento":2,
    "t_arrendamiento":100.45666055, "division":"SEDE CENTRAL", "piloto":"N/A", "destino":"CHIMALTENANGO"
  }

];
