from pyscript import display, document


def intrams_team(e):
    document.getElementById('output').innerHTML = " "
    register = float(document.getElementById('register').value)
    clearance = float(document.getElementById('clearance').value)
    grade = float(document.getElementById('level').value)
    section = float(document.getElementById('section').value)

    if register == 1 and clearance == 1 and section == 3:
        display(f'Congratulations! You are part of the Green Hornets.', target='output')
    elif register == 1 and clearance == 1 and section == 2:
        display(f'Congratulations! You are part of the Blue Bears.', target='output')
    elif register == 1 and clearance == 1 and section == 1:
        display(f'Congratulations! You are part of the Yellow Tigers.', target='output')
    elif register == 1 and clearance == 1 and section == 4:
        display(f'Congratulations! You are part of the Red Bulldogs.', target='output')
    elif register == 1 and clearance == 2:
        display(f'Before proceeding to check your team, please apply for medical clearance first.', target='output')
    elif register == 2 and clearance == 1:
        display(f'Before proceeding to check your team, please register first.', target='output')
    elif register == 2 and clearance == 2:
        display(f'Before proceeding to check your team, please register and apply for medical clearance first.', target='output')
    else:
        display(f'Please answer the questions!', target='output')