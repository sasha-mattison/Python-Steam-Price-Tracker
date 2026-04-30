import get_wishlist_attributes
import send_email

def main():
    game_data = get_wishlist_attributes.get_wishlist_attributes()
    discounted_games = []

    for game in game_data:
        for key, value in game.items():
            if key == "discount_pct":
                discounted_games.append(game)

    for game in discounted_games:
        send_email.send_email(game["name"] + "is on sale", get_formatted_game_info(game))

def get_formatted_game_info(game):
    final = ""
    for key, value in game.items():
        final = final + (f"{key}: {value}\n")
        
    return final.replace("_", " ")


main()