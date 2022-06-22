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



def query_data(form_id):
    global report_model
    match_query = {
        "form_id":form_id,
        "deleted_at":{"$exists":False}
    }
    project = {
        "_id":0,
        "Cantidad": "$answers.62631386499ded22dbc50c9e.62631f2f09168d1d8d36edb9",
        "Descripcion":"$answers.62631386499ded22dbc50c9e.62631f0177244f4eaec50c6e.62631f0277244f4eaec50c70",
        "Codigo":"$answers.62631386499ded22dbc50c9e.62631f0177244f4eaec50c6e.62631f0277244f4eaec50c6f",
        "Marca": "$answers.62631386499ded22dbc50c9e.62681108a77e2218dd7cd614"
    }

    query = [
        {"$match": match_query },
        {"$unwind":"$answers.62631386499ded22dbc50c9e"},
        {"$unwind":"$answers.62631386499ded22dbc50c9e.62631f0177244f4eaec50c6e.62631f0277244f4eaec50c6f"},
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

    form_id = data.get("form_id",83914)

    net = network.Network(settings)
    cr = net.get_collections()
    lkf_api = utils.Cache(settings)
    table_data = query_data(form_id)
    sys.stdout.write(simplejson.dumps({
        "firstElement":{'tabledata':table_data},
        }))
