import math
from engineering_app import app
# bootstrap
from flask import render_template
# , request, redirect, url_for
from engineering_app.form import LoadTable, CalculationsType, PowerCalc, SchedLoads


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
    return render_template('electrical_power.html', title='Basic Calculations', form=form)


@app.route('/power', methods=['GET', 'POST'])
def power():
    form= CalculationsType()
    p_calc = PowerCalc()
    if form.validate_on_submit():
        voltage = p_calc.vol_calc.data
        current = p_calc.amps_calc.data
        power = voltage * current
        answers = {
            'voltage': "{:.2f}".format(voltage),
            'current': "{:.2f}".format(current),
            'power': "{:.2f}".format(power),
        }
        return render_template('calc_power.html', title='Ohms Law - Answer', form=form, p_calc=p_calc, answers=answers)
    
    return render_template('calc_power.html', title='Ohms Law - Power', form=form, p_calc=p_calc)


@app.route('/current', methods=['GET', 'POST'])
def current():
    form= CalculationsType()
    p_calc = PowerCalc()
    if form.validate_on_submit():
        voltage = p_calc.vol_calc.data
        power = p_calc.pow_calc.data
        current = power/voltage
        answers = {
            'voltage': "{:.2f}".format(voltage),
            'power': "{:.2f}".format(power),
            'current': "{:.2f}".format(current),
        }
        return render_template('calc_current.html', title='Ohms Law - Answer', form=form, p_calc=p_calc, answers=answers)
    
    return render_template('calc_current.html', title='Ohms Law - Current', form=form, p_calc=p_calc)


@app.route('/resistance', methods=['GET', 'POST'])
def resistance():
    form= CalculationsType()
    p_calc = PowerCalc()
    if form.validate_on_submit():
        voltage = p_calc.vol_calc.data
        current = p_calc.amps_calc.data
        resistance = voltage/current
        answers = {
            'voltage': "{:.2f}".format(voltage),
            'resistance': "{:.2f}".format(resistance),
            'current': "{:.2f}".format(current),
        }
        return render_template('calc_resistance.html', title='Ohms Law - Answer', form=form, p_calc=p_calc, answers=answers)
    
    return render_template('calc_resistance.html', title='Ohms Law - Resistance', form=form, p_calc=p_calc)


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
        return render_template('solar.html', title='OffGrid-Computed', form=form, answers=answers)
    return render_template('solar.html', title='OffGrid Setup Design', form=form)


@app.route('/schedule_of_loads', methods=['GET', 'POST'])
def sched_loads():
    form = SchedLoads()
    if form.validate_on_submit():
        inputs = {
            'item1': form.item1.data,
            'item2': form.item2.data,
            'item3': form.item3.data,
            'description1': form.description1.data,
            'description2': form.description2.data,
            'description3': form.description3.data,
            'qty1': form.qty1.data,
            'qty2': form.qty2.data,
            'qty3': form.qty3.data,
            'power1': form.power1.data * form.qty1.data,
            'power2': form.power2.data * form.qty2.data,
            'power3': form.power3.data * form.qty3.data,
            'voltage': form.voltage.data,
        }
        calculated = {
            'current1': "{:.2f}".format(inputs['power1'] / inputs['voltage']),
            'current2': "{:.2f}".format(inputs['power2'] / inputs['voltage']),
            'current3': "{:.2f}".format(inputs['power3'] / inputs['voltage']),
        }
        return render_template('sched_loads_calc.html', title='Schedule Of Loads Calculated', form=form, inputs=inputs, calculated=calculated)
    
    return render_template('sched_loads.html', title='Schedule Of Loads', form=form)
