import pickle

def load_game():
    saves = open("GAME_STATE_FILE.dat", 'rb')
    game_state = pickle.load(saves)
    saves.close()
    return game_state

def save_game(game_state):
    saves = open("GAME_STATE_FILE.dat", 'wb')
    pickle.dump(game_state, saves)
    saves.close()
    print('Pomyślnie zapisano grę!')

def lokacja():
    # pokazuje aktualną lokację użytkownika
    print('---------------------------')
    global currentRoom
    print('Twoja obecna lokacja ' + str(currentRoom))
    print("---------------------------")
