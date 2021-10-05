from typing import List
import os
import json
import subprocess


config_template = {
    "num_vulnerabilities": 50,
    "num_intensity_bins": 50,
    "num_damage_bins": 50,
    "vulnerability_sparseness": 0.5,
    "num_events": 100000,
    "num_areaperils": 100,
    "areaperils_per_event": 100,
    "intensity_sparseness": 0.5,
    "num_periods": 1000,
    "num_locations": 1000,
    "coverages_per_location": 3,
    "num_layers": 1
}


def get_data_path(size: int) -> str:
    return str(os.getcwd()) + "/data/" + str(size) + "_config.json"


def get_config_path(size: int) -> str:
    return str(os.getcwd()) + "/configs/" + str(size) + "_config.json"


def write_configs(sizes: List[int]) -> None:
    for size in sizes:
        placeholder = config_template
        placeholder["num_events"] = size
        with open(get_config_path(size=size), "w") as outfile:
            json.dump(placeholder, outfile)


def generate_data(size: int) -> None:
    subprocess.call(f"sh ./generate_data.sh {size}", shell=True)


def run_the_processes_for_c(size: int) -> None:
    result = subprocess.Popen(f"sh ./run_c_model.sh {size}", shell=True, stdout=subprocess.PIPE)
    print(f"\n\n\nhere is the output: {result.stdout.read()}")


def run_the_processes_for_python():
    pass


def plot_outcomes():
    pass


if __name__ == "__main__":
    config_sizes = [3, 4, 5, 6, 7]

    write_configs(sizes=config_sizes)

    for i in config_sizes:
        generate_data(size=i)

    run_the_processes_for_c(size=7)

