"""
Create a skill damage calculator
Skill name: Distortion
Basic Damage: 225
Bonus damage based on Ability Power: 60% of AP
"""

def distortion(AP):
    calc_damage = int(AP) * 0.6 + 225
    print(calc_damage)

distortion(102)