from pymongo import MongoClient
from dotenv import load_dotenv
import os


def uploadURLS():
    load_dotenv()

    username = os.getenv("MONGODB_USERNAME")
    password = os.getenv("MONGODB_PASSWORD")

    s = f"mongodb+srv://{username}:{password}@sfhacks25.ahebnig.mongodb.net/"

    client = MongoClient(s)

    db = client.sports  # Ensure this matches your actual database name
    players = db.players

    unblured_dict = {
        "LeBron James": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885184/tnpbriooycn0rfdnnwrl.jpg",
        "Stephen Curry": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885185/ty16yhhhbhkpgazbnadm.jpg",
        "Kevin Durant": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885186/yomkfwbopaw2pwnifeu3.jpg",
        "Giannis Antetokounmpo": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885187/fr5kciaattieq9inuu2u.jpg",
        "Nikola Jokic": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885187/qaro9p0io7x52akr2e1v.jpg",
        "Luka Doncic": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885188/ohfwifxxiawpg0jsbsqq.png",
        "Jayson Tatum": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885189/wi8xzq43p30zjxjgrlte.jpg",
        "Anthony Edwards": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885190/ny2tpgbveazrwfik7qe7.jpg",
        "Ja Morant": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885191/p7m8dvakskm4jamqgm4x.jpg",
        "Zion Williamson": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885192/gmhocfmthuig2faqcwij.jpg",
        "Devin Booker": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885193/ag45kawxjpvcyisqph7b.jpg",
        "Joel Embiid": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885195/mvjc4r6nmlikhn1jhbkx.png",
        "Damian Lillard": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885196/hvd04hknp7jxribgxhon.png",
        "Trae Young": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885197/bp2uymqxhxhyd8ajs9m0.png",
        "Chris Paul": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885198/rxti0egxh9smjfje5t5o.jpg",
        "Bradley Beal": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885199/w2a7xmaefjvpxb86dsfg.jpg",
        "Jamal Murray": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885199/k1lbvgdfb6zaejho305u.jpg",
        "Kyrie Irving": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885201/ajz8qrpjjhjxtmogx5nv.png",
        "Jrue Holiday": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885201/rhlc5veuiktdxnsiay1b.jpg",
        "Kristaps Porzingis": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885202/o55d3pn1k6dowjouokvk.png",
        "Rudy Gobert": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885202/br3pvj2tpedcbzlxfvsr.jpg",
        "Karl-Anthony Towns": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885203/ik1wf8avyw7tqjuyhvdz.png",
        "Brandon Ingram": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885204/g7fdfaz72bttvynizjve.png",
    }
    blured_dict = {
        "LeBron James": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885205/iyhrwtgvm12le4vopkck.png",
        "Stephen Curry": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885206/hkd0mbgt7ta4aw0netxq.png",
        "Kevin Durant": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885206/ktoikohhdkkfk9svndu6.png",
        "Giannis Antetokounmpo": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885207/td9x9yd1reub3zl9rjo6.jpg",
        "Nikola Jokic": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885208/tn877tj3skrr3vw8acx8.png",
        "Luka Doncic": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885208/de0ovmkbmoofxlyfya2b.jpg",
        "Jayson Tatum": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885209/gm2vij7cuklfe37itwsq.png",
        "Anthony Edwards": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885209/asm22dkcxpscqo4lhvhh.png",
        "Ja Morant": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885210/iq9n2pb1zm4efxkvrwmg.png",
        "Zion Williamson": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885211/y8e54nm4kw5uck7y0cwc.png",
        "Devin Booker": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885211/wshr9ay0m3xsawfn1mhu.png",
        "Joel Embiid": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885212/yxyrslrfgmfjrgpvyg8r.jpg",
        "Damian Lillard": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885212/s86xczlbak1t7iw3sw0s.jpg",
        "Trae Young": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885213/qyiv6pycvnjhtznrvldi.jpg",
        "Chris Paul": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885214/podw0py6wtg5lnrhqtqp.png",
        "Bradley Beal": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885214/qt2x4hzzwnlodpg87vsb.png",
        "Jamal Murray": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885215/crpjoywvsulmnubghj80.png",
        "Kyrie Irving": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885216/jamycl5i7mcxn4bfqp88.jpg",
        "Jrue Holiday": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885216/fw8rxdq1q7h9zlqyigzs.png",
        "Kristaps Porzingis": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885217/fjqix8a1zczhbydinxbd.jpg",
        "Rudy Gobert": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885217/ywv9vqacfsbltbwmsf5w.png",
        "Karl-Anthony Towns": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885218/s72ni7alb84xdwbjpvyc.jpg",
        "Brandon Ingram": "https://res.cloudinary.com/da0ekt7db/image/upload/v1743885219/nrn24xdvtzdwrovhshfd.jpg",
    }
    for name, url in unblured_dict.items():
        result = players.update_one(
            {"name": name},  # Match based on the name
            {"$set": {"unblured_img": url}},  # Update the URL field
        )
        if result.modified_count > 0:
            print(f"Successfully updated {name}'s URL.")
        else:
            print(f"No document found for {name} or URL already up-to-date.")

    for name, url in blured_dict.items():
        result = players.update_one(
            {"name": name},  # Match based on the name
            {"$set": {"blured_img": url}},  # Update the URL field
        )
        if result.modified_count > 0:
            print(f"Successfully updated {name}'s URL.")
        else:
            print(f"No document found for {name} or URL already up-to-date.")


uploadURLS()
