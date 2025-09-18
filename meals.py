print("Goodness, not you again fatty. Go read the time yourself or not, im getting tired of you coming here every damn time just because you are to lazy to read an analog clock. But its not my job to criticize. So,")

def main():
    # Get time from user
    time = input("What time is it?")
    # Convert function thingy
    yummer = convert(time)
    # I cant believe somewhere somehow some needs this
    if yummer >= 7 and yummer <= 8:
        print("Breakfast time Big boy")

    elif yummer >= 1 and yummer <= 6:
        print("HOW ARE YOU UP THIS EARLY??")

    elif yummer >= 9 and yummer<= 11:
        print("You can wait a few hours cant you big boy?")

    elif yummer >= 14 and yummer <= 17:
        print("Do some excercise, itll do you good while you wait fatty")

    elif yummer >= 20 and yummer <= 24:
        print("I am tired of you fatty. Go read the time yourself, im getting tired of you coming here every damn time just because you are to lazy to read an analog clock.")

    elif yummer >= 12 and yummer <= 13:
        print("Lunch time Fatty")

    elif yummer >= 18 and yummer <= 19:
        print("Dinner time Bigback")


def convert(time):
    if time.startswith("12") and time.endswith("a.m"):
        time = time.strip("a.m")
        hours, minutes = time.split(":")
        hours = hours.replace("12", "00")
        hours = float(hours)
        minutes = float(minutes) / 60
        return hours + minutes
    elif time.startswith("12") and time.endswith("p.m"):
        time = time.strip("p.m")
        hours, minutes = time.strip().split(":")
        hours = float(hours)
        minutes = float(minutes) / 60
        return hours + minutes
    elif time.endswith("a.m"):
        time = time.strip("a.m")
        hours, minutes = time.strip().split(":")
        hours = float(hours)
        minutes = float(minutes) / 60
        return hours + minutes
    elif time.endswith("p.m"):
        time = time.strip("p.m")
        hours, minutes = time.split(":")
        hours = float(hours) + 12
        minutes = float(minutes) / 60
        return hours + minutes
    else:
        hours, minutes = time.strip().split(":")
        hours = float(hours)
        minutes = float(minutes) / 60
        return hours + minutes


if __name__ == "__main__":
    main()
