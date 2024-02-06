import pytest
from assignment0.main import createdb, connectdb, deletedb, print_status

@pytest.mark.parametrize("expected_output", [
    ("""Traffic Stop|39
Transfer/Interfacility|36
Disturbance/Domestic|23
Sick Person|22
Alarm|12
Welfare Check|10
Check Area|9
Contact a Subject|9
Follow Up|9
MVA With Injuries|8
Supplement Report|7
Unconscious/Fainting|7
Breathing Problems|6
Chest Pain|6
Hemorrhage/Lacerations|6
Traumatic Injury|6
Falls|5
Fraud|5
Harassment / Threats Report|5
Parking Problem|5
Public Assist|5
Trespassing|5
Animal at Large|4
Fire Alarm|4
Hit and Run|4
Larceny|4
Motorist Assist|4
Open Door/Premises Check|4
Suspicious|4
Unknown Problem/Man Down|4
COP Relationships|3
MVA Non Injury|3
Missing Person|3
Warrant Service|3
Abdominal Pains/Problems|2
Alarm Holdup/Panic|2
Animal Trapped|2
Cardiac Respritory Arrest|2
Escort/Transport|2
Found Item|2
Heart Problems/AICD|2
Mutual Aid|2
Noise Complaint|2
Officer Needed Nature Unk|2
Overdose/Poisoning|2
Reckless Driving|2
Road Rage|2
Stolen Vehicle|2
Vandalism|2
911 Call Nature Unknown|1
Animal Complaint|1
Animal Vicious|1
Assault|1
Assist Fire|1
COP DDACTS|1
Civil Standby|1
Drug Violation|1
Extra Patrol|1
Fire Carbon Monoxide Alarm|1
Fire Grass|1
Foot Patrol|1
Kidnapping|1
Runaway or Lost Child|1
Stake Out|1
Test Call|1
""")
])

def test_print_status(expected_output):
    final_str = print_status()
    # captured = capfd.readouterr()
    print("******", final_str, "____________", expected_output)
    assert final_str == expected_output
    # Add assertions based on your specific requirements
