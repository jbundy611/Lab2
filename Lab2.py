class Author:
    #initializes the author and their list of books
    def __init__(self, name):
        self.name = name
        self.List_of_Books = []
    
    #creates the way to add books
    def publish(self, title):
        if title in self.List_of_Books:
            print("ERROR. Already Published! no duplicates.")
        else:
            self.List_of_Books.append(title)
    
    #combines the author and their books
    def __str__(self):
        titles= ', '.join(self.List_of_Books) or'No books.'
        return f'{self.name}. Books: {titles}'

def main():

    Winters = Author('Ben H. Winters')
    Winters.publish('The Last Policeman')
    Winters.publish('World of Trouble')
    Winters.publish('Countdown City')
    Winters.publish('Countdown City')
    print(Winters)

    Anon = Author('Anon')
    print(Anon)

main()