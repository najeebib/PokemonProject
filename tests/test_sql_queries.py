import utils.sql_queries as fns
from data.database import get_db

class TestRequest:
    def setup_method(self):
        db_generator = get_db()
        self.db = next(db_generator)

    def test_is_type_in_table(self):
        assert fns.is_type_in_table(self.db, "grass") == True
        assert fns.is_type_in_table(self.db, "dasfv") == False

    def test_is_pokemon_in_table(self):
        assert fns.is_pokemon_in_table(self.db, "bulbasaur") == True
        assert fns.is_pokemon_in_table(self.db, "dasfv") == False
    
    def test_is_trainer_in_table(self):
        assert fns.is_trainer_in_table(self.db, "Tierno") == True
        assert fns.is_trainer_in_table(self.db, "dasfv") == False

    def test_insert_delete_pokemon(self):
        fns.insert_into_pokemons_table(self.db, "test", 1, 1)

        assert fns.is_pokemon_in_table(self.db, "test") == True

        # delete pokemon

        #assert fns.is_pokemon_in_table(self.db, "test") == False

    def test_insert_delete_type(self):
        fns.insert_into_types_table(self.db, ["aa"])

        assert fns.is_type_in_table(self.db, "aa") == True

        # delete type

        #assert fns.is_type_in_table(self.db, "aa") == False

    def test_insert_delete_trainer(self):
        fns.insert_into_trainers_table(self.db, "test", "a")

        assert fns.is_trainer_in_table(self.db, "test") == True

        # delete trainer

        #assert fns.is_trainer_in_table(self.db, "test") == False
    def test_insert_delete_pokedex(self):
        fns.insert_into_Pokedex_table(self.db, "test", "test")

        assert fns.is_in_pokedex(self.db, "test", "test") == True

        # delete from pokedex

        #assert fns.is_in_pokedex(self.db, "test", "test") == False

    def test_insert_delete_pokemontype(self):
        fns.insert_into_PokemonTypes_table(self.db, "test", "a")

        assert fns.is_in_pokemontype(self.db, "test", "a") == True

        # delete fdrom pokemontype

        #assert fns.is_in_pokemontype(self.db, "test", "a") == False