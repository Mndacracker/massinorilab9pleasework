'''
library for interacting with the PokeAPi.
https://pokeapi.co/
'''
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_into{} function
    # use breakpoints to view returned dictionary 
    poke_info = get_pokemon_info("Rockruff")
    poke_info = get_pokemon_info(123)
    
    return

def get_pokemon_info(pokemon_name):
    
    pokemon_name = str(pokemon_name).strip().lower()

    url = POKE_API_URL + pokemon_name

    print ('\n,',f'Finding the pokemon to patch the name {pokemon_name}..','\n', end='')
    resp_msg = requests.get(url)

    if resp_msg.status_code == requests.codes.ok:
        print('\n','It has been patched', '\n')
        return resp_msg.json()
    else:
        print('\n','No data has been approached', '\n')
        print('\n',f'Code Error : {resp_msg.status_code}, Reasoning for Error : {resp_msg.reason}', '\n')


if __name__ == '__main__':
    main()