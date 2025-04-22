def get_movie_ticket_price(seat_num):
    seats = []
    for x in range(seat_num):
        if x < 20:
            seats.append(10)
        elif x < 40:
            seats.append(12)
        elif x < 60:
            seats.append(13)
        elif x < 80:
            seats.append(16)
        else:
            seats.append(20)

    return seats


def main():
    seat_num = 100

    for number in get_movie_ticket_price(seat_num):
        print(number, end = ", ")
        


if __name__ == "__main__":
    main()