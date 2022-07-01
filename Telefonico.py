# -*- coding: utf-8 -*-
#####
#####
# Script para indicar quien asigno el regsitro
#
#
#####
import sys, json, simplejson#, subprocess
#from bson import ObjectId

from datetime import datetime, timedelta
import time
#85678 scirpt_id
from linkaform_api import settings
from linkaform_api import network
from settings_selecom import *



def query_data(form_id, Colaborador):
    global report_model
    match_query = {
        "form_id":form_id,
        "deleted_at":{"$exists":False}
    }
    if Colaborador:
        match_query.update({'answers.60007c5194d9a63b1caf534c.60007c5194d9a63b1caf534f':Colaborador})
    project = {
        "_id":0,
        'No':"$answers.60c8d69ba3f71c6145978afe",
        'Colaborador':"$answers.60007c5194d9a63b1caf534c.60007c5194d9a63b1caf534f",
        'Nombre de Area':"$answers.60007c5194d9a63b1caf534c.60007ca59253268e682b8760",
        'IP':"$answers.60c8d7bc641cce2899a6305c",
        'Mac Address':"$answers.60c8d7bc641cce2899a6305d",
        'Gateway':"$answers.60c8d7bc641cce2899a6305e",
        'DNS-SRV-1':"$answers.60c8d7bc641cce2899a6305f",
        'DNS-SRV-2':"$answers.60c8d7bc641cce2899a63060",
        'Mascara de Red':"$answers.60c8d7bc641cce2899a63061",
        'SIP Servidor':"$answers.60c8d7bc641cce2899a63062",
        'Activo':"$answers.60c8d7bc641cce2899a63063",
        'Sip Registro':"$answers.60c8d7bc641cce2899a63064",
        'Extension':"$answers.60c8d7bc641cce2899a63065",
        'No de Serie':"$answers.60c8d7bc641cce2899a63066",
        'Modelo':"$answers.60c8d7bc641cce2899a63067",
        'Version':"$answers.60c8d7bc641cce2899a63068",
        'Coste':"$answers.60c8d7bc641cce2899a63069",
        'Fecha':"$answers.60c8d7bc641cce2899a6306a"
    }

    query = [
        {"$match": match_query },
        {"$project":project},
    ]

    solicitudes = cr.aggregate(query)

    res = []

    for s in solicitudes:
        res.append(s)

    return res



if __name__ == '__main__':
    print(sys.argv)
    jwt_complete = simplejson.loads(sys.argv[2])
    all_data = simplejson.loads(sys.argv[2])
    data = all_data.get("data", {})
    config['USER_JWT_KEY'] = jwt_complete["jwt"].split(' ')[1]
    settings.config.update(config)

    form_id = data.get("form_id",71824)
    Colaborador = data.get("Colaborador","")
    if '--' in Colaborador:
        Colaborador = None

    net = network.Network(settings)
    cr = net.get_collections()
    lkf_api = utils.Cache(settings)
    table_data = query_data(form_id, Colaborador)
    
    sys.stdout.write(simplejson.dumps({
        "firstElement":{'tabledata':table_data},
        }))
