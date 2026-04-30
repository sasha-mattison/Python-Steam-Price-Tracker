import scraper
import emailer

def main():
    game_data = scraper.get_wishlist_attributes()
    discounted_games = []

    for game in game_data:
        for key, value in game.items():
            if key == "discount_pct":
                discounted_games.append(game)

    for game in discounted_games:
        emailer.send_email(game["name"] + "is on sale", get_formatted_game_info(game))
    print("Exited Succesfully")


def get_formatted_game_info(game):
    final = ""
    for key, value in game.items():
        final = final + (f"{key}: {value}\n")
        
    return final.replace("_", " ")

main()
