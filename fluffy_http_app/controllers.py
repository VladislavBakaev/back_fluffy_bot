from flask import (
    Blueprint,
    Response, 
    request)
import json
import sys
import pathlib

from fluffy_http_app.untill import motionControlManager

module = Blueprint('html', __name__, url_prefix=r'/api')

@module.route('/emotion/list', methods=['GET'])
def emotion_list():
    names = motionControlManager.get_emation_name()
    names_res = json.dumps({"emotions":names})
    return names_res

@module.route('/emotion/stop', methods=['GET'])
def emotion_stop():
    motionControlManager.stop_move()
    return "Stop move"

@module.route('/emotion/<string:name>/start', methods=['GET'])
def emotion_start(name):
    motionControlManager.play_emotion(name)
    return "Emotion '{}' is plaing".format(name)

@module.route('/movement/start', methods=['POST'])
def movement_start():
    movement = request.json
    motionControlManager.play_emotion(movement)
    return "Robot in moving"

@module.route('/emotion/save', methods=['POST'])
def emotion_save():
    emotion = request.json
    motionControlManager.save_emotion(emotion)
    return "Emotion was saving"