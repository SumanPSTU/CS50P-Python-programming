class Demo:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_data(self):
        return f"{self.name} and {self.email}"

def main():
    demo = Demo("sumon", "swadin@gmail.com")
    print(demo.get_data())

if __name__ == "__main__":
    main()