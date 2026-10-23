from pyscript import document

def candidate_checker(e):
    club_members = ["Andrey Santos","Cyra Cheang","Heather Son","Michael Barrameda","Mikaela Lindaya","Sage Aguinaldo","Warblebee Warblebee"]

    f_name = document.getElementById('first name').value
    l_name = document.getElementById('last name').value
    candidate = f_name + ' ' + l_name
    member_checker = candidate.title() in club_members

    messages = (f 'Sorry {candidate}, your name is not on the current club roster'),(f 'Congratulations {candidate}, you are a member of the Social Sciences Club')

    document.getElementById('result').innerHTML = messages[member_checker]
