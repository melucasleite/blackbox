from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler

from app import app
from app.jobs.start_serial_com import start_serial_com

if __name__ == "__main__":
    scheduler = BackgroundScheduler(
        jobstores={'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')})
    scheduler.start()
    job = scheduler.add_job(start_serial_com, id="start_serial_com", replace_existing=True)
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
