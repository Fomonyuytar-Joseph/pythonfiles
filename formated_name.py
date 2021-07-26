#optional arguements


def get_formated_name(first_name,last_name,middle_name=' '):
    #return full name fuly formatted
    if middle_name:
      full_name=first_name+ ' '+middle_name+ ' '+ last_name
    else:   
      full_name=first_name+ ' '+ last_name
    return full_name.title()

student=get_formated_name('fomonyuytar','joseph')
musician = get_formated_name('john', 'hooker', 'lee')
print(musician)
print(student)
