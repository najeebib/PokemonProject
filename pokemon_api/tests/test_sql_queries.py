import utils.sql_queries as fns
from data.database import get_db
import utils.get_queries as select_fns
import utils.delete_queries as delete_fns
import utils.insert_queries as insert_fns

class TestRequest:
    def setup_method(self):
        db_generator = get_db()
        self.db = next(db_generator)

    def test_is_type_in_table(self):
        """
        Test the functionality of the `is_type_in_table` function from the `fns` module.

        Parameters:
        - self: The instance of the test class.
        """
        assert fns.is_type_in_table(self.db, "dasfv") == False

    def test_is_pokemon_in_table(self):
        """
        Test the functionality of the `is_pokemon_in_table` function from the `fns` module.

        Parameters:
        - self: The instance of the test class.
        """
        assert fns.is_pokemon_in_table(self.db, "dasfv") == False
    
    def test_is_trainer_in_table(self):
        """
        Test the functionality of the is_trainer_in_table function.
        
        Parameters:
            self (TestRequest): The instance of the test class.
        """
        assert fns.is_trainer_in_table(self.db, "dasfv") == False

    def test_insert_delete_pokemon(self):
        """
        Test the functionality of inserting and deleting a pokemon from the pokemons table.

        Parameters:
        - self: The instance of the test class.
        """
        insert_fns.insert_into_pokemons_table(self.db, "test", 1, 1)

        assert fns.is_pokemon_in_table(self.db, "test") == True

        delete_fns.delete_from_pokemons(self.db, "test")

        assert fns.is_pokemon_in_table(self.db, "test") == False

    def test_insert_delete_type(self):
        """
        Test the functionality of inserting and deleting a type from the types table.

        Parameters:
        - self: The instance of the test class.
        """
        insert_fns.insert_into_types_table(self.db, ["aa"])

        assert fns.is_type_in_table(self.db, "aa") == True

        delete_fns.delete_from_types(self.db, "aa")

        assert fns.is_type_in_table(self.db, "aa") == False

    def test_insert_delete_trainer(self):
        """
        Test the functionality of inserting and deleting a trainer from the trainers table.

        Parameters:
        - self: The instance of the test class.
        """

        assert fns.is_trainer_in_table(self.db, "test") == True

        delete_fns.delete_from_trainer(self.db, "test")

        assert fns.is_trainer_in_table(self.db, "test")== False

    def test_insert_delete_pokedex(self):
        """
        Test the functionality of inserting and deleting a pokedex from the pokedex table.

        Parameters:
        - self: The instance of the test class.
        """
        insert_fns.insert_into_pokemons_table(self.db, "test", 1,1)
        insert_fns.insert_into_trainers_table(self.db, "test", "a")
        pokemon = select_fns.select_pokemon(self.db, "test")
        trainer = select_fns.select_trainer(self.db, "test")
        insert_fns.insert_into_Pokedex_table(self.db, pokemon.pokemon_id, trainer.trainer_id)

        assert fns.is_in_pokedex(self.db, pokemon.pokemon_id, trainer.trainer_id) == True

        delete_fns.delete_from_pokedex(self.db, pokemon.pokemon_id, trainer.trainer_id)

        assert fns.is_in_pokedex(self.db, pokemon.pokemon_id, trainer.trainer_id) == False

    def test_insert_delete_pokemontype(self):
        """
        Test the functionality of inserting and deleting a pokemontype from the pokemontypes table.

        Parameters:
        - self: The instance of the test class.
        """
        insert_fns.insert_into_pokemons_table(self.db, "test15", 1,1)
        insert_fns.insert_into_types_table(self.db, ["test15"])
        pokemon = select_fns.select_pokemon(self.db, "test15")
        type_obj = select_fns.select_type(self.db, "test15")
        insert_fns.insert_into_PokemonTypes_table(self.db, pokemon.pokemon_id, type_obj.types_id)

        assert fns.is_in_pokemontype(self.db, pokemon.pokemon_id, type_obj.types_id) == True

        delete_fns.delete_from_pokemontypes(self.db, pokemon.pokemon_id, type_obj.types_id)

        assert fns.is_in_pokemontype(self.db, pokemon.pokemon_id, type_obj.types_id) == False