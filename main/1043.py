import sys

input = sys.stdin.readline


def main():
    people, party = map(int, input().split())
    party_peoples = []
    num_party_people = []
    avoid = []
    check = []
    count = 0

    witness = list(map(int, input().split()))
    fact = witness[0]
    witness.remove(witness[0])
    if fact == 0:
        return party
    if fact != 0:
        avoid.extend(witness)

    for i in range(party):
        party_people = list(map(int, input().split()))
        num_party_people.append(party_people[0])
        party_people.remove(party_people[0])
        party_peoples.append(party_people)
    i = 0
    # print(party)
    while i < party:
        flag = False
        if i in check:
            # print("AA")
            i += 1
            continue
        # print("check, avoid", check, avoid)
        j = 0
        while j < len(avoid):
            # print("i", i, ",j", j, "call", party_peoples[j])
            j += 1
            if avoid[j - 1] in party_peoples[i]:
                # print("!!", party_peoples[i])
                avoid.extend(party_peoples[i])
                avoid = list(set(avoid))
                # print(avoid)
                check.append(i)
                # print("check",check)
                i = 0
                flag = True
                break
        if not flag:
            i+=1
        # i += 1
    # print(avoid)
    for i in range(party):
        temp = 0

        for j in range(len(avoid)):
            if avoid[j] in party_peoples[i]:
                break
            else:
                temp += 1
        if temp == len(avoid):
            count += 1

    return count


print(main())
