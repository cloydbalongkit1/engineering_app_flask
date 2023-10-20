from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, SelectField, DecimalField, FloatField
from wtforms.validators import DataRequired, InputRequired, NumberRange


class LoadTable(FlaskForm):
    
    autonomy = DecimalField('Days of Autonomy (ranges: 1-10)', validators=[InputRequired(), NumberRange(min=0)])
    system_voltage = IntegerField('System Voltage (12V, 24V, 36V, 48V, 60V ...etc)', validators=[InputRequired(), NumberRange(min=0)])
    sunhours = DecimalField('Sun Harvest (ranges: 1.0 hr/s - 10.0 hr/s)', validators=[InputRequired(), NumberRange(min=0)])
    battery_type = SelectField('Battery', choices=[('0.8', 'LiFeSo4'), ('0.5', 'Lead Acid')], validators=[DataRequired()])
    submit = SubmitField('Submit')

    hours_load1 = IntegerField('Hours Used', validators=[InputRequired(), NumberRange(min=0)])
    watts_load1 = IntegerField('Wattage', validators=[InputRequired(), NumberRange(min=0)])
    quantity_load1 = IntegerField('Quantity', validators=[InputRequired(), NumberRange(min=0)])

    hours_load2 = IntegerField('Hours Used', validators=[InputRequired(), NumberRange(min=0)])
    watts_load2 = IntegerField('Wattage', validators=[InputRequired(), NumberRange(min=0)])
    quantity_load2 = IntegerField('Quantity', validators=[InputRequired(), NumberRange(min=0)])

    hours_load3 = IntegerField('Hours Used', validators=[InputRequired(), NumberRange(min=0)])
    watts_load3 = IntegerField('Wattage', validators=[InputRequired(), NumberRange(min=0)])
    quantity_load3 = IntegerField('Quantity', validators=[InputRequired(), NumberRange(min=0)])


class CalculationsType(FlaskForm):
    power = SubmitField('Power')
    current = SubmitField('Current')
    resistance = SubmitField('Resistance')


class PowerCalc(FlaskForm):
    vol_calc = FloatField('Input Voltage', validators=[InputRequired(), NumberRange(min=1)])
    amps_calc = FloatField('Input Current', validators=[InputRequired(), NumberRange(min=1)])
    res_calc = FloatField('Input Resistance', validators=[InputRequired(), NumberRange(min=1)])
    submit = SubmitField('Submit')
    