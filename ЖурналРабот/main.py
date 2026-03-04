from flask import Flask, render_template
from data.db_session import global_init, create_session
from data.jobs import Job

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def get_works_list():
    global_init(f"db/mars_explorer.db")
    db_sess = create_session()

    lst = []

    for work in db_sess.query(Job).all():
        lst.append(
            {
                'id': work.id,
                'team_leader': work.team_leader,
                'job': work.job,
                'work_size': work.work_size,
                'collaborators': work.collaborators,
                'start_date': work.start_date,
                'end_date': work.end_date,
                'is_finished': work.is_finished
            }
        )

    return lst

@app.route('/')
@app.route('/index')
def index():
    works = get_works_list()
    return render_template('index.html', tables_data=works)

if __name__ == '__main__':
    app.run()
