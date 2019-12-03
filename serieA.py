#-------------------------------------------------------------------------------
# Name:        serieA
# Purpose:
#
# Author:      Lorenzo Bolognese
#
# Created:     28/11/2019
# Copyright:   (c) Lorenzo Bolognese 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

from player import Player
from formation import *

def Atalanta():
    name = "Atalanta BC"
    tactics = F343
    chariness = 1
    p1 = Player(0, 20, 40, 67, 'GK', ["L", "R", "C"], 'GOLLINI Pierluigi')
    p2 = Player(0, 2, 3, 5, 'GK', ["L", "R", "C"], 'ROSSI Francesco')
    p3 = Player(0, 2, 3, 5, 'GK', ["L", "R", "C"], 'SPORTIELLO Marco')
    p4 = Player(19, 38, 64, 0, 'D', ["L", "R", "C"], 'HATEBOER Hans')
    p5 = Player(17, 34, 57, 0, 'D', ["L", "R", "C"], 'CASTAGNE Timothy')
    p6 = Player(16, 32, 54, 0, 'D', ["L", "R", "C"], 'GOSENS Robin')
    p7 = Player(12, 23, 39, 0, 'D', ["L", "R", "C"], 'PALOMINO José Luis')
    p8 = Player(11, 22, 36, 0, 'D', ["L", "R", "C"], 'KJAER Simon')
    p9 = Player(11, 22, 36, 0, 'D', ["L", "R", "C"], 'TOLOI Rafael')
    p10 = Player(10, 19, 32, 0, 'D', ["L", "R", "C"], 'MASIELLO Andrea')
    p11 = Player(8, 15, 25, 0, 'D', ["L", "R", "C"], 'DJIMSITI Berat')
    p12 = Player(8, 15, 25, 0, 'D', ["L", "R", "C"], 'ARANA Guilherme')
    p13 = Player(3, 7, 11, 0, 'D', ["L", "R", "C"], 'IBANEZ -')
    p14 = Player(58, 96, 29, 0, 'M', ["L", "R", "C"], 'GOMEZ Alejandro')
    p15 = Player(38, 63, 19, 0, 'M', ["L", "R", "C"], 'FREULER Remo')
    p16 = Player(38, 63, 19, 0, 'M', ["L", "R", "C"], 'PASALIC Mario')
    p17 = Player(35, 59, 18, 0, 'M', ["L", "R", "C"], 'DE ROON Marten')
    p18 = Player(26, 44, 13, 0, 'M', ["L", "R", "C"], 'MALINOVSKIY Ruslan')
    p19 = Player(73, 44, 22, 0, 'A', ["L", "R", "C"], 'ZAPATA Duvan')
    p20 = Player(63, 38, 19, 0, 'A', ["L", "R", "C"], 'ILICIC Josip')
    p21 = Player(41, 25, 12, 0, 'A', ["L", "R", "C"], 'MURIEL Luis')
    p22 = Player(20, 12, 6, 0, 'A', ["L", "R", "C"], 'BARROW Musa')
    p23 = Player(6, 4, 2, 0, 'A', ["L", "R", "C"], 'PICCOLI Roberto')
    return name, tactics, chariness, [p1, p4, p5, p6, p14, p15, p16, p17, p19, p20, p21]

def Bologna():
    name = "Bologna FC"
    tactics = F433
    chariness = 2
    p1 = Player(0, 13, 20, 67, 'GK', ["L", "R", "C"], 'SKORUPSKI Lukasz')
    p2 = Player(0, 1, 2, 5, 'GK', ["L", "R", "C"], 'DA COSTA Angelo')
    p3 = Player(0, 1, 2, 5, 'GK', ["L", "R", "C"], 'SARR Mouhamadou')
    p4 = Player(7, 11, 36, 0, 'D', ["L", "R", "C"], 'DANILO Larangeira')
    p5 = Player(5, 8, 25, 0, 'D', ["L", "R", "C"], 'TOMIYASU Takehiro')
    p6 = Player(5, 8, 25, 0, 'D', ["L", "R", "C"], 'DENSWIL Stefano')
    p7 = Player(5, 8, 25, 0, 'D', ["L", "R", "C"], 'MBAYE Ibrahima')
    p8 = Player(4, 6, 21, 0, 'D', ["L", "R", "C"], 'DIJKS Mitchell')
    p9 = Player(3, 4, 14, 0, 'D', ["L", "R", "C"], 'BANI Mattia')
    p10 = Player(2, 3, 11, 0, 'D', ["L", "R", "C"], 'PAZ Nehuén')
    p11 = Player(1, 1, 4, 0, 'D', ["L", "R", "C"], 'CORBO Gabriele')
    p12 = Player(17, 56, 11, 0, 'M', ["L", "R", "C"], 'SORIANO Roberto')
    p13 = Player(12, 41, 8, 0, 'M', ["L", "R", "C"], 'POLI Andrea')
    p14 = Player(10, 33, 7, 0, 'M', ["L", "R", "C"], 'DZEMAILI Blerim')
    p15 = Player(9, 30, 6, 0, 'M', ["L", "R", "C"], 'SCHOUTEN Jerdy')
    p16 = Player(7, 22, 4, 0, 'M', ["L", "R", "C"], 'MEDEL Gary')
    p17 = Player(6, 19, 4, 0, 'M', ["L", "R", "C"], 'SVANBERG Mattias')
    p18 = Player(5, 15, 3, 0, 'M', ["L", "R", "C"], 'KREJCI Ladislav')
    p19 = Player(43, 13, 9, 0, 'A', ["L", "R", "C"], 'ORSOLINI Riccardo')
    p20 = Player(33, 10, 7, 0, 'A', ["L", "R", "C"], 'SANSONE Nicola')
    p21 = Player(31, 9, 6, 0, 'A', ["L", "R", "C"], 'PALACIO Rodrigo')
    p22 = Player(29, 9, 6, 0, 'A', ["L", "R", "C"], 'SANTANDER Federico')
    p23 = Player(25, 8, 5, 0, 'A', ["L", "R", "C"], 'DESTRO Mattia')
    p24 = Player(22, 7, 4, 0, 'A', ["L", "R", "C"], 'SKOV OLSEN Andreas')
    p25 = Player(2, 1, 0, 0, 'A', ["L", "R", "C"], 'JUWARA Musa')
    return name, tactics, chariness, [p1, p4, p5, p6, p7, p12, p13, p14, p19, p20, p21]

def Brescia():
    name = "Brescia Calcio"
    tactics = F433
    chariness = 2
    p1 = Player(0, 6, 6, 57, 'GK', ["L", "R", "C"], 'JORONEN Jesse')
    p2 = Player(0, 1, 1, 5, 'GK', ["L", "R", "C"], 'ALFONSO Enrico')
    p3 = Player(0, 1, 1, 5, 'GK', ["L", "R", "C"], 'ANDRENACCI Lorenzo')
    p4 = Player(3, 3, 29, 0, 'D', ["L", "R", "C"], 'MARTELLA Bruno')
    p5 = Player(3, 3, 25, 0, 'D', ["L", "R", "C"], 'MAGNANI Giangiacomo')
    p6 = Player(2, 2, 21, 0, 'D', ["L", "R", "C"], 'SABELLI Stefano')
    p7 = Player(2, 2, 18, 0, 'D', ["L", "R", "C"], 'CISTANA Andrea')
    p8 = Player(2, 2, 18, 0, 'D', ["L", "R", "C"], 'CHANCELLOR Jhon')
    p9 = Player(2, 2, 18, 0, 'D', ["L", "R", "C"], 'GASTALDELLO Daniele')
    p10 = Player(1, 1, 14, 0, 'D', ["L", "R", "C"], 'MATEJU Ales')
    p11 = Player(1, 1, 11, 0, 'D', ["L", "R", "C"], 'CURCIO Felipe')
    p12 = Player(0, 0, 4, 0, 'D', ["L", "R", "C"], 'MANGRAVITI Massimiliano')
    p13 = Player(0, 0, 4, 0, 'D', ["L", "R", "C"], 'SEMPRINI Alessandro')
    p14 = Player(4, 44, 4, 0, 'M', ["L", "R", "C"], 'BISOLI Dimitri')
    p15 = Player(4, 41, 4, 0, 'M', ["L", "R", "C"], 'ROMULO Orestes')
    p16 = Player(4, 41, 4, 0, 'M', ["L", "R", "C"], 'TONALI Sandro')
    p17 = Player(4, 37, 4, 0, 'M', ["L", "R", "C"], 'ZMRHAL Jaromir')
    p18 = Player(3, 33, 3, 0, 'M', ["L", "R", "C"], 'SPALEK Nikolas')
    p19 = Player(3, 26, 3, 0, 'M', ["L", "R", "C"], 'NDOJ Emanuele')
    p20 = Player(2, 22, 2, 0, 'M', ["L", "R", "C"], 'DESSENA Daniele')
    p21 = Player(2, 19, 2, 0, 'M', ["L", "R", "C"], 'TREMOLADA Luca')
    p22 = Player(0, 4, 0, 0, 'M', ["L", "R", "C"], 'VIVIANI Mattia')
    p23 = Player(49, 5, 5, 0, 'A', ["L", "R", "C"], 'BALOTELLI Mario')
    p24 = Player(39, 4, 4, 0, 'A', ["L", "R", "C"], 'DONNARUMMA Alfredo')
    p25 = Player(25, 3, 3, 0, 'A', ["L", "R", "C"], 'AYE Florian')
    p26 = Player(24, 2, 2, 0, 'A', ["L", "R", "C"], 'TORREGROSSA Ernesto')
    p27 = Player(18, 2, 2, 0, 'A', ["L", "R", "C"], 'MATRI Alessandro')
    p28 = Player(14, 1, 1, 0, 'A', ["L", "R", "C"], 'MOROSINI Leonardo')
    return name, tactics, chariness, [p1, p4, p5, p6, p14, p15, p16, p17, p19, p20, p21]

def Cagliari():
    name = "Cagliari Calcio"
    tactics = F433
    chariness = 2
    p1 = Player(0, 13, 34, 67, 'GK', ["L", "R", "C"], 'CRAGNO Alessio')
    p2 = Player(0, 2, 5, 10, 'GK', ["L", "R", "C"], 'RAFAEL De Andrade Bittencourt')
    p3 = Player(0, 2, 5, 10, 'GK', ["L", "R", "C"], 'OLSEN Robin')
    p4 = Player(0, 1, 3, 5, 'GK', ["L", "R", "C"], 'ARESTI Simone')
    p5 = Player(6, 15, 29, 0, 'D', ["L", "R", "C"], 'PELLEGRINI Luca')
    p6 = Player(6, 15, 29, 0, 'D', ["L", "R", "C"], 'CEPPITELLI Luca')
    p7 = Player(5, 13, 25, 0, 'D', ["L", "R", "C"], 'CACCIATORE Fabrizio')
    p8 = Player(4, 11, 21, 0, 'D', ["L", "R", "C"], 'KLAVAN Ragnar')
    p9 = Player(4, 11, 21, 0, 'D', ["L", "R", "C"], 'PISACANE Fabio')
    p10 = Player(3, 7, 14, 0, 'D', ["L", "R", "C"], 'MATTIELLO Federico')
    p11 = Player(3, 7, 14, 0, 'D', ["L", "R", "C"], 'LYKOGIANNIS Charalampos')
    p12 = Player(1, 4, 7, 0, 'D', ["L", "R", "C"], 'WALUKIEWICZ Sebastian')
    p13 = Player(1, 2, 4, 0, 'D', ["L", "R", "C"], 'PINNA Simone')
    p14 = Player(39, 78, 16, 0, 'M', ["L", "R", "C"], 'NAINGGOLAN Radja')
    p15 = Player(26, 52, 10, 0, 'M', ["L", "R", "C"], 'CASTRO Lucas')
    p16 = Player(24, 48, 10, 0, 'M', ["L", "R", "C"], 'NANDEZ Nahitan')
    p17 = Player(21, 41, 8, 0, 'M', ["L", "R", "C"], 'BIRSA Valter')
    p18 = Player(19, 37, 7, 0, 'M', ["L", "R", "C"], 'IONITA Artur')
    p19 = Player(17, 33, 7, 0, 'M', ["L", "R", "C"], 'ROG Marko')
    p20 = Player(15, 30, 6, 0, 'M', ["L", "R", "C"], 'CIGARINI Luca')
    p21 = Player(10, 19, 4, 0, 'M', ["L", "R", "C"], 'OLIVA Christian')
    p22 = Player(10, 19, 4, 0, 'M', ["L", "R", "C"], 'FARAGÒ Paolo')
    p23 = Player(8, 15, 3, 0, 'M', ["L", "R", "C"], 'DEIOLA Alessandro')
    p24 = Player(49, 25, 10, 0, 'A', ["L", "R", "C"], 'PAVOLETTI Leonardo')
    p25 = Player(37, 19, 7, 0, 'A', ["L", "R", "C"], 'JOAO PEDRO Geraldino Galvao')
    p26 = Player(35, 18, 7, 0, 'A', ["L", "R", "C"], 'SIMEONE Giovanni')
    p27 = Player(16, 8, 3, 0, 'A', ["L", "R", "C"], 'CERRI Alberto')
    p28 = Player(6, 3, 1, 0, 'A', ["L", "R", "C"], 'RAGATZU Daniele')
    return name, tactics, chariness, [p1, p4, p5, p6, p14, p15, p16, p17, p19, p20, p21]

def Fiorentina():
    name = "ACF Fiorentina"
    tactics = F433
    chariness = 2
    p1 = Player(0, 11, 29, 57, 'GK', ["L", "R", "C"], 'DRAGOWSKI Bartlomiej')
    p2 = Player(0, 1, 3, 5, 'GK', ["L", "R", "C"], 'TERRACCIANO Pietro')
    p3 = Player(10, 25, 50, 0, 'D', ["L", "R", "C"], 'MILENKOVIC Nikola')
    p4 = Player(9, 23, 46, 0, 'D', ["L", "R", "C"], 'PEZZELLA German')
    p5 = Player(7, 18, 36, 0, 'D', ["L", "R", "C"], 'LIROLA Pol')
    p6 = Player(6, 15, 29, 0, 'D', ["L", "R", "C"], 'CACERES Martín')
    p7 = Player(5, 13, 25, 0, 'D', ["L", "R", "C"], 'DALBERT Henrique')
    p8 = Player(4, 11, 21, 0, 'D', ["L", "R", "C"], 'VENUTI Lorenzo')
    p9 = Player(4, 9, 18, 0, 'D', ["L", "R", "C"], 'CECCHERINI Federico')
    p10 = Player(3, 7, 14, 0, 'D', ["L", "R", "C"], 'RASMUSSEN Jacob')
    p11 = Player(2, 6, 11, 0, 'D', ["L", "R", "C"], 'TERZIC Aleksa')
    p12 = Player(1, 4, 7, 0, 'D', ["L", "R", "C"], 'RANIERI Luca')
    p13 = Player(45, 89, 18, 0, 'M', ["L", "R", "C"], 'CHIESA Federico')
    p14 = Player(41, 81, 16, 0, 'M', ["L", "R", "C"], 'RIBERY Franck')
    p15 = Player(39, 78, 16, 0, 'M', ["L", "R", "C"], 'PULGAR Erick')
    p16 = Player(32, 63, 13, 0, 'M', ["L", "R", "C"], 'BENASSI Marco')
    p17 = Player(24, 48, 10, 0, 'M', ["L", "R", "C"], 'GHEZZAL Rachid')
    p18 = Player(21, 41, 8, 0, 'M', ["L", "R", "C"], 'BADELJ Milan')
    p19 = Player(13, 26, 5, 0, 'M', ["L", "R", "C"], 'ZURKOWSKI Szymon')
    p20 = Player(13, 26, 5, 0, 'M', ["L", "R", "C"], 'CASTROVILLI Gaetano')
    p21 = Player(11, 22, 4, 0, 'M', ["L", "R", "C"], 'DABO Bryan')
    p22 = Player(11, 22, 4, 0, 'M', ["L", "R", "C"], 'EYSSERIC Valentin')
    p23 = Player(8, 15, 3, 0, 'M', ["L", "R", "C"], 'CRISTOFORO Sebastian')
    p24 = Player(2, 4, 1, 0, 'M', ["L", "R", "C"], 'MONTIEL Cristobal')
    p25 = Player(41, 21, 8, 0, 'A', ["L", "R", "C"], 'PEDRO -')
    p26 = Player(39, 20, 8, 0, 'A', ["L", "R", "C"], 'BOATENG Kevin-Prince')
    p27 = Player(18, 9, 4, 0, 'A', ["L", "R", "C"], 'THEREAU Cyril')
    p28 = Player(8, 4, 2, 0, 'A', ["L", "R", "C"], 'SOTTIL Riccardo')
    p29 = Player(8, 4, 2, 0, 'A', ["L", "R", "C"], 'VLAHOVIC Dusan')
    return name, tactics, chariness, [p1, p4, p5, p6, p14, p15, p16, p17, p19, p20, p21]

def Genoa():
    name = "Genoa CFC"
    tactics = F343
    chariness = 2
    p1 = Player(0, 5, 10, 52, 'GK', ["L", "R", "C"], 'RADU Ionut')
    p2 = Player(0, 1, 1, 5, 'GK', ["L", "R", "C"], 'JANDREI Chitolina Carniel')
    p3 = Player(0, 1, 1, 5, 'GK', ["L", "R", "C"], 'MARCHETTI Federico')
    p4 = Player(0, 1, 1, 5, 'GK', ["L", "R", "C"], 'VODISEK Rok')
    p5 = Player(5, 10, 50, 0, 'D', ["L", "R", "C"], 'CRISCITO Domenico')
    p6 = Player(4, 8, 39, 0, 'D', ["L", "R", "C"], 'ROMERO Cristian')
    p7 = Player(4, 7, 36, 0, 'D', ["L", "R", "C"], 'ZAPATA Cristian')
    p8 = Player(3, 6, 29, 0, 'D', ["L", "R", "C"], 'BIRASCHI Davide')
    p9 = Player(3, 5, 25, 0, 'D', ["L", "R", "C"], 'BARRECA Antonio')
    p10 = Player(3, 5, 25, 0, 'D', ["L", "R", "C"], 'PAJAC Marko')
    p11 = Player(2, 4, 18, 0, 'D', ["L", "R", "C"], 'ANKERSEN Peter')
    p12 = Player(2, 4, 18, 0, 'D', ["L", "R", "C"], 'GOLDANIGA Edoardo')
    p13 = Player(2, 4, 18, 0, 'D', ["L", "R", "C"], 'GHIGLIONE Paolo')
    p14 = Player(1, 2, 11, 0, 'D', ["L", "R", "C"], 'EL YAMIQ Jawad')
    p15 = Player(11, 56, 6, 0, 'M', ["L", "R", "C"], 'SCHONE Lasse')
    p16 = Player(10, 48, 5, 0, 'M', ["L", "R", "C"], 'SAPONARA Riccardo')
    p17 = Player(9, 44, 4, 0, 'M', ["L", "R", "C"], 'PANDEV Goran')
    p18 = Player(6, 30, 3, 0, 'M', ["L", "R", "C"], 'LERAGER Lukas')
    p19 = Player(6, 30, 3, 0, 'M', ["L", "R", "C"], 'JAGIELLO Filip')
    p20 = Player(5, 26, 3, 0, 'M', ["L", "R", "C"], 'RADOVANOVIC Ivan')
    p21 = Player(4, 22, 2, 0, 'M', ["L", "R", "C"], 'STURARO Stefano')
    p22 = Player(4, 19, 2, 0, 'M', ["L", "R", "C"], 'CASSATA Francesco')
    p23 = Player(2, 11, 1, 0, 'M', ["L", "R", "C"], 'AGUDELO Kevin')
    p24 = Player(1, 4, 0, 0, 'M', ["L", "R", "C"], 'ZENNARO Mattia')
    p25 = Player(35, 7, 4, 0, 'A', ["L", "R", "C"], 'PINAMONTI Andrea')
    p26 = Player(33, 7, 3, 0, 'A', ["L", "R", "C"], 'KOUAMÉ Christian')
    p27 = Player(25, 5, 3, 0, 'A', ["L", "R", "C"], 'SANABRIA Antonio')
    p28 = Player(22, 4, 2, 0, 'A', ["L", "R", "C"], 'GUMUS Sinan')
    p29 = Player(16, 3, 2, 0, 'A', ["L", "R", "C"], 'FAVILLI Andrea')
    return name, tactics, chariness, [p1, p4, p5, p6, p14, p15, p16, p17, p19, p20, p21]

def Internazionale():
    name = "FC Inter Milan"
    tactics = F352
    chariness = 2
    p1 = Player(0, 38, 76, 95, 'GK', ["L", "R", "C"], 'HANDANOVIC Samir')
    p2 = Player(0, 2, 4, 5, 'GK', ["L", "R", "C"], 'PADELLI Daniele')
    p3 = Player(0, 2, 4, 5, 'GK', ["L", "R", "C"], 'BERNI Tommaso')
    p4 = Player(28, 57, 71, 0, 'D', ["L", "R", "C"], 'GODIN Diego')
    p5 = Player(27, 54, 68, 0, 'D', ["L", "R", "C"], 'DE VRIJ Stefan')
    p6 = Player(24, 49, 61, 0, 'D', ["L", "R", "C"], 'SKRINIAR Milan')
    p7 = Player(16, 31, 39, 0, 'D', ["L", "R", "C"], 'ASAMOAH Kwadwo')
    p8 = Player(13, 26, 32, 0, 'D', ["L", "R", "C"], 'D''AMBROSIO Danilo')
    p9 = Player(10, 20, 25, 0, 'D', ["L", "R", "C"], 'BIRAGHI Cristiano')
    p10 = Player(7, 14, 18, 0, 'D', ["L", "R", "C"], 'BASTONI Alessandro')
    p11 = Player(6, 11, 14, 0, 'D', ["L", "R", "C"], 'RANOCCHIA Andrea')
    p12 = Player(4, 9, 11, 0, 'D', ["L", "R", "C"], 'DIMARCO Federico')
    p13 = Player(54, 67, 27, 0, 'M', ["L", "R", "C"], 'BROZOVIC Marcelo')
    p14 = Player(50, 63, 25, 0, 'M', ["L", "R", "C"], 'BARELLA Nicolò')
    p15 = Player(47, 59, 24, 0, 'M', ["L", "R", "C"], 'SENSI Stefano')
    p16 = Player(42, 52, 21, 0, 'M', ["L", "R", "C"], 'LAZARO Valentino')
    p17 = Player(38, 48, 19, 0, 'M', ["L", "R", "C"], 'VECINO Matias')
    p18 = Player(33, 41, 16, 0, 'M', ["L", "R", "C"], 'CANDREVA Antonio')
    p19 = Player(30, 37, 15, 0, 'M', ["L", "R", "C"], 'GAGLIARDINI Roberto')
    p20 = Player(21, 26, 10, 0, 'M', ["L", "R", "C"], 'BORJA VALERO Iglesias')
    p21 = Player(3, 4, 2, 0, 'M', ["L", "R", "C"], 'AGOUME Lucien')
    p22 = Player(71, 57, 28, 0, 'A', ["L", "R", "C"], 'LUKAKU Romelu')
    p23 = Player(55, 44, 22, 0, 'A', ["L", "R", "C"], 'MARTINEZ Lautaro')
    p24 = Player(51, 41, 20, 0, 'A', ["L", "R", "C"], 'SANCHEZ Alexis')
    p25 = Player(35, 28, 14, 0, 'A', ["L", "R", "C"], 'POLITANO Matteo')
    p26 = Player(2, 2, 1, 0, 'A', ["L", "R", "C"], 'ESPOSITO Sebastiano')
    return name, tactics, chariness, [p1, p4, p5, p6, p14, p15, p16, p17, p19, p20, p21]

def Juventus():
    name = "Juventus FC"
    tactics = F433
    chariness = 2
    p1 = Player(0, 36, 81, 90, 'GK', ["L", "R", "C"], 'SZCZESNY Wojciech')
    p2 = Player(0, 4, 9, 10, 'GK', ["L", "R", "C"], 'BUFFON Gianluigi')
    p3 = Player(0, 2, 5, 5, 'GK', ["L", "R", "C"], 'PINSOGLIO Carlo')
    p4 = Player(0, 2, 5, 5, 'GK', ["L", "R", "C"], 'PERIN Mattia')
    p5 = Player(30, 68, 75, 0, 'D', ["L", "R", "C"], 'DE LIGT Matthijs')
    p6 = Player(28, 64, 71, 0, 'D', ["L", "R", "C"], 'CHIELLINI Giorgio')
    p7 = Player(26, 58, 64, 0, 'D', ["L", "R", "C"], 'ALEX SANDRO Lobo Silva')
    p8 = Player(23, 51, 57, 0, 'D', ["L", "R", "C"], 'BONUCCI Leonardo')
    p9 = Player(20, 45, 50, 0, 'D', ["L", "R", "C"], 'DANILO -')
    p10 = Player(14, 32, 36, 0, 'D', ["L", "R", "C"], 'DE SCIGLIO Mattia')
    p11 = Player(10, 23, 25, 0, 'D', ["L", "R", "C"], 'DEMIRAL Merih')
    p12 = Player(8, 19, 21, 0, 'D', ["L", "R", "C"], 'RUGANI Daniele')
    p13 = Player(77, 85, 34, 0, 'M', ["L", "R", "C"], 'RAMSEY Aaron')
    p14 = Player(70, 78, 31, 0, 'M', ["L", "R", "C"], 'PJANIC Miralem')
    p15 = Player(63, 70, 28, 0, 'M', ["L", "R", "C"], 'BERNARDESCHI Federico')
    p16 = Player(63, 70, 28, 0, 'M', ["L", "R", "C"], 'DOUGLAS COSTA de Souza')
    p17 = Player(60, 67, 27, 0, 'M', ["L", "R", "C"], 'RABIOT Adrien')
    p18 = Player(53, 59, 24, 0, 'M', ["L", "R", "C"], 'CAN Emre')
    p19 = Player(50, 56, 22, 0, 'M', ["L", "R", "C"], 'MATUIDI Blaise')
    p20 = Player(43, 48, 19, 0, 'M', ["L", "R", "C"], 'BENTANCUR Rodrigo')
    p21 = Player(40, 44, 18, 0, 'M', ["L", "R", "C"], 'CUADRADO Juan')
    p22 = Player(40, 44, 18, 0, 'M', ["L", "R", "C"], 'KHEDIRA Sami')
    p23 = Player(98, 88, 39, 0, 'A', ["L", "R", "C"], 'RONALDO Cristiano')
    p24 = Player(59, 53, 24, 0, 'A', ["L", "R", "C"], 'DYBALA Paulo')
    p25 = Player(55, 50, 22, 0, 'A', ["L", "R", "C"], 'HIGUAIN Gonzalo')
    p26 = Player(39, 35, 16, 0, 'A', ["L", "R", "C"], 'MANDZUKIC Mario')
    p27 = Player(16, 14, 6, 0, 'A', ["L", "R", "C"], 'PJACA Marko')
    p28 = Player(12, 11, 5, 0, 'A', ["L", "R", "C"], 'HAN Kwang Song')
    return name, tactics, chariness, [p1, p4, p5, p6, p14, p15, p16, p17, p19, p20, p21]

def Lazio():
    name = "SS Lazio"
    tactics = F343
    chariness = 2
    p1 = Player(0, 23, 46, 76, 'GK', ["L", "R", "C"], 'STRAKOSHA Thomas')
    p2 = Player(0, 2, 3, 5, 'GK', ["L", "R", "C"], 'GUERRIERI Guido')
    p3 = Player(0, 2, 3, 5, 'GK', ["L", "R", "C"], 'PROTO Silvio')
    p4 = Player(17, 34, 57, 0, 'D', ["L", "R", "C"], 'ACERBI Francesco')
    p5 = Player(9, 17, 29, 0, 'D', ["L", "R", "C"], 'VAVRO Denis')
    p6 = Player(8, 15, 25, 0, 'D', ["L", "R", "C"], 'LUIZ FELIPE Ramos Marchi')
    p7 = Player(8, 15, 25, 0, 'D', ["L", "R", "C"], 'BASTOS Jacinto Quissanga')
    p8 = Player(8, 15, 25, 0, 'D', ["L", "R", "C"], 'MARUSIC Adam')
    p9 = Player(8, 15, 25, 0, 'D', ["L", "R", "C"], 'RADU Stefan')
    p10 = Player(4, 8, 14, 0, 'D', ["L", "R", "C"], 'PATRIC Patricio Gabarron Gil')
    p11 = Player(4, 8, 14, 0, 'D', ["L", "R", "C"], 'LUKAKU Jordan Zacharie')
    p12 = Player(3, 7, 11, 0, 'D', ["L", "R", "C"], 'DURMISI Riza')
    p13 = Player(1, 2, 4, 0, 'D', ["L", "R", "C"], 'ARMINI Nicolo')
    p14 = Player(58, 96, 29, 0, 'M', ["L", "R", "C"], 'LUIS ALBERTO Romero Alconchel')
    p15 = Player(56, 93, 28, 0, 'M', ["L", "R", "C"], 'MILINKOVIC Sergej')
    p16 = Player(35, 59, 18, 0, 'M', ["L", "R", "C"], 'LULIC Senad')
    p17 = Player(31, 52, 16, 0, 'M', ["L", "R", "C"], 'PAROLO Marco')
    p18 = Player(31, 52, 16, 0, 'M', ["L", "R", "C"], 'LAZZARI Manuel')
    p19 = Player(29, 48, 14, 0, 'M', ["L", "R", "C"], 'LEIVA Lucas')
    p20 = Player(26, 44, 13, 0, 'M', ["L", "R", "C"], 'JONY -')
    p21 = Player(13, 22, 7, 0, 'M', ["L", "R", "C"], 'CATALDI Danilo')
    p22 = Player(11, 19, 6, 0, 'M', ["L", "R", "C"], 'BERISHA Valon')
    p23 = Player(4, 7, 2, 0, 'M', ["L", "R", "C"], 'ANDERSON Andre')
    p24 = Player(76, 46, 23, 0, 'A', ["L", "R", "C"], 'IMMOBILE Ciro')
    p25 = Player(45, 27, 14, 0, 'A', ["L", "R", "C"], 'CORREA Carlos Joaquin')
    p26 = Player(31, 19, 9, 0, 'A', ["L", "R", "C"], 'CAICEDO Felipe')
    p27 = Player(2, 1, 1, 0, 'A', ["L", "R", "C"], 'BOBBY Adekanye')
    return name, tactics, chariness, [p1, p4, p5, p6, p14, p15, p16, p17, p19, p20, p21]

def Lecce():
    name = "US Lecce"
    tactics = F433
    chariness = 2
    p1 = Player(0, 9, 9, 43, 'GK', ["L", "R", "C"], 'GABRIEL Vasconcelos Ferreira')
    p2 = Player(0, 1, 1, 5, 'GK', ["L", "R", "C"], 'VIGORITO Mauro')
    p3 = Player(0, 1, 1, 5, 'GK', ["L", "R", "C"], 'BLEVE Marco')
    p4 = Player(5, 5, 25, 0, 'D', ["L", "R", "C"], 'LUCIONI Fabio')
    p5 = Player(4, 4, 21, 0, 'D', ["L", "R", "C"], 'BENZAR Romario')
    p6 = Player(4, 4, 18, 0, 'D', ["L", "R", "C"], 'CALDERONI Marco')
    p7 = Player(4, 4, 18, 0, 'D', ["L", "R", "C"], 'DELL''ORCO Christian')
    p8 = Player(3, 3, 14, 0, 'D', ["L", "R", "C"], 'ROSSETTINI Luca')
    p9 = Player(3, 3, 14, 0, 'D', ["L", "R", "C"], 'MECCARIELLO Biagio')
    p10 = Player(3, 3, 14, 0, 'D', ["L", "R", "C"], 'VERA Brayan')
    p11 = Player(3, 3, 14, 0, 'D', ["L", "R", "C"], 'RISPOLI Andrea')
    p12 = Player(2, 2, 11, 0, 'D', ["L", "R", "C"], 'FIAMOZZI Riccardo')
    p13 = Player(1, 1, 4, 0, 'D', ["L", "R", "C"], 'GALLO Antonino')
    p14 = Player(1, 1, 4, 0, 'D', ["L", "R", "C"], 'DUMANCIC Luka')
    p15 = Player(1, 1, 4, 0, 'D', ["L", "R", "C"], 'RICCARDI Davide')
    p16 = Player(10, 48, 10, 0, 'M', ["L", "R", "C"], 'MANCOSU Marco')
    p17 = Player(7, 37, 7, 0, 'M', ["L", "R", "C"], 'SHAKHOV Evgen')
    p18 = Player(6, 30, 6, 0, 'M', ["L", "R", "C"], 'IMBULA Giannelli')
    p19 = Player(5, 26, 5, 0, 'M', ["L", "R", "C"], 'TACHTSIDIS Panagiotis')
    p20 = Player(4, 22, 4, 0, 'M', ["L", "R", "C"], 'TABANELLI Andrea')
    p21 = Player(4, 22, 4, 0, 'M', ["L", "R", "C"], 'PETRICCIONE Jacopo')
    p22 = Player(3, 15, 3, 0, 'M', ["L", "R", "C"], 'MAJER Zan')
    p23 = Player(29, 6, 6, 0, 'A', ["L", "R", "C"], 'BABACAR Khouma El')
    p24 = Player(25, 5, 5, 0, 'A', ["L", "R", "C"], 'FARIAS Diego')
    p25 = Player(25, 5, 5, 0, 'A', ["L", "R", "C"], 'LA MANTIA Andrea')
    p26 = Player(24, 5, 5, 0, 'A', ["L", "R", "C"], 'LAPADULA Gianluca')
    p27 = Player(22, 4, 4, 0, 'A', ["L", "R", "C"], 'FALCO Filippo')
    p28 = Player(6, 1, 1, 0, 'A', ["L", "R", "C"], 'LO FASO Simone')
    p29 = Player(2, 0, 0, 0, 'A', ["L", "R", "C"], 'DUBICKAS Edgaras')
    return name, tactics, chariness, [p1, p4, p5, p6, p14, p15, p16, p17, p19, p20, p21]

def Milan():
    name = "AC Milan"
    tactics = F433
    chariness = 2
    p1 = Player(0, 18, 36, 90, 'GK', ["L", "R", "C"], 'DONNARUMMA Gianluigi')
    p2 = Player(0, 1, 2, 5, 'GK', ["L", "R", "C"], 'REINA Pepe')
    p3 = Player(0, 1, 2, 5, 'GK', ["L", "R", "C"], 'DONNARUMMA Antonio')
    p4 = Player(11, 23, 57, 0, 'D', ["L", "R", "C"], 'ROMAGNOLI Alessio')
    p5 = Player(8, 16, 39, 0, 'D', ["L", "R", "C"], 'HERNANDEZ Theo')
    p6 = Player(7, 14, 36, 0, 'D', ["L", "R", "C"], 'CALABRIA Davide')
    p7 = Player(6, 13, 32, 0, 'D', ["L", "R", "C"], 'CONTI Andrea')
    p8 = Player(6, 12, 29, 0, 'D', ["L", "R", "C"], 'MUSACCHIO Mateo')
    p9 = Player(6, 12, 29, 0, 'D', ["L", "R", "C"], 'RODRIGUEZ Ricardo')
    p10 = Player(5, 10, 25, 0, 'D', ["L", "R", "C"], 'DUARTE Leo')
    p11 = Player(5, 10, 25, 0, 'D', ["L", "R", "C"], 'CALDARA Mattia')
    p12 = Player(1, 2, 4, 0, 'D', ["L", "R", "C"], 'GABBIA Matteo')
    p13 = Player(31, 78, 16, 0, 'M', ["L", "R", "C"], 'SUSO Jesus Fernandez Saez')
    p14 = Player(28, 70, 14, 0, 'M', ["L", "R", "C"], 'KESSIE Franck')
    p15 = Player(27, 67, 13, 0, 'M', ["L", "R", "C"], 'PAQUETA Lucas')
    p16 = Player(25, 63, 13, 0, 'M', ["L", "R", "C"], 'CALHANOGLU Hakan')
    p17 = Player(21, 52, 10, 0, 'M', ["L", "R", "C"], 'BONAVENTURA Giacomo')
    p18 = Player(19, 48, 10, 0, 'M', ["L", "R", "C"], 'KRUNIC Rade')
    p19 = Player(18, 44, 9, 0, 'M', ["L", "R", "C"], 'CASTILLEJO Samu')
    p20 = Player(18, 44, 9, 0, 'M', ["L", "R", "C"], 'BENNACER Ismael')
    p21 = Player(12, 30, 6, 0, 'M', ["L", "R", "C"], 'BORINI Fabio')
    p22 = Player(12, 30, 6, 0, 'M', ["L", "R", "C"], 'BIGLIA Lucas')
    p23 = Player(67, 27, 13, 0, 'A', ["L", "R", "C"], 'PIATEK Krzysztof')
    p24 = Player(39, 16, 8, 0, 'A', ["L", "R", "C"], 'REBIC Ante')
    p25 = Player(39, 16, 8, 0, 'A', ["L", "R", "C"], 'LEAO Rafael')
    return name, tactics, chariness, [p1, p4, p5, p6, p14, p15, p16, p17, p19, p20, p21]

def Napoli():
    name = "SSC Napoli"
    tactics = F442
    chariness = 2
    p1 = Player(0, 28, 50, 71, 'GK', ["L", "R", "C"], 'MERET Alex')
    p2 = Player(0, 4, 7, 10, 'GK', ["L", "R", "C"], 'OSPINA David')
    p3 = Player(0, 2, 4, 5, 'GK', ["L", "R", "C"], 'KARNEZIS Orestis')
    p4 = Player(27, 48, 68, 0, 'D', ["L", "R", "C"], 'MANOLAS Konstantinos')
    p5 = Player(26, 45, 64, 0, 'D', ["L", "R", "C"], 'KOULIBALY Kalidou')
    p6 = Player(24, 43, 61, 0, 'D', ["L", "R", "C"], 'DI LORENZO Giovanni')
    p7 = Player(18, 32, 46, 0, 'D', ["L", "R", "C"], 'GHOULAM Faouzi')
    p8 = Player(13, 22, 32, 0, 'D', ["L", "R", "C"], 'MARIO RUI Silva Duarte')
    p9 = Player(10, 18, 25, 0, 'D', ["L", "R", "C"], 'MALCUIT Kevin')
    p10 = Player(8, 15, 21, 0, 'D', ["L", "R", "C"], 'MAKSIMOVIC Nikola')
    p11 = Player(8, 15, 21, 0, 'D', ["L", "R", "C"], 'HYSAJ Elseid')
    p12 = Player(6, 10, 14, 0, 'D', ["L", "R", "C"], 'TONELLI Lorenzo')
    p13 = Player(4, 8, 11, 0, 'D', ["L", "R", "C"], 'LUPERTO Sebastiano')
    p14 = Player(65, 93, 37, 0, 'M', ["L", "R", "C"], 'CALLEJON Jose Maria')
    p15 = Player(57, 81, 32, 0, 'M', ["L", "R", "C"], 'RUIZ Fabian')
    p16 = Player(52, 74, 30, 0, 'M', ["L", "R", "C"], 'ZIELINSKI Piotr')
    p17 = Player(44, 63, 25, 0, 'M', ["L", "R", "C"], 'ALLAN Marques Loureiro')
    p18 = Player(34, 48, 19, 0, 'M', ["L", "R", "C"], 'YOUNES Amin')
    p19 = Player(26, 37, 15, 0, 'M', ["L", "R", "C"], 'ELMAS Eljif')
    p20 = Player(3, 4, 2, 0, 'M', ["L", "R", "C"], 'GAETANO Gianluca')
    p21 = Player(65, 46, 26, 0, 'A', ["L", "R", "C"], 'INSIGNE Lorenzo')
    p22 = Player(65, 46, 26, 0, 'A', ["L", "R", "C"], 'MILIK Arkadiusz')
    p23 = Player(65, 46, 26, 0, 'A', ["L", "R", "C"], 'MERTENS Dries')
    p24 = Player(55, 39, 22, 0, 'A', ["L", "R", "C"], 'LOZANO Hirving')
    p25 = Player(29, 20, 12, 0, 'A', ["L", "R", "C"], 'LLORENTE Fernando')
    return name, tactics, chariness, [p1, p4, p5, p6, p14, p15, p16, p17, p19, p20, p21]

def Parma():
    name = "Parma Calcio"
    tactics = F433
    chariness = 2
    p1 = Player(0, 10, 16, 52, 'GK', ["L", "R", "C"], 'SEPE Luigi')
    p2 = Player(0, 1, 2, 5, 'GK', ["L", "R", "C"], 'CORVI Edoardo')
    p3 = Player(0, 1, 2, 5, 'GK', ["L", "R", "C"], 'COLOMBI Simone')
    p4 = Player(0, 1, 2, 5, 'GK', ["L", "R", "C"], 'ALASTRA Fabrizio')
    p5 = Player(9, 14, 46, 0, 'D', ["L", "R", "C"], 'ALVES Bruno')
    p6 = Player(7, 11, 36, 0, 'D', ["L", "R", "C"], 'DARMIAN Matteo')
    p7 = Player(6, 10, 32, 0, 'D', ["L", "R", "C"], 'GAGLIOLO Riccardo')
    p8 = Player(4, 5, 18, 0, 'D', ["L", "R", "C"], 'PEZZELLA Giuseppe')
    p9 = Player(4, 5, 18, 0, 'D', ["L", "R", "C"], 'IACOPONI Simone')
    p10 = Player(3, 4, 14, 0, 'D', ["L", "R", "C"], 'LAURINI Vincent')
    p11 = Player(2, 3, 11, 0, 'D', ["L", "R", "C"], 'DERMAKU Kastriot')
    p12 = Player(17, 56, 11, 0, 'M', ["L", "R", "C"], 'KUCKA Juraj')
    p13 = Player(12, 41, 8, 0, 'M', ["L", "R", "C"], 'BARILLÀ Antonino')
    p14 = Player(11, 37, 7, 0, 'M', ["L", "R", "C"], 'HERNANI Azevedo Júnior')
    p15 = Player(9, 30, 6, 0, 'M', ["L", "R", "C"], 'BRUGMAN Gaston')
    p16 = Player(7, 22, 4, 0, 'M', ["L", "R", "C"], 'SCOZZARELLA Matteo')
    p17 = Player(7, 22, 4, 0, 'M', ["L", "R", "C"], 'GRASSI Alberto')
    p18 = Player(5, 15, 3, 0, 'M', ["L", "R", "C"], 'KULUSEVSKI Dejan')
    p19 = Player(3, 11, 2, 0, 'M', ["L", "R", "C"], 'MUNARI Gianni')
    p20 = Player(57, 17, 11, 0, 'A', ["L", "R", "C"], 'GERVINHO undefined')
    p21 = Player(43, 13, 9, 0, 'A', ["L", "R", "C"], 'INGLESE Roberto')
    p22 = Player(24, 7, 5, 0, 'A', ["L", "R", "C"], 'KARAMOH Yann')
    p23 = Player(20, 6, 4, 0, 'A', ["L", "R", "C"], 'CORNELIUS Andreas')
    p24 = Player(12, 4, 2, 0, 'A', ["L", "R", "C"], 'SPROCATI Mattia')
    p25 = Player(10, 3, 2, 0, 'A', ["L", "R", "C"], 'SILIGARDI Luca')
    p26 = Player(2, 1, 0, 0, 'A', ["L", "R", "C"], 'ADORANTE Andrea')
    return name, tactics, chariness, [p1, p4, p5, p6, p14, p15, p16, p17, p19, p20, p21]

def Roma():
    name = "AS Roma"
    tactics = F424
    chariness = 2
    p1 = Player(0, 23, 46, 76, 'GK', ["L", "R", "C"], 'LOPEZ Pau')
    p2 = Player(0, 2, 3, 5, 'GK', ["L", "R", "C"], 'FUZATO Daniel')
    p3 = Player(0, 2, 3, 5, 'GK', ["L", "R", "C"], 'MIRANTE Antonio')
    p4 = Player(29, 58, 96, 0, 'D', ["L", "R", "C"], 'KOLAROV Aleksandar')
    p5 = Player(17, 34, 57, 0, 'D', ["L", "R", "C"], 'FLORENZI Alessandro')
    p6 = Player(16, 32, 54, 0, 'D', ["L", "R", "C"], 'FAZIO Federico')
    p7 = Player(15, 30, 50, 0, 'D', ["L", "R", "C"], 'MANCINI Gianluca')
    p8 = Player(14, 28, 46, 0, 'D', ["L", "R", "C"], 'SMALLING Chris')
    p9 = Player(12, 23, 39, 0, 'D', ["L", "R", "C"], 'ZAPPACOSTA Davide')
    p10 = Player(11, 22, 36, 0, 'D', ["L", "R", "C"], 'SPINAZZOLA Leonardo')
    p11 = Player(4, 8, 14, 0, 'D', ["L", "R", "C"], 'CETIN Mert')
    p12 = Player(4, 8, 14, 0, 'D', ["L", "R", "C"], 'JUAN JESUS Guilherme Nunes')
    p13 = Player(4, 8, 14, 0, 'D', ["L", "R", "C"], 'SANTON Davide')
    p14 = Player(53, 89, 27, 0, 'M', ["L", "R", "C"], 'MKHITARYAN Henrikh')
    p15 = Player(51, 85, 26, 0, 'M', ["L", "R", "C"], 'UNDER Cengiz')
    p16 = Player(47, 78, 23, 0, 'M', ["L", "R", "C"], 'ZANIOLO Nicolò')
    p17 = Player(38, 63, 19, 0, 'M', ["L", "R", "C"], 'PELLEGRINI Lorenzo')
    p18 = Player(38, 63, 19, 0, 'M', ["L", "R", "C"], 'VERETOUT Jordan')
    p19 = Player(38, 63, 19, 0, 'M', ["L", "R", "C"], 'PEROTTI Diego')
    p20 = Player(34, 56, 17, 0, 'M', ["L", "R", "C"], 'KLUIVERT Justin')
    p21 = Player(34, 56, 17, 0, 'M', ["L", "R", "C"], 'CRISTANTE Bryan')
    p22 = Player(26, 44, 13, 0, 'M', ["L", "R", "C"], 'PASTORE Javier')
    p23 = Player(20, 33, 10, 0, 'M', ["L", "R", "C"], 'DIAWARA Amadou')
    p24 = Player(2, 4, 1, 0, 'M', ["L", "R", "C"], 'RICCARDI Alessio')
    p25 = Player(55, 33, 17, 0, 'A', ["L", "R", "C"], 'DZEKO Edin')
    p26 = Player(31, 19, 9, 0, 'A', ["L", "R", "C"], 'KALINIC Nikola')
    p27 = Player(4, 2, 1, 0, 'A', ["L", "R", "C"], 'ANTONUCCI Mirko')
    return name, tactics, chariness, [p1, p4, p5, p6, p14, p15, p16, p17, p19, p20, p21]

def Sampdoria():
    name = "UC Sampdoria"
    tactics = F433
    chariness = 2
    p1 = Player(0, 10, 10, 52, 'GK', ["L", "R", "C"], 'AUDERO Emil')
    p2 = Player(0, 1, 1, 5, 'GK', ["L", "R", "C"], 'FALCONE Wladimiro')
    p3 = Player(0, 1, 1, 5, 'GK', ["L", "R", "C"], 'SECULIN Andrea')
    p4 = Player(5, 5, 25, 0, 'D', ["L", "R", "C"], 'MURILLO Jeison Fabian')
    p5 = Player(5, 5, 25, 0, 'D', ["L", "R", "C"], 'MURRU Nicola')
    p6 = Player(4, 4, 21, 0, 'D', ["L", "R", "C"], 'COLLEY Omar')
    p7 = Player(4, 4, 18, 0, 'D', ["L", "R", "C"], 'BERESZYNSKI Bartosz')
    p8 = Player(4, 4, 18, 0, 'D', ["L", "R", "C"], 'DEPAOLI Fabio')
    p9 = Player(3, 3, 14, 0, 'D', ["L", "R", "C"], 'CHABOT Julian')
    p10 = Player(2, 2, 11, 0, 'D', ["L", "R", "C"], 'AUGELLO Tommaso')
    p11 = Player(2, 2, 11, 0, 'D', ["L", "R", "C"], 'FERRARI Alex')
    p12 = Player(2, 2, 11, 0, 'D', ["L", "R", "C"], 'REGINI Vasco')
    p13 = Player(10, 52, 10, 0, 'M', ["L", "R", "C"], 'RAMIREZ Gastón')
    p14 = Player(10, 48, 10, 0, 'M', ["L", "R", "C"], 'LINETTY Karol')
    p15 = Player(8, 41, 8, 0, 'M', ["L", "R", "C"], 'JANKTO Jakub')
    p16 = Player(7, 37, 7, 0, 'M', ["L", "R", "C"], 'EKDAL Albin')
    p17 = Player(7, 33, 7, 0, 'M', ["L", "R", "C"], 'MARONI Gonzalo')
    p18 = Player(6, 30, 6, 0, 'M', ["L", "R", "C"], 'THORSBY Morten')
    p19 = Player(4, 19, 4, 0, 'M', ["L", "R", "C"], 'LERIS Mehdi')
    p20 = Player(4, 19, 4, 0, 'M', ["L", "R", "C"], 'BARRETO Edgar')
    p21 = Player(3, 15, 3, 0, 'M', ["L", "R", "C"], 'VIEIRA Ronaldo')
    p22 = Player(1, 4, 1, 0, 'M', ["L", "R", "C"], 'POMPETTI Marco')
    p23 = Player(69, 14, 14, 0, 'A', ["L", "R", "C"], 'QUAGLIARELLA Fabio')
    p24 = Player(35, 7, 7, 0, 'A', ["L", "R", "C"], 'RIGONI Emiliano')
    p25 = Player(27, 5, 5, 0, 'A', ["L", "R", "C"], 'GABBIADINI Manolo')
    p26 = Player(24, 5, 5, 0, 'A', ["L", "R", "C"], 'CAPRARI Gianluca')
    p27 = Player(14, 3, 3, 0, 'A', ["L", "R", "C"], 'BONAZZOLI Federico')
    return name, tactics, chariness, [p1, p4, p5, p6, p14, p15, p16, p17, p19, p20, p21]

def Sassuolo():
    name = "USS Sassuolo Calcio"
    tactics = F433
    chariness = 2
    p1 = Player(0, 10, 10, 52, 'GK', ["L", "R", "C"], 'CONSIGLI Andrea')
    p2 = Player(0, 1, 1, 5, 'GK', ["L", "R", "C"], 'PEGOLO Gianluca')
    p3 = Player(0, 1, 1, 5, 'GK', ["L", "R", "C"], 'RUSSO Alessandro')
    p4 = Player(9, 9, 46, 0, 'D', ["L", "R", "C"], 'FERRARI Gianmarco')
    p5 = Player(5, 5, 25, 0, 'D', ["L", "R", "C"], 'CHIRICHES Vlad')
    p6 = Player(5, 5, 25, 0, 'D', ["L", "R", "C"], 'ROGERIO Oliveira Da Silva')
    p7 = Player(5, 5, 25, 0, 'D', ["L", "R", "C"], 'TOLJAN Jeremy')
    p8 = Player(4, 4, 21, 0, 'D', ["L", "R", "C"], 'PELUSO Federico')
    p9 = Player(4, 4, 21, 0, 'D', ["L", "R", "C"], 'MARLON -')
    p10 = Player(4, 4, 18, 0, 'D', ["L", "R", "C"], 'MULDUR Mert')
    p11 = Player(4, 4, 18, 0, 'D', ["L", "R", "C"], 'KYRIAKOPOULOS Georgios')
    p12 = Player(4, 4, 18, 0, 'D', ["L", "R", "C"], 'ROMAGNA Filippo')
    p13 = Player(1, 1, 7, 0, 'D', ["L", "R", "C"], 'TRIPALDELLI Alessandro')
    p14 = Player(13, 63, 13, 0, 'M', ["L", "R", "C"], 'TRAORE Hamed Junior')
    p15 = Player(12, 59, 12, 0, 'M', ["L", "R", "C"], 'DUNCAN Alfred')
    p16 = Player(8, 41, 8, 0, 'M', ["L", "R", "C"], 'LOCATELLI Manuel')
    p17 = Player(7, 33, 7, 0, 'M', ["L", "R", "C"], 'OBIANG Pedro')
    p18 = Player(6, 30, 6, 0, 'M', ["L", "R", "C"], 'BOURABIA Mehdi')
    p19 = Player(6, 30, 6, 0, 'M', ["L", "R", "C"], 'DJURICIC Filip')
    p20 = Player(4, 22, 4, 0, 'M', ["L", "R", "C"], 'MAGNANELLI Francesco')
    p21 = Player(3, 15, 3, 0, 'M', ["L", "R", "C"], 'MAZZITELLI Luca')
    p22 = Player(51, 10, 10, 0, 'A', ["L", "R", "C"], 'CAPUTO Francesco')
    p23 = Player(49, 10, 10, 0, 'A', ["L", "R", "C"], 'BERARDI Domenico')
    p24 = Player(39, 8, 8, 0, 'A', ["L", "R", "C"], 'DEFREL Gregoire')
    p25 = Player(25, 5, 5, 0, 'A', ["L", "R", "C"], 'BOGA Jeremie')
    p26 = Player(2, 0, 0, 0, 'A', ["L", "R", "C"], 'RASPADORI Giacomo')
    return name, tactics, chariness, [p1, p4, p5, p6, p14, p15, p16, p17, p19, p20, p21]

def Spal():
    name = "S.P.A.L"
    tactics = F352
    chariness = 2
    p1 = Player(0, 6, 11, 57, 'GK', ["L", "R", "C"], 'BERISHA Etrit')
    p2 = Player(0, 1, 1, 5, 'GK', ["L", "R", "C"], 'THIAM Demba')
    p3 = Player(0, 1, 1, 5, 'GK', ["L", "R", "C"], 'LETICA Karlo')
    p4 = Player(4, 7, 36, 0, 'D', ["L", "R", "C"], 'FARES Mohamed')
    p5 = Player(3, 5, 25, 0, 'D', ["L", "R", "C"], 'VICARI Francesco')
    p6 = Player(2, 4, 21, 0, 'D', ["L", "R", "C"], 'FELIPE Dal Belo')
    p7 = Player(2, 4, 21, 0, 'D', ["L", "R", "C"], 'IGOR JULIO dos Santos de Paulo')
    p8 = Player(2, 4, 21, 0, 'D', ["L", "R", "C"], 'CIONEK Thiago')
    p9 = Player(2, 4, 21, 0, 'D', ["L", "R", "C"], 'RECA Arkadiusz')
    p10 = Player(2, 4, 18, 0, 'D', ["L", "R", "C"], 'SALA Jacopo')
    p11 = Player(1, 3, 14, 0, 'D', ["L", "R", "C"], 'TOMOVIC Nenad')
    p12 = Player(0, 1, 4, 0, 'D', ["L", "R", "C"], 'FARCAS Ricardo')
    p13 = Player(12, 59, 6, 0, 'M', ["L", "R", "C"], 'KURTIC Jasmin')
    p14 = Player(6, 30, 3, 0, 'M', ["L", "R", "C"], 'MISSIROLI Simone')
    p15 = Player(6, 30, 3, 0, 'M', ["L", "R", "C"], 'D''ALESSANDRO Marco')
    p16 = Player(5, 26, 3, 0, 'M', ["L", "R", "C"], 'MURGIA Alessandro')
    p17 = Player(5, 26, 3, 0, 'M', ["L", "R", "C"], 'VALOTI Mattia')
    p18 = Player(3, 15, 2, 0, 'M', ["L", "R", "C"], 'STREFEZZA Gabriel')
    p19 = Player(3, 15, 2, 0, 'M', ["L", "R", "C"], 'VALDIFIORI Mirko')
    p20 = Player(1, 4, 0, 0, 'M', ["L", "R", "C"], 'MAWULI Shaka Eklu')
    p21 = Player(47, 9, 5, 0, 'A', ["L", "R", "C"], 'PETAGNA Andrea')
    p22 = Player(29, 6, 3, 0, 'A', ["L", "R", "C"], 'DI FRANCESCO Federico')
    p23 = Player(25, 5, 3, 0, 'A', ["L", "R", "C"], 'MONCINI Gabriele')
    p24 = Player(22, 4, 2, 0, 'A', ["L", "R", "C"], 'FLOCCARI Sergio')
    p25 = Player(18, 4, 2, 0, 'A', ["L", "R", "C"], 'PALOSCHI Alberto')
    p26 = Player(10, 2, 1, 0, 'A', ["L", "R", "C"], 'JANKOVIC Marko')
    return name, tactics, chariness, [p1, p4, p5, p6, p14, p15, p16, p17, p19, p20, p21]

def Torino():
    name = "Torino FC"
    tactics = F343
    chariness = 2
    p1 = Player(0, 26, 34, 86, 'GK', ["L", "R", "C"], 'SIRIGU Salvatore')
    p2 = Player(0, 2, 2, 5, 'GK', ["L", "R", "C"], 'UJKANI Samir')
    p3 = Player(0, 2, 2, 5, 'GK', ["L", "R", "C"], 'ZACCAGNO Andrea')
    p4 = Player(0, 2, 2, 5, 'GK', ["L", "R", "C"], 'ROSATI Antonio')
    p5 = Player(23, 30, 75, 0, 'D', ["L", "R", "C"], 'IZZO Armando')
    p6 = Player(16, 22, 54, 0, 'D', ["L", "R", "C"], 'NKOULOU Nicolas')
    p7 = Player(14, 18, 46, 0, 'D', ["L", "R", "C"], 'DE SILVESTRI Lorenzo')
    p8 = Player(11, 14, 36, 0, 'D', ["L", "R", "C"], 'AINA Ola')
    p9 = Player(10, 13, 32, 0, 'D', ["L", "R", "C"], 'BONIFAZI Kevin')
    p10 = Player(8, 10, 25, 0, 'D', ["L", "R", "C"], 'LAXALT Diego')
    p11 = Player(8, 10, 25, 0, 'D', ["L", "R", "C"], 'LYANCO Silveira Neves Vojnovic')
    p12 = Player(6, 8, 21, 0, 'D', ["L", "R", "C"], 'DJIDJI Koffi')
    p13 = Player(3, 4, 11, 0, 'D', ["L", "R", "C"], 'BREMER Gleison Silva Nascimento')
    p14 = Player(2, 3, 7, 0, 'D', ["L", "R", "C"], 'BUONGIORNO Alessandro')
    p15 = Player(1, 2, 4, 0, 'D', ["L", "R", "C"], 'SINGO Wilfried Stephane')
    p16 = Player(25, 63, 19, 0, 'M', ["L", "R", "C"], 'VERDI Simone')
    p17 = Player(25, 63, 19, 0, 'M', ["L", "R", "C"], 'BASELLI Daniele')
    p18 = Player(22, 56, 17, 0, 'M', ["L", "R", "C"], 'BERENGUER Alex')
    p19 = Player(21, 52, 16, 0, 'M', ["L", "R", "C"], 'ANSALDI Cristian')
    p20 = Player(21, 52, 16, 0, 'M', ["L", "R", "C"], 'RINCON Tomas')
    p21 = Player(19, 48, 14, 0, 'M', ["L", "R", "C"], 'MEITE Soualiho')
    p22 = Player(12, 30, 9, 0, 'M', ["L", "R", "C"], 'LUKIC Sasa')
    p23 = Player(63, 25, 19, 0, 'A', ["L", "R", "C"], 'BELOTTI Andrea')
    p24 = Player(49, 20, 15, 0, 'A', ["L", "R", "C"], 'IAGO Falque')
    p25 = Player(29, 12, 9, 0, 'A', ["L", "R", "C"], 'ZAZA Simone')
    p26 = Player(10, 4, 3, 0, 'A', ["L", "R", "C"], 'EDERA Simone')
    p27 = Player(10, 4, 3, 0, 'A', ["L", "R", "C"], 'PARIGINI Vittorio')
    p28 = Player(4, 2, 1, 0, 'A', ["L", "R", "C"], 'MILLICO Vincenzo')
    return name, tactics, chariness, [p1, p4, p5, p6, p14, p15, p16, p17, p19, p20, p21]

def Udinese():
    name = "Udinese Calcio"
    tactics = F433
    chariness = 2
    p1 = Player(0, 5, 10, 52, 'GK', ["L", "R", "C"], 'MUSSO Juan')
    p2 = Player(0, 1, 1, 5, 'GK', ["L", "R", "C"], 'NICOLAS Andrade')
    p3 = Player(0, 1, 1, 5, 'GK', ["L", "R", "C"], 'GASPARINI Manuel')
    p4 = Player(0, 1, 1, 5, 'GK', ["L", "R", "C"], 'PERISAN Samuele')
    p5 = Player(4, 8, 39, 0, 'D', ["L", "R", "C"], 'LARSEN Jens Stryger')
    p6 = Player(4, 7, 36, 0, 'D', ["L", "R", "C"], 'RODRIGO BECãO Nascimiento Franca')
    p7 = Player(3, 6, 32, 0, 'D', ["L", "R", "C"], 'SAMIR Caetano de Sousa')
    p8 = Player(3, 6, 29, 0, 'D', ["L", "R", "C"], 'TROOST-EKONG William')
    p9 = Player(2, 4, 21, 0, 'D', ["L", "R", "C"], 'DE MAIO Sebastian')
    p10 = Player(2, 4, 18, 0, 'D', ["L", "R", "C"], 'NUYTINCK Bram')
    p11 = Player(1, 3, 14, 0, 'D', ["L", "R", "C"], 'TER AVEST Hidde')
    p12 = Player(1, 3, 14, 0, 'D', ["L", "R", "C"], 'OPOKU Nicholas')
    p13 = Player(1, 2, 11, 0, 'D', ["L", "R", "C"], 'SIERRALTA Francisco')
    p14 = Player(15, 74, 7, 0, 'M', ["L", "R", "C"], 'DE PAUL Rodrigo')
    p15 = Player(9, 44, 4, 0, 'M', ["L", "R", "C"], 'FOFANA Seko')
    p16 = Player(8, 41, 4, 0, 'M', ["L", "R", "C"], 'MANDRAGORA Rolando')
    p17 = Player(7, 37, 4, 0, 'M', ["L", "R", "C"], 'BARAK Antonin')
    p18 = Player(6, 30, 3, 0, 'M', ["L", "R", "C"], 'JAJALO Mato')
    p19 = Player(5, 26, 3, 0, 'M', ["L", "R", "C"], 'WALACE -')
    p20 = Player(5, 26, 3, 0, 'M', ["L", "R", "C"], 'SEMA Ken')
    p21 = Player(33, 7, 3, 0, 'A', ["L", "R", "C"], 'LASAGNA Kevin')
    p22 = Player(33, 7, 3, 0, 'A', ["L", "R", "C"], 'NESTOROVSKI Ilija')
    p23 = Player(33, 7, 3, 0, 'A', ["L", "R", "C"], 'OKAKA Stefano')
    p24 = Player(24, 5, 2, 0, 'A', ["L", "R", "C"], 'PUSSETTO Ignacio')
    p25 = Player(20, 4, 2, 0, 'A', ["L", "R", "C"], 'TEODORCZYK Lukasz')
    return name, tactics, chariness, [p1, p4, p5, p6, p14, p15, p16, p17, p19, p20, p21]

def Verona():
    name = "Hellas Verona FC"
    tactics = F343
    chariness = 2
    p1 = Player(0, 5, 5, 48, 'GK', ["L", "R", "C"], 'SILVESTRI Marco')
    p2 = Player(0, 1, 1, 10, 'GK', ["L", "R", "C"], 'RADUNOVIC Boris')
    p3 = Player(0, 1, 1, 5, 'GK', ["L", "R", "C"], 'BERARDI Alessandro')
    p4 = Player(3, 3, 29, 0, 'D', ["L", "R", "C"], 'FARAONI Davide')
    p5 = Player(3, 3, 25, 0, 'D', ["L", "R", "C"], 'RRAHMANI Amir')
    p6 = Player(2, 2, 21, 0, 'D', ["L", "R", "C"], 'ADJAPONG Claud')
    p7 = Player(2, 2, 21, 0, 'D', ["L", "R", "C"], 'BOCCHETTI Salvatore')
    p8 = Player(2, 2, 18, 0, 'D', ["L", "R", "C"], 'VITALE Luigi')
    p9 = Player(1, 1, 14, 0, 'D', ["L", "R", "C"], 'GUNTER Koray')
    p10 = Player(1, 1, 11, 0, 'D', ["L", "R", "C"], 'DAWIDOWICZ Pawel')
    p11 = Player(1, 1, 11, 0, 'D', ["L", "R", "C"], 'CRESCENZI Alessandro')
    p12 = Player(1, 1, 11, 0, 'D', ["L", "R", "C"], 'EMPEREUR Alan')
    p13 = Player(1, 1, 7, 0, 'D', ["L", "R", "C"], 'KUMBULLA Marash')
    p14 = Player(0, 0, 4, 0, 'D', ["L", "R", "C"], 'WESLEY -')
    p15 = Player(5, 48, 5, 0, 'M', ["L", "R", "C"], 'VERRE Valerio')
    p16 = Player(4, 37, 4, 0, 'M', ["L", "R", "C"], 'VELOSO Miguel')
    p17 = Player(4, 37, 4, 0, 'M', ["L", "R", "C"], 'BESSA Daniel')
    p18 = Player(4, 37, 4, 0, 'M', ["L", "R", "C"], 'LAZOVIC Darko')
    p19 = Player(3, 30, 3, 0, 'M', ["L", "R", "C"], 'ZACCAGNI Mattia')
    p20 = Player(3, 30, 3, 0, 'M', ["L", "R", "C"], 'PESSINA Matteo')
    p21 = Player(3, 26, 3, 0, 'M', ["L", "R", "C"], 'HENDERSON Liam')
    p22 = Player(2, 22, 2, 0, 'M', ["L", "R", "C"], 'AMRABAT Sofyan')
    p23 = Player(2, 19, 2, 0, 'M', ["L", "R", "C"], 'BADU Emmanuel')
    p24 = Player(1, 7, 1, 0, 'M', ["L", "R", "C"], 'JOCIC Bogdan')
    p25 = Player(1, 7, 1, 0, 'M', ["L", "R", "C"], 'DANZI Andrea')
    p26 = Player(0, 4, 0, 0, 'M', ["L", "R", "C"], 'LUCAS Martello Nascimento')
    p27 = Player(27, 3, 3, 0, 'A', ["L", "R", "C"], 'STEPINSKI Mariusz')
    p28 = Player(25, 3, 3, 0, 'A', ["L", "R", "C"], 'DI CARMINE Samuel')
    p29 = Player(24, 2, 2, 0, 'A', ["L", "R", "C"], 'TUTINO Gennaro')
    p30 = Player(24, 2, 2, 0, 'A', ["L", "R", "C"], 'PAZZINI Giampaolo')
    p31 = Player(14, 1, 1, 0, 'A', ["L", "R", "C"], 'DI GAUDIO Antonio')
    p32 = Player(4, 0, 0, 0, 'A', ["L", "R", "C"], 'SALCEDO Eddie')
    p33 = Player(4, 0, 0, 0, 'A', ["L", "R", "C"], 'TUPTA Lubomir')
    return name, tactics, chariness, [p1, p4, p5, p6, p14, p15, p16, p17, p19, p20, p21]

if __name__ == '__main__':
    pass
