import pokemonuniversum as pk
import os
import random
import time
global pokedex
pokedex=''
def welcome():
    print(
    """
                                   .:-::.                                                      
                                :=--::::.                                                      
                             :+:::::::-=                                                       
                          .-=::::::::-=                                                        
                       .-=:::::::::-=-                                                         
                     .-------------=.            .::.                                          
                   .==-----------=-.        .--:::::+.                                         
                 .==-----------=+..:=+-:::::::::::::-*                                         
               .-+-------=====+:-=::::::::::::::-::---.                                        
             .-=------=--::::--::::::::::::::::::-----:                                        
            :==-------=:::::::::::::::::::---::-:::----                                        
           ==--------=*-:::::::::::::::::-:::--:::-::--:.                                      
         :+=---====:  .:-::::::::::::::::--:--+#+--:::---.                                     
       .-=====-.       :-:::::::::::::::------=.:#=-::::+.                                     
      .===+-.          .--:::==::-::::::::=-=:=**##--:--+.                                     
     -===-.            :-::-=:=----::::::::-=..%+++=-::-:.                                     
    -===.              --:--..*-#--:::::::---...#+=--:--.        ...:-=###*=========--=*+:.    
  .-===                ---:--.-**+---::::::---:+::-----..::-=#*===++====+**=:......  .==--==+-.
 .-==-                 .-----:.=*+-:::::--:::------+#-++==++==+=.                          :==:
 :==-                   .:=:::-----::::::::-::-=+===+*+-=:...                              .-=-
.==-.                      .:=-:::::::::::::--==---------------::=:                       .-=+:
:=-:                             .=--::---:-==--------:::::::::::::.                      *==: 
-==.                       .:-*==+==*#+==*=--------------::::::--+.                    .====-  
.+==.                ..--=*=+=-+. .:=------+------------=.                           .-====.   
 .===+-=+*+++****=--++=++:-.    .+-::-----=*+:::::::::::--:                        .=====:     
    ...+%%*+++#%%%#:..         :-::---*...  .::::::::::::::--                    .====+.       
                                -+=:        .::::::::::::::::=-.               .*===+          
                                           ..:::::::::--:::::::-+:.         .=+==+:            
                                           .:::::::::::--::--:::---:.    .=++=+=.              
                                           .=:::::::::::::::--::::--+++=++++=:.                
                                           -=::::::::::::::::::::::-:*+=+*..                   
                                          .=-:::::::::::-::::::::::-:-*=.                      
                                          +--:::::::::::--::::::::::::-.                       
                                          *::::::::::::::---:::::::::--:                       
                                          #::--::::::::::--=-:::::----=-                       
                                         .#*::--:::::::-----=+=--------=-.                     
                                         .%==-::=------------==*#**#=---=:                     
                                          #===+==+++--======+-.    .=----+.                    
                                          -=======     ...          ------+.                   
                                          .*==----:                  +-----=.                  
                                           =-------.                 =--:::--.                 
                                           :=------=.                .-:::::-:                 
                                           .--------=.               .=::::::-:                
                                            :--::::::+.              .:-::::::=.               
                                             --:::::-::               :-:::::::+.              
                                              =::::::=:               :-::::::::-              
                                               .==--==.               :-::::::::-:             
                                                 .--.                 .::::::::::=.            
                                                                       ::-::::-::-.            
                                                                       :::-::::=:-.            
                                                                        :=--:::+=-             
                                                                          :=+===.              
    """
    )
    print("Loading...")
    for i in range(81):

            progress = "█" * i
            empty = "░" * (80 - i)

            print(
                f"\r[{progress}{empty}] {i * (5/4)}%                  ",
                end="",
                flush=True
            )

            time.sleep(0.01)
    os.system("cls")
def find_available_boosterpacks():
    booster_packs = []
    for file in os.listdir("."):
        if file.endswith(".bstp"):
            booster_packs.append(file)
    return booster_packs
def find_available_badges():
    av_badges = []
    for file in os.listdir("."):
        if file.endswith(".bdg"):
            av_badges.append(file)
    return av_badges
def find_available_pokedex():
    pokedexe=[]
    for file in os.listdir("."):
        if file.endswith(".dex"):
            pokedexe.append(file)
    return pokedexe
def main():
    os.system("color 07")
    global pokedex
    os.system('cls')  # Clear the console
    if pokedex=='':
        print("Available PokeDex':")
        pokedexe=find_available_pokedex()
        for i, pack in enumerate(pokedexe):
            print(f"{i + 1}. {pack}")
        while True:
            io=input("Select your PokeDex (n to create a new PokeDex): ")
            if io=="n":
                newname=input("Name: ")
                pokedex=pk.PokeDex(newname)
                pokedex.save()
            else:
                pokedex=pk.PokeDex(pokedexe[int(io)-1])
            break
    os.system('cls')
    print("\nAvailable booster packs:")
    booster_packs = find_available_boosterpacks()
    for i, pack in enumerate(booster_packs):
        print(f"{i + 1}. {pack}")
    print("\nv - View all cards in the PokeDex without efects")
    print("vc - View all cards in the PokeDex with efects")
    print("va - View all cards in the PokeDex at once")
    print("vchase - View your chase-card")
    print("vfav - View favourites")
    print("c - Change selected PokeDex")
    print("reset - Resets the PokeDex")
    
    print("search - Search Pokemon(s) with a keyword")
    print("s - Sell a Pokemon for Money")
    print("sellall - Sell EVERY Pokemon in the PokeDex")
    print("scc - Set your chase-card")
    print("sfc - Add favourite-cards")
    
    print("\nr - Reload the game")
    
    print(f"\n--> Money: {pokedex.money} Pk€  <--")
    io=input("\nSelect a booster pack to open or view(enter the number or pokedex-option-letter): ")
    if io=="v":
        pokedex.dia()
    elif io == "vc":
        pokedex.dia(True)
    elif io == "va":
        pokedex.all_at_once()
    elif io=="vchase":
        if pokedex.chase!=0:
            pokedex.chase.print_ascii_pokemoncard()
        else:
            print("No chase is set!")
    elif io=="vfav":
        if pokedex.favourites!=[]:
            for pokemon in pokedex.favourites:
                pokemon.print_ascii_pokemoncard()
                os.system("pause")
                
    elif io=="c":
        pokedex=''
        main()
    elif io=="search":
        word=input("\nKeyword: ")
        pokedex.search(word)
        os.system("color 07")
    elif io=="reset":
        conform=input("\nAre you REALLY sure to reset your PokeDex? ALL GAINED POKEMONS WILL BE NOT IN THE POKEDEX ANYMORE!! Type 'yes' if your're sure, otherwise just press enter: ")
        if conform=="yes":
            with open(pokedex.name,"w") as f:
                f.write(" ")
                f.close()
            print("PokeDex has been reseted.")
            ioo=input("Press ENTER to continue")
            main()
    elif io=="s":
        which=input("Enter the -exact- name OR the (national) PokeDex-Number (please don't use a #): ")
        pokedex.sell(which)
    elif io == "r":
        os.system('python "pokemon violett 1.1 beta.py"')
    elif io=="sellall":
        pokedex.sellall()
    elif io=="scc":
        inp=input("\nSearch for the card (name or type or number or ...): ")
        results2={}
        results=[]
        print("Suche...")
        for i in range(21):

            progress = "█" * i
            empty = "░" * (20 - i)

            print(
                f"\r[{progress}{empty}] {i * 5:3d}%",
                end="",
                flush=True
            )

            time.sleep(0.02)

        print()
        time.sleep(0.3)
        for bpack in booster_packs:
            bp=pk.PokeDex(bpack.removesuffix(".bstp"),0,False)
            bp.pokemons=pk.BoosterPack.load_bstp(self=pk.BoosterPack(bpack),filename=bpack)
            for thing in bp.search(inp,False):
                results2[thing]=bpack
                results.append(thing)
        if len(results)==0:
            print("There was no card in the available Booster-Packs found...")
            os.system('pause')
            return
        os.system("cls")
        for pokemon in results:
            bname=results2[pokemon]
            print(f"From {bname}")            
            pokemon.print_ascii_pokemoncard()
            dec=input("Set this as chase-card? (Y - Yes, N - No): ")
            if dec in ["Y","y"]:
                pokedex.chase=pokemon
                print("Set!")
                os.system("pause")
                return
            os.system("cls")
        return
    elif io=="sfc":
        word=input("Keyword for the Pokemon: ")
        results=pokedex.search(word,False)
        if len(results)==0:
            print("There was no matching card in your PokeDex found...")
            os.system('pause')
            return
        os.system("cls")
        for pokemon in results:          
            pokemon.print_ascii_pokemoncard()
            dec=input("Add this to the favourites? (Y - Yes, e - exit menu, N - No, r - activly remove from favourites): ")
            if dec in ["Y","y"]:
                pokedex.favourites.append(pokemon)
                print("Added!")
                os.system("pause")
            elif dec in ["r","R"]:
                try:
                    pokedex.favourites.remove(pokemon)
                    print("Removed!")
                    os.system("pause")
                except:
                    print("Pokemon is not in favourites! (or an ERROR occoured.)")
            elif dec in ["E","e"]:
                return
            os.system("cls")
        return
    elif not io.isdigit():
        io="1"
   
    else:
        choice = int(io) - 1
        if 0 <= choice < len(booster_packs):
            selected_pack = booster_packs[choice]
            
            time.sleep(0.21)
            os.system("pause") 
            os.system('cls')  # Clear the console
            # Here you can add code to open the selected booster pack and display its contents
            bp=pk.BoosterPack(selected_pack)
            while True:
                count=0
                for card in bp.card_pool:
                    for cardio in pokedex.pokemons:
                        if card.no == cardio.no:
                            count=count+1
                if count/len(bp.card_pool)>0.74 and not (selected_pack.removesuffix(".bstp")+".bdg" in pokedex.badges) and selected_pack.removesuffix(".bstp")+".bdg" in find_available_badges():
                    pokedex.claim_badge(selected_pack.removesuffix(".bstp")+".bdg")
                    os.system('pause')
                else:
                    if not count/len(bp.card_pool)>0.74:
                        try:
                            pokedex.badges.remove(selected_pack.removesuffix(".bstp")+".bdg")
                        except:
                            pass
                
                print(f"You selected: {selected_pack}")
                print(f"Money: {pokedex.money} Pk€\n")
                if selected_pack.removesuffix(".bstp")+".bdg" in find_available_badges() and selected_pack.removesuffix(".bstp")+".bdg" in pokedex.badges:
                    print("b - View badge")
                io=input(f"1. Open Pack {str(bp.price)} Pk€ (Standart)\n2. View Possible Cards (with rare effekts)\n3. View possible Cards (without rare effects: only color)\n4. Open 10 Packs {str(bp.price*10)} Pk€\nc - Cheat Menu(after exit the cheats are deleted)\ne - exit\nYour Option: ")
                
                if io in ["2","2."]:
                    bp._print_cardpool(pokedex)
                elif io in["3","3."]:
                    bp._print_cardpool_color(pokedex)
                elif io in ["4","4."]:
                    if pokedex.money<(bp.price*10):
                        print("Not enough money!")
                        os.system('pause')
                        return
                    godpack=random.randint(1,500)
                    if bp.name=="Deluxepack ex.bstp":
                        bp.rarity_chances={
                            "Common":35,
                            "Uncommon":25,
                            "Rare":4,
                            "Ultra Rare":0,
                            "Secret Rare":0
                        }
                        bp.hit_chances={
                            "Common": 2,
                            "Uncommon": 20,
                            "Rare": 20,
                            "Ultra Rare": 7,
                            "Secret Rare": 4
                        }
                        os.system("pause")
                    if godpack==179:
                        bp.rarity_chances={
                            "Common":0,
                            "Uncommon":0,
                            "Rare":0,
                            "Ultra Rare":50,
                            "Secret Rare":40
                        }
                    pokedex.addmoney(bp.price*(-10))
                    gainedcards=bp.open_pack(pokedex=pokedex,fast=False,chase=pokedex.chase)
                    for card in gainedcards:
                        pokedex.add(card["card"])
                    for _ in range(9):
                        bp.rarity_chances ={
                            "Common": 40,
                            "Uncommon": 15,
                            "Rare": 1,
                            "Ultra Rare": 0.1,
                            "Secret Rare": 0.1
                        }
                        bp.hit_chances={
                            "Common": 2,
                            "Uncommon": 25,
                            "Rare": 15,
                            "Ultra Rare": 2,
                            "Secret Rare": 0.5
                        }
                        godpack=random.randint(1,500)
                        if bp.name=="Deluxepack ex.bstp":
                            bp.rarity_chances={
                                "Common":35,
                                "Uncommon":25,
                                "Rare":4,
                                "Ultra Rare":0,
                                "Secret Rare":0
                            }
                            bp.hit_chances={
                                "Common": 2,
                                "Uncommon": 20,
                                "Rare": 20,
                                "Ultra Rare": 7,
                                "Secret Rare": 4
                            }
                            os.system("pause")
                        if godpack==179:
                            bp.rarity_chances={
                                "Common":0,
                                "Uncommon":0,
                                "Rare":0,
                                "Ultra Rare":50,
                                "Secret Rare":40
                            }
                        gainedcards=bp.open_pack(pokedex=pokedex,fast=True,chase=pokedex.chase)
                        for card in gainedcards:
                            pokedex.add(card["card"])
                elif io in ["e","E"]:
                    return
                elif io in ["B","b"]:
                    pokedex.claim_badge(selected_pack.removesuffix(".bstp")+".bdg", False)
                    os.system('pause')
                    os.system('cls')
                elif io in ["c","C"]:
                    count=0
                    for card in bp.card_pool:
                        for cardio in pokedex.pokemons:
                            if card.no == cardio.no:
                                count=count+1
                    if count/len(bp.card_pool)>0.74:
                        bp.cheatmenu()
                
                    else:
                        print(f"You have to get more Cards from this Boosterpacks to unlock the cheatmenu! You need at least {round(len(bp.card_pool)*0.74)} Cards from this Boosterpack. ({count}/{round(len(bp.card_pool)*0.74)}/{len(bp.card_pool)})")
                        os.system("pause")
                elif io=="plscheats":
                    bp.cheatmenu()      
                else:
                    if pokedex.money<bp.price:
                        print("Not enough money!")
                        os.system('pause')
                        return
                    godpack=random.randint(1,500)
                    bp.rarity_chances ={
                            "Common": 40,
                            "Uncommon": 15,
                            "Rare": 1,
                            "Ultra Rare": 0.1,
                            "Secret Rare": 0.1
                        }
                    bp.hit_chances={
                        "Common": 2,
                        "Uncommon": 25,
                        "Rare": 15,
                        "Ultra Rare": 2,
                        "Secret Rare": 0.5
                    }
                    if bp.name=="Deluxepack ex.bstp":
                        bp.rarity_chances={
                            "Common":35,
                            "Uncommon":25,
                            "Rare":4,
                            "Ultra Rare":0.1,
                            "Secret Rare":0.1
                        }
                        bp.hit_chances={
                            "Common": 2,
                            "Uncommon": 20,
                            "Rare": 20,
                            "Ultra Rare": 7,
                            "Secret Rare": 4
                        }
                        os.system("pause")
                    if godpack==179:
                        bp.rarity_chances={
                            "Common":0.1,
                            "Uncommon":0.1,
                            "Rare":0.1,
                            "Ultra Rare":50,
                            "Secret Rare":40
                        }
                    pokedex.addmoney(bp.price*(-1))
                    gainedcards=bp.open_pack(pokedex=pokedex,fast=False,chase=pokedex.chase)
                    for card in gainedcards:
                        pokedex.add(card["card"])
                os.system('cls')
        else:
            print("Invalid selection. Please try again.")
    os.system("pause")
welcome()
while True:
    main()