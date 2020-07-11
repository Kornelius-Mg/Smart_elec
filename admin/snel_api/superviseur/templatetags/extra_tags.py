from django import template

register = template.Library()

@register.filter(name="exists")
def exists_variable(variable):
    try:
        id = id(variable)
    except:
        return False
    else:
        return True
