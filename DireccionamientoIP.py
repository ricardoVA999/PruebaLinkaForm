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

from linkaform_api import settings
from linkaform_api import network
from settings_selecom import *



def query_data(form_id, Area, Usuario):
    global report_model
    match_query = {
        "form_id":form_id,
        "deleted_at":{"$exists":False}
    }

    if Area:
        match_query.update({'answers.60007c5194d9a63b1caf534c.60007ca59253268e682b8760':Area})
    if Usuario:
        match_query.update({'answers.60007c5194d9a63b1caf534c.60007c5194d9a63b1caf534f':Usuario})

    else:
        project = {
            "_id":0,
            "Direccion IP":"$answers.60c28676eb621713f3908761",
            "Mac Address":"$answers.60c28676eb621713f3908762",
            "Descripción":"$answers.60c28676eb621713f3908763",
            "Nombre de Area":"$answers.60007c5194d9a63b1caf534c.60007ca59253268e682b8760",
            "Colaborador":"$answers.60007c5194d9a63b1caf534c.60007c5194d9a63b1caf534f"
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
    form_id = data.get("form_id",71726)
    Area = data.get("Area","")
    Usuario = data.get("Usuario","")

    if '--' in Area:
        Area = None
    if '--' in Usuario:
        Usuario = None

    net = network.Network(settings)
    cr = net.get_collections()
    lkf_api = utils.Cache(settings)
    table_data = query_data(form_id, Area, Usuario)
    sys.stdout.write(simplejson.dumps({
        "firstElement":{'tabledata':table_data},
        }))