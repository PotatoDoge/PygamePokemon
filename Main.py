from Motor import *
if __name__ == "__main__":
    newMotor = motor()
    newMotor.run()

    pokemon = ['Magnemite','Magneton','Mankey','Marowak','Meowth','Metapod','Mew','Mewtwo','Moltres','Mr_Mime','Muk','Nidoking','Nidoqueen','Nidoran',
                "Nidorina",'Nidorino','Ninetales','Oddish','Omanyte','Omastar','Onix','Paras','Parasect','Persian','Pidgeot','Pidgeotto','Pidgey',
                'Pikachu','Pinsir','Poliwag','Poliwhirl','Poliwrath','Ponyta','Porygon','Primeape','Psyduck','Raichu','Rapidash','Raticate',
                'Rattata','Rhydon','Rhyhorn','Sandshrew','Sandslash','Scyther','Seadra','Seaking','Seel','Shellder','Slowbro','Slowpoke','Snorlax',
                'Spearow','Squirtle','Starmie','Staryu','Tangela','Tauros','Tentacool','Tentacruel','Vaporeon','Venomoth','Venonat','Venusaur',
                'Victreebel','Vileplume','Voltorb','Vulpix','Wartortle','Weedle','Weepinbell','Weezing','Wigglytuff','Zapdoss','Zubat']
    for i in range(0,len(pokemon)):
        print(pokemon[i]+f"Sprite = [pygame.image.load('images/pokemon/secondHalf/{pokemon[i]}/{pokemon[i]}.png'),pygame.image.load('images/pokemon/secondHalf/{pokemon[i]}/{pokemon[i]}_back.png')]")
