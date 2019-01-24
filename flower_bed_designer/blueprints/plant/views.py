from flask import Blueprint

from flower_bed_designer.blueprints.plant.api import PlantAPI
from flower_bed_designer.helpers import register_api

bp = Blueprint('plant', __name__)

register_api(bp, PlantAPI, 'plant', '/plant/', pk='plant_id')
