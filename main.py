import math
import os
from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, request, redirect, url_for
from form import LoadTable, CalculationsType, PowerCalc


app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = os.environ.get('ENG_AP_SECRET_KEY')


@app.route('/', methods=["GET", "POST"])
def home():
    return render_template('home.html', title='Home')


@app.route('/about')
def about():
    return render_template('about.html', title='About Page')


@app.route('/cement')
def cement():
    return render_template('cement.html', title='Cement Computations')


@app.route('/electrical_power')
def electrical_power():
    form = CalculationsType()
    return render_template('electrical_power.html', title='Ohms Law Calculations', form=form)


@app.route('/power', methods=['GET', 'POST'])
def power():
    form= CalculationsType()
    p_calc = PowerCalc()
    if form.validate_on_submit():
        voltage = p_calc.vol_calc.data
        current = p_calc.amps_calc.data
        power = voltage * current
        answers = {
            'voltage': voltage,
            'current': current,
            'power': power,
        }
        return render_template('calc.html', title='Ohms Law - Answer', form=form, p_calc=p_calc, answers=answers)
    
    return render_template('calc.html', title='Ohms Law - Power', form=form, p_calc=p_calc)


@app.route('/solar', methods=['GET', 'POST'])
def solar():
    form = LoadTable()
    if form.validate_on_submit():
        datas = {
            'system_voltage': form.system_voltage.data,
            'autonomy': float(form.autonomy.data),
            'battery_type': float(form.battery_type.data),
            'sunhours': float(form.sunhours.data),

            'hours_load1': form.hours_load1.data,
            'hours_load2': form.hours_load2.data,
            'hours_load3': form.hours_load3.data,

            'watts_load1': form.watts_load1.data,
            'watts_load2': form.watts_load2.data,
            'watts_load3': form.watts_load3.data,

            'quantity_load1': form.quantity_load1.data,
            'quantity_load2': form.quantity_load2.data,
            'quantity_load3': form.quantity_load3.data,
        }
        
        load1_wh = datas['hours_load1'] * datas['quantity_load1'] * datas['watts_load1']
        load2_wh = datas['hours_load2'] * datas['quantity_load2'] * datas['watts_load2']
        load3_wh = datas['hours_load3'] * datas['quantity_load3'] * datas['watts_load3']
        total_wh = load1_wh + load2_wh + load3_wh
        inverter_rating = math.ceil(1.25 * total_wh)

        watts_system_loss = 1.35 * total_wh
        watts_autonomy = watts_system_loss * datas['autonomy']
        watts_battery_maxDOD = watts_autonomy / datas['battery_type']
        battery_ah_needed = watts_battery_maxDOD / datas['system_voltage']
        pv_panels_needed = watts_autonomy / datas['sunhours']
        max_pv_panels_needed = watts_battery_maxDOD / datas['sunhours']

        answers = {
            'system_voltage': datas['system_voltage'],
            'load_total_wh': "{:.2f}".format(total_wh),
            'watts_system_loss': "{:.2f}".format(watts_system_loss),
            'watts_autonomy': "{:.2f}".format(watts_autonomy),
            'watts_battery_maxDOD': "{:.2f}".format(watts_battery_maxDOD),
            'battery_ah_needed': "{:.2f}".format(battery_ah_needed),
            'min_pv_panels_needed': "{:.2f}".format(pv_panels_needed),
            'max_pv_panels_needed': "{:.2f}".format(max_pv_panels_needed),
            'inverter_rating': inverter_rating,
        }

        return render_template('solar.html', title='Computed', form=form, answers=answers)
    
    return render_template('solar.html', title='Compute', form=form)


if __name__ == '__main__':
    app.run(debug=True)

