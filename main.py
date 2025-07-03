from cake_repo.cakes_db import CakesDatabase

def main():
    db = CakesDatabase('cakes.db')       # 1. Otvori (ili napravi) bazu
    db.create_table()                   # 2. Napravi tablicu meals ako ne postoji
    db.add_meal('Čokoladna torta', 350, 3.5)
    print('Dodano jelo u bazu!')        # 3. Samo potvrda korisniku
    
    meals = db.get_all_meals()
    print('Sva jela u bazi:')
    for meal in meals:
        print(meal)
    
if __name__ == '__main__':
    main()