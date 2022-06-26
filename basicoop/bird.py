class Bird: 
    global bird_type
    bird_type = "parrot" 
    bird_name = "Lori" 

    def __init__(self,color) -> None: 
        self.color = color
        name = "Peter"
        print(f'{name} in init')

if __name__ == '__main__':
    my_bird = Bird('Green,Blue')

    print(my_bird.color) #ชื่อวัตถุ

    print(Bird.bird_name) #ชื่อคาส

    print(bird_type) #ตัวแปร


