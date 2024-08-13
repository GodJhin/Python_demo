from pivottablejs import  pivot_ui
import  pandas as pd

data = pd.read_csv('CCD2_20231228 .csv')
data["Year"] = pd.to_datetime(data["Date Joined"]).dt.year
pivot_ui(data)