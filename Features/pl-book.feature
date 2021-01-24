# language: pl
Właściwość: Sprawdzanie zachowania struktury danych book
  @mocked
  Scenariusz: Poprawnie zwracana książka
    Zakładając że mamy atrapę bazy
    Jeżeli podajemy id
    Wtedy otrzymujemy książkę


  Szablon scenariusza: Chcemy tytuł książki
    Zakładając że mamy atrapę bazy zwracającą <book>
    Jeżeli podajemy <id>
    Wtedy zwrócony tytuł książki powinien być <title>

    Przykłady:
      | book | id | title |
      |{"title": "Ja, Ibra", "author": {"name": "Zlatan", "surname": "Ibrahimovic", "email":"abc123@onet.pl"}, "ISBN": "3-221-3333-1332-0"} | 0 | Ja, Ibra |
      |{"title": "Pan Tadeusz", "author": {"name": "Bonzo", "surname": "Uzumaki", "email":"abc124@onet.pl"}, "ISBN": "3-221-3333-1442-0"} | 1 | Pan Tadeusz |