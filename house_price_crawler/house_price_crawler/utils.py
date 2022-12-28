from datetime import datetime
from dateutil.relativedelta import relativedelta

def handle_time_delta(time_str : str) -> str:
    if "ساعت" in time_str:
        return datetime.now().strftime("%Y-%d-%m")

    elif "روز" in time_str:
        time_delta = int(time_str.split(" ")[0])
        adv_date = datetime.now() - relativedelta(days= time_delta)
        return adv_date.strftime("%Y-%d-%m")

    elif "هفته" in time_str:
        time_delta = int(time_str.split(" ")[0])
        adv_date = datetime.now() - relativedelta(weeks= time_delta)
        return adv_date.strftime("%Y-%d-%m")

    elif "ماه" in time_str:
        time_delta = int(time_str.split(" ")[0])
        adv_date = datetime.now() - relativedelta(months= time_delta)
        return adv_date.strftime("%Y-%d-%m")



if __name__ == "__main__":
    pass
