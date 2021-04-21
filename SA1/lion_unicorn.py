# Lucy Langenberg
# program that counts from 1 to 20;
# if odd, prints Lion, if even, prints Unicorn

count = 1

while count <= 20:
    if count%2 == 0:
        print(str(count) + " Unicorn")
    else:
        print(str(count) + " Lion")

    count = count + 1