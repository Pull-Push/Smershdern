from whiskeywheel.models import PersonClass
new_person = PersonClass()
new_person.first = "Luigi"
new_person.last = "Mario"

new_person.save()

test_dict = {}

test_dict["FIRST"] = new_person.first
test_dict['LAST'] = new_person.last

print(test_dict['FIRST'])
print(test_dict['LAST'])