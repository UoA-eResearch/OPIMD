#!/usr/bin/env python3

import pandas as pd
import json

df = pd.read_excel("OPIMD Calc_checked_03Feb21AL.xlsx", sheet_name=None)

obj = {}

dz = df["OPIMD15ACCESSDATAZONERANK"]
dz = dz.dropna(subset=["datazone"])
dz.datazone = dz.datazone.astype(int)
dz.index = dz.datazone
obj["dz"] = dz.OPIMDAccPopRank_AL.to_dict()

hlth = df["HEALTHCALC"]
hlth.index = hlth.HlthPattern
obj["hlth"] = hlth.HlthRank.to_dict()

inc = df["INCOMECALC"]
inc.index = inc.IncPattern
obj["inc"] = inc.IncRank.to_dict()

house = df["HOUSECALC"]
house.index = house.HouPattern
obj["house"] = house.HouRank.to_dict()

con = df["CONNECTCALC"]
con = con.dropna(subset=["ConPattern"])
con.index = con.ConPattern
obj["con"] = con.ConRank.to_dict()

assets = df["ASSETSCALC"]
assets = assets.dropna(subset=["AsPattern"])
assets.index = assets.AsPattern
obj["assets"] = assets.AsRank.to_dict()

breaks = df["OPIMDRankDecile"]
breaks = breaks.iloc[3:13,0:3]
breaks.columns = ["min", "max", "decile"]
obj["breaks"] = breaks.to_dict(orient='records')

with open("data.json", "w") as f:
    json.dump(obj, f)
    print("Saved")