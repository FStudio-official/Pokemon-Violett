import os
import time
import random
class Move:
    def __init__(self, name, type, power, accuracy, description, energy):
        self.name = name
        self.type = type
        self.power = power
        self.accuracy = accuracy
        self.description = description
        self.energy = energy
class Pokemon:
    def __init__(self, no, name, type, hp, moves, retreatcost, rarity):
        self.no = int(no)
        self.name = name
        self.type = type
        self.hp = int(hp)
        self.moves = list(moves)
        self.rarity = rarity
        self.retreatcost = int(retreatcost)

    def print_ascii_pokemoncard(self):
        width = 40

        # Symbole für verschiedene Pokémon-Typen
        type_symbols = {
            "Fire": "🔥",
            "Water": "💧",
            "Electric": "⚡",
            "Grass": "🌿",
            "Psychic": "🔮",
            "Fighting": "✊",
            "Darkness": "🌑",
            "Metal": "⚙",
            "Fairy": "✨",
            "Dragon": "🐉",
            "Colorless": "◇"
        }

        symbol = type_symbols.get(self.type, "◇")

        # Hilfsfunktion für eine normale Zeile
        def line(text=""):
            text = str(text)

            if len(text) > width - 4:
                text = text[:width - 7] + "..."

            return f"║ {text:<{width - 4}} ║"

        # Hilfsfunktion für eine Trennlinie
        def separator():
            return f"╠{'═' * (width - 2)}╣"

        # Karte aufbauen
        card = []

        # Oberer Rand
        card.append(f"╔{'═' * (width - 2)}╗")

        # Nummer, Name und HP
        header = f"#{self.no:03d}  {self.name.upper()}"
        hp_text = f"HP {self.hp}"

        available_space = width - 6
        header = header[:available_space - len(hp_text)]

        card.append(
            f"║ {header:<{available_space}} {hp_text:>{len(hp_text)}} ║"
        )

        # Pokémon-Typ
        card.append(line(f"{symbol} {self.type} TYPE"))

        card.append(separator())

        # Pokémon-Bildbereich
        card.append(line(""))
        card.append(line(""))
        card.append(line(f"             {self.name.upper()}"))
        card.append(line(""))
        card.append(line(f"                 {symbol}"))
        card.append(line(""))
        card.append(line(""))

        card.append(separator())

        # Attacken
        for move in self.moves:
            # Energie
            energy = str(move.energy)

            # Attackenname und Power
            attack_name = move.name
            power = str(move.power)

            left = f"{energy}  {attack_name}"

            # Platz für Power berechnen
            available = width - 6 - len(power)

            if len(left) > available:
                left = left[:available - 3] + "..."

            card.append(
                f"║ {left:<{available}} {power:>{len(power)}} ║"
            )

            # Beschreibung
            description = str(move.description)
            description_width = width - 8

            # Beschreibung auf mehrere Zeilen aufteilen
            while len(description) > description_width:
                split_at = description_width

                # Möglichst bei einem Leerzeichen umbrechen
                space = description.rfind(" ", 0, description_width)

                if space > 0:
                    split_at = space

                card.append(
                    line("    " + description[:split_at])
                )

                description = description[split_at:].strip()

            if description:
                card.append(
                    line("    " + description)
                )

            # Genauigkeit
            card.append(
                line(f"Accuracy: {move.accuracy}%")
            )

            card.append("")

        # Rückzugskosten
        card.append(separator())

        retreat = " ".join([symbol] * self.retreatcost)

        card.append(
            line(f"Retreat Cost: {retreat}")
        )

        # Unterer Rand
        card.append(f"╚{'═' * (width - 2)}╝")

        # Karte ausgeben
        print("\n".join(card))
class Trainer:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def print_ascii_trainercard(self):
        width = 58

        # Hilfsfunktion für eine normale Zeile
        def line(text=""):
            text = str(text)

            if len(text) > width - 4:
                text = text[:width - 7] + "..."

            return f"║ {text:<{width - 4}} ║"

        # Hilfsfunktion für eine Trennlinie
        def separator():
            return f"╠{'═' * (width - 2)}╣"

        # Beschreibung in einzelne Wörter aufteilen
        words = self.description.split()

        description_width = width - 8
        description_lines = []

        current_line = ""

        for word in words:
            # Prüfen, ob das Wort noch in die aktuelle Zeile passt
            if len(current_line) + len(word) + 1 <= description_width:
                if current_line:
                    current_line += " "

                current_line += word

            else:
                description_lines.append(current_line)
                current_line = word

        if current_line:
            description_lines.append(current_line)

        # Karte erstellen
        card = []

        # Oberer Rand
        card.append(f"╔{'═' * (width - 2)}╗")

        # Trainer-Label
        card.append(line("TRAINER"))

        # Name zentrieren
        name = self.name.upper()

        if len(name) > width - 8:
            name = name[:width - 11] + "..."

        card.append(line(""))

        card.append(
            f"║ {name:^{width - 4}} ║"
        )

        card.append(line(""))

        # Trennlinie
        card.append(separator())

        # Abstand zwischen Name und Beschreibung
        card.append(line(""))
        card.append(line(""))

        # Beschreibung zentriert
        for description_line in description_lines:
            card.append(
                f"║ {description_line:^{width - 4}} ║"
            )

        # Mindesthöhe für die Beschreibung
        minimum_description_lines = 4

        missing_lines = (
            minimum_description_lines - len(description_lines)
        )

        for _ in range(max(0, missing_lines)):
            card.append(line(""))

        card.append(line(""))
        card.append(line(""))

        # Untere Trennlinie
        card.append(separator())

        # Fußzeile
        card.append(
            line("POKÉMON TRADING CARD GAME")
        )

        # Unterer Rand
        card.append(f"╚{'═' * (width - 2)}╝")

        # Karte ausgeben
        print("\n".join(card))
class Energy:
    def __init__(self, type):
        self.type = type

    def print_ascii_energycard(self):
        width = 58

        # Symbole für die verschiedenen Energie-Typen
        type_symbols = {
            "Fire": "🔥",
            "Water": "💧",
            "Electric": "⚡",
            "Grass": "🌿",
            "Psychic": "🔮",
            "Fighting": "✊",
            "Darkness": "🌑",
            "Metal": "⚙",
            "Fairy": "✨",
            "Dragon": "🐉",
            "Colorless": "◇"
        }

        symbol = type_symbols.get(self.type, "◇")

        # Hilfsfunktion für normale Zeilen
        def line(text=""):
            text = str(text)

            if len(text) > width - 4:
                text = text[:width - 7] + "..."

            return f"║ {text:<{width - 4}} ║"

        # Hilfsfunktion für Trennlinien
        def separator():
            return f"╠{'═' * (width - 2)}╣"

        # Karte erstellen
        card = []

        # Oberer Rand
        card.append(f"╔{'═' * (width - 2)}╗")

        # Titel
        card.append(
            line(f"{symbol} ENERGY")
        )

        # Energie-Typ
        card.append(line(""))

        card.append(
            f"║ {self.type.upper():^{width - 4}} ║"
        )

        card.append(line(""))

        # Trennlinie
        card.append(separator())

        # Großes Energie-Symbol
        card.append(line(""))
        card.append(line(""))
        card.append(
            f"║ {symbol:^{width - 4}} ║"
        )
        card.append(line(""))
        card.append(line(""))
        card.append(line(""))

        # Untere Trennlinie
        card.append(separator())

        # Fußzeile
        card.append(
            line("POKÉMON TRADING CARD GAME")
        )

        # Unterer Rand
        card.append(f"╚{'═' * (width - 2)}╝")

        # Karte ausgeben
        print("\n".join(card))
class BoosterPack:

    def __init__(
        self,
        name=None,
        card_pool=None,
        pack_size=5,
        rarity_chances=None,
        hit_chances=None,
        price=None
    ):  
        self.name=name
        self.card_pool = card_pool or self.load_bstp(self,self.name)
        self.pack_size = pack_size
        
        # Wahrscheinlichkeiten für die verschiedenen Seltenheiten.
        # Die Werte müssen nicht zusammen 100 ergeben.
        self.rarity_chances = rarity_chances or {
            "Common": 40,
            "Uncommon": 15,
            "Rare": 1,
            "Ultra Rare": 0.1,
            "Secret Rare": 0.1
        }
        self.hit_chances= hit_chances or {
            "Common": 2,
            "Uncommon": 25,
            "Rare": 15,
            "Ultra Rare": 2,
            "Secret Rare": 0.5
        }
        self.price=price or 10

        # Karten, die tatsächlich gezogen wurden.
        self.cards = []

        # Diese Reihenfolge bestimmt die Reihenfolge
        # der späteren Enthüllung.
        self.rarity_order = [
            "Common",
            "Uncommon",
            "Rare",
            "Ultra Rare",
            "Secret Rare"
        ]

        # Farben für die Seltenheiten.
        self.rarity_colors = {
            "Common": "07",
            "Uncommon": "0A",
            "Rare": "09",
            "Ultra Rare": "0E",
            "Secret Rare": "0D"
        }
        self.load_bstp(self,self.name)
    def cheatmenu(self):
        while True:
            print("Willkommen im Cheat Menü >:D\nTippe exit ein um zu verlassen\nDu kannst hier Wahrscheinlichkeiten und Packungsgröße verändern (Bitte %Zeichen unbedingt weglassen) >:D")
            packsize=input("Packungsgröße: ")
            if packsize=="exit":
                return
            try:
                self.pack_size=int(packsize)
            except ValueError:
                print("Es wurde keine valide Zahl eingegeben")
            co=input("Wahrscheinlichkeit für Common: ")
            if co=="exit":
                return
            un=input("Wahrscheinlichkeit für Uncommon: ")
            if un=="exit":
                return
            ra=input("Wahrscheinlichkeit für Rare: ")
            if ra=="exit":
                return
            ul=input("Wahrscheinlichkeit für Ultra Rare: ")
            if ul=="exit":
                return
            se=input("Wahrscheinlichkeit für Secret Rare: ")
            if se=="exit":
                return
            break
        try:
            self.rarity_chances={
                "Common":int(co),
                "Uncommon":int(un),
                "Rare":int(ra),
                "Ultra Rare":int(ul),
                "Secret Rare":int(se)
            }
        except ValueError:
            print("Es wurden nicht nur Zahlen eingegeben. Hast du ein %Zeichen verwendet? Tu es keinesfalls.")
            os.system("pause")
            pass
    # =========================================================
    # BSTP DATEI EINLESEN
    # =========================================================

    @staticmethod
    def load_bstp(self,filename):
        cards = []

        try:
            with open(filename, "r", encoding="utf-8") as file:

                for line_number, line in enumerate(file, start=1):

                    line = line.strip()

                    # Leere Zeilen ignorieren
                    if not line:
                        continue
                    if line.startswith("price="):
                        self.price=int(line.removeprefix("price="))
                        continue
                    # Kommentare ignorieren
                    if line.startswith("#"):
                        continue
                    if not line.startswith("money="):
                        try:
                            pokemon = BoosterPack._parse_bstp_line(line)

                            if pokemon is not None:
                                cards.append(pokemon)

                        except Exception as error:
                            print(
                                f"Fehler in Zeile {line_number}:\n"
                                f"{line}\n"
                                f"Fehler: {error}\n"
                            )

        except FileNotFoundError:
            print(f"Datei nicht gefunden: {filename}")

        except OSError as error:
            print(f"Fehler beim Öffnen der Datei: {error}")
        
        return cards

    # =========================================================
    # BSTP PARSER
    # =========================================================

    @staticmethod
    def _parse_bstp_line(line):

        # Die ersten vier Werte werden getrennt.
        parts = line.split("|", 4)

        if len(parts) != 5:
            raise ValueError(
                "Ungültiges BSTP-Format."
            )

        no = parts[0].strip()
        name = parts[1].strip()
        pokemon_type = parts[2].strip()
        hp = parts[3].strip()

        moves_retreat_rarity = parts[4].strip()

        # Format:
        #
        # [[moves]]|retreatcost|rarity
        #
        end_parts = moves_retreat_rarity.rsplit("|", 2)

        if len(end_parts) != 3:
            raise ValueError(
                "Retreatcost oder Rarity fehlt."
            )

        moves_text = end_parts[0].strip()
        retreatcost = end_parts[1].strip()
        rarity = end_parts[2].strip()

        # -----------------------------------------------------
        # Werte überprüfen
        # -----------------------------------------------------

        if not no:
            raise ValueError("Pokémon-Nummer fehlt.")

        if not name:
            raise ValueError("Pokémon-Name fehlt.")

        if not pokemon_type:
            raise ValueError("Pokémon-Typ fehlt.")

        if not hp:
            raise ValueError("HP fehlt.")

        if not rarity:
            raise ValueError("Rarity fehlt.")

        # Prüfen, ob die Rarity überhaupt bekannt ist.
        valid_rarities = {
            "Common",
            "Uncommon",
            "Rare",
            "Ultra Rare",
            "Secret Rare"
        }

        if rarity not in valid_rarities:
            raise ValueError(
                f"Unbekannte Rarity: {rarity}"
            )

        # -----------------------------------------------------
        # Moves überprüfen
        # -----------------------------------------------------

        if not moves_text.startswith("[["):
            raise ValueError(
                "Moves müssen mit [[ beginnen."
            )

        if not moves_text.endswith("]]"):
            raise ValueError(
                "Moves müssen mit ]] enden."
            )

        # Äußere [[ ]] entfernen.
        moves_text = moves_text[2:-2]

        moves = []

        if moves_text.strip():

            # Mehrere Moves:
            #
            # Move],[Move
            #
            move_data_list = moves_text.split("],[")

            for move_data in move_data_list:

                move_parts = move_data.split("|")

                if len(move_parts) != 6:
                    raise ValueError(
                        f"Ungültiger Move: {move_data}"
                    )

                move_name = move_parts[0].strip()
                move_type = move_parts[1].strip()
                move_power = move_parts[2].strip()
                move_accuracy = move_parts[3].strip()
                move_description = move_parts[4].strip()
                move_energy = move_parts[5].strip()

                move = Move(
                    move_name,
                    move_type,
                    move_power,
                    move_accuracy,
                    move_description,
                    move_energy
                )

                moves.append(move)

        # -----------------------------------------------------
        # Pokémon erstellen
        # -----------------------------------------------------

        pokemon = Pokemon(
            no,
            name,
            pokemon_type,
            hp,
            moves,
            retreatcost,
            rarity
        )

        return pokemon

    # =========================================================
    # RARITY AUSWÄHLEN
    # =========================================================

    def _get_random_rarity(self):

        rarities = list(self.rarity_chances.keys())
        chances = list(self.rarity_chances.values())

        return random.sample(
            rarities,
            weights=chances,
            k=1
        )[0]

    # =========================================================
    # KARTE FÜR RARITY FINDEN
    # =========================================================

    def _get_card_for_rarity(self, rarity):

        matching_cards = [
            card
            for card in self.card_pool
            if getattr(card, "rarity", "").strip().lower()
            == rarity.strip().lower()
        ]

        if not matching_cards:
            return None

        return random.choice(matching_cards)
    def _print_cardpool(self,pokedex=None):
        count=0
        for card in self.card_pool:
            count=count+1
            owned=" Not owned❌"
            os.system("cls")
            self._reset_color()
            self._rare_effect(card.rarity)
            for cardio in pokedex.pokemons:
                if card.no == cardio.no:
                    owned=" Owned✅"
            print(str(count)+"/"+str(len(self.card_pool))+owned)
            card.print_ascii_pokemoncard()
            os.system("pause")
        self._reset_color()  
    def _print_cardpool_color(self,pokedex=None):
        count=0
        for card in self.card_pool:
            count=count+1
            owned=" Not owned❌"
            os.system("cls")
            self._reset_color()
            self._rare_effect_color(card.rarity)
            for cardio in pokedex.pokemons:
                if card.no == cardio.no:
                    owned=" Owned✅"
            print(card.rarity +" | "+str(count)+"/"+str(len(self.card_pool))+owned)
            card.print_ascii_pokemoncard()
            os.system("pause")
           
        self._reset_color()
    # =========================================================
    # BOOSTER ZIEHEN
    # =========================================================

    def _draw_cards(self):

        self.cards = []

        # Karten nach Rarity gruppieren
        rarity_pools = {}

        for card in self.card_pool:

            rarity = getattr(card, "rarity", None)

            if rarity is None:
                continue

            rarity = rarity.strip()

            if rarity not in rarity_pools:
                rarity_pools[rarity] = []

            rarity_pools[rarity].append(card)

        # ---------------------------------------------------------
        # Rarity-Reihenfolge
        # ---------------------------------------------------------

        rarity_positions = {
            rarity: index
            for index, rarity in enumerate(self.rarity_order)
        }

        # ---------------------------------------------------------
        # Verfügbare Rarities für normale Karten
        # ---------------------------------------------------------

        available_rarities = [
            rarity
            for rarity in self.rarity_chances
            if rarity in rarity_pools
            and rarity_pools[rarity]
            and self.rarity_chances[rarity] > 0
        ]

        if not available_rarities:

            print("Keine passende Rarity im Kartenpool gefunden.")

            print("\nGefundene Rarities:")

            for rarity in rarity_pools:
                print(
                    f"  {repr(rarity)}: "
                    f"{len(rarity_pools[rarity])} Karten"
                )

            return []

        available_chances = [
            self.rarity_chances[rarity]
            for rarity in available_rarities
        ]

        # ---------------------------------------------------------
        # Normale Karten
        #
        # Alle Karten BIS AUF DIE LETZTE Karte werden mit
        # rarity_chances gezogen.
        # ---------------------------------------------------------

        normal_card_count = max(0, self.pack_size - 1)

        for _ in range(normal_card_count):

            rarity = random.choices(
                available_rarities,
                weights=available_chances,
                k=1
            )[0]

            card = random.choice(
                rarity_pools[rarity]
            )

            self.cards.append({
                "card": card,
                "rarity": rarity
            })

        # ---------------------------------------------------------
        # Letzte Karte = HIT-Karte
        # ---------------------------------------------------------
        minimum_position=0
        if self.pack_size > 0:

            # -----------------------------------------------------
            # Seltenste Rarity der normalen Karten bestimmen
            # -----------------------------------------------------

            if self.cards:

                # Die seltenste Karte der bisherigen Karten.
                #
                # Common       = 0
                # Uncommon     = 1
                # Rare         = 2
                # Ultra Rare   = 3
                # Secret Rare  = 4
                #
                # max() bedeutet hier also:
                # die HÖCHSTE / seltenste Rarity finden.

                rarest_previous_card = max(
                    self.cards,
                    key=lambda card_data:
                        rarity_positions.get(
                            card_data["rarity"],
                            -1
                        )
                )
                if random.randint(1,100)>66:
                    minimum_position = rarity_positions[
                        rarest_previous_card["rarity"]
                    ]-1
                else:
                    minimum_position = rarity_positions[
                        rarest_previous_card["rarity"]
                    ]

            else:
                # Bei pack_size = 1 gibt es keine vorherigen Karten.
                # Deshalb darf die Hit-Karte jede Rarity haben,
                # die in hit_chances vorhanden ist.

                minimum_position = 0

            # -----------------------------------------------------
            # Mögliche Hit-Rarities bestimmen
            # -----------------------------------------------------

            hit_rarities = [
                rarity
                for rarity in self.hit_chances
                if rarity in rarity_pools
                and rarity_pools[rarity]
                and self.hit_chances[rarity] > 0
                and rarity_positions.get(rarity, -1)
                    > minimum_position
            ]

            # -----------------------------------------------------
            # Falls keine Hit-Rarity die Bedingung erfüllt
            # -----------------------------------------------------
            self._sort_cards_by_rarity()
            if not hit_rarities:

                print(
                    "Keine passende Hit-Rarity gefunden. "
                    "Verwende die seltenste vorhandene Rarity."
                )

                # Alle Rarities, die mindestens so selten sind
                # wie die benötigte Mindest-Rarity.
                fallback_rarities = [
                    rarity
                    for rarity in rarity_pools
                    if rarity_pools[rarity]
                    and rarity_positions.get(rarity, -1)
                        >= minimum_position
                ]

                if not fallback_rarities:

                    print(
                        "Es konnte keine gültige Hit-Karte "
                        "gezogen werden."
                    )

                    return self.cards

                hit_rarities = fallback_rarities

            # -----------------------------------------------------
            # Hit-Chancen verwenden
            # -----------------------------------------------------

            hit_weights = [
                self.hit_chances.get(rarity, 0)
                for rarity in hit_rarities
            ]

            # Falls alle erlaubten Hit-Chancen 0 sind,
            # gleichmäßig aus den erlaubten Rarities wählen.
            if sum(hit_weights) <= 0:

                hit_rarity = random.choice(
                    hit_rarities
                )

            else:

                hit_rarity = random.choices(
                    hit_rarities,
                    weights=hit_weights,
                    k=1
                )[0]

            # Karte aus der entsprechenden Rarity auswählen
            hit_card = random.choice(
                rarity_pools[hit_rarity]
            )

            # Hit-Karte IMMER ganz ans Ende
            self.cards.append({
                "card": hit_card,
                "rarity": hit_rarity
            })

        # ---------------------------------------------------------
        # NICHT SORTIEREN!
        #
        # Die Reihenfolge ist jetzt:
        #
        # 1 ... pack_size-1 = rarity_chances
        # pack_size         = hit_chances
        # ---------------------------------------------------------

        return self.cards


    # =========================================================
    # KARTEN SORTIEREN
    # =========================================================

    def _sort_cards_by_rarity(self):

        rarity_positions = {
            rarity: index
            for index, rarity in enumerate(self.rarity_order)
        }

        self.cards.sort(
            key=lambda card_data:
                rarity_positions.get(
                    card_data["rarity"],
                    999
                )
        )

    # =========================================================
    # TERMINAL
    # =========================================================

    @staticmethod
    def _clear():
        os.system("cls")

    @staticmethod
    def _set_color(color):
        os.system(f"color {color}")

    @staticmethod
    def _reset_color():
        os.system("color 07")

    # =========================================================
    # BOOSTER ANZEIGEN
    # =========================================================

    def _print_booster(self):

        print(
            """
╔════════════════════════════════════════════════════════╗
║                                                        ║
║                    POKÉMON TCG                         ║
║                                                        ║
║              ╭──────────────────╮                      ║
║              │                  │                      ║
║              │      BOOSTER     │                      ║
║              │                  │                      ║
║              │    ⚡  ✨  ⚡   │                      ║
║              │                  │                      ║
║              │      TCG         │                      ║
║              │                  │                      ║
║              ╰──────────────────╯                      ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
"""
        )

    # =========================================================
    # LADEANIMATION
    # =========================================================

    def _loading_animation(self):

        print("Opening booster...")

        for i in range(21):

            progress = "█" * i
            empty = "░" * (20 - i)

            print(
                f"\r[{progress}{empty}] {i * 5:3d}%",
                end="",
                flush=True
            )

            time.sleep(0.03)

        print()
        time.sleep(0.3)

    # =========================================================
    # BOOSTER AUFREISSEN
    # =========================================================

    def _open_animation(self):

        animations = [

            """
╔════════════════════════════════════════════════════════╗
║                                                        ║
║                 OPENING BOOSTER...                     ║
║                                                        ║
║                 ┌──────────────┐                       ║
║                 │    BOOSTER   │                       ║
║                 │              │                       ║
║                 └──────────────┘                       ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
""",

            """
╔════════════════════════════════════════════════════════╗
║                                                        ║
║                 OPENING BOOSTER...                     ║
║                                                        ║
║                 ┌──────────────┐                       ║
║                 │    /         │                       ║
║                 │   /          │                       ║
║                 │  /           │                       ║
║                 └──────────────┘                       ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
""",

            """
╔════════════════════════════════════════════════════════╗
║                                                        ║
║                 BOOSTER OPENED!                        ║
║                                                        ║
║                    ╲        ╱                          ║
║                     ╲      ╱                           ║
║                      ╲    ╱                            ║
║                       ╲  ╱                             ║
║                        ✨                              ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
"""
        ]

        for animation in animations:

            self._clear()

            print(animation)

            time.sleep(0.3)

    # =========================================================
    # RARE EFFECT
    # =========================================================

    def _rare_effect(self, rarity):
       

        if rarity == "Common":
            return

        self._clear()

        if rarity == "Uncommon":

            self._set_color(
                self.rarity_colors["Uncommon"]
            )

            print(
                """
──────────────────────────────────────────────────────────
                    ✦ UNCOMMON ✦
──────────────────────────────────────────────────────────
"""
            )

            time.sleep(0.4)

        elif rarity == "Rare":

            self._set_color(
                self.rarity_colors["Rare"]
            )

            for _ in range(2):

                print(
                    "✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨ ✨"
                )

                time.sleep(0.15)

            print()
            print("                    RARE CARD!")
            print()

            time.sleep(0.5)

        elif rarity == "Ultra Rare":

            self._set_color(
                self.rarity_colors["Ultra Rare"]
            )

            for _ in range(3):

                print(
                    "⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐"
                )

                time.sleep(0.1)

            print()
            print("                 ULTRA RARE!")
            print()

            time.sleep(1)

        elif rarity == "Secret Rare":

            self._set_color(
                self.rarity_colors["Secret Rare"]
            )

            for _ in range(3):

                print(
                    "✨ ⭐ ✨ ⭐ ✨ ⭐ ✨ ⭐ ✨"
                )

                time.sleep(0.15)

            print()
            print("              ★ SECRET RARE ★")
            print()
            print(
                "       YOU FOUND SOMETHING SPECIAL!"
            )
            print()

            time.sleep(1.5)

    def _rare_effect_color(self, rarity):

        if rarity == "Common":
            return

        self._clear()

        if rarity == "Uncommon":

            self._set_color(
                self.rarity_colors["Uncommon"]
            )

        elif rarity == "Rare":

            self._set_color(
                self.rarity_colors["Rare"]
            )

        elif rarity == "Ultra Rare":

            self._set_color(
                self.rarity_colors["Ultra Rare"]
            )
        elif rarity == "Secret Rare":

            self._set_color(
                self.rarity_colors["Secret Rare"]
            )

    # =========================================================
    # KARTE ANZEIGEN
    # =========================================================

    def _display_card(self, card_data):

        card = card_data["card"]
        rarity = card_data["rarity"]

        color = self.rarity_colors.get(
            rarity,
            "07"
        )

        self._set_color(color)

        print()
        print(
            f"                    {rarity.upper()}"
        )
        print()

        # Pokémon
        if isinstance(card, Pokemon):

            card.print_ascii_pokemoncard()

        # Trainer
        elif isinstance(card, Trainer):

            card.print_ascii_trainercard()

        # Energie
        elif isinstance(card, Energy):

            card.print_ascii_energycard()

        # Unbekannter Kartentyp
        else:

            print(card)

        time.sleep(0.5)

    # =========================================================
    # BOOSTER ÖFFNEN
    # =========================================================

    def open_pack(self,pokedex,fast=False,chase=None):
        
        if not self.card_pool:

            print("Der Kartenpool ist leer.")

            return []

        # -----------------------------------------------------
        # Karten ziehen
        # -----------------------------------------------------

        self._draw_cards()

        if not self.cards:

            print("Es konnten keine Karten gezogen werden.")

            return []

        # -----------------------------------------------------
        # Farbe zurücksetzen
        # -----------------------------------------------------

        self._reset_color()

        # -----------------------------------------------------
        # Booster anzeigen
        # -----------------------------------------------------

        self._clear()
        if not fast:
            self._print_booster()

            input(
                "\nDrücke ENTER, um das Booster zu öffnen..."
            )

            # -----------------------------------------------------
            # Ladeanimation
            # -----------------------------------------------------

            self._clear()

            self._loading_animation()

            # -----------------------------------------------------
            # Booster aufreißen
            # -----------------------------------------------------

            self._open_animation()
        else:
            print("~~~~ Next ~~~~")
            os.system('pause')

        # -----------------------------------------------------
        # Karten enthüllen
        #
        # Durch _sort_cards_by_rarity() kommen die Common-Karten
        # zuerst und die seltensten Karten zuletzt.
        # -----------------------------------------------------

        for index, card_data in enumerate(self.cards):
            owned=" "
            self._clear()

            print(
                f"                 CARD "
                f"{index + 1}/{len(self.cards)}"
            )

            print()
            print("Revealing...")

            time.sleep(0.4)
            os.system('cls')
            #print(card_data["card"].name,chase.name,card_data["card"].moves[0].name, chase.moves[0].name)

            self._rare_effect(
                card_data["rarity"]
            )
            if not chase==0:
                if card_data["card"].name==chase.name and card_data["card"].moves[0].name==chase.moves[0].name and card_data["card"].moves[0].description==chase.moves[0].description:
                    raritycol=["07","0A","09","0E","0D"]
                    os.system('cls')
                    for _ in range(4):
                        i2=0
                        for i in range(10):
                            print("✨ !",end="",flush=True)
                            try:
                                os.system("color "+raritycol[i2])
                            except:
                                i2=0
                                os.system("color "+raritycol[i2])
                            i2+=1
                        print("\n")
                    
                
            # Spezialeffekt
            

            # Karte anzeigen
            self._clear()
            new=True
            for cardio in pokedex.pokemons:
                if  not self.cards[index]['card'].no == cardio.no:
                    continue
                else:
                    new=False
                    break
            if new:
                print("-------->>>NEW!!!<<<-----------")
            else:
                print("Not new")
            self._display_card(card_data)
            

            input(
                "\nDrücke ENTER für die nächste Karte..."
            )

        # -----------------------------------------------------
        # Zusammenfassung
        # -----------------------------------------------------

        self._clear()

        self._reset_color()
        print(self.cards)
        print(
            """
╔════════════════════════════════════════════════════════╗
║                                                        ║
║                  BOOSTER COMPLETE!                     ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
"""
        )
        time.sleep(0.5)

        for index, card_data in enumerate(self.cards):

            card = card_data["card"]
            rarity = card_data["rarity"]

            print(
                f"{index + 1:02d}. "
                f"{rarity:<15} "
                f"{card.name}"
            )

        print()
        os.system("pause")
        self._reset_color()

        return self.cards  
class PokeDex:

    def __init__(self, name, money=None,loadalso=True):
        # Falls jemand "xy" statt "xy.dex" angibt
        if not name.endswith(".dex"):
            name += ".dex"

        self.name = name
        self.pokemons = []

        self.rarity_colors = {
            "Common": "07",
            "Uncommon": "0A",
            "Rare": "09",
            "Ultra Rare": "0E",
            "Secret Rare": "0D"
        }
        self.money = money or 15
        self.chase = 0
        self.favourites=[]
        self.badges=[]
        # Bereits vorhandene Dex-Datei laden
        if loadalso:
            self.load()

    # =========================================================
    # DEX-DATEI LADEN
    # =========================================================

    def load(self):

        self.pokemons = []
        
        try:

            with open(self.name, "r", encoding="utf-8") as file:

                for line_number, line in enumerate(file, start=1):
                    line = line.strip()

                    # Leere Zeilen ignorieren
                    if not line:
                        continue
                    if line.startswith("money="):
                        try:
                            self.money=int(line.removeprefix("money="))
                            continue
                        except ValueError:
                            print("Ungültiges DEX-Format!")
                    if line.startswith("favourites="):
                        if line!="favourites=0":
                            favos=line.removeprefix("favourites=").split('^')
                            for pokemon in favos:
                                print(pokemon)
                                self.favourites.append(BoosterPack._parse_bstp_line(pokemon))
                                self.pokemons.append(BoosterPack._parse_bstp_line(pokemon))
                        
                    if line.startswith("chase="):
                        if not line=="chase=0":
                            self.chase=BoosterPack._parse_bstp_line(line.removeprefix('chase='))
                            continue
                        else:
                            continue
                    if line.startswith("badges="):
                        if line!="badges=0":
                            self.badges=line.removeprefix("badges=").split(",")
                    # Kommentare ignorieren
                    if line.startswith("#"):
                        continue

                    try:

                        pokemon = BoosterPack._parse_bstp_line(line)

                        if pokemon is not None:
                            self.pokemons.append(pokemon)

                    except Exception as error:

                        print(
                            f"Fehler in {self.name}, Zeile "
                            f"{line_number}:\n"
                            f"{line}\n"
                            f"Fehler: {error}\n"
                        )

        except FileNotFoundError:

            # Wenn die Datei noch nicht existiert,
            # wird sie automatisch erstellt.
            with open(self.name, "w", encoding="utf-8") as f:
                f.write(f"money=18")
                f.write("chase=0")
                f.write("favourites=0")
                f.write("badges=0")
                pass

        except OSError as error:

            print(
                f"Fehler beim Öffnen von {self.name}: {error}"
            )

        # Nach National-Dex-Nummer sortieren
        self.pokemons.sort(
            key=lambda pokemon: pokemon.no
        )

    # =========================================================
    # POKEMON HINZUFÜGEN
    # =========================================================

    def add(self, pokemon):

        # Nur Pokemon erlauben
        if not isinstance(pokemon, Pokemon):

            raise TypeError(
                "Mit add() können nur Pokemon hinzugefügt werden."
            )

        # Prüfen, ob die Nummer bereits existiert
        for existing_pokemon in self.pokemons:

            if existing_pokemon.no == pokemon.no:

                print(
                    f"#{pokemon.no:03d} "
                    f"{pokemon.name} ist bereits im Dex."
                )

                return False

        # Pokemon hinzufügen
        self.pokemons.append(pokemon)

        # Nach Nummer sortieren
        self.pokemons.sort(
            key=lambda pokemon: pokemon.no
        )

        # Datei speichern
        self.save()

        print(
            f"#{pokemon.no:03d} "
            f"{pokemon.name} wurde zum Dex hinzugefügt."
        )

        return True

    # =========================================================
    # DEX SPEICHERN
    # =========================================================
    
    def save(self):

        try:

            with open(
                self.name,
                "w",
                encoding="utf-8"
            ) as file:
                file.write("money="+str(self.money)+"\n")
                cmoves=[]
                if not self.chase==0:
                    for move in self.chase.moves:
                        cmoves.append(
                            f"{move.name}|"
                            f"{move.type}|"
                            f"{move.power}|"
                            f"{move.accuracy}|"
                            f"{move.description}|"
                            f"{move.energy}"
                        )
                    cmoves_text = "[[" + "],[".join(cmoves) + "]]"
                    cline = (
                        f"{self.chase.no:04d}|"
                        f"{self.chase.name}|"
                        f"{self.chase.type}|"
                        f"{self.chase.hp}|"
                        f"{cmoves_text}|"
                        f"{self.chase.retreatcost}|"
                        f"{self.chase.rarity}"
                    )
                    file.write("chase="+cline+"\n")
                else:
                    file.write("chase=0")
                    print(self.favourites)
                if not len(self.favourites)==0:
                    file.write("favourites=")
                    for pokemon in self.favourites:

                    # Moves wieder in BSTP-Format umwandeln
                        moves = []

                        for move in pokemon.moves:

                            moves.append(
                                f"{move.name}|"
                                f"{move.type}|"
                                f"{move.power}|"
                                f"{move.accuracy}|"
                                f"{move.description}|"
                                f"{move.energy}"
                            )

                        moves_text = "[[" + "],[".join(moves) + "]]"

                        fline = (
                            f"{pokemon.no:04d}|"
                            f"{pokemon.name}|"
                            f"{pokemon.type}|"
                            f"{pokemon.hp}|"
                            f"{moves_text}|"
                            f"{pokemon.retreatcost}|"
                            f"{pokemon.rarity}"
                        )
                        if pokemon != self.favourites[len(self.favourites)-1]:
                            file.write(fline + "^")
                        else:
                            file.write(fline+"\n")
                bline="badges="
                if len(self.badges)==0:
                    bline=bline+"0\n"
                for badge in self.badges:
                    if badge!=self.badges[len(self.badges)-1]:
                        bline=bline+badge+","
                    else:
                        bline=bline+badge+"\n"
                file.write(bline)
                for pokemon in self.pokemons:

                    # Moves wieder in BSTP-Format umwandeln
                    moves = []

                    for move in pokemon.moves:

                        moves.append(
                            f"{move.name}|"
                            f"{move.type}|"
                            f"{move.power}|"
                            f"{move.accuracy}|"
                            f"{move.description}|"
                            f"{move.energy}"
                        )

                    moves_text = "[[" + "],[".join(moves) + "]]"

                    line = (
                        f"{pokemon.no:04d}|"
                        f"{pokemon.name}|"
                        f"{pokemon.type}|"
                        f"{pokemon.hp}|"
                        f"{moves_text}|"
                        f"{pokemon.retreatcost}|"
                        f"{pokemon.rarity}"
                    )

                    file.write(line + "\n")

        except OSError as error:

            print(
                f"Fehler beim Speichern von {self.name}: "
                f"{error}"
            )
    def addmoney(self,amount=None):
        self.money=self.money+amount
        self.save()
    def sell(self,name=None,listcount=0):
        no=None
        count=listcount
        if name.isdigit():
            no=int(name)
        if not name and not no:
            print("Nichts angegeben!")
            return
        resultsindexes=[]
        for i in range(len(self.pokemons)):
            pok=self.pokemons[i]
            if name in pok.name or name in pok.moves[0].name or name==pok.type or name==pok.rarity:
                if count<1:
                    resultsindexes.append(i)
                    continue
                else:
                    count=count-1
            if len(pok.moves)==2:
                if name in pok.moves[1].name:
                    if count<1:
                        resultsindexes.append(i)
                        continue
                    else:
                        count=count-1
                    
            try:
                if no == pok.no:
                    if count<1:
                        resultsindexes.append(i)
                        continue
                    else:
                        count=count-1
            except:
                pass
        if len(resultsindexes)<1:
            print("Kein Pokemon gefunden!")
            return
        for i in resultsindexes:
            self.pokemons[i].print_ascii_pokemoncard()
            io=input(f'\nDo you want to sell this Pokemon for {str({"Common":1,"Uncommon":3,"Rare": 7,"Ultra Rare": 60,"Secret Rare":150}[self.pokemons[i].rarity])}? (y to confirm, Enter to cancel) >')
            if io=="y":
                self.addmoney({"Common":1,"Uncommon":3,"Rare": 7,"Ultra Rare": 60,"Secret Rare":150}[self.pokemons[i].rarity])
            
                print(f'+{str({"Common":1,"Uncommon":3,"Rare": 7,"Ultra Rare": 60,"Secret Rare":150}[self.pokemons[i].rarity])} Pk€')
                
                try:
                    for pokemon in self.favourites:
                        if self.pokemons[i].name == pokemon.name :#and pokemon.moves[0]==self.pokemons[i].moves[0]:
                            self.favourites.remove(pokemon)
                            break
                    
                except:
                    try:
                        print(self.pokemons[i] in self.favourites)
                        os.system("pause")
                    except:
                        pass
                    pass
                self.pokemons.pop(i)
                os.system("pause")
                self.save()
                if not name:
                    name=no
                self.sell(name,listcount)
            os.system('cls')
            listcount=listcount+1
            continue
    def sellall(self):
        io=input("Every Card (except the favourites) will be selled! Are you sure to sell everything from this PokeDex? (YES if you are sure) ")
        if io=="YES":
            count=0
            print(len(self.pokemons))
            i2=1
            for _ in range(len(self.pokemons)):
                skip=False
                if len(self.pokemons)-i2 <0:
                    break
                for favo in self.favourites:
                    if favo.name== self.pokemons[len(self.pokemons)-i2].name:
                        skip=True
                        i2=i2+1
                if not skip:
                    print(f'+{str({"Common":1,"Uncommon":3,"Rare": 7,"Ultra Rare": 60,"Secret Rare":150}[self.pokemons[len(self.pokemons)-i2].rarity])} Pk€')
                    self.addmoney({"Common":1,"Uncommon":3,"Rare": 7,"Ultra Rare": 60,"Secret Rare":150}[self.pokemons[len(self.pokemons)-i2].rarity])
                    
                    count=count+{"Common":1,"Uncommon":3,"Rare": 7,"Ultra Rare": 60,"Secret Rare":150}[self.pokemons[len(self.pokemons)-i2].rarity]
                    len(self.pokemons)
                    self.pokemons.pop(len(self.pokemons)-i2)
                    self.save()
            print(f"\n---> {count}")
             
                
                
        
                    
    # =========================================================
    # POKEMON SUCHEN
    # =========================================================
    def claim_badge(self,filename,new=True):
        print("Please Zoom out really far...")
        time.sleep(0.3)
        os.system("pause")
        if new:
            print(f"NEW BADGE!!! OF {filename.removeprefix(".bdg")}!")
            if not filename in self.badges:
                self.badges.append(filename)
                self.badges=list(set(self.badges))
                self.save()
        else:
            print(f"Badge of {filename.removeprefix(".bdg")}")
        try:
            with open(filename,"r",encoding="utf-8") as f:
                lines=f.readlines()
                i2=0
                raritycol=["07","0A","09","0E","0D"]
                bigline=""
                for line in lines:               
                    bigline=bigline+line+"\n"
                print(bigline)
                if new:
                    for _ in range(5):
                        try:
                            os.system("color "+raritycol[i2])
                        except:
                            i2=0
                            os.system("color "+raritycol[i2])
                        time.sleep(0.1)
                        i2+=1
        except:
            print("Ups! An ERROR occured!")
    def get(self, number):

        try:
            number = int(number)

        except ValueError:

            return None

        for pokemon in self.pokemons:

            if pokemon.no == number:
                return pokemon

        return None
    def dia(self,effects=False):
        if self.pokemons==[]:
            print("\nDer PokeDex ist leer.\n")
            return
        vbooster=BoosterPack("Vbooster",self.pokemons)
        if effects==False:
            vbooster._print_cardpool_color(self)
        else:
            vbooster._print_cardpool(self)
    def search(self,word, printout=True):
        results=[]
        os.system("cls")
        for pok in self.pokemons:
           
            if word in pok.name or word in pok.moves[0].name or word==pok.type or word==pok.rarity:
                if printout:
                    os.system(f"color {self.rarity_colors[pok.rarity]}")
                    pok.print_ascii_pokemoncard()
                results.append(pok)
                continue
            if len(pok.moves)==2:
                if word in pok.moves[1].name:
                    if printout:
                        if word==pok.type:
                            os.system(f"color {self.rarity_colors[pok.rarity]}")
                        pok.print_ascii_pokemoncard()
                    results.append(pok)
                    os.system(f"color {self.rarity_colors[pok.rarity]}")
                    continue
            try:
                if int(word) == pok.no:
                    if printout:
                        pok.print_ascii_pokemoncard()
                    results.append(pok)
                    os.system(f"color {self.rarity_colors[pok.rarity]}")
            except:
                pass
        return results
        os.system("pause")
        os.system(f"color 07")
    def all_at_once(self):
        if self.pokemons==[]:
            print("\nDer PokeDex ist leer.\n")
            return
        for pok in self.pokemons:
            pok.print_ascii_pokemoncard()
#---------------------------------------------------------#
