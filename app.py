import flask
import calendar


app = flask.Flask(__name__, template_folder='templates')

def generate_calendar(year):
    cal = calendar.TextCalendar(calendar.SUNDAY)
    return cal.formatyear(year)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/calendar')
def calendar_page():
    year = 2024  # You can change this to the desired year
    cal = generate_calendar(year)
    return flask.render_template('calendar_page.html', calendar=cal)


if __name__ == '__main__':
    app.run(debug=True)