import string

from werkzeug.exceptions import abort

from app import db
from app.models.pid_controller import PidController


def create(name: string):
    pid_controller: PidController = PidController(name)
    db.session.add(pid_controller)
    db.session.commit()
    return pid_controller


def retrieve(id: int):
    pid_controller: PidController = PidController.query.filter_by(deleted=False).filter_by(id=id).first()
    if not pid_controller:
        abort(404)
    return pid_controller


def retrieve_all():
    pid_controllers: [PidController] = PidController.query.filter_by(deleted=False).all()
    return pid_controllers


def delete(pid_controller: PidController):
    pid_controller.deleted = True
    db.session.commit()


def update(pid_controller: PidController, name: string = None, P: int = None, I: int = None, D: int = None):
    if name:
        pid_controller.name = name
    if P:
        pid_controller.P = P
    if I:
        pid_controller.I = I
    if D:
        pid_controller.D = D
    db.session.commit()
    return pid_controller
