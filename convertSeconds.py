def convert_seconds(seconds):
    hours = seconds //3600 #double slash "//" returns as an integer not a double, for example : 5//2 = 2, instead of 2.5
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    print(hours, minutes, seconds)


convert_seconds(10000)
