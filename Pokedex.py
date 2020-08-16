from Pokemon import *
import pygame

# [0] = front , [1] = back
# HYPNO'S BACK SPRITE MISSING
# NIDORAN MALE/FEMALE SPRITES, I DON'T REMEMBER WHICH ONE, MISSING

AbraSprites = [pygame.image.load('images/pokemon/firstHalf/Abra/Abra.png'),pygame.image.load('images/pokemon/firstHalf/Abra/Abra_back.png')]
AerodactylSprites = [pygame.image.load('images/pokemon/firstHalf/Aerodactyl/Aerodactyl.png'),pygame.image.load('images/pokemon/firstHalf/Aerodactyl/Aerodactyl_back.png')]
AlakazamSprites = [pygame.image.load('images/pokemon/firstHalf/Alakazam/Alakazam.png'),pygame.image.load('images/pokemon/firstHalf/Alakazam/Alakazam_back.png')]
ArbokSprites = [pygame.image.load('images/pokemon/firstHalf/Arbok/Arbok.png'),pygame.image.load('images/pokemon/firstHalf/Arbok/Arbok_back.png')]
ArcanineSprites = [pygame.image.load('images/pokemon/firstHalf/Arcanine/Arcanine.png'),pygame.image.load('images/pokemon/firstHalf/Arcanine/Arcanine_back.png')]
ArticunoSprites = [pygame.image.load('images/pokemon/firstHalf/Articuno/Articuno.png'),pygame.image.load('images/pokemon/firstHalf/Articuno/Articuno_back.png')]
BeedrillSprites = [pygame.image.load('images/pokemon/firstHalf/Beedrill/Beedrill.png'),pygame.image.load('images/pokemon/firstHalf/Beedrill/Beedrill_back.png')]
BellsproutSprites = [pygame.image.load('images/pokemon/firstHalf/Bellsprout/Bellsprout.png'),pygame.image.load('images/pokemon/firstHalf/Bellsprout/Bellsprout_back.png')]
BlastoiseSprites = [pygame.image.load('images/pokemon/firstHalf/Blastoise/Blastoise.png'),pygame.image.load('images/pokemon/firstHalf/Blastoise/Blastoise_back.png')]
BulbasaurSprites = [pygame.image.load('images/pokemon/firstHalf/Bulbasaur/Bulbasaur.png'),pygame.image.load('images/pokemon/firstHalf/Bulbasaur/Bulbasaur_back.png')]
ButterfreeSprites = [pygame.image.load('images/pokemon/firstHalf/Butterfree/Butterfree.png'),pygame.image.load('images/pokemon/firstHalf/Butterfree/Butterfree_back.png')]
CaterpieSprites = [pygame.image.load('images/pokemon/firstHalf/Caterpie/Caterpie.png'),pygame.image.load('images/pokemon/firstHalf/Caterpie/Caterpie_back.png')]
ChanseySprites = [pygame.image.load('images/pokemon/firstHalf/Chansey/Chansey.png'),pygame.image.load('images/pokemon/firstHalf/Chansey/Chansey_back.png')]
CharizardSprites = [pygame.image.load('images/pokemon/firstHalf/Charizard/Charizard.png'),pygame.image.load('images/pokemon/firstHalf/Charizard/Charizard_back.png')]
CharmanderSprites = [pygame.image.load('images/pokemon/firstHalf/Charmander/Charmander.png'),pygame.image.load('images/pokemon/firstHalf/Charmander/Charmander_back.png')]
CharmeleonSprites = [pygame.image.load('images/pokemon/firstHalf/Charmeleon/Charmeleon.png'),pygame.image.load('images/pokemon/firstHalf/Charmeleon/Charmeleon_back.png')]
ClefableSprites = [pygame.image.load('images/pokemon/firstHalf/Clefable/Clefable.png'),pygame.image.load('images/pokemon/firstHalf/Clefable/Clefable_back.png')]
ClefairySprites = [pygame.image.load('images/pokemon/firstHalf/Clefairy/Clefairy.png'),pygame.image.load('images/pokemon/firstHalf/Clefairy/Clefairy_back.png')]
CloysterSprites = [pygame.image.load('images/pokemon/firstHalf/Cloyster/Cloyster.png'),pygame.image.load('images/pokemon/firstHalf/Cloyster/Cloyster_back.png')]
CuboneSprites = [pygame.image.load('images/pokemon/firstHalf/Cubone/Cubone.png'),pygame.image.load('images/pokemon/firstHalf/Cubone/Cubone_back.png')]
DewgongSprites = [pygame.image.load('images/pokemon/firstHalf/Dewgong/Dewgong.png'),pygame.image.load('images/pokemon/firstHalf/Dewgong/Dewgong_back.png')]
DiglettSprites = [pygame.image.load('images/pokemon/firstHalf/Diglett/Diglett.png'),pygame.image.load('images/pokemon/firstHalf/Diglett/Diglett_back.png')]
DittoSprites = [pygame.image.load('images/pokemon/firstHalf/Ditto/Ditto.png'),pygame.image.load('images/pokemon/firstHalf/Ditto/Ditto_back.png')]
DodrioSprites = [pygame.image.load('images/pokemon/firstHalf/Dodrio/Dodrio.png'),pygame.image.load('images/pokemon/firstHalf/Dodrio/Dodrio_back.png')]
DoduoSprites = [pygame.image.load('images/pokemon/firstHalf/Doduo/Doduo.png'),pygame.image.load('images/pokemon/firstHalf/Doduo/Doduo_back.png')]
DragonairSprites = [pygame.image.load('images/pokemon/firstHalf/Dragonair/Dragonair.png'),pygame.image.load('images/pokemon/firstHalf/Dragonair/Dragonair_back.png')]
DragoniteSprites = [pygame.image.load('images/pokemon/firstHalf/Dragonite/Dragonite.png'),pygame.image.load('images/pokemon/firstHalf/Dragonite/Dragonite_back.png')]
DratiniSprites = [pygame.image.load('images/pokemon/firstHalf/Dratini/Dratini.png'),pygame.image.load('images/pokemon/firstHalf/Dratini/Dratini_back.png')]
DrowzeeSprites = [pygame.image.load('images/pokemon/firstHalf/Drowzee/Drowzee.png'),pygame.image.load('images/pokemon/firstHalf/Drowzee/Drowzee_back.png')]
DugtrioSprites = [pygame.image.load('images/pokemon/firstHalf/Dugtrio/Dugtrio.png'),pygame.image.load('images/pokemon/firstHalf/Dugtrio/Dugtrio_back.png')]
EeveeSprites = [pygame.image.load('images/pokemon/firstHalf/Eevee/Eevee.png'),pygame.image.load('images/pokemon/firstHalf/Eevee/Eevee_back.png')]
EkansSprites = [pygame.image.load('images/pokemon/firstHalf/Ekans/Ekans.png'),pygame.image.load('images/pokemon/firstHalf/Ekans/Ekans_back.png')]
ElectabuzzSprites = [pygame.image.load('images/pokemon/firstHalf/Electabuzz/Electabuzz.png'),pygame.image.load('images/pokemon/firstHalf/Electabuzz/Electabuzz_back.png')]
ElectrodeSprites = [pygame.image.load('images/pokemon/firstHalf/Electrode/Electrode.png'),pygame.image.load('images/pokemon/firstHalf/Electrode/Electrode_back.png')]
ExeggcuteSprites = [pygame.image.load('images/pokemon/firstHalf/Exeggcute/Exeggcute.png'),pygame.image.load('images/pokemon/firstHalf/Exeggcute/Exeggcute_back.png')]
ExeggutorSprites = [pygame.image.load('images/pokemon/firstHalf/Exeggutor/Exeggutor.png'),pygame.image.load('images/pokemon/firstHalf/Exeggutor/Exeggutor_back.png')]
FarfetchSprites = [pygame.image.load('images/pokemon/firstHalf/Farfetch/Farfetch.png'),pygame.image.load('images/pokemon/firstHalf/Farfetch/Farfetch_back.png')]
FearowSprites = [pygame.image.load('images/pokemon/firstHalf/Fearow/Fearow.png'),pygame.image.load('images/pokemon/firstHalf/Fearow/Fearow_back.png')]
FlareonSprites = [pygame.image.load('images/pokemon/firstHalf/Flareon/Flareon.png'),pygame.image.load('images/pokemon/firstHalf/Flareon/Flareon_back.png')]
GastlySprites = [pygame.image.load('images/pokemon/firstHalf/Gastly/Gastly.png'),pygame.image.load('images/pokemon/firstHalf/Gastly/Gastly_back.png')]
GengarSprites = [pygame.image.load('images/pokemon/firstHalf/Gengar/Gengar.png'),pygame.image.load('images/pokemon/firstHalf/Gengar/Gengar_back.png')]
GeodudeSprites = [pygame.image.load('images/pokemon/firstHalf/Geodude/Geodude.png'),pygame.image.load('images/pokemon/firstHalf/Geodude/Geodude_back.png')]
GloomSprites = [pygame.image.load('images/pokemon/firstHalf/Gloom/Gloom.png'),pygame.image.load('images/pokemon/firstHalf/Gloom/Gloom_back.png')]
GolbatSprites = [pygame.image.load('images/pokemon/firstHalf/Golbat/Golbat.png'),pygame.image.load('images/pokemon/firstHalf/Golbat/Golbat_back.png')]
GoldeenSprites = [pygame.image.load('images/pokemon/firstHalf/Goldeen/Goldeen.png'),pygame.image.load('images/pokemon/firstHalf/Goldeen/Goldeen_back.png')]
GolduckSprites = [pygame.image.load('images/pokemon/firstHalf/Golduck/Golduck.png'),pygame.image.load('images/pokemon/firstHalf/Golduck/Golduck_back.png')]
GolemSprites = [pygame.image.load('images/pokemon/firstHalf/Golem/Golem.png'),pygame.image.load('images/pokemon/firstHalf/Golem/Golem_back.png')]
GravelerSprites = [pygame.image.load('images/pokemon/firstHalf/Graveler/Graveler.png'),pygame.image.load('images/pokemon/firstHalf/Graveler/Graveler_back.png')]
GrimerSprites = [pygame.image.load('images/pokemon/firstHalf/Grimer/Grimer.png'),pygame.image.load('images/pokemon/firstHalf/Grimer/Grimer_back.png')]
GrowlitheSprites = [pygame.image.load('images/pokemon/firstHalf/Growlithe/Growlithe.png'),pygame.image.load('images/pokemon/firstHalf/Growlithe/Growlithe_back.png')]
GyaradosSprites = [pygame.image.load('images/pokemon/firstHalf/Gyarados/Gyarados.png'),pygame.image.load('images/pokemon/firstHalf/Gyarados/Gyarados_back.png')]
HaunterSprites = [pygame.image.load('images/pokemon/firstHalf/Haunter/Haunter.png'),pygame.image.load('images/pokemon/firstHalf/Haunter/Haunter_back.png')]
HitmonchanSprites = [pygame.image.load('images/pokemon/firstHalf/Hitmonchan/Hitmonchan.png'),pygame.image.load('images/pokemon/firstHalf/Hitmonchan/Hitmonchan_back.png')]
HitmonleeSprites = [pygame.image.load('images/pokemon/firstHalf/Hitmonlee/Hitmonlee.png'),pygame.image.load('images/pokemon/firstHalf/Hitmonlee/Hitmonlee_back.png')]
HorseaSprites = [pygame.image.load('images/pokemon/firstHalf/Horsea/Horsea.png'),pygame.image.load('images/pokemon/firstHalf/Horsea/Horsea_back.png')]
HypnoSprites = [pygame.image.load('images/pokemon/firstHalf/Hypno/Hypno.png'),pygame.image.load('images/pokemon/firstHalf/Hypno/Hypno.png')]
IvysaurSprites = [pygame.image.load('images/pokemon/firstHalf/Ivysaur/Ivysaur.png'),pygame.image.load('images/pokemon/firstHalf/Ivysaur/Ivysaur_back.png')]
JigglypuffSprites = [pygame.image.load('images/pokemon/firstHalf/Jigglypuff/Jigglypuff.png'),pygame.image.load('images/pokemon/firstHalf/Jigglypuff/Jigglypuff_back.png')]
JolteonSprites = [pygame.image.load('images/pokemon/firstHalf/Jolteon/Jolteon.png'),pygame.image.load('images/pokemon/firstHalf/Jolteon/Jolteon_back.png')]
JynxSprites = [pygame.image.load('images/pokemon/firstHalf/Jynx/Jynx.png'),pygame.image.load('images/pokemon/firstHalf/Jynx/Jynx_back.png')]
KabutoSprites = [pygame.image.load('images/pokemon/firstHalf/Kabuto/Kabuto.png'),pygame.image.load('images/pokemon/firstHalf/Kabuto/Kabuto_back.png')]
KabutopsSprites = [pygame.image.load('images/pokemon/firstHalf/Kabutops/Kabutops.png'),pygame.image.load('images/pokemon/firstHalf/Kabutops/Kabutops_back.png')]
KadabraSprites = [pygame.image.load('images/pokemon/firstHalf/Kadabra/Kadabra.png'),pygame.image.load('images/pokemon/firstHalf/Kadabra/Kadabra_back.png')]
KakunaSprites = [pygame.image.load('images/pokemon/firstHalf/Kakuna/Kakuna.png'),pygame.image.load('images/pokemon/firstHalf/Kakuna/Kakuna_back.png')]
KangaskhanSprites = [pygame.image.load('images/pokemon/firstHalf/Kangaskhan/Kangaskhan.png'),pygame.image.load('images/pokemon/firstHalf/Kangaskhan/Kangaskhan_back.png')]
KinglerSprites = [pygame.image.load('images/pokemon/firstHalf/Kingler/Kingler.png'),pygame.image.load('images/pokemon/firstHalf/Kingler/Kingler_back.png')]
KoffingSprites = [pygame.image.load('images/pokemon/firstHalf/Koffing/Koffing.png'),pygame.image.load('images/pokemon/firstHalf/Koffing/Koffing_back.png')]
KrabbySprites = [pygame.image.load('images/pokemon/firstHalf/Krabby/Krabby.png'),pygame.image.load('images/pokemon/firstHalf/Krabby/Krabby_back.png')]
LaprasSprites = [pygame.image.load('images/pokemon/firstHalf/Lapras/Lapras.png'),pygame.image.load('images/pokemon/firstHalf/Lapras/Lapras_back.png')]
LickitungSprites = [pygame.image.load('images/pokemon/firstHalf/Lickitung/Lickitung.png'),pygame.image.load('images/pokemon/firstHalf/Lickitung/Lickitung_back.png')]
MachampSprites = [pygame.image.load('images/pokemon/firstHalf/Machamp/Machamp.png'),pygame.image.load('images/pokemon/firstHalf/Machamp/Machamp_back.png')]
MachokeSprites = [pygame.image.load('images/pokemon/firstHalf/Machoke/Machoke.png'),pygame.image.load('images/pokemon/firstHalf/Machoke/Machoke_back.png')]
MachopSprites = [pygame.image.load('images/pokemon/firstHalf/Machop/Machop.png'),pygame.image.load('images/pokemon/firstHalf/Machop/Machop_back.png')]
MagikarpSprites = [pygame.image.load('images/pokemon/firstHalf/Magikarp/Magikarp.png'),pygame.image.load('images/pokemon/firstHalf/Magikarp/Magikarp_back.png')]
MagmarSprites = [pygame.image.load('images/pokemon/firstHalf/Magmar/Magmar.png'),pygame.image.load('images/pokemon/firstHalf/Magmar/Magmar_back.png')]
MagnemiteSprites = [pygame.image.load('images/pokemon/secondHalf/Magnemite/Magnemite.png'),pygame.image.load('images/pokemon/secondHalf/Magnemite/Magnemite_back.png')]
MagnetonSprites = [pygame.image.load('images/pokemon/secondHalf/Magneton/Magneton.png'),pygame.image.load('images/pokemon/secondHalf/Magneton/Magneton_back.png')]
MankeySprites = [pygame.image.load('images/pokemon/secondHalf/Mankey/Mankey.png'),pygame.image.load('images/pokemon/secondHalf/Mankey/Mankey_back.png')]
MarowakSprites = [pygame.image.load('images/pokemon/secondHalf/Marowak/Marowak.png'),pygame.image.load('images/pokemon/secondHalf/Marowak/Marowak_back.png')]
MeowthSprites = [pygame.image.load('images/pokemon/secondHalf/Meowth/Meowth.png'),pygame.image.load('images/pokemon/secondHalf/Meowth/Meowth_back.png')]
MetapodSprites = [pygame.image.load('images/pokemon/secondHalf/Metapod/Metapod.png'),pygame.image.load('images/pokemon/secondHalf/Metapod/Metapod_back.png')]
MewSprites = [pygame.image.load('images/pokemon/secondHalf/Mew/Mew.png'),pygame.image.load('images/pokemon/secondHalf/Mew/Mew_back.png')]
MewtwoSprites = [pygame.image.load('images/pokemon/secondHalf/Mewtwo/Mewtwo.png'),pygame.image.load('images/pokemon/secondHalf/Mewtwo/Mewtwo_back.png')]
MoltresSprites = [pygame.image.load('images/pokemon/secondHalf/Moltres/Moltres.png'),pygame.image.load('images/pokemon/secondHalf/Moltres/Moltres_back.png')]
Mr_MimeSprites = [pygame.image.load('images/pokemon/secondHalf/Mr_Mime/Mr_Mime.png'),pygame.image.load('images/pokemon/secondHalf/Mr_Mime/Mr_Mime_back.png')]
MukSprites = [pygame.image.load('images/pokemon/secondHalf/Muk/Muk.png'),pygame.image.load('images/pokemon/secondHalf/Muk/Muk_back.png')]
NidokingSprites = [pygame.image.load('images/pokemon/secondHalf/Nidoking/Nidoking.png'),pygame.image.load('images/pokemon/secondHalf/Nidoking/Nidoking_back.png')]
NidoqueenSprites = [pygame.image.load('images/pokemon/secondHalf/Nidoqueen/Nidoqueen.png'),pygame.image.load('images/pokemon/secondHalf/Nidoqueen/Nidoqueen_back.png')]
NidoranSprites = [pygame.image.load('images/pokemon/secondHalf/Nidoran/Nidoran.png'),pygame.image.load('images/pokemon/secondHalf/Nidoran/Nidoran_back.png')]
NidorinaSprites = [pygame.image.load('images/pokemon/secondHalf/Nidorina/Nidorina.png'),pygame.image.load('images/pokemon/secondHalf/Nidorina/Nidorina_back.png')]
NidorinoSprites = [pygame.image.load('images/pokemon/secondHalf/Nidorino/Nidorino.png'),pygame.image.load('images/pokemon/secondHalf/Nidorino/Nidorino_back.png')]
NinetalesSprites = [pygame.image.load('images/pokemon/secondHalf/Ninetales/Ninetales.png'),pygame.image.load('images/pokemon/secondHalf/Ninetales/Ninetales_back.png')]
OddishSprites = [pygame.image.load('images/pokemon/secondHalf/Oddish/Oddish.png'),pygame.image.load('images/pokemon/secondHalf/Oddish/Oddish_back.png')]
OmanyteSprites = [pygame.image.load('images/pokemon/secondHalf/Omanyte/Omanyte.png'),pygame.image.load('images/pokemon/secondHalf/Omanyte/Omanyte_back.png')]
OmastarSprites = [pygame.image.load('images/pokemon/secondHalf/Omastar/Omastar.png'),pygame.image.load('images/pokemon/secondHalf/Omastar/Omastar_back.png')]
OnixSprites = [pygame.image.load('images/pokemon/secondHalf/Onix/Onix.png'),pygame.image.load('images/pokemon/secondHalf/Onix/Onix_back.png')]
ParasSprites = [pygame.image.load('images/pokemon/secondHalf/Paras/Paras.png'),pygame.image.load('images/pokemon/secondHalf/Paras/Paras_back.png')]
ParasectSprites = [pygame.image.load('images/pokemon/secondHalf/Parasect/Parasect.png'),pygame.image.load('images/pokemon/secondHalf/Parasect/Parasect_back.png')]
PersianSprites = [pygame.image.load('images/pokemon/secondHalf/Persian/Persian.png'),pygame.image.load('images/pokemon/secondHalf/Persian/Persian_back.png')]
PidgeotSprites = [pygame.image.load('images/pokemon/secondHalf/Pidgeot/Pidgeot.png'),pygame.image.load('images/pokemon/secondHalf/Pidgeot/Pidgeot_back.png')]
PidgeottoSprites = [pygame.image.load('images/pokemon/secondHalf/Pidgeotto/Pidgeotto.png'),pygame.image.load('images/pokemon/secondHalf/Pidgeotto/Pidgeotto_back.png')]
PidgeySprites = [pygame.image.load('images/pokemon/secondHalf/Pidgey/Pidgey.png'),pygame.image.load('images/pokemon/secondHalf/Pidgey/Pidgey_back.png')]
PikachuSprites = [pygame.image.load('images/pokemon/secondHalf/Pikachu/Pikachu.png'),pygame.image.load('images/pokemon/secondHalf/Pikachu/Pikachu_back.png')]
PinsirSprites = [pygame.image.load('images/pokemon/secondHalf/Pinsir/Pinsir.png'),pygame.image.load('images/pokemon/secondHalf/Pinsir/Pinsir_back.png')]
PoliwagSprites = [pygame.image.load('images/pokemon/secondHalf/Poliwag/Poliwag.png'),pygame.image.load('images/pokemon/secondHalf/Poliwag/Poliwag_back.png')]
PoliwhirlSprites = [pygame.image.load('images/pokemon/secondHalf/Poliwhirl/Poliwhirl.png'),pygame.image.load('images/pokemon/secondHalf/Poliwhirl/Poliwhirl_back.png')]
PoliwrathSprites = [pygame.image.load('images/pokemon/secondHalf/Poliwrath/Poliwrath.png'),pygame.image.load('images/pokemon/secondHalf/Poliwrath/Poliwrath_back.png')]
PonytaSprites = [pygame.image.load('images/pokemon/secondHalf/Ponyta/Ponyta.png'),pygame.image.load('images/pokemon/secondHalf/Ponyta/Ponyta_back.png')]
PorygonSprites = [pygame.image.load('images/pokemon/secondHalf/Porygon/Porygon.png'),pygame.image.load('images/pokemon/secondHalf/Porygon/Porygon_back.png')]
PrimeapeSprites = [pygame.image.load('images/pokemon/secondHalf/Primeape/Primeape.png'),pygame.image.load('images/pokemon/secondHalf/Primeape/Primeape_back.png')]
PsyduckSprites = [pygame.image.load('images/pokemon/secondHalf/Psyduck/Psyduck.png'),pygame.image.load('images/pokemon/secondHalf/Psyduck/Psyduck_back.png')]
RaichuSprites = [pygame.image.load('images/pokemon/secondHalf/Raichu/Raichu.png'),pygame.image.load('images/pokemon/secondHalf/Raichu/Raichu_back.png')]
RapidashSprites = [pygame.image.load('images/pokemon/secondHalf/Rapidash/Rapidash.png'),pygame.image.load('images/pokemon/secondHalf/Rapidash/Rapidash_back.png')]
RaticateSprites = [pygame.image.load('images/pokemon/secondHalf/Raticate/Raticate.png'),pygame.image.load('images/pokemon/secondHalf/Raticate/Raticate_back.png')]
RattataSprites = [pygame.image.load('images/pokemon/secondHalf/Rattata/Rattata.png'),pygame.image.load('images/pokemon/secondHalf/Rattata/Rattata_back.png')]
RhydonSprites = [pygame.image.load('images/pokemon/secondHalf/Rhydon/Rhydon.png'),pygame.image.load('images/pokemon/secondHalf/Rhydon/Rhydon_back.png')]
RhyhornSprites = [pygame.image.load('images/pokemon/secondHalf/Rhyhorn/Rhyhorn.png'),pygame.image.load('images/pokemon/secondHalf/Rhyhorn/Rhyhorn_back.png')]
SandshrewSprites = [pygame.image.load('images/pokemon/secondHalf/Sandshrew/Sandshrew.png'),pygame.image.load('images/pokemon/secondHalf/Sandshrew/Sandshrew_back.png')]
SandslashSprites = [pygame.image.load('images/pokemon/secondHalf/Sandslash/Sandslash.png'),pygame.image.load('images/pokemon/secondHalf/Sandslash/Sandslash_back.png')]
ScytherSprites = [pygame.image.load('images/pokemon/secondHalf/Scyther/Scyther.png'),pygame.image.load('images/pokemon/secondHalf/Scyther/Scyther_back.png')]
SeadraSprites = [pygame.image.load('images/pokemon/secondHalf/Seadra/Seadra.png'),pygame.image.load('images/pokemon/secondHalf/Seadra/Seadra_back.png')]
SeakingSprites = [pygame.image.load('images/pokemon/secondHalf/Seaking/Seaking.png'),pygame.image.load('images/pokemon/secondHalf/Seaking/Seaking_back.png')]
SeelSprites = [pygame.image.load('images/pokemon/secondHalf/Seel/Seel.png'),pygame.image.load('images/pokemon/secondHalf/Seel/Seel_back.png')]
ShellderSprites = [pygame.image.load('images/pokemon/secondHalf/Shellder/Shellder.png'),pygame.image.load('images/pokemon/secondHalf/Shellder/Shellder_back.png')]
SlowbroSprites = [pygame.image.load('images/pokemon/secondHalf/Slowbro/Slowbro.png'),pygame.image.load('images/pokemon/secondHalf/Slowbro/Slowbro_back.png')]
SlowpokeSprites = [pygame.image.load('images/pokemon/secondHalf/Slowpoke/Slowpoke.png'),pygame.image.load('images/pokemon/secondHalf/Slowpoke/Slowpoke_back.png')]
SnorlaxSprites = [pygame.image.load('images/pokemon/secondHalf/Snorlax/Snorlax.png'),pygame.image.load('images/pokemon/secondHalf/Snorlax/Snorlax_back.png')]
SpearowSprites = [pygame.image.load('images/pokemon/secondHalf/Spearow/Spearow.png'),pygame.image.load('images/pokemon/secondHalf/Spearow/Spearow_back.png')]
SquirtleSprites = [pygame.image.load('images/pokemon/secondHalf/Squirtle/Squirtle.png'),pygame.image.load('images/pokemon/secondHalf/Squirtle/Squirtle_back.png')]
StarmieSprites = [pygame.image.load('images/pokemon/secondHalf/Starmie/Starmie.png'),pygame.image.load('images/pokemon/secondHalf/Starmie/Starmie_back.png')]
StaryuSprites = [pygame.image.load('images/pokemon/secondHalf/Staryu/Staryu.png'),pygame.image.load('images/pokemon/secondHalf/Staryu/Staryu_back.png')]
TangelaSprites = [pygame.image.load('images/pokemon/secondHalf/Tangela/Tangela.png'),pygame.image.load('images/pokemon/secondHalf/Tangela/Tangela_back.png')]
TaurosSprites = [pygame.image.load('images/pokemon/secondHalf/Tauros/Tauros.png'),pygame.image.load('images/pokemon/secondHalf/Tauros/Tauros_back.png')]
TentacoolSprites = [pygame.image.load('images/pokemon/secondHalf/Tentacool/Tentacool.png'),pygame.image.load('images/pokemon/secondHalf/Tentacool/Tentacool_back.png')]
TentacruelSprites = [pygame.image.load('images/pokemon/secondHalf/Tentacruel/Tentacruel.png'),pygame.image.load('images/pokemon/secondHalf/Tentacruel/Tentacruel_back.png')]
VaporeonSprites = [pygame.image.load('images/pokemon/secondHalf/Vaporeon/Vaporeon.png'),pygame.image.load('images/pokemon/secondHalf/Vaporeon/Vaporeon_back.png')]
VenomothSprites = [pygame.image.load('images/pokemon/secondHalf/Venomoth/Venomoth.png'),pygame.image.load('images/pokemon/secondHalf/Venomoth/Venomoth_back.png')]
VenonatSprites = [pygame.image.load('images/pokemon/secondHalf/Venonat/Venonat.png'),pygame.image.load('images/pokemon/secondHalf/Venonat/Venonat_back.png')]
VenusaurSprites = [pygame.image.load('images/pokemon/secondHalf/Venusaur/Venusaur.png'),pygame.image.load('images/pokemon/secondHalf/Venusaur/Venusaur_back.png')]
VictreebelSprites = [pygame.image.load('images/pokemon/secondHalf/Victreebel/Victreebel.png'),pygame.image.load('images/pokemon/secondHalf/Victreebel/Victreebel_back.png')]
VileplumeSprites = [pygame.image.load('images/pokemon/secondHalf/Vileplume/Vileplume.png'),pygame.image.load('images/pokemon/secondHalf/Vileplume/Vileplume_back.png')]
VoltorbSprites = [pygame.image.load('images/pokemon/secondHalf/Voltorb/Voltorb.png'),pygame.image.load('images/pokemon/secondHalf/Voltorb/Voltorb_back.png')]
VulpixSprites = [pygame.image.load('images/pokemon/secondHalf/Vulpix/Vulpix.png'),pygame.image.load('images/pokemon/secondHalf/Vulpix/Vulpix_back.png')]
WartortleSprites = [pygame.image.load('images/pokemon/secondHalf/Wartortle/Wartortle.png'),pygame.image.load('images/pokemon/secondHalf/Wartortle/Wartortle_back.png')]
WeedleSprites = [pygame.image.load('images/pokemon/secondHalf/Weedle/Weedle.png'),pygame.image.load('images/pokemon/secondHalf/Weedle/Weedle_back.png')]
WeepinbellSprites = [pygame.image.load('images/pokemon/secondHalf/Weepinbell/Weepinbell.png'),pygame.image.load('images/pokemon/secondHalf/Weepinbell/Weepinbell_back.png')]
WeezingSprites = [pygame.image.load('images/pokemon/secondHalf/Weezing/Weezing.png'),pygame.image.load('images/pokemon/secondHalf/Weezing/Weezing_back.png')]
WigglytuffSprites = [pygame.image.load('images/pokemon/secondHalf/Wigglytuff/Wigglytuff.png'),pygame.image.load('images/pokemon/secondHalf/Wigglytuff/Wigglytuff_back.png')]
ZapdosSprites = [pygame.image.load('images/pokemon/secondHalf/Zapdos/Zapdos.png'),pygame.image.load('images/pokemon/secondHalf/Zapdos/Zapdos_back.png')]
ZubatSprites = [pygame.image.load('images/pokemon/secondHalf/Zubat/Zubat.png'),pygame.image.load('images/pokemon/secondHalf/Zubat/Zubat_back.png')]

class pokedex:
    def __init__(self):
        self.cauhght = []

    @staticmethod
    def generatePokeList(self):
        mew = Pokemon("Mew", "Psychic", 1, 151, None,MewSprites[0],MewSprites[1],300)  # LEGENDARY
        mewtwo = Pokemon("Mewtwo", "Psychic", 1, 150, None,MewtwoSprites[0],MewtwoSprites[1],200)  # LEGENDARY
        dragonite = Pokemon("Dragonite", "Dragon/Flying", 20, 149, None,DragoniteSprites[0],DragoniteSprites[1],80)
        dragonair = Pokemon("Dragonair", "Dragon", 10, 148, dragonite,DragonairSprites[0],DragonairSprites[1],60)
        dratini = Pokemon("Dratini", "Dragon", 1, 147, dragonair,DratiniSprites[0],DratiniSprites[1],45)
        moltres = Pokemon("Moltres", "Fire/Flying", 1, 146, None,MoltresSprites[0],MoltresSprites[1],200)  # LEGENDARY
        zapdos = Pokemon("Zapdos", "Electric/Flying", 1, 145, None,ZapdosSprites[0],ZapdosSprites[1],200)  # LEGENDARY
        articuno = Pokemon("Articuno", "Ice/Flying", 1, 144, None,ArticunoSprites[0],ArticunoSprites[1],200)  # LEGENDARY
        snorlax = Pokemon("Snorlax", "Normal", 1, 143, None,SnorlaxSprites[0],SnorlaxSprites[1],45)
        aerodactyl = Pokemon("Aerodactyl", "Rock/Flying", 1, 142, None,AerodactylSprites[0],AerodactylSprites[1],45)
        kabutops = Pokemon("Kabutops", "Rock/Water", 10, 141, None,KabutopsSprites[0],KabutopsSprites[1],60)
        kabuto = Pokemon("Kabuto", "Rock/Water", 1, 140, kabutops,KabutoSprites[0],KabutoSprites[1],45)
        omastar = Pokemon("Omastar", "Rock/Water", 10, 139, None,OmastarSprites[0],OmastarSprites[1],60)
        omanyte = Pokemon("Omanyte", "Rock/Water", 1, 138, omastar,OmanyteSprites[0],OmanyteSprites[1],45)
        porygon = Pokemon("Porygon", "Normal", 1, 137, None,PorygonSprites[0],PorygonSprites[1],45)
        flareon = Pokemon("Flareon", "Fire", 10, 136, None,FlareonSprites[0],FlareonSprites[1],60)
        jolteon = Pokemon("Jolteon", "Electric", 10, 135, None,JolteonSprites[0],JolteonSprites[1],60)
        vaporeon = Pokemon("Vaporeon", "Water", 10, 134, None,VaporeonSprites[0],VaporeonSprites[1],60)
        eevee = Pokemon("Eevve", "Normal", 1, 133, None, EeveeSprites[0],EeveeSprites[1],45)  # CHECARLE COMO EVOLUCIONAR A ESTE VATO
        ditto = Pokemon("Ditto", "Normal", 1, 132, None,DittoSprites[0],DittoSprites[1],45)
        lapras = Pokemon("Lapras", "Water/Ice", 1, 131, None,LaprasSprites[0],LaprasSprites[1],45)
        gyarados = Pokemon("Gyarados", "Water/Flying", 10, 130, None,GyaradosSprites[0],GyaradosSprites[1],60)
        magikarp = Pokemon("Magikarp", "Water", 1, 129, gyarados,MagikarpSprites[0],MagikarpSprites[1],45)
        tauros = Pokemon("Tauros", "Normal", 1, 128, None,TaurosSprites[0],TaurosSprites[1],45)
        pinsir = Pokemon("Pinsir", "Bug", 1, 127, None,PinsirSprites[0],PinsirSprites[1],45)
        magmar = Pokemon("Magmar", "Fire", 1, 126, None,MagmarSprites[0],MagmarSprites[1],45)
        electabuzz = Pokemon("Electabuzz", "Electric", 1, 125, None,ElectabuzzSprites[0],ElectabuzzSprites[1],45)
        jynx = Pokemon("Jynx", "Ice/Psychic", 1, 124, None,JynxSprites[0],JynxSprites[1],45)
        scyther = Pokemon("Scyther", "Bug/Flying", 1, 123, None,ScytherSprites[0],ScytherSprites[1],45)
        mrMime = Pokemon("Mr. Mime", "Psychic", 1, 122, None,Mr_MimeSprites[0],Mr_MimeSprites[1],45)
        starmie = Pokemon("Starmie", "Water/Psychic", 1, 121, None,StarmieSprites[0],StarmieSprites[1],60)
        staryu = Pokemon("Staryu", "Water", 1, 120, None,StaryuSprites[0],StaryuSprites[1],45)
        seaking = Pokemon("Seaking", "Water", 10, 119, None,SeakingSprites[0],SeakingSprites[1],60)
        goldeen = Pokemon("Goldeen", "Water", 1, 118, seaking,GoldeenSprites[0],GoldeenSprites[1],45)
        seadra = Pokemon("Seadra", "Water", 10, 117, None,SeadraSprites[0],SeadraSprites[1],60)
        horsea = Pokemon("Horsea", "Water", 1, 116, seadra,HorseaSprites[0],HorseaSprites[1],45)
        kangaskhan = Pokemon("Kangaskhan", "Normal", 1, 115, None,KangaskhanSprites[0],KangaskhanSprites[1],45)
        tangela = Pokemon("Tangela", "Normal", 1, 114, None,TangelaSprites[0],TangelaSprites[1],45)
        chansey = Pokemon("Chansey", "Normal", 1, 113, None,ChanseySprites[0],ChanseySprites[1],45)
        rhydon = Pokemon("Rhydon", "Ground/Rock", 10, 112, None,RhydonSprites[0],RhydonSprites[1],60)
        rhyhorn = Pokemon("Rhyhorn", "Ground/Rock", 1, 111, rhydon,RhyhornSprites[0],RhyhornSprites[1],45)
        weezing = Pokemon("Weezing", "Poisonous", 10, 110, None,WeezingSprites[0],WeezingSprites[1],60)
        koffing = Pokemon("Koffing", "Poisonous", 1, 109, weezing,KoffingSprites[0],KoffingSprites[1],45)
        lickitung = Pokemon("Lickitung", "Normal", 1, 108, None,LickitungSprites[0],LickitungSprites[1],45)
        hitmonchan = Pokemon("Hitmonchan", "Fighting", 1, 107, None,HitmonchanSprites[0],HitmonchanSprites[1],45)
        hitmonlee = Pokemon("Hitmonlee", "Fighting", 1, 106, None,HitmonleeSprites[0],HitmonleeSprites[1],45)
        marowak = Pokemon("Marowak", "Ground", 10, 105, None,MarowakSprites[0],MarowakSprites[1],60)
        cubone = Pokemon("Cubone", "Ground", 1, 104, marowak,CuboneSprites[0],CuboneSprites[1],45)
        exeggutor = Pokemon("Exeggutor", "Plant/Psychic", 10, 103, None,ExeggutorSprites[0],ExeggutorSprites[1],60)
        exeggcute = Pokemon("Exeggcute", "Plant/Psychic", 1, 102, exeggutor,ExeggcuteSprites[0],ExeggcuteSprites[1],45)
        electrode = Pokemon("Electrode", "Electric", 10, 101, None,ElectrodeSprites[0],ElectrodeSprites[1],60)
        voltorb = Pokemon("Voltorb", "Electric", 1, 100, electrode,VoltorbSprites[0],VoltorbSprites[1],45)
        kingler = Pokemon("Kingler", "Water", 10, 99, None,KinglerSprites[0],KinglerSprites[1],60)
        krabby = Pokemon("Krabby", "Water", 1, 98, kingler,KrabbySprites[0],KrabbySprites[1],45)
        hypno = Pokemon("Hypno", "Psychic", 10, 97, None,HypnoSprites[0],HypnoSprites[1],60)
        drowzee = Pokemon("Drowzee", "Psychic", 1, 96, hypno,DrowzeeSprites[0],DrowzeeSprites[1],45)
        onix = Pokemon("Onix", "Ground/Rock", 1, 95, None,OnixSprites[0],OnixSprites[1],45)
        gengar = Pokemon("Gengar", "Ghost/Poisonous", 20, 94, None,GengarSprites[0],GengarSprites[1],80)
        haunter = Pokemon("Haunter", "Ghost/Poisonous", 10, 93, gengar,HaunterSprites[0],HaunterSprites[1],60)
        gastly = Pokemon("Gastly", "Ghost/Poisonous", 1, 92, haunter,GastlySprites[0],GastlySprites[1],45)
        cloyster = Pokemon("Cloyster", "Water/Ice", 10, 91, None,CloysterSprites[0],CloysterSprites[1],60)
        shellder = Pokemon("Shellder", "Water", 1, 90, cloyster,ShellderSprites[0],ShellderSprites[1],45)
        muk = Pokemon("Muk", "Poisonous", 10, 89, None,MukSprites[0],MukSprites[1],60)
        grimer = Pokemon("Grimer", "Poisonous", 1, 88, muk,GrimerSprites[0],GrimerSprites[1],45)
        dewgong = Pokemon("Dewgong", "Water/Ice", 10, 87, None,DewgongSprites[0],DewgongSprites[1],60)
        seel = Pokemon("Seel", "Water", 1, 86, dewgong,SeelSprites[0],SeelSprites[1],45)
        dodrio = Pokemon("Dodrio", "Normal/Flying", 10, 85, None,DodrioSprites[0],DodrioSprites[1],60)
        doduo = Pokemon("Doduo", "Normal/Flying", 1, 84, dodrio,DoduoSprites[0],DoduoSprites[1],45)
        farfetchd = Pokemon("Farfetch'd", "Normal/Flying", 1, 83, None,FarfetchSprites[0],FarfetchSprites[1],45)
        magneton = Pokemon("Magneton", "Electric", 10, 82, None,MagnetonSprites[0],MagnetonSprites[1],60)
        magnemite = Pokemon("Magnemite", "Electric", 1, 81, magneton,MagnemiteSprites[0],MagnemiteSprites[1],45)
        slowbro = Pokemon("Slowbro", "Water/Psychic", 10, 80, None,SlowbroSprites[0],SlowbroSprites[1],60)
        slowpoke = Pokemon("Slowpoke", "Water/Psychic", 1, 79, slowbro,SlowpokeSprites[0],SlowpokeSprites[1],45)
        rapidash = Pokemon("Rapidash", "Fire", 10, 78, None,RapidashSprites[0],RapidashSprites[1],60)
        ponyta = Pokemon("Ponyta", "Fire", 1, 77, rapidash,PonytaSprites[0],PonytaSprites[1],45)
        golem = Pokemon("Golem", "Rock/Ground", 20, 76, None,GolemSprites[0],GolemSprites[1],80)
        graveler = Pokemon("Graveler", "Rock/Ground", 10, 75, golem,GravelerSprites[0],GravelerSprites[1],60)
        geodude = Pokemon("Geodude", "Rock/Ground", 1, 74, graveler,GeodudeSprites[0],GeodudeSprites[1],45)
        tentacruel = Pokemon("Tentacruel", 10, "Water/Poisonous", 73, None,TentacruelSprites[0],TentacruelSprites[1],60)
        tentacool = Pokemon("Tentacool", "Water/Poisonous", 1, 72, tentacruel,TentacoolSprites[0],TentacoolSprites[1],45)
        victreebel = Pokemon("Victreebel", "Plant/Poisonous", 20, 71, None, VictreebelSprites[0], VictreebelSprites[1],80)
        weepinbell = Pokemon("Weepinbell", "Plant/Poisonous", 10, 70, victreebel,WeepinbellSprites[0],WeepinbellSprites[1],60)
        bellsprout = Pokemon("Bellsprout", "Plant/Poisonous", 1, 69, weepinbell,BellsproutSprites[0],BellsproutSprites[1],45)
        machamp = Pokemon("Machamp", "Fighting", 20, 68, None,MachampSprites[0],MachampSprites[1],80)
        machoke = Pokemon("Machoke","Fighting", 10, 67, machamp,MachokeSprites[0],MachokeSprites[1],60)
        machop = Pokemon("Machop", "Fighting", 1, 66, machoke,MachopSprites[0],MachopSprites[1],45)
        alakazam = Pokemon("Alakazam", "Psychic", 20, 65, None,AlakazamSprites[0],AlakazamSprites[1],80)
        kadabra = Pokemon("Kadabra", "Psychic", 10, 64, alakazam,KadabraSprites[0],KadabraSprites[1],60)
        abra = Pokemon("Abra", "Psychic", 1, 63, kadabra,AbraSprites[0],AbraSprites[1],45)
        poliwrath = Pokemon("Poliwrath", "Water", 20, 62, None,PoliwrathSprites[0],PoliwrathSprites[1],80)
        poliwhirl = Pokemon("Poliwhirl", "Water", 10, 61, poliwrath,PoliwhirlSprites[0],PoliwhirlSprites[1],60)
        poliwag = Pokemon("Poliwag", "Water", 1, 60, poliwhirl,PoliwagSprites[0],PoliwagSprites[1],45)
        arcanine = Pokemon("Arcanine", "Fire", 10, 59, None,ArcanineSprites[0],ArcanineSprites[1],60)
        growlithe = Pokemon("Growlithe", "Fire", 1, 58, arcanine,GrowlitheSprites[0],GrowlitheSprites[1],45)
        primeape = Pokemon("Primeape", "Fighting", 10, 57, None,PrimeapeSprites[0],PrimeapeSprites[1],60)
        mankey = Pokemon("Mankey", "Fighting", 1, 56, primeape,MankeySprites[0],MankeySprites[1],45)
        golduck = Pokemon("Golduck", "Water", 10, 55, None,GolduckSprites[0],GolduckSprites[1],60)
        psyduck = Pokemon("Psyduck", "Water", 1, 54, golduck,PsyduckSprites[0],PsyduckSprites[1],45)
        persian = Pokemon("Persian", "Normal", 10, 53, None,PersianSprites[0],PersianSprites[1],60)
        meowth = Pokemon("Meowth", "Normal", 1, 52, persian,MeowthSprites[0],MeowthSprites[1],45)
        dugtrio = Pokemon("Dugtrio", 10, "Ground", 51, None,DugtrioSprites[0],DugtrioSprites[1],60)
        diglett = Pokemon("Diglett", "Ground", 1, 50, dugtrio,DiglettSprites[0],DiglettSprites[1],45)
        venomoth = Pokemon("Venomoth", "Bug/Poisonous", 10, 49, None,VenomothSprites[0],VenomothSprites[1],60)
        venonat = Pokemon("Venonat", "Bug/Poisonous", 1, 48, venomoth,VenonatSprites[0],VenonatSprites[1],45)
        parasect = Pokemon("Parasect", "Bug/Plant", 10, 47, None,ParasectSprites[0],ParasectSprites[1],60)
        paras = Pokemon("Paras", "Bug/Plant", 1, 46, parasect,ParasSprites[0],ParasectSprites[1],45)
        vileplume = Pokemon("Vileplume", "Bug/Plant", 20, 45, None,VileplumeSprites[0],VileplumeSprites[1],80)
        gloom = Pokemon("Gloom", "Bug/Plant", 10, 44, vileplume,GloomSprites[0],GloomSprites[1],60)
        oddish = Pokemon("Oddish", "Bug/Plant", 1, 43, gloom,OddishSprites[0],OddishSprites[1],45)
        golbat = Pokemon("Golbat", "Poisonous/Flying", 10, 42, None,GolbatSprites[0],GolbatSprites[1],60)
        zubat = Pokemon("Zubat", "Poisonous/Flying", 1, 41, golbat,ZubatSprites[0],ZubatSprites[1],45)
        wigglytuff = Pokemon("Wigglytuff", "Normal", 10, 40, None,WigglytuffSprites[0],WigglytuffSprites[1],60)
        jigglypuff = Pokemon("Jigglypuff", "Normal", 1, 39, wigglytuff,JigglypuffSprites[0],JigglypuffSprites[1],45)
        ninetales = Pokemon("Ninetales", "Fire", 10, 38, None,NinetalesSprites[0],NinetalesSprites[1],60)
        vulpix = Pokemon("Vulpix", "Fire", 1, 37, ninetales,VulpixSprites[0],VulpixSprites[1],45)
        clefable = Pokemon("Clefable", "Normal", 10, 36, None,ClefableSprites[0],ClefableSprites[1],60)
        clefairy = Pokemon("Clefairy", "Normal", 1, 35, clefable,ClefairySprites[0],ClefairySprites[1],45)
        nidoking = Pokemon("Nidoking", "Poisonous/Ground", 20, 34, None,NidokingSprites[0],NidokingSprites[1],80)
        nidorino = Pokemon("Nidorino", "Poisonous", 10, 33, nidoking,NidorinoSprites[0],NidorinoSprites[1],60)
        nidoranMale = Pokemon("Nidoran♂", "Poisonous", 1, 32, nidorino,NidoranSprites[0],NidoranSprites[1],45)
        nidoqueen = Pokemon("Nidoqueen", "Poisonous/Ground", 20, 31, None,NidoqueenSprites[0],NidoqueenSprites[1],80)
        nidorina = Pokemon("Nidorina", "Poisonous/Ground", 10, 30, nidoqueen,NidorinaSprites[0],NidorinaSprites[1],60)
        nidoranFemale = Pokemon("Nidoran♀", "Poisonous", 1, 29, nidorina,NidoranSprites[0],NidoranSprites[1],45)
        sandslash = Pokemon("Sandslash", "Ground", 10, 28, None,SandslashSprites[0],SandslashSprites[1],60)
        sandshrew = Pokemon("Sandshrew", "Ground", 1, 27, sandslash,SandshrewSprites[0],SandshrewSprites[1],45)
        raichu = Pokemon("Raichu", "Electric", 10, 26, None,RaichuSprites[0],RaichuSprites[1],80)
        pikachu = Pokemon("Pikachu", "Electric", 1, 25, raichu,PikachuSprites[0],PikachuSprites[1],60)
        arbok = Pokemon("Arbok", "Poisonous", 10, 24, None,ArbokSprites[0],ArbokSprites[1],60)
        ekans = Pokemon("Ekans", "Poisonous", 1, 23, arbok,EkansSprites[0],EkansSprites[1],45)
        fearow = Pokemon("Fearow", "Normal/Flying", 10, 22, None,FearowSprites[0], FearowSprites[1],60)
        spearow = Pokemon("Spearow", "Normal/Flying", 1, 21, fearow,SpearowSprites[0],SpearowSprites[1],45)
        raticate = Pokemon("Raticate", "Normal", 10, 20, None,RaticateSprites[0],RaticateSprites[1],60)
        rattata = Pokemon("Rattata", "Normal", 1, 19, raticate,RattataSprites[0],RattataSprites[1],45)
        pidgeot = Pokemon("Pidgeot", "Normal/Flying", 20, 18, None,PidgeotSprites[0],PidgeotSprites[1],80)
        pidgeotto = Pokemon("Pidgeotto", "Normal/Flying", 10, 17, pidgeot,PidgeottoSprites[0],PidgeottoSprites[1],60)
        pidgey = Pokemon("Pidgey","Normal/Flying", 1, 16, pidgeotto,PidgeySprites[0],PidgeySprites[1],45)
        beedrill = Pokemon("Beedrill", "Bug/Poisonous", 20, 15, None,BeedrillSprites[0],BeedrillSprites[1],80)
        kakuna = Pokemon("Kakuna", "Bug/Poisonous", 10, 14, beedrill,KakunaSprites[0],KakunaSprites[1],60)
        weedle = Pokemon("Weedle", "Bug/Poisnous", 1, 13, kakuna,WeedleSprites[0],WeedleSprites[1],45)
        butterfree = Pokemon("Butterfree", "Bug/Flying", 20, 12, None,ButterfreeSprites[0],ButterfreeSprites[1],80)
        metapod = Pokemon("Metapod", "Bug", 10, 11, butterfree,MetapodSprites[0],MetapodSprites[1],60)
        caterpie = Pokemon("Caterpie", "Bug", 1, 10, metapod,CaterpieSprites[0],CaterpieSprites[1],45)
        blastoise = Pokemon("Blastoise", "Water", 20, 9, None,BlastoiseSprites[0],BlastoiseSprites[1],80)
        wartortle = Pokemon("Wartortle", "Water", 10, 8, blastoise,WartortleSprites[0],WartortleSprites[1],60)
        squirtle = Pokemon("Squirtle", "Water", 1, 7, wartortle,SquirtleSprites[0],SquirtleSprites[1],45)
        charizard = Pokemon("Charizard", "Fire/Flying", 20, 6, None,CharizardSprites[0],CharizardSprites[1],80)
        charmeleon = Pokemon("Charmeleon", "Fire", 10, 5, charizard,CharmeleonSprites[0],CharmeleonSprites[1],60)
        charmander = Pokemon("Charmander", "Fire", 1, 4, charmeleon,CharmanderSprites[0],CharmanderSprites[1],45)
        venusaur = Pokemon("Venusaur", "Plant/Poisonous", 20, 3, None,VenusaurSprites[0],VenusaurSprites[1],80)
        ivysaur = Pokemon("Ivysaur", "Plant/Poisonous", 10, 2, venusaur,IvysaurSprites[0],IvysaurSprites[1],60)
        bulbasaur = Pokemon("Bulbasaur", "Plant/Poisonous", 1, 1, ivysaur,BulbasaurSprites[0],BulbasaurSprites[1],45)

        pkList = [bulbasaur, ivysaur, venusaur, charmander, charmeleon, charizard, squirtle, wartortle, blastoise,
                  caterpie, metapod, butterfree, weedle, kakuna, beedrill, pidgey,
                  pidgeotto, pidgeot, rattata, raticate, spearow, fearow, ekans, arbok, pikachu, raichu, sandshrew,
                  sandslash, nidoranFemale, nidorina, nidoqueen, nidoranMale, nidorino, nidoking, clefairy,
                  clefable, vulpix, ninetales, jigglypuff, wigglytuff, zubat, golbat, oddish, gloom, vileplume, paras,
                  parasect, venonat, venomoth, diglett, dugtrio, meowth, persian, psyduck, golduck, mankey,
                  primeape, growlithe, arcanine, poliwag, poliwhirl, poliwrath, abra, kadabra, alakazam, machop,
                  machoke, machamp, bellsprout, weepinbell, victreebel, tentacool, tentacruel, geodude, graveler,
                  golem, ponyta, rapidash, slowpoke, slowbro, magnemite, magneton, farfetchd, doduo, dodrio, seel,
                  dewgong, grimer, muk, shellder, cloyster, gastly, haunter, gengar, onix, drowzee, hypno, krabby,
                  kingler, voltorb, electrode, exeggcute, exeggutor, cubone, marowak, hitmonlee, hitmonchan, lickitung,
                  koffing, weezing, rhyhorn, rhydon, chansey, tangela, kangaskhan, horsea, seadra, goldeen,
                  seaking, staryu, starmie, mrMime, scyther, jynx, electabuzz, magmar, pinsir, tauros, magikarp,
                  gyarados, lapras, ditto, eevee, vaporeon, jolteon, flareon, porygon, omanyte, omastar, kabuto,
                  kabutops,
                  aerodactyl, snorlax, articuno, zapdos, moltres, dratini, dragonair, dragonite, mewtwo, mew]

        return pkList

    def zonePkAvailable(self,lr,rg):
        return Pokedex.generatePokeList()[lr:rg]
