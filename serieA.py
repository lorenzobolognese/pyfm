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
	roster = [Player(0, 27, 40, 67, 'GK', '', 'GOLLINI Pierluigi')]
	roster.append(Player(0, 2, 3, 5, 'GK', '', 'ROSSI Francesco'))
	roster.append(Player(0, 2, 3, 5, 'GK', '', 'SPORTIELLO Marco'))
	roster.append(Player(26, 38, 64, 0, 'D', ['L', 'R', 'C'], 'HATEBOER Hans'))
	roster.append(Player(23, 34, 57, 0, 'D', ['L', 'R', 'C'], 'CASTAGNE Timothy'))
	roster.append(Player(22, 32, 54, 0, 'D', ['L', 'R', 'C'], 'GOSENS Robin'))
	roster.append(Player(16, 23, 39, 0, 'D', ['L', 'R', 'C'], 'PALOMINO José Luis'))
	roster.append(Player(14, 22, 36, 0, 'D', ['L', 'R', 'C'], 'KJAER Simon'))
	roster.append(Player(14, 22, 36, 0, 'D', ['L', 'R', 'C'], 'TOLOI Rafael'))
	roster.append(Player(13, 19, 32, 0, 'D', ['L', 'R', 'C'], 'MASIELLO Andrea'))
	roster.append(Player(10, 15, 25, 0, 'D', ['L', 'R', 'C'], 'DJIMSITI Berat'))
	roster.append(Player(10, 15, 25, 0, 'D', ['L', 'R', 'C'], 'ARANA Guilherme'))
	roster.append(Player(4, 7, 11, 0, 'D', ['L', 'R', 'C'], 'IBANEZ -'))
	roster.append(Player(58, 96, 38, 0, 'M', ['L', 'R', 'C'], 'GOMEZ Alejandro'))
	roster.append(Player(38, 63, 25, 0, 'M', ['L', 'R', 'C'], 'FREULER Remo'))
	roster.append(Player(38, 63, 25, 0, 'M', ['L', 'R', 'C'], 'PASALIC Mario'))
	roster.append(Player(35, 59, 24, 0, 'M', ['L', 'R', 'C'], 'DE ROON Marten'))
	roster.append(Player(26, 44, 18, 0, 'M', ['L', 'R', 'C'], 'MALINOVSKIY Ruslan'))
	roster.append(Player(73, 44, 29, 0, 'A', ['L', 'R', 'C'], 'ZAPATA Duvan'))
	roster.append(Player(63, 38, 25, 0, 'A', ['L', 'R', 'C'], 'ILICIC Josip'))
	roster.append(Player(41, 25, 16, 0, 'A', ['L', 'R', 'C'], 'MURIEL Luis'))
	roster.append(Player(20, 12, 8, 0, 'A', ['L', 'R', 'C'], 'BARROW Musa'))
	roster.append(Player(6, 4, 2, 0, 'A', ['L', 'R', 'C'], 'PICCOLI Roberto'))
	return name, tactics, chariness, roster

def Bologna():
	name = "Bologna FC"
	tactics = F433
	chariness = 2
	roster = [Player(0, 27, 27, 67, 'GK', '', 'SKORUPSKI Lukasz')]
	roster.append(Player(0, 2, 2, 5, 'GK', '', 'DA COSTA Angelo'))
	roster.append(Player(0, 2, 2, 5, 'GK', '', 'SARR Mouhamadou'))
	roster.append(Player(14, 14, 36, 0, 'D', ['L', 'R', 'C'], 'DANILO Larangeira'))
	roster.append(Player(10, 10, 25, 0, 'D', ['L', 'R', 'C'], 'TOMIYASU Takehiro'))
	roster.append(Player(10, 10, 25, 0, 'D', ['L', 'R', 'C'], 'DENSWIL Stefano'))
	roster.append(Player(10, 10, 25, 0, 'D', ['L', 'R', 'C'], 'MBAYE Ibrahima'))
	roster.append(Player(8, 8, 21, 0, 'D', ['L', 'R', 'C'], 'DIJKS Mitchell'))
	roster.append(Player(6, 6, 14, 0, 'D', ['L', 'R', 'C'], 'BANI Mattia'))
	roster.append(Player(4, 4, 11, 0, 'D', ['L', 'R', 'C'], 'PAZ Nehuén'))
	roster.append(Player(2, 2, 4, 0, 'D', ['L', 'R', 'C'], 'CORBO Gabriele'))
	roster.append(Player(22, 56, 22, 0, 'M', ['L', 'R', 'C'], 'SORIANO Roberto'))
	roster.append(Player(16, 41, 16, 0, 'M', ['L', 'R', 'C'], 'POLI Andrea'))
	roster.append(Player(13, 33, 13, 0, 'M', ['L', 'R', 'C'], 'DZEMAILI Blerim'))
	roster.append(Player(12, 30, 12, 0, 'M', ['L', 'R', 'C'], 'SCHOUTEN Jerdy'))
	roster.append(Player(9, 22, 9, 0, 'M', ['L', 'R', 'C'], 'MEDEL Gary'))
	roster.append(Player(8, 19, 8, 0, 'M', ['L', 'R', 'C'], 'SVANBERG Mattias'))
	roster.append(Player(6, 15, 6, 0, 'M', ['L', 'R', 'C'], 'KREJCI Ladislav'))
	roster.append(Player(43, 17, 17, 0, 'A', ['L', 'R', 'C'], 'ORSOLINI Riccardo'))
	roster.append(Player(33, 13, 13, 0, 'A', ['L', 'R', 'C'], 'SANSONE Nicola'))
	roster.append(Player(31, 12, 12, 0, 'A', ['L', 'R', 'C'], 'PALACIO Rodrigo'))
	roster.append(Player(29, 12, 12, 0, 'A', ['L', 'R', 'C'], 'SANTANDER Federico'))
	roster.append(Player(25, 10, 10, 0, 'A', ['L', 'R', 'C'], 'DESTRO Mattia'))
	roster.append(Player(22, 9, 9, 0, 'A', ['L', 'R', 'C'], 'SKOV OLSEN Andreas'))
	roster.append(Player(2, 1, 1, 0, 'A', ['L', 'R', 'C'], 'JUWARA Musa'))
	return name, tactics, chariness, roster

def Brescia():
	name = "Brescia Calcio"
	tactics = F433
	chariness = 3
	roster = [Player(0, 23, 23, 57, 'GK', '', 'JORONEN Jesse')]
	roster.append(Player(0, 2, 2, 5, 'GK', '', 'ALFONSO Enrico'))
	roster.append(Player(0, 2, 2, 5, 'GK', '', 'ANDRENACCI Lorenzo'))
	roster.append(Player(12, 12, 29, 0, 'D', ['L', 'R', 'C'], 'MARTELLA Bruno'))
	roster.append(Player(10, 10, 25, 0, 'D', ['L', 'R', 'C'], 'MAGNANI Giangiacomo'))
	roster.append(Player(8, 8, 21, 0, 'D', ['L', 'R', 'C'], 'SABELLI Stefano'))
	roster.append(Player(7, 7, 18, 0, 'D', ['L', 'R', 'C'], 'CISTANA Andrea'))
	roster.append(Player(7, 7, 18, 0, 'D', ['L', 'R', 'C'], 'CHANCELLOR Jhon'))
	roster.append(Player(7, 7, 18, 0, 'D', ['L', 'R', 'C'], 'GASTALDELLO Daniele'))
	roster.append(Player(6, 6, 14, 0, 'D', ['L', 'R', 'C'], 'MATEJU Ales'))
	roster.append(Player(4, 4, 11, 0, 'D', ['L', 'R', 'C'], 'CURCIO Felipe'))
	roster.append(Player(2, 2, 4, 0, 'D', ['L', 'R', 'C'], 'MANGRAVITI Massimiliano'))
	roster.append(Player(2, 2, 4, 0, 'D', ['L', 'R', 'C'], 'SEMPRINI Alessandro'))
	roster.append(Player(18, 44, 18, 0, 'M', ['L', 'R', 'C'], 'BISOLI Dimitri'))
	roster.append(Player(16, 41, 16, 0, 'M', ['L', 'R', 'C'], 'ROMULO Orestes'))
	roster.append(Player(16, 41, 16, 0, 'M', ['L', 'R', 'C'], 'TONALI Sandro'))
	roster.append(Player(15, 37, 15, 0, 'M', ['L', 'R', 'C'], 'ZMRHAL Jaromir'))
	roster.append(Player(13, 33, 13, 0, 'M', ['L', 'R', 'C'], 'SPALEK Nikolas'))
	roster.append(Player(10, 26, 10, 0, 'M', ['L', 'R', 'C'], 'NDOJ Emanuele'))
	roster.append(Player(9, 22, 9, 0, 'M', ['L', 'R', 'C'], 'DESSENA Daniele'))
	roster.append(Player(8, 19, 8, 0, 'M', ['L', 'R', 'C'], 'TREMOLADA Luca'))
	roster.append(Player(2, 4, 2, 0, 'M', ['L', 'R', 'C'], 'VIVIANI Mattia'))
	roster.append(Player(49, 20, 20, 0, 'A', ['L', 'R', 'C'], 'BALOTELLI Mario'))
	roster.append(Player(39, 16, 16, 0, 'A', ['L', 'R', 'C'], 'DONNARUMMA Alfredo'))
	roster.append(Player(25, 10, 10, 0, 'A', ['L', 'R', 'C'], 'AYE Florian'))
	roster.append(Player(24, 10, 10, 0, 'A', ['L', 'R', 'C'], 'TORREGROSSA Ernesto'))
	roster.append(Player(18, 7, 7, 0, 'A', ['L', 'R', 'C'], 'MATRI Alessandro'))
	roster.append(Player(14, 6, 6, 0, 'A', ['L', 'R', 'C'], 'MOROSINI Leonardo'))
	return name, tactics, chariness, roster

def Cagliari():
	name = "Cagliari Calcio"
	tactics = F433
	chariness = 2
	roster = [Player(0, 27, 34, 67, 'GK', '', 'CRAGNO Alessio')]
	roster.append(Player(0, 4, 5, 10, 'GK', '', 'RAFAEL De Andrade Bittencourt'))
	roster.append(Player(0, 4, 5, 10, 'GK', '', 'OLSEN Robin'))
	roster.append(Player(0, 2, 3, 5, 'GK', '', 'ARESTI Simone'))
	roster.append(Player(12, 15, 29, 0, 'D', ['L', 'R', 'C'], 'PELLEGRINI Luca'))
	roster.append(Player(12, 15, 29, 0, 'D', ['L', 'R', 'C'], 'CEPPITELLI Luca'))
	roster.append(Player(10, 13, 25, 0, 'D', ['L', 'R', 'C'], 'CACCIATORE Fabrizio'))
	roster.append(Player(8, 11, 21, 0, 'D', ['L', 'R', 'C'], 'KLAVAN Ragnar'))
	roster.append(Player(8, 11, 21, 0, 'D', ['L', 'R', 'C'], 'PISACANE Fabio'))
	roster.append(Player(6, 7, 14, 0, 'D', ['L', 'R', 'C'], 'MATTIELLO Federico'))
	roster.append(Player(6, 7, 14, 0, 'D', ['L', 'R', 'C'], 'LYKOGIANNIS Charalampos'))
	roster.append(Player(3, 4, 7, 0, 'D', ['L', 'R', 'C'], 'WALUKIEWICZ Sebastian'))
	roster.append(Player(2, 2, 4, 0, 'D', ['L', 'R', 'C'], 'PINNA Simone'))
	roster.append(Player(39, 78, 31, 0, 'M', ['L', 'R', 'C'], 'NAINGGOLAN Radja'))
	roster.append(Player(26, 52, 21, 0, 'M', ['L', 'R', 'C'], 'CASTRO Lucas'))
	roster.append(Player(24, 48, 19, 0, 'M', ['L', 'R', 'C'], 'NANDEZ Nahitan'))
	roster.append(Player(21, 41, 16, 0, 'M', ['L', 'R', 'C'], 'BIRSA Valter'))
	roster.append(Player(19, 37, 15, 0, 'M', ['L', 'R', 'C'], 'IONITA Artur'))
	roster.append(Player(17, 33, 13, 0, 'M', ['L', 'R', 'C'], 'ROG Marko'))
	roster.append(Player(15, 30, 12, 0, 'M', ['L', 'R', 'C'], 'CIGARINI Luca'))
	roster.append(Player(10, 19, 8, 0, 'M', ['L', 'R', 'C'], 'OLIVA Christian'))
	roster.append(Player(10, 19, 8, 0, 'M', ['L', 'R', 'C'], 'FARAGÒ Paolo'))
	roster.append(Player(8, 15, 6, 0, 'M', ['L', 'R', 'C'], 'DEIOLA Alessandro'))
	roster.append(Player(49, 25, 20, 0, 'A', ['L', 'R', 'C'], 'PAVOLETTI Leonardo'))
	roster.append(Player(37, 19, 15, 0, 'A', ['L', 'R', 'C'], 'JOAO PEDRO Geraldino Galvao'))
	roster.append(Player(35, 18, 14, 0, 'A', ['L', 'R', 'C'], 'SIMEONE Giovanni'))
	roster.append(Player(16, 8, 6, 0, 'A', ['L', 'R', 'C'], 'CERRI Alberto'))
	roster.append(Player(6, 3, 2, 0, 'A', ['L', 'R', 'C'], 'RAGATZU Daniele'))
	return name, tactics, chariness, roster

def Fiorentina():
	name = "ACF Fiorentina"
	tactics = F433
	chariness = 2
	roster = [Player(0, 23, 29, 57, 'GK', '', 'DRAGOWSKI Bartlomiej')]
	roster.append(Player(0, 2, 3, 5, 'GK', '', 'TERRACCIANO Pietro'))
	roster.append(Player(20, 25, 50, 0, 'D', ['L', 'R', 'C'], 'MILENKOVIC Nikola'))
	roster.append(Player(18, 23, 46, 0, 'D', ['L', 'R', 'C'], 'PEZZELLA German'))
	roster.append(Player(14, 18, 36, 0, 'D', ['L', 'R', 'C'], 'LIROLA Pol'))
	roster.append(Player(12, 15, 29, 0, 'D', ['L', 'R', 'C'], 'CACERES Martín'))
	roster.append(Player(10, 13, 25, 0, 'D', ['L', 'R', 'C'], 'DALBERT Henrique'))
	roster.append(Player(8, 11, 21, 0, 'D', ['L', 'R', 'C'], 'VENUTI Lorenzo'))
	roster.append(Player(7, 9, 18, 0, 'D', ['L', 'R', 'C'], 'CECCHERINI Federico'))
	roster.append(Player(6, 7, 14, 0, 'D', ['L', 'R', 'C'], 'RASMUSSEN Jacob'))
	roster.append(Player(4, 6, 11, 0, 'D', ['L', 'R', 'C'], 'TERZIC Aleksa'))
	roster.append(Player(3, 4, 7, 0, 'D', ['L', 'R', 'C'], 'RANIERI Luca'))
	roster.append(Player(45, 89, 36, 0, 'M', ['L', 'R', 'C'], 'CHIESA Federico'))
	roster.append(Player(41, 81, 32, 0, 'M', ['L', 'R', 'C'], 'RIBERY Franck'))
	roster.append(Player(39, 78, 31, 0, 'M', ['L', 'R', 'C'], 'PULGAR Erick'))
	roster.append(Player(32, 63, 25, 0, 'M', ['L', 'R', 'C'], 'BENASSI Marco'))
	roster.append(Player(24, 48, 19, 0, 'M', ['L', 'R', 'C'], 'GHEZZAL Rachid'))
	roster.append(Player(21, 41, 16, 0, 'M', ['L', 'R', 'C'], 'BADELJ Milan'))
	roster.append(Player(13, 26, 10, 0, 'M', ['L', 'R', 'C'], 'ZURKOWSKI Szymon'))
	roster.append(Player(13, 26, 10, 0, 'M', ['L', 'R', 'C'], 'CASTROVILLI Gaetano'))
	roster.append(Player(11, 22, 9, 0, 'M', ['L', 'R', 'C'], 'DABO Bryan'))
	roster.append(Player(11, 22, 9, 0, 'M', ['L', 'R', 'C'], 'EYSSERIC Valentin'))
	roster.append(Player(8, 15, 6, 0, 'M', ['L', 'R', 'C'], 'CRISTOFORO Sebastian'))
	roster.append(Player(2, 4, 2, 0, 'M', ['L', 'R', 'C'], 'MONTIEL Cristobal'))
	roster.append(Player(41, 21, 16, 0, 'A', ['L', 'R', 'C'], 'PEDRO -'))
	roster.append(Player(39, 20, 16, 0, 'A', ['L', 'R', 'C'], 'BOATENG Kevin-Prince'))
	roster.append(Player(18, 9, 7, 0, 'A', ['L', 'R', 'C'], 'THEREAU Cyril'))
	roster.append(Player(8, 4, 3, 0, 'A', ['L', 'R', 'C'], 'SOTTIL Riccardo'))
	roster.append(Player(8, 4, 3, 0, 'A', ['L', 'R', 'C'], 'VLAHOVIC Dusan'))
	return name, tactics, chariness, roster

def Genoa():
	name = "Genoa CFC"
	tactics = F343
	chariness = 1
	roster = [Player(0, 21, 21, 52, 'GK', '', 'RADU Ionut')]
	roster.append(Player(0, 2, 2, 5, 'GK', '', 'JANDREI Chitolina Carniel'))
	roster.append(Player(0, 2, 2, 5, 'GK', '', 'MARCHETTI Federico'))
	roster.append(Player(0, 2, 2, 5, 'GK', '', 'VODISEK Rok'))
	roster.append(Player(20, 20, 50, 0, 'D', ['L', 'R', 'C'], 'CRISCITO Domenico'))
	roster.append(Player(16, 16, 39, 0, 'D', ['L', 'R', 'C'], 'ROMERO Cristian'))
	roster.append(Player(14, 14, 36, 0, 'D', ['L', 'R', 'C'], 'ZAPATA Cristian'))
	roster.append(Player(12, 12, 29, 0, 'D', ['L', 'R', 'C'], 'BIRASCHI Davide'))
	roster.append(Player(10, 10, 25, 0, 'D', ['L', 'R', 'C'], 'BARRECA Antonio'))
	roster.append(Player(10, 10, 25, 0, 'D', ['L', 'R', 'C'], 'PAJAC Marko'))
	roster.append(Player(7, 7, 18, 0, 'D', ['L', 'R', 'C'], 'ANKERSEN Peter'))
	roster.append(Player(7, 7, 18, 0, 'D', ['L', 'R', 'C'], 'GOLDANIGA Edoardo'))
	roster.append(Player(7, 7, 18, 0, 'D', ['L', 'R', 'C'], 'GHIGLIONE Paolo'))
	roster.append(Player(4, 4, 11, 0, 'D', ['L', 'R', 'C'], 'EL YAMIQ Jawad'))
	roster.append(Player(22, 56, 22, 0, 'M', ['L', 'R', 'C'], 'SCHONE Lasse'))
	roster.append(Player(19, 48, 19, 0, 'M', ['L', 'R', 'C'], 'SAPONARA Riccardo'))
	roster.append(Player(18, 44, 18, 0, 'M', ['L', 'R', 'C'], 'PANDEV Goran'))
	roster.append(Player(12, 30, 12, 0, 'M', ['L', 'R', 'C'], 'LERAGER Lukas'))
	roster.append(Player(12, 30, 12, 0, 'M', ['L', 'R', 'C'], 'JAGIELLO Filip'))
	roster.append(Player(10, 26, 10, 0, 'M', ['L', 'R', 'C'], 'RADOVANOVIC Ivan'))
	roster.append(Player(9, 22, 9, 0, 'M', ['L', 'R', 'C'], 'STURARO Stefano'))
	roster.append(Player(8, 19, 8, 0, 'M', ['L', 'R', 'C'], 'CASSATA Francesco'))
	roster.append(Player(4, 11, 4, 0, 'M', ['L', 'R', 'C'], 'AGUDELO Kevin'))
	roster.append(Player(2, 4, 2, 0, 'M', ['L', 'R', 'C'], 'ZENNARO Mattia'))
	roster.append(Player(35, 14, 14, 0, 'A', ['L', 'R', 'C'], 'PINAMONTI Andrea'))
	roster.append(Player(33, 13, 13, 0, 'A', ['L', 'R', 'C'], 'KOUAMÉ Christian'))
	roster.append(Player(25, 10, 10, 0, 'A', ['L', 'R', 'C'], 'SANABRIA Antonio'))
	roster.append(Player(22, 9, 9, 0, 'A', ['L', 'R', 'C'], 'GUMUS Sinan'))
	roster.append(Player(16, 6, 6, 0, 'A', ['L', 'R', 'C'], 'FAVILLI Andrea'))
	return name, tactics, chariness, roster

def Internazionale():
	name = "FC Inter Milan"
	tactics = F352
	chariness = 1
	roster = [Player(0, 38, 57, 95, 'GK', '', 'HANDANOVIC Samir')]
	roster.append(Player(0, 2, 3, 5, 'GK', '', 'PADELLI Daniele'))
	roster.append(Player(0, 2, 3, 5, 'GK', '', 'BERNI Tommaso'))
	roster.append(Player(28, 43, 71, 0, 'D', ['L', 'R', 'C'], 'GODIN Diego'))
	roster.append(Player(27, 41, 68, 0, 'D', ['L', 'R', 'C'], 'DE VRIJ Stefan'))
	roster.append(Player(24, 37, 61, 0, 'D', ['L', 'R', 'C'], 'SKRINIAR Milan'))
	roster.append(Player(16, 23, 39, 0, 'D', ['L', 'R', 'C'], 'ASAMOAH Kwadwo'))
	roster.append(Player(13, 19, 32, 0, 'D', ['L', 'R', 'C'], 'D''AMBROSIO Danilo'))
	roster.append(Player(10, 15, 25, 0, 'D', ['L', 'R', 'C'], 'BIRAGHI Cristiano'))
	roster.append(Player(7, 11, 18, 0, 'D', ['L', 'R', 'C'], 'BASTONI Alessandro'))
	roster.append(Player(6, 8, 14, 0, 'D', ['L', 'R', 'C'], 'RANOCCHIA Andrea'))
	roster.append(Player(4, 7, 11, 0, 'D', ['L', 'R', 'C'], 'DIMARCO Federico'))
	roster.append(Player(40, 67, 27, 0, 'M', ['L', 'R', 'C'], 'BROZOVIC Marcelo'))
	roster.append(Player(38, 63, 25, 0, 'M', ['L', 'R', 'C'], 'BARELLA Nicolò'))
	roster.append(Player(35, 59, 24, 0, 'M', ['L', 'R', 'C'], 'SENSI Stefano'))
	roster.append(Player(31, 52, 21, 0, 'M', ['L', 'R', 'C'], 'LAZARO Valentino'))
	roster.append(Player(29, 48, 19, 0, 'M', ['L', 'R', 'C'], 'VECINO Matias'))
	roster.append(Player(25, 41, 16, 0, 'M', ['L', 'R', 'C'], 'CANDREVA Antonio'))
	roster.append(Player(22, 37, 15, 0, 'M', ['L', 'R', 'C'], 'GAGLIARDINI Roberto'))
	roster.append(Player(16, 26, 10, 0, 'M', ['L', 'R', 'C'], 'BORJA VALERO Iglesias'))
	roster.append(Player(2, 4, 2, 0, 'M', ['L', 'R', 'C'], 'AGOUME Lucien'))
	roster.append(Player(71, 43, 28, 0, 'A', ['L', 'R', 'C'], 'LUKAKU Romelu'))
	roster.append(Player(55, 33, 22, 0, 'A', ['L', 'R', 'C'], 'MARTINEZ Lautaro'))
	roster.append(Player(51, 31, 20, 0, 'A', ['L', 'R', 'C'], 'SANCHEZ Alexis'))
	roster.append(Player(35, 21, 14, 0, 'A', ['L', 'R', 'C'], 'POLITANO Matteo'))
	roster.append(Player(2, 1, 1, 0, 'A', ['L', 'R', 'C'], 'ESPOSITO Sebastiano'))
	return name, tactics, chariness, roster

def Juventus():
	name = "Juventus FC"
	tactics = F433
	chariness = 1
	roster = [Player(0, 36, 54, 90, 'GK', '', 'SZCZESNY Wojciech')]
	roster.append(Player(0, 4, 6, 10, 'GK', '', 'BUFFON Gianluigi'))
	roster.append(Player(0, 2, 3, 5, 'GK', '', 'PINSOGLIO Carlo'))
	roster.append(Player(0, 2, 3, 5, 'GK', '', 'PERIN Mattia'))
	roster.append(Player(30, 45, 75, 0, 'D', ['L', 'R', 'C'], 'DE LIGT Matthijs'))
	roster.append(Player(28, 43, 71, 0, 'D', ['L', 'R', 'C'], 'CHIELLINI Giorgio'))
	roster.append(Player(26, 38, 64, 0, 'D', ['L', 'R', 'C'], 'ALEX SANDRO Lobo Silva'))
	roster.append(Player(23, 34, 57, 0, 'D', ['L', 'R', 'C'], 'BONUCCI Leonardo'))
	roster.append(Player(20, 30, 50, 0, 'D', ['L', 'R', 'C'], 'DANILO -'))
	roster.append(Player(14, 22, 36, 0, 'D', ['L', 'R', 'C'], 'DE SCIGLIO Mattia'))
	roster.append(Player(10, 15, 25, 0, 'D', ['L', 'R', 'C'], 'DEMIRAL Merih'))
	roster.append(Player(8, 13, 21, 0, 'D', ['L', 'R', 'C'], 'RUGANI Daniele'))
	roster.append(Player(51, 85, 34, 0, 'M', ['L', 'R', 'C'], 'RAMSEY Aaron'))
	roster.append(Player(47, 78, 31, 0, 'M', ['L', 'R', 'C'], 'PJANIC Miralem'))
	roster.append(Player(42, 70, 28, 0, 'M', ['L', 'R', 'C'], 'BERNARDESCHI Federico'))
	roster.append(Player(42, 70, 28, 0, 'M', ['L', 'R', 'C'], 'DOUGLAS COSTA de Souza'))
	roster.append(Player(40, 67, 27, 0, 'M', ['L', 'R', 'C'], 'RABIOT Adrien'))
	roster.append(Player(35, 59, 24, 0, 'M', ['L', 'R', 'C'], 'CAN Emre'))
	roster.append(Player(34, 56, 22, 0, 'M', ['L', 'R', 'C'], 'MATUIDI Blaise'))
	roster.append(Player(29, 48, 19, 0, 'M', ['L', 'R', 'C'], 'BENTANCUR Rodrigo'))
	roster.append(Player(26, 44, 18, 0, 'M', ['L', 'R', 'C'], 'CUADRADO Juan'))
	roster.append(Player(26, 44, 18, 0, 'M', ['L', 'R', 'C'], 'KHEDIRA Sami'))
	roster.append(Player(98, 59, 39, 0, 'A', ['L', 'R', 'C'], 'RONALDO Cristiano'))
	roster.append(Player(59, 35, 24, 0, 'A', ['L', 'R', 'C'], 'DYBALA Paulo'))
	roster.append(Player(55, 33, 22, 0, 'A', ['L', 'R', 'C'], 'HIGUAIN Gonzalo'))
	roster.append(Player(39, 23, 16, 0, 'A', ['L', 'R', 'C'], 'MANDZUKIC Mario'))
	roster.append(Player(16, 10, 6, 0, 'A', ['L', 'R', 'C'], 'PJACA Marko'))
	roster.append(Player(12, 7, 5, 0, 'A', ['L', 'R', 'C'], 'HAN Kwang Song'))
	return name, tactics, chariness, roster

def Lazio():
	name = "SS Lazio"
	tactics = F343
	chariness = 1
	roster = [Player(0, 30, 46, 76, 'GK', '', 'STRAKOSHA Thomas')]
	roster.append(Player(0, 2, 3, 5, 'GK', '', 'GUERRIERI Guido'))
	roster.append(Player(0, 2, 3, 5, 'GK', '', 'PROTO Silvio'))
	roster.append(Player(23, 34, 57, 0, 'D', ['L', 'R', 'C'], 'ACERBI Francesco'))
	roster.append(Player(12, 17, 29, 0, 'D', ['L', 'R', 'C'], 'VAVRO Denis'))
	roster.append(Player(10, 15, 25, 0, 'D', ['L', 'R', 'C'], 'LUIZ FELIPE Ramos Marchi'))
	roster.append(Player(10, 15, 25, 0, 'D', ['L', 'R', 'C'], 'BASTOS Jacinto Quissanga'))
	roster.append(Player(10, 15, 25, 0, 'D', ['L', 'R', 'C'], 'MARUSIC Adam'))
	roster.append(Player(10, 15, 25, 0, 'D', ['L', 'R', 'C'], 'RADU Stefan'))
	roster.append(Player(6, 8, 14, 0, 'D', ['L', 'R', 'C'], 'PATRIC Patricio Gabarron Gil'))
	roster.append(Player(6, 8, 14, 0, 'D', ['L', 'R', 'C'], 'LUKAKU Jordan Zacharie'))
	roster.append(Player(4, 7, 11, 0, 'D', ['L', 'R', 'C'], 'DURMISI Riza'))
	roster.append(Player(2, 2, 4, 0, 'D', ['L', 'R', 'C'], 'ARMINI Nicolo'))
	roster.append(Player(58, 96, 38, 0, 'M', ['L', 'R', 'C'], 'LUIS ALBERTO Romero Alconchel'))
	roster.append(Player(56, 93, 37, 0, 'M', ['L', 'R', 'C'], 'MILINKOVIC Sergej'))
	roster.append(Player(35, 59, 24, 0, 'M', ['L', 'R', 'C'], 'LULIC Senad'))
	roster.append(Player(31, 52, 21, 0, 'M', ['L', 'R', 'C'], 'PAROLO Marco'))
	roster.append(Player(31, 52, 21, 0, 'M', ['L', 'R', 'C'], 'LAZZARI Manuel'))
	roster.append(Player(29, 48, 19, 0, 'M', ['L', 'R', 'C'], 'LEIVA Lucas'))
	roster.append(Player(26, 44, 18, 0, 'M', ['L', 'R', 'C'], 'JONY -'))
	roster.append(Player(13, 22, 9, 0, 'M', ['L', 'R', 'C'], 'CATALDI Danilo'))
	roster.append(Player(11, 19, 8, 0, 'M', ['L', 'R', 'C'], 'BERISHA Valon'))
	roster.append(Player(4, 7, 3, 0, 'M', ['L', 'R', 'C'], 'ANDERSON Andre'))
	roster.append(Player(76, 46, 30, 0, 'A', ['L', 'R', 'C'], 'IMMOBILE Ciro'))
	roster.append(Player(45, 27, 18, 0, 'A', ['L', 'R', 'C'], 'CORREA Carlos Joaquin'))
	roster.append(Player(31, 19, 12, 0, 'A', ['L', 'R', 'C'], 'CAICEDO Felipe'))
	roster.append(Player(2, 1, 1, 0, 'A', ['L', 'R', 'C'], 'BOBBY Adekanye'))
	return name, tactics, chariness, roster

def Lecce():
	name = "US Lecce"
	tactics = F433
	chariness = 3
	roster = [Player(0, 17, 17, 43, 'GK', '', 'GABRIEL Vasconcelos Ferreira')]
	roster.append(Player(0, 2, 2, 5, 'GK', '', 'VIGORITO Mauro'))
	roster.append(Player(0, 2, 2, 5, 'GK', '', 'BLEVE Marco'))
	roster.append(Player(10, 10, 25, 0, 'D', ['L', 'R', 'C'], 'LUCIONI Fabio'))
	roster.append(Player(8, 8, 21, 0, 'D', ['L', 'R', 'C'], 'BENZAR Romario'))
	roster.append(Player(7, 7, 18, 0, 'D', ['L', 'R', 'C'], 'CALDERONI Marco'))
	roster.append(Player(7, 7, 18, 0, 'D', ['L', 'R', 'C'], 'DELL''ORCO Christian'))
	roster.append(Player(6, 6, 14, 0, 'D', ['L', 'R', 'C'], 'ROSSETTINI Luca'))
	roster.append(Player(6, 6, 14, 0, 'D', ['L', 'R', 'C'], 'MECCARIELLO Biagio'))
	roster.append(Player(6, 6, 14, 0, 'D', ['L', 'R', 'C'], 'VERA Brayan'))
	roster.append(Player(6, 6, 14, 0, 'D', ['L', 'R', 'C'], 'RISPOLI Andrea'))
	roster.append(Player(4, 4, 11, 0, 'D', ['L', 'R', 'C'], 'FIAMOZZI Riccardo'))
	roster.append(Player(2, 2, 4, 0, 'D', ['L', 'R', 'C'], 'GALLO Antonino'))
	roster.append(Player(2, 2, 4, 0, 'D', ['L', 'R', 'C'], 'DUMANCIC Luka'))
	roster.append(Player(2, 2, 4, 0, 'D', ['L', 'R', 'C'], 'RICCARDI Davide'))
	roster.append(Player(19, 48, 19, 0, 'M', ['L', 'R', 'C'], 'MANCOSU Marco'))
	roster.append(Player(15, 37, 15, 0, 'M', ['L', 'R', 'C'], 'SHAKHOV Evgen'))
	roster.append(Player(12, 30, 12, 0, 'M', ['L', 'R', 'C'], 'IMBULA Giannelli'))
	roster.append(Player(10, 26, 10, 0, 'M', ['L', 'R', 'C'], 'TACHTSIDIS Panagiotis'))
	roster.append(Player(9, 22, 9, 0, 'M', ['L', 'R', 'C'], 'TABANELLI Andrea'))
	roster.append(Player(9, 22, 9, 0, 'M', ['L', 'R', 'C'], 'PETRICCIONE Jacopo'))
	roster.append(Player(6, 15, 6, 0, 'M', ['L', 'R', 'C'], 'MAJER Zan'))
	roster.append(Player(29, 12, 12, 0, 'A', ['L', 'R', 'C'], 'BABACAR Khouma El'))
	roster.append(Player(25, 10, 10, 0, 'A', ['L', 'R', 'C'], 'FARIAS Diego'))
	roster.append(Player(25, 10, 10, 0, 'A', ['L', 'R', 'C'], 'LA MANTIA Andrea'))
	roster.append(Player(24, 10, 10, 0, 'A', ['L', 'R', 'C'], 'LAPADULA Gianluca'))
	roster.append(Player(22, 9, 9, 0, 'A', ['L', 'R', 'C'], 'FALCO Filippo'))
	roster.append(Player(6, 2, 2, 0, 'A', ['L', 'R', 'C'], 'LO FASO Simone'))
	roster.append(Player(2, 1, 1, 0, 'A', ['L', 'R', 'C'], 'DUBICKAS Edgaras'))
	return name, tactics, chariness, roster

def Milan():
	name = "AC Milan"
	tactics = F433
	chariness = 2
	roster = [Player(0, 36, 36, 90, 'GK', '', 'DONNARUMMA Gianluigi')]
	roster.append(Player(0, 2, 2, 5, 'GK', '', 'REINA Pepe'))
	roster.append(Player(0, 2, 2, 5, 'GK', '', 'DONNARUMMA Antonio'))
	roster.append(Player(23, 23, 57, 0, 'D', ['L', 'R', 'C'], 'ROMAGNOLI Alessio'))
	roster.append(Player(16, 16, 39, 0, 'D', ['L', 'R', 'C'], 'HERNANDEZ Theo'))
	roster.append(Player(14, 14, 36, 0, 'D', ['L', 'R', 'C'], 'CALABRIA Davide'))
	roster.append(Player(13, 13, 32, 0, 'D', ['L', 'R', 'C'], 'CONTI Andrea'))
	roster.append(Player(12, 12, 29, 0, 'D', ['L', 'R', 'C'], 'MUSACCHIO Mateo'))
	roster.append(Player(12, 12, 29, 0, 'D', ['L', 'R', 'C'], 'RODRIGUEZ Ricardo'))
	roster.append(Player(10, 10, 25, 0, 'D', ['L', 'R', 'C'], 'DUARTE Leo'))
	roster.append(Player(10, 10, 25, 0, 'D', ['L', 'R', 'C'], 'CALDARA Mattia'))
	roster.append(Player(2, 2, 4, 0, 'D', ['L', 'R', 'C'], 'GABBIA Matteo'))
	roster.append(Player(31, 78, 31, 0, 'M', ['L', 'R', 'C'], 'SUSO Jesus Fernandez Saez'))
	roster.append(Player(28, 70, 28, 0, 'M', ['L', 'R', 'C'], 'KESSIE Franck'))
	roster.append(Player(27, 67, 27, 0, 'M', ['L', 'R', 'C'], 'PAQUETA Lucas'))
	roster.append(Player(25, 63, 25, 0, 'M', ['L', 'R', 'C'], 'CALHANOGLU Hakan'))
	roster.append(Player(21, 52, 21, 0, 'M', ['L', 'R', 'C'], 'BONAVENTURA Giacomo'))
	roster.append(Player(19, 48, 19, 0, 'M', ['L', 'R', 'C'], 'KRUNIC Rade'))
	roster.append(Player(18, 44, 18, 0, 'M', ['L', 'R', 'C'], 'CASTILLEJO Samu'))
	roster.append(Player(18, 44, 18, 0, 'M', ['L', 'R', 'C'], 'BENNACER Ismael'))
	roster.append(Player(12, 30, 12, 0, 'M', ['L', 'R', 'C'], 'BORINI Fabio'))
	roster.append(Player(12, 30, 12, 0, 'M', ['L', 'R', 'C'], 'BIGLIA Lucas'))
	roster.append(Player(67, 27, 27, 0, 'A', ['L', 'R', 'C'], 'PIATEK Krzysztof'))
	roster.append(Player(39, 16, 16, 0, 'A', ['L', 'R', 'C'], 'REBIC Ante'))
	roster.append(Player(39, 16, 16, 0, 'A', ['L', 'R', 'C'], 'LEAO Rafael'))
	return name, tactics, chariness, roster

def Napoli():
	name = "SSC Napoli"
	tactics = F442
	chariness = 2
	roster = [Player(0, 28, 43, 71, 'GK', '', 'MERET Alex')]
	roster.append(Player(0, 4, 6, 10, 'GK', '', 'OSPINA David'))
	roster.append(Player(0, 2, 3, 5, 'GK', '', 'KARNEZIS Orestis'))
	roster.append(Player(27, 41, 68, 0, 'D', ['L', 'R', 'C'], 'MANOLAS Konstantinos'))
	roster.append(Player(26, 38, 64, 0, 'D', ['L', 'R', 'C'], 'KOULIBALY Kalidou'))
	roster.append(Player(24, 37, 61, 0, 'D', ['L', 'R', 'C'], 'DI LORENZO Giovanni'))
	roster.append(Player(18, 28, 46, 0, 'D', ['L', 'R', 'C'], 'GHOULAM Faouzi'))
	roster.append(Player(13, 19, 32, 0, 'D', ['L', 'R', 'C'], 'MARIO RUI Silva Duarte'))
	roster.append(Player(10, 15, 25, 0, 'D', ['L', 'R', 'C'], 'MALCUIT Kevin'))
	roster.append(Player(8, 13, 21, 0, 'D', ['L', 'R', 'C'], 'MAKSIMOVIC Nikola'))
	roster.append(Player(8, 13, 21, 0, 'D', ['L', 'R', 'C'], 'HYSAJ Elseid'))
	roster.append(Player(6, 8, 14, 0, 'D', ['L', 'R', 'C'], 'TONELLI Lorenzo'))
	roster.append(Player(4, 7, 11, 0, 'D', ['L', 'R', 'C'], 'LUPERTO Sebastiano'))
	roster.append(Player(56, 93, 37, 0, 'M', ['L', 'R', 'C'], 'CALLEJON Jose Maria'))
	roster.append(Player(49, 81, 32, 0, 'M', ['L', 'R', 'C'], 'RUIZ Fabian'))
	roster.append(Player(44, 74, 30, 0, 'M', ['L', 'R', 'C'], 'ZIELINSKI Piotr'))
	roster.append(Player(38, 63, 25, 0, 'M', ['L', 'R', 'C'], 'ALLAN Marques Loureiro'))
	roster.append(Player(29, 48, 19, 0, 'M', ['L', 'R', 'C'], 'YOUNES Amin'))
	roster.append(Player(22, 37, 15, 0, 'M', ['L', 'R', 'C'], 'ELMAS Eljif'))
	roster.append(Player(2, 4, 2, 0, 'M', ['L', 'R', 'C'], 'GAETANO Gianluca'))
	roster.append(Player(65, 39, 26, 0, 'A', ['L', 'R', 'C'], 'INSIGNE Lorenzo'))
	roster.append(Player(65, 39, 26, 0, 'A', ['L', 'R', 'C'], 'MILIK Arkadiusz'))
	roster.append(Player(65, 39, 26, 0, 'A', ['L', 'R', 'C'], 'MERTENS Dries'))
	roster.append(Player(55, 33, 22, 0, 'A', ['L', 'R', 'C'], 'LOZANO Hirving'))
	roster.append(Player(29, 17, 12, 0, 'A', ['L', 'R', 'C'], 'LLORENTE Fernando'))
	return name, tactics, chariness, roster

def Parma():
	name = "Parma Calcio"
	tactics = F433
	chariness = 2
	roster = [Player(0, 21, 21, 52, 'GK', '', 'SEPE Luigi')]
	roster.append(Player(0, 2, 2, 5, 'GK', '', 'CORVI Edoardo'))
	roster.append(Player(0, 2, 2, 5, 'GK', '', 'COLOMBI Simone'))
	roster.append(Player(0, 2, 2, 5, 'GK', '', 'ALASTRA Fabrizio'))
	roster.append(Player(18, 18, 46, 0, 'D', ['L', 'R', 'C'], 'ALVES Bruno'))
	roster.append(Player(14, 14, 36, 0, 'D', ['L', 'R', 'C'], 'DARMIAN Matteo'))
	roster.append(Player(13, 13, 32, 0, 'D', ['L', 'R', 'C'], 'GAGLIOLO Riccardo'))
	roster.append(Player(7, 7, 18, 0, 'D', ['L', 'R', 'C'], 'PEZZELLA Giuseppe'))
	roster.append(Player(7, 7, 18, 0, 'D', ['L', 'R', 'C'], 'IACOPONI Simone'))
	roster.append(Player(6, 6, 14, 0, 'D', ['L', 'R', 'C'], 'LAURINI Vincent'))
	roster.append(Player(4, 4, 11, 0, 'D', ['L', 'R', 'C'], 'DERMAKU Kastriot'))
	roster.append(Player(22, 56, 22, 0, 'M', ['L', 'R', 'C'], 'KUCKA Juraj'))
	roster.append(Player(16, 41, 16, 0, 'M', ['L', 'R', 'C'], 'BARILLÀ Antonino'))
	roster.append(Player(15, 37, 15, 0, 'M', ['L', 'R', 'C'], 'HERNANI Azevedo Júnior'))
	roster.append(Player(12, 30, 12, 0, 'M', ['L', 'R', 'C'], 'BRUGMAN Gaston'))
	roster.append(Player(9, 22, 9, 0, 'M', ['L', 'R', 'C'], 'SCOZZARELLA Matteo'))
	roster.append(Player(9, 22, 9, 0, 'M', ['L', 'R', 'C'], 'GRASSI Alberto'))
	roster.append(Player(6, 15, 6, 0, 'M', ['L', 'R', 'C'], 'KULUSEVSKI Dejan'))
	roster.append(Player(4, 11, 4, 0, 'M', ['L', 'R', 'C'], 'MUNARI Gianni'))
	roster.append(Player(57, 23, 23, 0, 'A', ['L', 'R', 'C'], 'GERVINHO undefined'))
	roster.append(Player(43, 17, 17, 0, 'A', ['L', 'R', 'C'], 'INGLESE Roberto'))
	roster.append(Player(24, 10, 10, 0, 'A', ['L', 'R', 'C'], 'KARAMOH Yann'))
	roster.append(Player(20, 8, 8, 0, 'A', ['L', 'R', 'C'], 'CORNELIUS Andreas'))
	roster.append(Player(12, 5, 5, 0, 'A', ['L', 'R', 'C'], 'SPROCATI Mattia'))
	roster.append(Player(10, 4, 4, 0, 'A', ['L', 'R', 'C'], 'SILIGARDI Luca'))
	roster.append(Player(2, 1, 1, 0, 'A', ['L', 'R', 'C'], 'ADORANTE Andrea'))
	return name, tactics, chariness, roster

def Roma():
	name = "AS Roma"
	tactics = F424
	chariness = 1
	roster = [Player(0, 30, 46, 76, 'GK', '', 'LOPEZ Pau')]
	roster.append(Player(0, 2, 3, 5, 'GK', '', 'FUZATO Daniel'))
	roster.append(Player(0, 2, 3, 5, 'GK', '', 'MIRANTE Antonio'))
	roster.append(Player(38, 58, 96, 0, 'D', ['L', 'R', 'C'], 'KOLAROV Aleksandar'))
	roster.append(Player(23, 34, 57, 0, 'D', ['L', 'R', 'C'], 'FLORENZI Alessandro'))
	roster.append(Player(22, 32, 54, 0, 'D', ['L', 'R', 'C'], 'FAZIO Federico'))
	roster.append(Player(20, 30, 50, 0, 'D', ['L', 'R', 'C'], 'MANCINI Gianluca'))
	roster.append(Player(18, 28, 46, 0, 'D', ['L', 'R', 'C'], 'SMALLING Chris'))
	roster.append(Player(16, 23, 39, 0, 'D', ['L', 'R', 'C'], 'ZAPPACOSTA Davide'))
	roster.append(Player(14, 22, 36, 0, 'D', ['L', 'R', 'C'], 'SPINAZZOLA Leonardo'))
	roster.append(Player(6, 8, 14, 0, 'D', ['L', 'R', 'C'], 'CETIN Mert'))
	roster.append(Player(6, 8, 14, 0, 'D', ['L', 'R', 'C'], 'JUAN JESUS Guilherme Nunes'))
	roster.append(Player(6, 8, 14, 0, 'D', ['L', 'R', 'C'], 'SANTON Davide'))
	roster.append(Player(53, 89, 36, 0, 'M', ['L', 'R', 'C'], 'MKHITARYAN Henrikh'))
	roster.append(Player(45, 27, 18, 0, 'A', ['L', 'R', 'C'], 'UNDER Cengiz'))
	roster.append(Player(41, 25, 16, 0, 'A', ['L', 'R', 'C'], 'ZANIOLO Nicolò'))
	roster.append(Player(38, 63, 25, 0, 'M', ['L', 'R', 'C'], 'PELLEGRINI Lorenzo'))
	roster.append(Player(38, 63, 25, 0, 'M', ['L', 'R', 'C'], 'VERETOUT Jordan'))
	roster.append(Player(38, 63, 25, 0, 'M', ['L', 'R', 'C'], 'PEROTTI Diego'))
	roster.append(Player(33, 20, 13, 0, 'A', ['L', 'R', 'C'], 'KLUIVERT Justin'))
	roster.append(Player(34, 56, 22, 0, 'M', ['L', 'R', 'C'], 'CRISTANTE Bryan'))
	roster.append(Player(26, 44, 18, 0, 'M', ['L', 'R', 'C'], 'PASTORE Javier'))
	roster.append(Player(20, 33, 13, 0, 'M', ['L', 'R', 'C'], 'DIAWARA Amadou'))
	roster.append(Player(2, 4, 2, 0, 'M', ['L', 'R', 'C'], 'RICCARDI Alessio'))
	roster.append(Player(55, 33, 22, 0, 'A', ['L', 'R', 'C'], 'DZEKO Edin'))
	roster.append(Player(31, 19, 12, 0, 'A', ['L', 'R', 'C'], 'KALINIC Nikola'))
	roster.append(Player(4, 2, 2, 0, 'A', ['L', 'R', 'C'], 'ANTONUCCI Mirko'))
	return name, tactics, chariness, roster

def Sampdoria():
	name = "UC Sampdoria"
	tactics = F433
	chariness = 3
	roster = [Player(0, 21, 21, 52, 'GK', '', 'AUDERO Emil')]
	roster.append(Player(0, 2, 2, 5, 'GK', '', 'FALCONE Wladimiro'))
	roster.append(Player(0, 2, 2, 5, 'GK', '', 'SECULIN Andrea'))
	roster.append(Player(10, 10, 25, 0, 'D', ['L', 'R', 'C'], 'MURILLO Jeison Fabian'))
	roster.append(Player(10, 10, 25, 0, 'D', ['L', 'R', 'C'], 'MURRU Nicola'))
	roster.append(Player(8, 8, 21, 0, 'D', ['L', 'R', 'C'], 'COLLEY Omar'))
	roster.append(Player(7, 7, 18, 0, 'D', ['L', 'R', 'C'], 'BERESZYNSKI Bartosz'))
	roster.append(Player(7, 7, 18, 0, 'D', ['L', 'R', 'C'], 'DEPAOLI Fabio'))
	roster.append(Player(6, 6, 14, 0, 'D', ['L', 'R', 'C'], 'CHABOT Julian'))
	roster.append(Player(4, 4, 11, 0, 'D', ['L', 'R', 'C'], 'AUGELLO Tommaso'))
	roster.append(Player(4, 4, 11, 0, 'D', ['L', 'R', 'C'], 'FERRARI Alex'))
	roster.append(Player(4, 4, 11, 0, 'D', ['L', 'R', 'C'], 'REGINI Vasco'))
	roster.append(Player(21, 52, 21, 0, 'M', ['L', 'R', 'C'], 'RAMIREZ Gastón'))
	roster.append(Player(19, 48, 19, 0, 'M', ['L', 'R', 'C'], 'LINETTY Karol'))
	roster.append(Player(16, 41, 16, 0, 'M', ['L', 'R', 'C'], 'JANKTO Jakub'))
	roster.append(Player(15, 37, 15, 0, 'M', ['L', 'R', 'C'], 'EKDAL Albin'))
	roster.append(Player(13, 33, 13, 0, 'M', ['L', 'R', 'C'], 'MARONI Gonzalo'))
	roster.append(Player(12, 30, 12, 0, 'M', ['L', 'R', 'C'], 'THORSBY Morten'))
	roster.append(Player(8, 19, 8, 0, 'M', ['L', 'R', 'C'], 'LERIS Mehdi'))
	roster.append(Player(8, 19, 8, 0, 'M', ['L', 'R', 'C'], 'BARRETO Edgar'))
	roster.append(Player(6, 15, 6, 0, 'M', ['L', 'R', 'C'], 'VIEIRA Ronaldo'))
	roster.append(Player(2, 4, 2, 0, 'M', ['L', 'R', 'C'], 'POMPETTI Marco'))
	roster.append(Player(69, 28, 28, 0, 'A', ['L', 'R', 'C'], 'QUAGLIARELLA Fabio'))
	roster.append(Player(35, 14, 14, 0, 'A', ['L', 'R', 'C'], 'RIGONI Emiliano'))
	roster.append(Player(27, 11, 11, 0, 'A', ['L', 'R', 'C'], 'GABBIADINI Manolo'))
	roster.append(Player(24, 10, 10, 0, 'A', ['L', 'R', 'C'], 'CAPRARI Gianluca'))
	roster.append(Player(14, 6, 6, 0, 'A', ['L', 'R', 'C'], 'BONAZZOLI Federico'))
	return name, tactics, chariness, roster

def Sassuolo():
	name = "USS Sassuolo Calcio"
	tactics = F433
	chariness = 2
	roster = [Player(0, 21, 21, 52, 'GK', '', 'CONSIGLI Andrea')]
	roster.append(Player(0, 2, 2, 5, 'GK', '', 'PEGOLO Gianluca'))
	roster.append(Player(0, 2, 2, 5, 'GK', '', 'RUSSO Alessandro'))
	roster.append(Player(18, 18, 46, 0, 'D', ['L', 'R', 'C'], 'FERRARI Gianmarco'))
	roster.append(Player(10, 10, 25, 0, 'D', ['L', 'R', 'C'], 'CHIRICHES Vlad'))
	roster.append(Player(10, 10, 25, 0, 'D', ['L', 'R', 'C'], 'ROGERIO Oliveira Da Silva'))
	roster.append(Player(10, 10, 25, 0, 'D', ['L', 'R', 'C'], 'TOLJAN Jeremy'))
	roster.append(Player(8, 8, 21, 0, 'D', ['L', 'R', 'C'], 'PELUSO Federico'))
	roster.append(Player(8, 8, 21, 0, 'D', ['L', 'R', 'C'], 'MARLON -'))
	roster.append(Player(7, 7, 18, 0, 'D', ['L', 'R', 'C'], 'MULDUR Mert'))
	roster.append(Player(7, 7, 18, 0, 'D', ['L', 'R', 'C'], 'KYRIAKOPOULOS Georgios'))
	roster.append(Player(7, 7, 18, 0, 'D', ['L', 'R', 'C'], 'ROMAGNA Filippo'))
	roster.append(Player(3, 3, 7, 0, 'D', ['L', 'R', 'C'], 'TRIPALDELLI Alessandro'))
	roster.append(Player(25, 63, 25, 0, 'M', ['L', 'R', 'C'], 'TRAORE Hamed Junior'))
	roster.append(Player(24, 59, 24, 0, 'M', ['L', 'R', 'C'], 'DUNCAN Alfred'))
	roster.append(Player(16, 41, 16, 0, 'M', ['L', 'R', 'C'], 'LOCATELLI Manuel'))
	roster.append(Player(13, 33, 13, 0, 'M', ['L', 'R', 'C'], 'OBIANG Pedro'))
	roster.append(Player(12, 30, 12, 0, 'M', ['L', 'R', 'C'], 'BOURABIA Mehdi'))
	roster.append(Player(12, 30, 12, 0, 'M', ['L', 'R', 'C'], 'DJURICIC Filip'))
	roster.append(Player(9, 22, 9, 0, 'M', ['L', 'R', 'C'], 'MAGNANELLI Francesco'))
	roster.append(Player(6, 15, 6, 0, 'M', ['L', 'R', 'C'], 'MAZZITELLI Luca'))
	roster.append(Player(51, 20, 20, 0, 'A', ['L', 'R', 'C'], 'CAPUTO Francesco'))
	roster.append(Player(49, 20, 20, 0, 'A', ['L', 'R', 'C'], 'BERARDI Domenico'))
	roster.append(Player(39, 16, 16, 0, 'A', ['L', 'R', 'C'], 'DEFREL Gregoire'))
	roster.append(Player(25, 10, 10, 0, 'A', ['L', 'R', 'C'], 'BOGA Jeremie'))
	roster.append(Player(2, 1, 1, 0, 'A', ['L', 'R', 'C'], 'RASPADORI Giacomo'))
	return name, tactics, chariness, roster

def Spal():
	name = "S.P.A.L"
	tactics = F352
	chariness = 3
	roster = [Player(0, 23, 23, 57, 'GK', '', 'BERISHA Etrit')]
	roster.append(Player(0, 2, 2, 5, 'GK', '', 'THIAM Demba'))
	roster.append(Player(0, 2, 2, 5, 'GK', '', 'LETICA Karlo'))
	roster.append(Player(14, 14, 36, 0, 'D', ['L', 'R', 'C'], 'FARES Mohamed'))
	roster.append(Player(10, 10, 25, 0, 'D', ['L', 'R', 'C'], 'VICARI Francesco'))
	roster.append(Player(8, 8, 21, 0, 'D', ['L', 'R', 'C'], 'FELIPE Dal Belo'))
	roster.append(Player(8, 8, 21, 0, 'D', ['L', 'R', 'C'], 'IGOR JULIO dos Santos de Paulo'))
	roster.append(Player(8, 8, 21, 0, 'D', ['L', 'R', 'C'], 'CIONEK Thiago'))
	roster.append(Player(8, 8, 21, 0, 'D', ['L', 'R', 'C'], 'RECA Arkadiusz'))
	roster.append(Player(7, 7, 18, 0, 'D', ['L', 'R', 'C'], 'SALA Jacopo'))
	roster.append(Player(6, 6, 14, 0, 'D', ['L', 'R', 'C'], 'TOMOVIC Nenad'))
	roster.append(Player(2, 2, 4, 0, 'D', ['L', 'R', 'C'], 'FARCAS Ricardo'))
	roster.append(Player(24, 59, 24, 0, 'M', ['L', 'R', 'C'], 'KURTIC Jasmin'))
	roster.append(Player(12, 30, 12, 0, 'M', ['L', 'R', 'C'], 'MISSIROLI Simone'))
	roster.append(Player(12, 30, 12, 0, 'M', ['L', 'R', 'C'], 'D''ALESSANDRO Marco'))
	roster.append(Player(10, 26, 10, 0, 'M', ['L', 'R', 'C'], 'MURGIA Alessandro'))
	roster.append(Player(10, 26, 10, 0, 'M', ['L', 'R', 'C'], 'VALOTI Mattia'))
	roster.append(Player(6, 15, 6, 0, 'M', ['L', 'R', 'C'], 'STREFEZZA Gabriel'))
	roster.append(Player(6, 15, 6, 0, 'M', ['L', 'R', 'C'], 'VALDIFIORI Mirko'))
	roster.append(Player(2, 4, 2, 0, 'M', ['L', 'R', 'C'], 'MAWULI Shaka Eklu'))
	roster.append(Player(47, 19, 19, 0, 'A', ['L', 'R', 'C'], 'PETAGNA Andrea'))
	roster.append(Player(29, 12, 12, 0, 'A', ['L', 'R', 'C'], 'DI FRANCESCO Federico'))
	roster.append(Player(25, 10, 10, 0, 'A', ['L', 'R', 'C'], 'MONCINI Gabriele'))
	roster.append(Player(22, 9, 9, 0, 'A', ['L', 'R', 'C'], 'FLOCCARI Sergio'))
	roster.append(Player(18, 7, 7, 0, 'A', ['L', 'R', 'C'], 'PALOSCHI Alberto'))
	roster.append(Player(10, 4, 4, 0, 'A', ['L', 'R', 'C'], 'JANKOVIC Marko'))
	return name, tactics, chariness, roster

def Torino():
	name = "Torino FC"
	tactics = F343
	chariness = 2
	roster = [Player(0, 34, 34, 86, 'GK', '', 'SIRIGU Salvatore')]
	roster.append(Player(0, 2, 2, 5, 'GK', '', 'UJKANI Samir'))
	roster.append(Player(0, 2, 2, 5, 'GK', '', 'ZACCAGNO Andrea'))
	roster.append(Player(0, 2, 2, 5, 'GK', '', 'ROSATI Antonio'))
	roster.append(Player(30, 30, 75, 0, 'D', ['L', 'R', 'C'], 'IZZO Armando'))
	roster.append(Player(22, 22, 54, 0, 'D', ['L', 'R', 'C'], 'NKOULOU Nicolas'))
	roster.append(Player(18, 18, 46, 0, 'D', ['L', 'R', 'C'], 'DE SILVESTRI Lorenzo'))
	roster.append(Player(14, 14, 36, 0, 'D', ['L', 'R', 'C'], 'AINA Ola'))
	roster.append(Player(13, 13, 32, 0, 'D', ['L', 'R', 'C'], 'BONIFAZI Kevin'))
	roster.append(Player(10, 10, 25, 0, 'D', ['L', 'R', 'C'], 'LAXALT Diego'))
	roster.append(Player(10, 10, 25, 0, 'D', ['L', 'R', 'C'], 'LYANCO Silveira Neves Vojnovic'))
	roster.append(Player(8, 8, 21, 0, 'D', ['L', 'R', 'C'], 'DJIDJI Koffi'))
	roster.append(Player(4, 4, 11, 0, 'D', ['L', 'R', 'C'], 'BREMER Gleison Silva Nascimento'))
	roster.append(Player(3, 3, 7, 0, 'D', ['L', 'R', 'C'], 'BUONGIORNO Alessandro'))
	roster.append(Player(2, 2, 4, 0, 'D', ['L', 'R', 'C'], 'SINGO Wilfried Stephane'))
	roster.append(Player(25, 63, 25, 0, 'M', ['L', 'R', 'C'], 'VERDI Simone'))
	roster.append(Player(25, 63, 25, 0, 'M', ['L', 'R', 'C'], 'BASELLI Daniele'))
	roster.append(Player(22, 56, 22, 0, 'M', ['L', 'R', 'C'], 'BERENGUER Alex'))
	roster.append(Player(21, 52, 21, 0, 'M', ['L', 'R', 'C'], 'ANSALDI Cristian'))
	roster.append(Player(21, 52, 21, 0, 'M', ['L', 'R', 'C'], 'RINCON Tomas'))
	roster.append(Player(19, 48, 19, 0, 'M', ['L', 'R', 'C'], 'MEITE Soualiho'))
	roster.append(Player(12, 30, 12, 0, 'M', ['L', 'R', 'C'], 'LUKIC Sasa'))
	roster.append(Player(63, 25, 25, 0, 'A', ['L', 'R', 'C'], 'BELOTTI Andrea'))
	roster.append(Player(49, 20, 20, 0, 'A', ['L', 'R', 'C'], 'IAGO Falque'))
	roster.append(Player(29, 12, 12, 0, 'A', ['L', 'R', 'C'], 'ZAZA Simone'))
	roster.append(Player(10, 4, 4, 0, 'A', ['L', 'R', 'C'], 'EDERA Simone'))
	roster.append(Player(10, 4, 4, 0, 'A', ['L', 'R', 'C'], 'PARIGINI Vittorio'))
	roster.append(Player(4, 2, 2, 0, 'A', ['L', 'R', 'C'], 'MILLICO Vincenzo'))
	return name, tactics, chariness, roster

def Udinese():
	name = "Udinese Calcio"
	tactics = F433
	chariness = 2
	roster = [Player(0, 21, 21, 52, 'GK', '', 'MUSSO Juan')]
	roster.append(Player(0, 2, 2, 5, 'GK', '', 'NICOLAS Andrade'))
	roster.append(Player(0, 2, 2, 5, 'GK', '', 'GASPARINI Manuel'))
	roster.append(Player(0, 2, 2, 5, 'GK', '', 'PERISAN Samuele'))
	roster.append(Player(16, 16, 39, 0, 'D', ['L', 'R', 'C'], 'LARSEN Jens Stryger'))
	roster.append(Player(14, 14, 36, 0, 'D', ['L', 'R', 'C'], 'RODRIGO BECãO Nascimiento Franca'))
	roster.append(Player(13, 13, 32, 0, 'D', ['L', 'R', 'C'], 'SAMIR Caetano de Sousa'))
	roster.append(Player(12, 12, 29, 0, 'D', ['L', 'R', 'C'], 'TROOST-EKONG William'))
	roster.append(Player(8, 8, 21, 0, 'D', ['L', 'R', 'C'], 'DE MAIO Sebastian'))
	roster.append(Player(7, 7, 18, 0, 'D', ['L', 'R', 'C'], 'NUYTINCK Bram'))
	roster.append(Player(6, 6, 14, 0, 'D', ['L', 'R', 'C'], 'TER AVEST Hidde'))
	roster.append(Player(6, 6, 14, 0, 'D', ['L', 'R', 'C'], 'OPOKU Nicholas'))
	roster.append(Player(4, 4, 11, 0, 'D', ['L', 'R', 'C'], 'SIERRALTA Francisco'))
	roster.append(Player(30, 74, 30, 0, 'M', ['L', 'R', 'C'], 'DE PAUL Rodrigo'))
	roster.append(Player(18, 44, 18, 0, 'M', ['L', 'R', 'C'], 'FOFANA Seko'))
	roster.append(Player(16, 41, 16, 0, 'M', ['L', 'R', 'C'], 'MANDRAGORA Rolando'))
	roster.append(Player(15, 37, 15, 0, 'M', ['L', 'R', 'C'], 'BARAK Antonin'))
	roster.append(Player(12, 30, 12, 0, 'M', ['L', 'R', 'C'], 'JAJALO Mato'))
	roster.append(Player(10, 26, 10, 0, 'M', ['L', 'R', 'C'], 'WALACE -'))
	roster.append(Player(10, 26, 10, 0, 'M', ['L', 'R', 'C'], 'SEMA Ken'))
	roster.append(Player(33, 13, 13, 0, 'A', ['L', 'R', 'C'], 'LASAGNA Kevin'))
	roster.append(Player(33, 13, 13, 0, 'A', ['L', 'R', 'C'], 'NESTOROVSKI Ilija'))
	roster.append(Player(33, 13, 13, 0, 'A', ['L', 'R', 'C'], 'OKAKA Stefano'))
	roster.append(Player(24, 10, 10, 0, 'A', ['L', 'R', 'C'], 'PUSSETTO Ignacio'))
	roster.append(Player(20, 8, 8, 0, 'A', ['L', 'R', 'C'], 'TEODORCZYK Lukasz'))
	return name, tactics, chariness, roster

def Verona():
	name = "Hellas Verona FC"
	tactics = F343
	chariness = 3
	roster = [Player(0, 19, 19, 48, 'GK', '', 'SILVESTRI Marco')]
	roster.append(Player(0, 4, 4, 10, 'GK', '', 'RADUNOVIC Boris'))
	roster.append(Player(0, 2, 2, 5, 'GK', '', 'BERARDI Alessandro'))
	roster.append(Player(12, 12, 29, 0, 'D', ['L', 'R', 'C'], 'FARAONI Davide'))
	roster.append(Player(10, 10, 25, 0, 'D', ['L', 'R', 'C'], 'RRAHMANI Amir'))
	roster.append(Player(8, 8, 21, 0, 'D', ['L', 'R', 'C'], 'ADJAPONG Claud'))
	roster.append(Player(8, 8, 21, 0, 'D', ['L', 'R', 'C'], 'BOCCHETTI Salvatore'))
	roster.append(Player(7, 7, 18, 0, 'D', ['L', 'R', 'C'], 'VITALE Luigi'))
	roster.append(Player(6, 6, 14, 0, 'D', ['L', 'R', 'C'], 'GUNTER Koray'))
	roster.append(Player(4, 4, 11, 0, 'D', ['L', 'R', 'C'], 'DAWIDOWICZ Pawel'))
	roster.append(Player(4, 4, 11, 0, 'D', ['L', 'R', 'C'], 'CRESCENZI Alessandro'))
	roster.append(Player(4, 4, 11, 0, 'D', ['L', 'R', 'C'], 'EMPEREUR Alan'))
	roster.append(Player(3, 3, 7, 0, 'D', ['L', 'R', 'C'], 'KUMBULLA Marash'))
	roster.append(Player(2, 2, 4, 0, 'D', ['L', 'R', 'C'], 'WESLEY -'))
	roster.append(Player(19, 48, 19, 0, 'M', ['L', 'R', 'C'], 'VERRE Valerio'))
	roster.append(Player(15, 37, 15, 0, 'M', ['L', 'R', 'C'], 'VELOSO Miguel'))
	roster.append(Player(15, 37, 15, 0, 'M', ['L', 'R', 'C'], 'BESSA Daniel'))
	roster.append(Player(15, 37, 15, 0, 'M', ['L', 'R', 'C'], 'LAZOVIC Darko'))
	roster.append(Player(12, 30, 12, 0, 'M', ['L', 'R', 'C'], 'ZACCAGNI Mattia'))
	roster.append(Player(12, 30, 12, 0, 'M', ['L', 'R', 'C'], 'PESSINA Matteo'))
	roster.append(Player(10, 26, 10, 0, 'M', ['L', 'R', 'C'], 'HENDERSON Liam'))
	roster.append(Player(9, 22, 9, 0, 'M', ['L', 'R', 'C'], 'AMRABAT Sofyan'))
	roster.append(Player(8, 19, 8, 0, 'M', ['L', 'R', 'C'], 'BADU Emmanuel'))
	roster.append(Player(3, 7, 3, 0, 'M', ['L', 'R', 'C'], 'JOCIC Bogdan'))
	roster.append(Player(3, 7, 3, 0, 'M', ['L', 'R', 'C'], 'DANZI Andrea'))
	roster.append(Player(2, 4, 2, 0, 'M', ['L', 'R', 'C'], 'LUCAS Martello Nascimento'))
	roster.append(Player(27, 11, 11, 0, 'A', ['L', 'R', 'C'], 'STEPINSKI Mariusz'))
	roster.append(Player(25, 10, 10, 0, 'A', ['L', 'R', 'C'], 'DI CARMINE Samuel'))
	roster.append(Player(24, 10, 10, 0, 'A', ['L', 'R', 'C'], 'TUTINO Gennaro'))
	roster.append(Player(24, 10, 10, 0, 'A', ['L', 'R', 'C'], 'PAZZINI Giampaolo'))
	roster.append(Player(14, 6, 6, 0, 'A', ['L', 'R', 'C'], 'DI GAUDIO Antonio'))
	roster.append(Player(4, 2, 2, 0, 'A', ['L', 'R', 'C'], 'SALCEDO Eddie'))
	roster.append(Player(4, 2, 2, 0, 'A', ['L', 'R', 'C'], 'TUPTA Lubomir'))
	return name, tactics, chariness, roster

SERIEA = [Atalanta, Bologna, Brescia, Cagliari, Fiorentina, Genoa, Internazionale, Juventus, Lazio, Lecce, Milan, Napoli, Parma, Roma, Sampdoria, Sassuolo, Spal, Torino, Udinese, Verona ]

if __name__ == '__main__':
    for club in SERIEA:
        n, t, c, r = club()
        print(n, t().module, c, len(r))