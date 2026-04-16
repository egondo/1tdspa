import datetime

def get_data_hora() -> str:
    data = datetime.datetime.now()
    return f"{data.day}-{data.month}-{data.year} {data.hour}:{data.minute}"

