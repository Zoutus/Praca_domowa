from measurements.models import Measurement
import csv



def create_measurements(row: dict):
    value, measured_date, notes = row
    measurements = Measurement.objects.create(value=value, measured_date=measured_date, notes=notes)
    return measurements



def import_measurements():
    with open("dane/dane.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            create_measurements(row)


