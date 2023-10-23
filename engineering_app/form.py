from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, SelectField, DecimalField, FloatField, StringField
from wtforms.validators import DataRequired, InputRequired, NumberRange, Length


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
    pow_calc = FloatField('Input Power', validators=[InputRequired(), NumberRange(min=1)])
    submit = SubmitField('Submit')
    

class SchedLoads(FlaskForm):
    item1 = IntegerField('Item/s', validators=[InputRequired(), NumberRange(min=1, max=100)])
    description1 = StringField('Description', validators=[DataRequired(), Length(min=1, max=20)])
    qty1 = IntegerField('Qty', validators=[InputRequired(), NumberRange(min=0)])
    power1 = IntegerField('Power', validators=[InputRequired(), NumberRange(min=0)])

    item2 = IntegerField('Item/s', validators=[InputRequired(), NumberRange(min=1, max=100)])
    description2 = StringField('Description', validators=[DataRequired(), Length(min=1, max=20)])
    qty2 = IntegerField('Qty', validators=[InputRequired(), NumberRange(min=0)])
    power2 = IntegerField('Power', validators=[InputRequired(), NumberRange(min=0)])

    item3 = IntegerField('Item/s', validators=[InputRequired(), NumberRange(min=1, max=100)])
    description3 = StringField('Description', validators=[DataRequired(), Length(min=1, max=20)])
    qty3 = IntegerField('Qty', validators=[InputRequired(), NumberRange(min=0)])
    power3 = IntegerField('Power', validators=[InputRequired(), NumberRange(min=0)])

    voltage = IntegerField('System Voltage', validators=[InputRequired(), NumberRange(min=1)])
    submit = SubmitField('Calculate')
