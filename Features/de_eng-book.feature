# language:de
Funktionalität: Checking and editing books in database
  @mocked
  Szenario: Getting all the books
    Gegeben sei we have a mocked database
    Wenn books are to be retrieved
    Dann we can return all the books

  Szenariogrundriss: Returning author's second name
    Gegeben sei we have a mocked db with mocked method returning <book>
    Wenn we have id equal to <id>
    Dann returned second name should be equal to <surname>

    Beispiele:
   | book   | id               | surname                |
   | {"title": "title1", "author": {"name": "name1", "email": "abc124@onet.pl", "surname":"wozniak"}, "isbn": "1534554554"}   | 0  | wozniak |
   | {"title": "title2", "author": {"name": "name2", "email": "abc124@onet.pl", "surname":"hej"}, "isbn": "1423423243"}   | 1 | hej |