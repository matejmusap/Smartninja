birthdays = {}
add_person = int(raw_input("How many persons you wanna add?)"))
for x in range(add_person):
    person = raw_input("Name and surname of person:")
    birthday = raw_input("Write bitthday: ")
    birthdays[person] = birthday
print birthdays
wanted = raw_input("Who's birthday you wanna look?")
wanted_birth = birthdays.get(wanted)
print "%s birthday is %s" % (wanted, wanted_birth)

# Anthony Bourdain
# 25 June 1956
#
# Mohamed Salah
# 15 June 1992
#
# Bruce Lee
# 27 November 1940
#
# Sharon Tate
# 24 January 1943