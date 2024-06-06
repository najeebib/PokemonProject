import utils.get_functions as get_functions
import utils.delete_functions as delete_functions
import utils.insert_functions as insert_functions
import utils.update_functions as update_functions

def test_is_pokemon_in_table():
    """
    Test the functionality of the `is_pokemon_in_table` function from the `fns` module.

    Parameters:
    - self: The instance of the test class.
    """
    assert get_functions.get_pokemon("dasda") == None

def test_is_trainer_in_table():
    """
    Test the functionality of the is_trainer_in_table function.
    
    Parameters:
        self (TestRequest): The instance of the test class.
    """
    assert get_functions.get_trainer_by_name("Dasdav")  == None

def test_insert_delete_pokemon():
    """
    Test the functionality of inserting and deleting a pokemon from the pokemons table.

    Parameters:
    - self: The instance of the test class.
    """
    insert_functions.insert_pokemon({"name": "test", "types": ["test"], "weight": 1, "height": 1})
    poke = get_functions.get_pokemon("test")
    assert poke != None

    delete_functions.delete_pokemon(poke["_id"])

    poke = get_functions.get_pokemon("test")
    assert poke == None


def test_insert_delete_trainer():
    """
    Test the functionality of inserting and deleting a trainer from the trainers table.

    Parameters:
    - self: The instance of the test class.
    """
    insert_functions.insert_trainer({"name": "test", "town": "adsda"})
    trainer = get_functions.get_trainer_by_name("test")
    assert trainer != None

    delete_functions.delete_trainer(trainer["_id"])
    trainer = get_functions.get_trainer_by_name("test")
    assert trainer == None

def test_get_pokemons_by_type():
    get_functions.get_pokemons_by_type("dasdasd") == []
    get_functions.get_pokemons_by_type("grass") != []

def test_get_pokemons_by_trainer():
    trainer = get_functions.get_trainer_by_name("Tierno")
    assert get_functions.get_pokemons_by_trainer(trainer["_id"]) != []