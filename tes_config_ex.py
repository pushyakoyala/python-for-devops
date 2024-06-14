def update_config(file, key, value):
    with open(file, "r") as files:
        lines = files.readlines()
    with open(file, "w") as files:
        for line in lines:
            if key in line:
                files.write(key + " = " + value + "\n")

            else:
                files.write(line)

update_config("server.conf", "PORT" ,"9090")

