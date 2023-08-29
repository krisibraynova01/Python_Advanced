n_guests = int(input())
reservations = set()
guest_come_to_party = set()

for _ in range(n_guests):
    reservation_code = input()
    reservations.add(reservation_code)


while True:
    line = input()
    if line == 'END':
        break
    guest_come_to_party.add(line)

reservations -= guest_come_to_party
sorted_reservations = sorted(reservations)
print(len(reservations))
[print(person) for person in sorted_reservations]






