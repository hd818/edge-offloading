parameter = {
    "esc": 1e-28,  # effective switch capacitance
    "alpha": 0.6,  # weight factor
    "cph_edge": 0.1,  # money per hour in edge server
    "cph_cloud": 0.01,  # money per hour in cloud
    "tr_power": 1.865,  # transmission power of mobile device in W, 1865mW
    "tail_energy": 1.125,  # average lte tail energy is 1125 mW
    "tail_duration": 11.5, # 11576.0±26.1 in seconds
    "mobile_com_cap": 2.6e9,  # 2.6 GHz processor speed, 1e9 cpu cycle per second
    "edge_com_cap": 3.4e9,  # 3.4 GHz processor speed
    "cloud_com_cap": 5e9,  # cloud computing capability 5 GHZ processor speed
    "cloud_cap": 0.6, # allocated resource in cloud
    "max_penalty": -1000,  # maximum penalty if violates constraint
    "total_energy": 100   # in J, energy = watt * voltage = wh, 3110 mah * 110V
}
