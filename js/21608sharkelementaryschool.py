classroom_size = int(input())
seats = [[0] * classroom_size for _ in range(classroom_size)]
favorite_friends = {}

for _ in range(classroom_size**2):
    line = list(map(int, input().split(" ")))
    favorite_friends[line[0]] = line[1:]

seated = {}
points = 0

dir_c = [0, -1, 1, 0]
dir_r = [-1, 0, 0, 1]
DIRECTION_SIZE = 4
satisfaction_points = [0, 1, 10, 100, 1000]

def is_bound(new_r, new_c):
    return 0 <= new_r < classroom_size and 0 <= new_c < classroom_size

def find_near_possible_seats(seat):
    possible_seats = []
    for i in range(DIRECTION_SIZE):
        new_r = seat[0] + dir_r[i]
        new_c = seat[1] + dir_c[i]
        if is_bound(new_r, new_c) and seats[new_r][new_c] == 0:
            possible_seats.append([new_r, new_c])
    return possible_seats

def count_my_friends_near_seat(seat, me):
    my_fav_friends = favorite_friends[me]
    friend_count = 0
    for i in range(DIRECTION_SIZE):
        new_r = seat[0] + dir_r[i]
        new_c = seat[1] + dir_c[i]
        if is_bound(new_r, new_c) and seats[new_r][new_c] in my_fav_friends:
            friend_count += 1
    return friend_count

def is_smaller_than(seat, other_seat):
    r, c = seat
    rr, cc = other_seat
    if r < rr or (r == rr and c < cc):
        return True
    return False

def get_my_best_seat(me):
    my_fav_friends = favorite_friends[me]
    if not my_fav_friends:
        return None
    best_friend_count = 0
    best_seat = [-1, -1]
    best_near_empty_count = 0
    for friend in my_fav_friends:
        if seated.get(friend):
            r, c = seated[friend]
            possible_seats = find_near_possible_seats([r, c])
            for seat in possible_seats:
                friend_count = count_my_friends_near_seat(seat, me)
                if friend_count > best_friend_count:
                    best_friend_count = friend_count
                    best_seat = seat
                    best_near_empty_count = len(find_near_possible_seats(seat))
                elif friend_count == best_friend_count:
                    friend_count_empty_seats = len(find_near_possible_seats(seat))
                    best_friend_count_empty_seats = len(find_near_possible_seats(best_seat))
                    if friend_count_empty_seats > best_friend_count_empty_seats:
                        if friend_count_empty_seats > best_near_empty_count:
                            best_seat = seat
                            best_near_empty_count = friend_count_empty_seats
                    elif friend_count_empty_seats == best_near_empty_count:
                        if is_smaller_than(seat, best_seat):
                            best_seat = seat
    return best_seat

def get_any_empty_seat():
    best_seat = [-1, -1]
    near_empty_best_count = -1
    for i in range(classroom_size):
        for j in range(classroom_size):
            if seats[i][j] == 0:
                near_empty_count = len(find_near_possible_seats([i, j]))
                if near_empty_count == 4:
                    return [i, j]
                if near_empty_count > near_empty_best_count:
                    near_empty_best_count = near_empty_count
                    best_seat = [i, j]
    return best_seat

def count_satisfaction_points():
    global points
    for i in range(classroom_size):
        for j in range(classroom_size):
            friend_count = 0
            me = seats[i][j]
            my_fav_friends = favorite_friends[me]
            for d in range(DIRECTION_SIZE):
                new_i = i + dir_r[d]
                new_j = j + dir_c[d]
                if is_bound(new_i, new_j):
                    checking_friend = seats[new_i][new_j]
                    if checking_friend in my_fav_friends:
                        friend_count += 1
            points += satisfaction_points[friend_count]
    print(points)
    return points

def solve():
    for person in range(1, classroom_size * classroom_size + 1):
        print(person)
        person_seat = get_my_best_seat(person)
        if person_seat is None or person_seat == [-1, -1]:
            person_seat = get_any_empty_seat()
        seated[person] = person_seat
        i, j = person_seat
        seats[i][j] = person
    count_satisfaction_points()
    return

solve()
