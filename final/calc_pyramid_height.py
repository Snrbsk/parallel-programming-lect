num_of_blocks = int(input("Lütfen bir sayı giriniz")) 

def pyramid_first_last(num_of_blocks):
    total= 0
    height = 0
    add_block = 0
    while True:
        if total < num_of_blocks:
            add_block += 1
            total += add_block
            height += 1
        else:
            break
    print(height)
    return height

pyramid_first_last(num_of_blocks)