# Tests that the NLL algorithm is correctly solved

import machupX as MX
import numpy as np
import json
import subprocess as sp

input_file = "test/input_for_testing.json"


def test_linear_solver():
    # Tests the NLL algorithm is correctly solved

    # Alter input
    with open(input_file, 'r') as input_file_handle:
        input_dict = json.load(input_file_handle)

    input_dict["solver"]["type"] = "linear"

    input_dict["scene"]["aircraft"]["test_plane"]["control_state"] = {
        "elevator" : 0.0,
        "rudder" : 0.0,
        "aileron" : 0.0
    }

    input_dict["scene"]["aircraft"]["test_plane"]["state"] = {
        "position" : [0, 0, 1000],
        "angular_rates" : [0.0, 0.0, 0.0],
        "velocity" : 100,
        "alpha" : 2.0,
        "beta" : 0.0
    }

    # Create scene
    scene = MX.Scene(input_dict)
    FM = scene.solve_forces()
    print(json.dumps(FM["test_plane"]["total"], indent=4))
    assert abs(FM["test_plane"]["total"]["FL"]-20.961790953642968)<1e-10
    assert abs(FM["test_plane"]["total"]["FD"]-1.3934413451737937)<1e-10
    assert abs(FM["test_plane"]["total"]["FS"])<1e-10
    assert abs(FM["test_plane"]["total"]["Fx"]+0.6610365440906614)<1e-10
    assert abs(FM["test_plane"]["total"]["Fy"])<1e-10
    assert abs(FM["test_plane"]["total"]["Fz"]+20.997651998593668)<1e-10
    assert abs(FM["test_plane"]["total"]["Mx"])<1e-10
    assert abs(FM["test_plane"]["total"]["My"]+12.877269524986069)<1e-10
    assert abs(FM["test_plane"]["total"]["Mz"])<1e-10


def test_linear_solver_with_rotation():
    # Tests the NLL algorithm is correctly solved

    # Alter input
    with open(input_file, 'r') as input_file_handle:
        input_dict = json.load(input_file_handle)

    input_dict["solver"]["type"] = "linear"

    input_dict["scene"]["aircraft"]["test_plane"]["control_state"] = {
        "elevator" : 0.0,
        "rudder" : 0.0,
        "aileron" : 0.0
    }

    input_dict["scene"]["aircraft"]["test_plane"]["state"] = {
        "position" : [0, 0, 1000],
        "angular_rates" : [0.2, 0.2, 0.2],
        "velocity" : 100,
        "alpha" : 2.0,
        "beta" : 0.0
    }

    # Create scene
    scene = MX.Scene(input_dict)
    FM = scene.solve_forces()
    print(json.dumps(FM["test_plane"]["total"], indent=4))
    assert abs(FM["test_plane"]["total"]["FL"]-22.199329484957747)<1e-10
    assert abs(FM["test_plane"]["total"]["FD"]-1.4182873883741445)<1e-10
    assert abs(FM["test_plane"]["total"]["FS"]-0.4463758217770067)<1e-10
    assert abs(FM["test_plane"]["total"]["Fx"]+0.6426779798599743)<1e-10
    assert abs(FM["test_plane"]["total"]["Fy"]-0.4463758217770067)<1e-10
    assert abs(FM["test_plane"]["total"]["Fz"]+22.235303769275085)<1e-10
    assert abs(FM["test_plane"]["total"]["Mx"]+3.5422710730907068)<1e-10
    assert abs(FM["test_plane"]["total"]["My"]+16.3420085486301)<1e-10
    assert abs(FM["test_plane"]["total"]["Mz"]+1.4273289149763269)<1e-10


def test_nonlinear_solver():
    # Tests the NLL algorithm is correctly solved

    # Alter input
    with open(input_file, 'r') as input_file_handle:
        input_dict = json.load(input_file_handle)

    input_dict["solver"]["type"] = "nonlinear"

    input_dict["scene"]["aircraft"]["test_plane"]["control_state"] = {
        "elevator" : 0.0,
        "rudder" : 0.0,
        "aileron" : 0.0
    }

    input_dict["scene"]["aircraft"]["test_plane"]["state"] = {
        "position" : [0, 0, 1000],
        "angular_rates" : [0.0, 0.0, 0.0],
        "velocity" : 100,
        "alpha" : 2.0,
        "beta" : 0.0
    }

    # Create scene
    scene = MX.Scene(input_dict)
    FM = scene.solve_forces()
    print(json.dumps(FM["test_plane"]["total"], indent=4))
    assert abs(FM["test_plane"]["total"]["FL"]-20.959074770349314)<1e-10
    assert abs(FM["test_plane"]["total"]["FD"]-1.3934114313254868)<1e-10
    assert abs(FM["test_plane"]["total"]["FS"])<1e-10
    assert abs(FM["test_plane"]["total"]["Fx"]+0.661101441894963)<1e-10
    assert abs(FM["test_plane"]["total"]["Fy"])<1e-10
    assert abs(FM["test_plane"]["total"]["Fz"]+20.994936425947238)<1e-10
    assert abs(FM["test_plane"]["total"]["Mx"])<1e-10
    assert abs(FM["test_plane"]["total"]["My"]+12.873864820066961)<1e-10
    assert abs(FM["test_plane"]["total"]["Mz"])<1e-10


def test_sideslip():
    # Tests the algorithm is correctly solved when there is sideslip

    # Alter input
    with open(input_file, 'r') as input_file_handle:
        input_dict = json.load(input_file_handle)

    input_dict["solver"]["type"] = "linear"

    input_dict["scene"]["aircraft"]["test_plane"]["control_state"] = {
        "elevator" : 0.0,
        "rudder" : 0.0,
        "aileron" : 0.0
    }

    input_dict["scene"]["aircraft"]["test_plane"]["state"] = {
        "position" : [0, 0, 1000],
        "angular_rates" : [0.0, 0.0, 0.0],
        "velocity" : 100,
        "alpha" : 2.0,
        "beta" : 3.0
    }

    # Create scene
    scene = MX.Scene(input_dict)
    FM = scene.solve_forces()
    print(json.dumps(FM["test_plane"]["total"], indent=4))
    assert abs(FM["test_plane"]["total"]["FL"]-20.974530024918774)<1e-10
    assert abs(FM["test_plane"]["total"]["FD"]-1.5652160687735406)<1e-10
    assert abs(FM["test_plane"]["total"]["FS"]+4.058609066006053)<1e-10
    assert abs(FM["test_plane"]["total"]["Fx"]+0.6178364811613699)<1e-10
    assert abs(FM["test_plane"]["total"]["Fy"]+4.134963963022404)<1e-10
    assert abs(FM["test_plane"]["total"]["Fz"]+21.00889025545816)<1e-10
    assert abs(FM["test_plane"]["total"]["Mx"]+3.2179510813875187)<1e-10
    assert abs(FM["test_plane"]["total"]["My"]+13.079817929574196)<1e-10
    assert abs(FM["test_plane"]["total"]["Mz"]-12.29316240278045)<1e-10


def test_angular_rotation():
    # Tests the algorithm is correctly solved when there is angular rotation

    # Alter input
    with open(input_file, 'r') as input_file_handle:
        input_dict = json.load(input_file_handle)

    input_dict["solver"]["type"] = "nonlinear"

    input_dict["scene"]["aircraft"]["test_plane"]["control_state"] = {
        "elevator" : 0.0,
        "rudder" : 0.0,
        "aileron" : 0.0
    }

    input_dict["scene"]["aircraft"]["test_plane"]["state"] = {
        "position" : [0, 0, 1000],
        "angular_rates" : [0.0, 0.1, 0.1],
        "velocity" : 100,
        "alpha" : 2.0,
        "beta" : 3.0
    }

    # Create scene
    scene = MX.Scene(input_dict)
    FM = scene.solve_forces()
    print(json.dumps(FM["test_plane"]["total"], indent=4))
    assert abs(FM["test_plane"]["total"]["FL"]-21.577973332611467)<1e-10
    assert abs(FM["test_plane"]["total"]["FD"]-1.5715676937388965)<1e-10
    assert abs(FM["test_plane"]["total"]["FS"]+3.8259279872299494)<1e-10
    assert abs(FM["test_plane"]["total"]["Fx"]+0.6152858382833962)<1e-10
    assert abs(FM["test_plane"]["total"]["Fy"]+3.9029341839442906)<1e-10
    assert abs(FM["test_plane"]["total"]["Fz"]+21.61261231816672)<1e-10
    assert abs(FM["test_plane"]["total"]["Mx"]+2.9268795847665534)<1e-10
    assert abs(FM["test_plane"]["total"]["My"]+14.780806933014897)<1e-10
    assert abs(FM["test_plane"]["total"]["Mz"]-11.5917753218481)<1e-10


def test_flap_deflection():
    # Tests the algorithm is correctly solved when there is flap deflection

    # Alter input
    with open(input_file, 'r') as input_file_handle:
        input_dict = json.load(input_file_handle)

    input_dict["solver"]["type"] = "linear"

    input_dict["scene"]["aircraft"]["test_plane"]["control_state"] = {
        "elevator" : -2.0,
        "rudder" : 0.0,
        "aileron" : 3.0
    }

    input_dict["scene"]["aircraft"]["test_plane"]["state"] = {
        "position" : [0, 0, 1000],
        "angular_rates" : [0.0, 0.0, 0.0],
        "velocity" : 100,
        "alpha" : 2.0,
        "beta" : 0.0
    }

    # Create scene
    scene = MX.Scene(input_dict)
    FM = scene.solve_forces(non_dimensional=False)
    print(json.dumps(FM["test_plane"]["total"], indent=4))
    assert abs(FM["test_plane"]["total"]["FL"]-15.381452407184405)<1e-10
    assert abs(FM["test_plane"]["total"]["FD"]-2.1713087073211823)<1e-10
    assert abs(FM["test_plane"]["total"]["FS"]-0.640734030322335)<1e-10
    assert abs(FM["test_plane"]["total"]["Fx"]+1.6331810571592724)<1e-10
    assert abs(FM["test_plane"]["total"]["Fy"]-0.640734030322335)<1e-10
    assert abs(FM["test_plane"]["total"]["Fz"]+15.447860023042152)<1e-10
    assert abs(FM["test_plane"]["total"]["Mx"]+9.613302174142484)<1e-10
    assert abs(FM["test_plane"]["total"]["My"]-3.615122963872464)<1e-10
    assert abs(FM["test_plane"]["total"]["Mz"]+2.2740074284582805)<1e-10


def test_coefficients():
    # Tests the NLL algorithm correctly returns nondimensional coefficients

    # Alter input
    with open(input_file, 'r') as input_file_handle:
        input_dict = json.load(input_file_handle)

    input_dict["solver"]["type"] = "linear"

    input_dict["scene"]["aircraft"]["test_plane"]["control_state"] = {
        "elevator" : 0.0,
        "rudder" : 0.0,
        "aileron" : 0.0
    }

    input_dict["scene"]["aircraft"]["test_plane"]["state"] = {
        "position" : [0, 0, 1000],
        "angular_rates" : [0.0, 0.0, 0.0],
        "velocity" : 100,
        "alpha" : 2.0,
        "beta" : 0.0
    }

    # Create scene
    scene = MX.Scene(input_dict)
    FM = scene.solve_forces(non_dimensional=True)
    print(json.dumps(FM["test_plane"]["total"], indent=4))
    assert abs(FM["test_plane"]["total"]["CL"]-0.22047491174230177)<1e-10
    assert abs(FM["test_plane"]["total"]["CD"]-0.014656135932024195)<1e-10
    assert abs(FM["test_plane"]["total"]["CS"])<1e-10
    assert abs(FM["test_plane"]["total"]["Cx"]+0.006952744354675291)<1e-10
    assert abs(FM["test_plane"]["total"]["Cy"])<1e-10
    assert abs(FM["test_plane"]["total"]["Cz"]+0.2208520961507322)<1e-10
    assert abs(FM["test_plane"]["total"]["Cl"])<1e-10
    assert abs(FM["test_plane"]["total"]["Cm"]+0.13544238029478695)<1e-10
    assert abs(FM["test_plane"]["total"]["Cn"])<1e-10


def test_swept_wing():
    # Tests the NLL algorithm correctly calculates a swept wing

    # Load input
    input_dict, aircraft_name, aircraft_dict, state, control_state = MX.helpers.parse_input(input_file)

    # Alter input
    input_dict["solver"]["type"] = "nonlinear"

    aircraft_dict["wings"]["main_wing"]["sweep"] = 30.0

    # Create scene
    scene = MX.Scene(input_dict)
    scene.add_aircraft(aircraft_name, aircraft_dict, state=state, control_state=control_state)
    FM = scene.solve_forces(non_dimensional=True)
    print(json.dumps(FM["test_plane"]["total"], indent=4))
    assert abs(FM["test_plane"]["total"]["FL"]-19.783804843985347)<1e-10
    assert abs(FM["test_plane"]["total"]["FD"]-1.3995975291276221)<1e-10
    assert abs(FM["test_plane"]["total"]["FS"])<1e-10
    assert abs(FM["test_plane"]["total"]["Fx"]+0.7083001002131478)<1e-10
    assert abs(FM["test_plane"]["total"]["Fy"])<1e-10
    assert abs(FM["test_plane"]["total"]["Fz"]+19.820598333967528)<1e-10
    assert abs(FM["test_plane"]["total"]["Mx"])<1e-10
    assert abs(FM["test_plane"]["total"]["My"]+30.13434354434114)<1e-10
    assert abs(FM["test_plane"]["total"]["Mz"])<1e-10


def test_swept_wing_with_controls():
    # Tests the NLL algorithm correctly calculates a swept wing

    # Load input
    input_dict, aircraft_name, aircraft_dict, state, control_state = MX.helpers.parse_input(input_file)

    # Alter input
    input_dict["solver"]["type"] = "nonlinear"

    aircraft_dict["wings"]["main_wing"]["sweep"] = 30.0
    aircraft_dict["wings"]["h_stab"]["sweep"] = 30.0

    control_state = {
        "elevator" : 5.0,
        "aileron" : 5.0,
        "rudder" : 5.0
    }

    # Create scene
    scene = MX.Scene(input_dict)
    scene.add_aircraft(aircraft_name, aircraft_dict, state=state, control_state=control_state)
    FM = scene.solve_forces(non_dimensional=True)
    print(json.dumps(FM["test_plane"]["total"], indent=4))
    assert abs(FM["test_plane"]["total"]["FL"]-32.445031339087635)<1e-10
    assert abs(FM["test_plane"]["total"]["FD"]-4.123299947318139)<1e-10
    assert abs(FM["test_plane"]["total"]["FS"]+4.4145932035790505)<1e-10
    assert abs(FM["test_plane"]["total"]["Fx"]+2.9884728801670395)<1e-10
    assert abs(FM["test_plane"]["total"]["Fy"]+4.4145932035790505)<1e-10
    assert abs(FM["test_plane"]["total"]["Fz"]+32.569167795546115)<1e-10
    assert abs(FM["test_plane"]["total"]["Mx"]+17.912175298121873)<1e-10
    assert abs(FM["test_plane"]["total"]["My"]+76.51336732249929)<1e-10
    assert abs(FM["test_plane"]["total"]["Mz"]-14.040324769001394)<1e-10


def test_tapered_wing():
    # Tests the NLL algorithm correctly calculates a swept wing

    # Load input
    input_dict, aircraft_name, aircraft_dict, state, control_state = MX.helpers.parse_input(input_file)

    # Alter input
    input_dict["solver"]["type"] = "nonlinear"

    aircraft_dict["wings"]["main_wing"]["chord"] = [[0.0, 1.0],[1.0, 0.5]]
    aircraft_dict["wings"]["main_wing"]["dihedral"] = 10.0

    # Create scene
    scene = MX.Scene(input_dict)
    scene.add_aircraft(aircraft_name, aircraft_dict, state=state, control_state=control_state)
    FM = scene.solve_forces(non_dimensional=True)
    print(json.dumps(FM["test_plane"]["total"], indent=4))
    assert abs(FM["test_plane"]["total"]["FL"]-17.722533099036767)<1e-10
    assert abs(FM["test_plane"]["total"]["FD"]-1.184375545596456)<1e-10
    assert abs(FM["test_plane"]["total"]["FS"])<1e-10
    assert abs(FM["test_plane"]["total"]["Fx"]+0.565146570565037)<1e-10
    assert abs(FM["test_plane"]["total"]["Fy"])<1e-10
    assert abs(FM["test_plane"]["total"]["Fz"]+17.753071121167718)<1e-10
    assert abs(FM["test_plane"]["total"]["Mx"])<1e-10
    assert abs(FM["test_plane"]["total"]["My"]+13.573362229826092)<1e-10
    assert abs(FM["test_plane"]["total"]["Mz"])<1e-10


def test_step_change_in_twist_wing():
    # Tests the NLL algorithm correctly calculates a wing with a step change in twist

    # Load input
    input_dict, aircraft_name, aircraft_dict, state, control_state = MX.helpers.parse_input(input_file)

    # Alter input
    input_dict["solver"]["type"] = "nonlinear"

    aircraft_dict["wings"]["main_wing"]["chord"] = [[0.0, 1.0],[1.0, 0.5]]
    aircraft_dict["wings"]["main_wing"]["dihedral"] = 10.0
    aircraft_dict["wings"]["main_wing"]["twist"] = [[0.0, 5.0],
                                                    [0.5, 5.0],
                                                    [0.5, 0.0],
                                                    [1.0, 0.0]]
    aircraft_dict["wings"]["main_wing"]["sweep"] = 30.0
    aircraft_dict["wings"]["main_wing"]["grid"]["N"] = 100

    # Create scene
    scene = MX.Scene(input_dict)
    scene.add_aircraft(aircraft_name, aircraft_dict, state=state, control_state=control_state)
    FM = scene.solve_forces(non_dimensional=True)
    print(json.dumps(FM["test_plane"]["total"], indent=4))
    assert abs(FM["test_plane"]["total"]["FL"]-28.36516174602864)<1e-10
    assert abs(FM["test_plane"]["total"]["FD"]-2.996305717918925)<1e-10
    assert abs(FM["test_plane"]["total"]["FS"])<1e-10
    assert abs(FM["test_plane"]["total"]["Fx"]+2.004550580611607)<1e-10
    assert abs(FM["test_plane"]["total"]["Fy"])<1e-10
    assert abs(FM["test_plane"]["total"]["Fz"]+28.452452017416174)<1e-10
    assert abs(FM["test_plane"]["total"]["Mx"])<1e-10
    assert abs(FM["test_plane"]["total"]["My"]+18.71714165086305)<1e-10
    assert abs(FM["test_plane"]["total"]["Mz"])<1e-10


def test_jackson_compare():
    # Tests that the circulation distribution for a swept wing matches Jackson's result (quickly becoming obsolete...)
    return # Yep; it's obsolete now.

    # Inputs
    input_dict = {
        "solver" : {
            "type" : "scipy_fsolve"
        },
        "scene" : {}
    }
    airplane_dict = {
        "weight" : 10,
        "airfoils" : {
            "NACA_0012" : {
                "CLa" : 6.907213339669221,
                "geometry" : {
                    "NACA" : "0012"
                }
            }
        },
        "wings" : {
            "main_wing" : {
                "ID" : 1,
                "side" : "both",
                "is_main" : True,
                "semispan" : 2.5,
                "chord" : 1.0,
                "airfoil" : "NACA_0012",
                "sweep" : 45.0,
                "ac_offset" : "kuchemann",
                "grid" : {
                    "N" : 20,
                    "reid_corrections" : True
                }
            }
        }
    }

    # Get results
    state = {
        "velocity" : 10.0,
        "alpha" : 10.0
    }
    scene = MX.Scene(input_dict)
    scene.add_aircraft("jackson_wing", airplane_dict, state=state)
    FM = scene.solve_forces(verbose=True, report_by_segment=True, non_dimensional=False)

    # Check circulation distribution
    correct_gamma = np.array([0.47123536, 1.36936314, 2.16971088, 2.78795243, 3.18301932, 3.41035458, 3.53474218, 3.59736899, 3.62115168, 3.61858063, 3.59673976, 3.56030944, 3.5136121,  3.46215726, 3.41358434, 3.37738807, 3.36088964, 3.35806733, 3.35540463, 3.353645,   3.353645,   3.35540463, 3.35806733, 3.36088964, 3.37738807, 3.41358434, 3.46215726, 3.5136121,  3.56030944, 3.59673976, 3.61858063, 3.62115168, 3.59736899, 3.53474218, 3.41035458, 3.18301932, 2.78795243, 2.16971088, 1.36936314, 0.47123536])
    assert np.allclose(scene._gamma, correct_gamma)


def test_swept_wing_with_aerodynamic_twist():
    # Tests for fix implemented 6/18/2021 based on a bug report from Julian Schmidt

    # Load input
    input_dict, aircraft_name, aircraft_dict, state, control_state = MX.helpers.parse_input(input_file)

    # Alter input
    input_dict["solver"]["type"] = "nonlinear"
    aircraft_dict["airfoils"] = {
        "root" : {
            "type" : "database",
            "input_file" : "test/NACA 2414.txt"
        },
        "tip" : {
            "type" : "database",
            "input_file" : "test/NACA 0012.txt"
        }
    }

    aircraft_dict["wings"]["main_wing"]["sweep"] = 20.0
    aircraft_dict["wings"]["main_wing"]["airfoil"] = [[0.0, "root"],
                                                      [1.0, "tip"]]
    aircraft_dict["wings"]["main_wing"]["grid"]["N"] = 100
    aircraft_dict["wings"].pop("h_stab")
    aircraft_dict["wings"].pop("v_stab")

    state['alpha'] = -1.5

    # Create scene
    scene = MX.Scene(input_dict)
    scene.add_aircraft(aircraft_name, aircraft_dict, state=state, control_state=control_state)
    FM = scene.solve_forces(non_dimensional=True, verbose=True)
    print(json.dumps(FM["test_plane"]["total"], indent=4))
    assert abs(FM["test_plane"]["total"]["FL"]+1.921431422738798)<1e-10
    assert abs(FM["test_plane"]["total"]["FD"]-0.6730156268500228)<1e-10
    assert abs(FM["test_plane"]["total"]["FS"])<1e-10
    assert abs(FM["test_plane"]["total"]["Fx"]+0.622487790173485)<1e-10
    assert abs(FM["test_plane"]["total"]["Fy"])<1e-10
    assert abs(FM["test_plane"]["total"]["Fz"]-1.9383904914534897)<1e-10
    assert abs(FM["test_plane"]["total"]["Mx"])<1e-10
    assert abs(FM["test_plane"]["total"]["My"]-0.41401938251627074)<1e-10
    assert abs(FM["test_plane"]["total"]["Mz"])<1e-10