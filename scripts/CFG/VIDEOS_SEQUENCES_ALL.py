#!/usr/bin/env python3

################################################################################
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
#       Script desenvolvido por Alex Borges, amborges@inf.ufpel.edu.br.        #
#                  Grupo de Pesquisa Video Technology Research Group -- ViTech #
#                                     Universidade Federal de Pelotas -- UFPel #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
################################################################################



################################################################################
#               ARQUIVO DE CONFIGURAÇÃO DEDICADO PARA A LISTA DE               #
################################################################################
#                                                                              #
#                                                                              #
#                 #        # ##### ###    ##### ##### #####                    #
#                  #      #    #   #  ##  #     #   # #                        #
#                   #    #     #   #    # ###   #   # #####                    #
#                    #  #      #   #  ##  #     #   #     #                    #
#                     ##     ##### ###    ##### ##### #####                    #
#                                                                              #
#                                                                              #
################################################################################


 
################################################################################
###                            Configurações Gerais                          ###
### - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -###
### Aqui estão a lista dos vídeos que serão utilizados peo main.py           ###
### Deversão estar aqui o nome dos vídeos e a localização deles.             ###
### Apenas comente os vídeos que não pretende utilizar na execução dos       ###
### experimentos. Caso for utilizar uma lista diferente, crie uma nova a     ###
### vontade, mas seguindo a mesma estrutura da lista abaixo.                 ###
################################################################################


##########################
## Definição das Pastas ##
##########################

VIDEO_HOME_PATH = '/home/alex/Videos/'

#caminhos das pastas dos vídeos separados por resolução
VIDEOS_PATH = {
	'A': VIDEO_HOME_PATH + 'class_A/',
	'B': VIDEO_HOME_PATH + 'class_B/',
	'C': VIDEO_HOME_PATH + 'class_C/',
	'D': VIDEO_HOME_PATH + 'class_D/',
	'E': VIDEO_HOME_PATH + 'class_E/',
	'F': VIDEO_HOME_PATH + 'class_F/',
	'G': VIDEO_HOME_PATH + 'class_G/',
	'H': VIDEO_HOME_PATH + 'class_H/',
	'I': VIDEO_HOME_PATH + 'class_I/'
}

#Lista de vídeos a serem utilizados
#Cada linha é composta por uma resolução (vide acima) e o nome do vídeo
#Também incluí o SI-TI do vídeo, e marquei aqueles que eu considerdo
#recomendados para os nossos experimentos no ViTech.
#Descomente os vídeos que queres utilizar
#Cada linha é composta pelos seguintes elementos
# [ CLASSE, NOME DO VÍDEO, LARGURA, ALTURA, SUBAMOSTRAGEM, PROFUNDIDADE DE BITS, NUMERO DE QUADROS, FRAMES PER UNIT, UNIT SIZE]
VIDEOS_LIST = [
	#######
	# AV1 #
	#######

	['A', 'bqfree_240p_120f', 426, 240, 420, 8, 120, 60000, 1001],
	['A', 'bqhighway_240p_120f', 426, 240, 420, 8, 120, 60000, 1001],
	['A', 'bqzoom_240p_120f', 426, 240, 420, 8, 120, 30000, 1001],
	['A', 'chairlift_240p_120f', 426, 240, 420, 8, 64, 24000, 1001],
	['A', 'dirtbike_240p_120f', 426, 240, 420, 8, 61, 24000, 1001],
	['A', 'mozzoom_240p_120f', 426, 240, 420, 8, 57, 30000, 1001],

	['B', 'blue_sky_360p_120f', 640, 360, 420, 8, 120, 25, 1],
	['B', 'controlled_burn_640x360_120f', 640, 360, 420, 8, 120, 30000, 1001],
	['B', 'desktop2360p_120f', 640, 360, 420, 8, 120, 30, 1],
	['B', 'kirland360p_120f', 640, 360, 420, 8, 120, 30, 1],
	['B', 'mmstationary360p_120f', 640, 480, 420, 8, 120, 30, 1],
	['B', 'niklas360p_120f', 640, 360, 420, 8, 120, 30, 1],
	['B', 'rain2_hdr_amazon_360p', 640, 360, 420, 10, 60, 24000, 1001],
	['B', 'red_kayak_360p_120f', 640, 360, 420, 8, 120, 30000, 1001],
	['B', 'riverbed_360p25_120f', 640, 360, 420, 8, 120, 25, 1],
	['B', 'shields2_640x360_120f', 640, 360, 420, 8, 120, 50, 1],
	['B', 'snow_mnt_640x360_120f', 640, 360, 420, 8, 120, 30000, 1001],
	['B', 'speed_bag_640x360_120f', 640, 360, 420, 8, 120, 30000, 1001],
	['B', 'stockholm_640x360_120f', 640, 360, 420, 8, 120, 60000, 1001],
	['B', 'tacomanarrows360p_120f', 640, 360, 420, 8, 120, 30, 1],
	['B', 'thaloundeskmtg360p_120f', 640, 360, 420, 8, 120, 30, 1],
	['B', 'water_hdr_amazon_360p', 640, 360, 420, 10, 60, 24000, 1001],

	['C', 'boat_hdr_amazon_720p', 1280, 720, 420, 10, 60, 24000, 1001],
	['C', 'dark720p_120f', 1280, 720, 420, 8, 120, 30, 1],
	['C', 'FourPeople_1280x720_60_120f', 1280, 720, 420, 8, 120, 60, 1],
	['C', 'gipsrestat720p_120f', 1280, 720, 420, 8, 120, 50, 1],
	['C', 'Johnny_1280x720_60_120f', 1280, 720, 420, 8, 120, 60, 1],
	['C', 'KristenAndSara_1280x720_60_120f', 1280, 720, 420, 8, 120, 60, 1],
	['C', 'Netflix_DinnerScene_1280x720_60fps_8bit_420_120f', 1280, 720, 420, 8, 120, 60, 1],
	['C', 'Netflix_DrivingPOV_1280x720_60fps_8bit_420_120f', 1280, 720, 420, 8, 120, 60, 1],
	['C', 'Netflix_FoodMarket2_1280x720_60fps_8bit_420_120f', 1280, 720, 420, 8, 120, 60, 1],
	['C', 'Netflix_RollerCoaster_1280x720_60fps_8bit_420_120f', 1280, 720, 420, 8, 120, 60, 1],
	['C', 'Netflix_Tango_1280x720_60fps_8bit_420_120f', 1280, 720, 420, 8, 120, 60, 1],
	['C', 'rain_hdr_amazon_720p', 1280, 720, 420, 10, 60, 24000, 1001],
	['C', 'vidyo1_720p_60fps_120f', 1280, 720, 420, 8, 120, 60, 1],
	['C', 'vidyo3_720p_60fps_120f', 1280, 720, 420, 8, 120, 60, 1],
	['C', 'vidyo4_720p_60fps_120f', 1280, 720, 420, 8, 120, 60, 1],

	['E', 'aspen_1080p_60f', 1920, 1080, 420, 8, 60, 30000, 1001],
	['E', 'crowd_run_1080p50_60f', 1920, 1080, 420, 8, 60, 50, 1],
	['E', 'ducks_take_off_1080p50_60f', 1920, 1080, 420, 8, 60, 50, 1],
	['E', 'guitar_hdr_amazon_1080p', 1920, 1080, 420, 10, 60, 24000, 1001],
	['E', 'Netflix_Aerial_1920x1080_60fps_8bit_420_60f', 1920, 1080, 420, 8, 60, 60, 1],
	['E', 'Netflix_Boat_1920x1080_60fps_8bit_420_60f', 1920, 1080, 420, 8, 60, 60, 1],
	['E', 'Netflix_Crosswalk_1920x1080_60fps_8bit_420_60f', 1920, 1080, 420, 8, 60, 60, 1],
	['E', 'Netflix_FoodMarket_1920x1080_60fps_8bit_420_60f', 1920, 1080, 420, 8, 60, 60, 1],
	['E', 'Netflix_PierSeaside_1920x1080_60fps_8bit_420_60f', 1920, 1080, 420, 8, 60, 60, 1],
	['E', 'Netflix_SquareAndTimelapse_1920x1080_60fps_8bit_420_60f', 1920, 1080, 420, 8, 60, 60, 1],
	['E', 'Netflix_TunnelFlag_1920x1080_60fps_8bit_420_60f', 1920, 1080, 420, 8, 60, 60, 1],
	['E', 'old_town_cross_1080p50_60f', 1920, 1080, 420, 8, 60, 50, 1],
	['E', 'pan_hdr_amazon_1080p', 1920, 1080, 420, 10, 60, 24000, 1],
	['E', 'park_joy_1080p50_60f', 1920, 1080, 420, 8, 60, 50, 1],
	['E', 'pedestrian_area_1080p25_60f', 1920, 1080, 420, 8, 60, 25, 1],
	['E', 'rush_field_cuts_1080p_60f', 1920, 1080, 420, 8, 60, 30000, 1001],
	['E', 'rush_hour_1080p25_60f', 1920, 1080, 420, 8, 60, 25, 1],
	['E', 'seaplane_hdr_amazon_1080p', 1920, 1080, 420, 10, 60, 24000, 1001],
	['E', 'station2_1080p25_60f', 1920, 1080, 420, 8, 60, 25, 1],
	['E', 'touchdown_pass_1080p_60f', 1920, 1080, 420, 8, 60, 30000, 1001],

	['F', 'CSGO_60f', 1920, 1080, 444, 8, 60, 60, 1],
	['F', 'DOTA2_60f_420', 1920, 1080, 420, 8, 60, 60, 1],
	['F', 'EuroTruckSimulator2_60f', 1920, 1080, 444, 8, 60, 60, 1],
	['F', 'Hearthstone_60f', 1920, 1080, , 8, 60, 60, 1],
	['F', 'life_1080p30_60f', 1920, 1080, 420, 8, 60, 30, 1],
	['F', 'MINECRAFT_60f_420', 1920, 1080, 420, 8, 60, 60, 1],
	['F', 'pvq_slideshow', 1920, 1080, 444, 8, 60, 30, 1],
	['F', 'STARCRAFT_60f_420', 1920, 1080, 420, 8, 60, 60, 1],
	['F', 'wikipedia_420', 1920, 1080, 420, 8, 60, 30, 1],

	['H', 'Netflix_BarScene_4096x2160_60fps_10bit_420_60f', 4096, 2160, 420, 10, 60, 60, 1],
	['H', 'Netflix_BoxingPractice_4096x2160_60fps_10bit_420_60f', 4096, 2160, 420, 10, 60, 60, 1],
	['H', 'Netflix_Dancers_4096x2160_60fps_10bit_420_60f', 4096, 2160, 420, 10, 60, 60, 1],
	['H', 'Netflix_Narrator_4096x2160_60fps_10bit_420_60f', 4096, 2160, 420, 10, 60, 60, 1],
	['H', 'Netflix_RitualDance_4096x2160_60fps_10bit_420_60f', 4096, 2160, 420, 10, 60, 60, 1],
	['H', 'Netflix_ToddlerFountain_4096x2160_60fps_10bit_420_60f', 4096, 2160, 420, 10, 60, 60, 1],
	['H', 'Netflix_WindAndNature_4096x2160_60fps_10bit_420_60f', 4096, 2160, 420, 10, 60, 60, 1],
	['H', 'street_hdr_amazon_2160p', 3840, 2160, 420, 10, 60, 24000, 1001],

	#######
	# AV2 #
	#######

	['A', 'Vertical_Bayshore_2997_270x480', 270, 480, 420, 8, 150, 30000, 1001],

	['C', 'raw_720x1280@15.walking.in.street', 720, 1280, 420, 8, 500, 15, 1],

	['E', 'FountainSky_1920x1080p30_130f', 1920, 1080, 420, 8, 130, 30000, 1001],
	['E', 'raw_1080x1920@15.blured.background.2', 1080, 1920, 420, 8, 500, 15, 1],
	['E', 'raw_1080x1920@30.walking.in.street', 1080, 1920, 420, 8, 500, 30, 1],
	['E', 'Skater227_1920x1080_30fps', 1920, 1080, 420, 10, 300, 30, 1],
	['E', 'TimeLapseStreet_1920x1080p30_130f', 1920, 1080, 420, 8, 130, 30, 1],
	['E', 'Vertical_bees_2997_1080x1920', 1080, 1920, 420, 8, 150, 30000, 1001],
	['E', 'Vertical_Carnaby_5994_1080x1920', 1080, 1920, 420, 8, 300, 60000, 1001],
	['E', 'Vertical_Dancers_2997p_1080x1920', 1080, 1920, 420, 8, 150, 30000, 1001],
	['E', 'Vertical_DJ_1080x1920_24p', 1080, 1920, 420, 8, 120, 24000, 1001],
	['E', 'Vertical_Fireworks_2997_1080x1920', 1080, 1920, 420, 8, 150, 30000, 1001],
	['E', 'Vertical_Frog_24p_1080x1920', 1080, 1920, 420, 8, 120, 24000, 1001],
	['E', 'Vertical_Moon_5994_1080x1920', 1080, 1920, 420, 8, 300, 60000, 1001],
	['E', 'Wheat_1920x1080', 1920, 1080, 420, 8, 300, 30000, 1001],
	['E', 'WorldCup_1920x1080_30p', 1920, 1080, 420, 8, 150, 30, 1],
	['E', 'WorldCup_far_1920x1080_30p', 1920, 1080, 420, 8, 150, 30, 1],
	['E', 'WorldCupFarSky_1920x1080_30p', 1920, 1080, 420, 8, 150, 30, 1],

	['F', 'AOV5_1920x1080_60_8bit_420', 1920, 1080, 420, 8, 600, 60, 1],
	['F', 'MissionControlClip3_1920x1080_60_444', 1920, 1080, 444, 8, 602, 60, 1],

	['H', 'Chimera-ep01_3840x2160_2997fps_10bit_422', 4096, 2160, 422, 10, 210, 30000, 1001],
	['H', 'Chimera-ep02_3840x2160_2997fps_10bit_422', 4096, 2160, 422, 10, 210, 30000, 1001],
	['H', 'Chimera-ep08_3840x2160_2997fps_10bit_422', 4096, 2160, 422, 10, 450, 30000, 1001],
	['H', 'Chimera-ep11_3840x2160_2997fps_10bit_422', 4096, 2160, 422, 10, 600, 30000, 1001],
	['H', 'Chimera-ep12_3840x2160_2997fps_10bit_422', 4096, 2160, 422, 10, 300, 30000, 1001],
	['H', 'Chimera-ep16_3840x2160_2997fps_10bit_422', 4096, 2160, 422, 10, 40, 30000, 1001],
	['H', 'FlowerSky_A_3840x2160p30_130f', 3840, 2160, 420, 8, 130, 30, 1],
	['H', 'FlowerSky_B_3840x2160p30_130f', 3840, 2160, 420, 8, 130, 30, 1],
	['H', 'meridian_aom_sdr_11872-12263', 3840, 2160, 420, 10, 392, 60000, 1001],
	['H', 'meridian_aom_sdr_12264-12745', 3840, 2160, 420, 10, 482, 60000, 1001],
	['H', 'meridian_aom_sdr_15932-16309', 3840, 2160, 420, 10, 378, 60000, 1001],
	['H', 'meridian_aom_sdr_1782-2163', 3840, 2160, 420, 10, 382, 60000, 1001],
	['H', 'meridian_aom_sdr_20988-21412', 3840, 2160, 420, 10, 425, 60000, 1001],
	['H', 'meridian_aom_sdr_22412-22738', 3840, 2160, 420, 10, 327, 60000, 1001],
	['H', 'meridian_aom_sdr_24058-24550', 3840, 2160, 420, 10, 493, 60000, 1001],
	['H', 'Neon1224_3840x2160_2997fps', 3840, 2160, 420, 10, 300, 30000, 1001],
	['H', 'Netflix_BoxingPractice_4096x2160_60fps_10bit_420', 4096, 2160, 420, 10, 255, 60, 1],
	['H', 'Netflix_FoodMarket2_4096x2160_60fps_10bit_420', 4096, 2160, 420, 10, 300, 60, 1],
	['H', 'Netflix_Narrator_4096x2160_60fps_10bit_420', 4096, 2160, 420, 10, 300, 60, 1],
	['H', 'Netflix_RitualDanceShot_4096x2160_60fps_10bit_420', 4096, 2160, 420, 10, 280, 60, 1],
	['H', 'Netflix_Tango_4096x2160_60fps_10bit_420', 4096, 2160, 420, 10, 295, 60, 1],
	['H', 'Nightclub113_3840x2160_24p', 3840, 2160, 422, 10, 242, 24000, 1001],
	['H', 'nocturne_aom_sdr_17140-17709', 3840, 2160, 420, 10, 570, 60000, 1001],
	['H', 'nocturne_aom_sdr_18013-18315', 3840, 2160, 420, 10, 303, 60000, 1001],
	['H', 'nocturne_aom_sdr_2370-2539', 3840, 2160, 420, 10, 170, 60000, 1001],
	['H', 'nocturne_aom_sdr_23820-24322', 3840, 2160, 420, 10, 503, 60000, 1001],
	['H', 'nocturne_aom_sdr_27740-28109', 3840, 2160, 420, 10, 370, 60000, 1001],
	['H', 'nocturne_aom_sdr_32660-32799', 3840, 2160, 420, 10, 140, 60000, 1001],
	['H', 'nocturne_aom_sdr_8540-9009', 3840, 2160, 420, 10, 470, 60000, 1001],
	['H', 'nocturne_aom_sdr_9010-9349', 3840, 2160, 420, 10, 340, 60000, 1001],
	['H', 'SmoothSkaterP5_3840x2160_30fps', 3840, 2160, 422, 10, 300, 30000, 1001],
	['H', 'sparks_aom_sdr_11198-11570', 4096, 2160, 420, 10, 373, 60000, 1001],
	['H', 'sparks_aom_sdr_2024-2455', 4096, 2160, 420, 10, 432, 60000, 1001],
	['H', 'sparks_aom_sdr_30-511', 4096, 2160, 420, 10, 482, 60000, 1001],
	['H', 'sparks_aom_sdr_5363-5763', 4096, 2160, 420, 10, 401, 60000, 1001],
	['H', 'sparks_aom_sdr_5764-6024', 4096, 2160, 420, 10, 261, 60000, 1001],
	['H', 'sparks_aom_sdr_6026-6502', 4096, 2160, 420, 10, 477, 60000, 1001],
	['H', 'sparks_aom_sdr_8396-8941', 4096, 2160, 420, 10, 546, 60000, 1001],
	['H', 'sparks_aom_sdr_9774-10071', 4096, 2160, 420, 10, 298, 60000, 1001],
	['H', 'Water1394_3840x2160', 3840, 2160, 422, 10, 300, 30000, 1001],

	['I', 'cosmos_aom_sdr_11589-11752', 4096, 2160, 420, 10, 163, 24, 1],
	['I', 'cosmos_aom_sdr_12025-12075', 4096, 2160, 420, 10, 50, 24, 1],
	['I', 'cosmos_aom_sdr_12149-12330', 4096, 2160, 420, 10, 181, 24, 1],
	['I', 'cosmos_aom_sdr_12916-13078', 4096, 2160, 420, 10, 162, 24, 1],
	['I', 'cosmos_aom_sdr_13446-13649', 4096, 2160, 420, 10, 203, 24, 1],
	['I', 'cosmos_aom_sdr_1573-1749', 4096, 2160, 420, 10, 177, 24, 1],
	['I', 'cosmos_aom_sdr_8686-8826', 4096, 2160, 420, 10, 140, 24, 1],
	['I', 'cosmos_aom_sdr_9561-9789', 4096, 2160, 420, 10, 228, 24, 1],
	['I', 'sol_levante_aom_sdr_2268-2412', 3840, 2160, 420, 10, 145, 24, 1],
	['I', 'sol_levante_aom_sdr_289-453', 3840, 2160, 420, 10, 165, 24, 1],
	['I', 'sol_levante_aom_sdr_3282-3874', 3840, 2160, 420, 10, 593, 24, 1],
	['I', 'sol_levante_aom_sdr_4123-4545', 3840, 2160, 420, 10, 423, 24, 1],
	['I', 'sol_levante_aom_sdr_519-649', 3840, 2160, 420, 10, 131, 24, 1],

	###############
	# HEVC / JVET #
	###############

	['A', 'akiyo_qcif', 176, 144, 420, 8, 300, 24, 1],
	['A', 'container_qcif', 176, 144, 420, 8, 300, 24, 1],
	['A', 'mother-daughter_qcif', 176, 144, 420, 8, 300, 24, 1],
	['A', 'bridge-close_qcif', 176, 144, 420, 8, 2000, 24, 1],
	['A', 'grandma_qcif', 176, 144, 420, 8, 870, 24, 1],
	['A', 'news_qcif', 176, 144, 420, 8, 300, 24, 1],
	['A', 'bridge-far_qcif', 176, 144, 420, 8, 2100, 24, 1],
	['A', 'hall_qcif', 176, 144, 420, 8, 300, 24, 1],
	['A', 'salesman_qcif', 176, 144, 420, 8, 450, 24, 1],
	['A', 'carphone_qcif', 176, 144, 420, 8, 380, 24, 1],
	['A', 'highway_qcif', 176, 144, 420, 8, 2000, 24, 1],
	['A', 'silent_qcif', 176, 144, 420, 8, 300, 24, 1],
	['A', 'claire_qcif', 176, 144, 420, 8, 495, 24, 1],
	['A', 'miss-america_qcif', 176, 144, 420, 8, 150, 24, 1],
	['A', 'suzie_qcif', 176, 144, 420, 8, 150, 24, 1],
	['A', 'coastguard_qcif', 176, 144, 420, 8, 300, 24, 1],
	['A', 'mobile_qcif', 176, 144, 420, 8, 300, 24, 1],
	['A', 'BasketballPass_416x240_50', 416, 240, 420, 8, 500, 50, 1],
	['A', 'Flowervase_416x240_30', 416, 240, 420, 8, 300, 30, 1],
	['A', 'BlowingBubbles_416x240_50', 416, 240, 420, 8, 500, 50, 1],
	['A', 'RaceHorses_416x240_30', 416, 240, 420, 8, 300, 30, 1],
	['A', 'BQSquare_416x240_60', 416, 240, 420, 8, 600, 60, 1],

	['B', 'BasketballDrill_832x480_50', 832, 480, 420, 8, 500, 50, 1],
	['B', 'PartyScene_832x480_50', 832, 480, 420, 8, 500, 50, 1],
	['B', 'BasketballDrillText_832x480_50', 832, 480, 420, 8, 500, 50, 1],
	['B', 'RaceHorsesC_832x480_30', 832, 480, 420, 8, 300, 30, 1],
	['B', 'BQMall_832x480_60', 832, 480, 420, 8, 600, 60, 1],

	['C', 'FourPeople_1280x720_60', 1280, 720, 420, 8, 600, 60, 1],
	['C', 'Johnny_1280x720_60', 1280, 720, 420, 8, 600, 60, 1],
	['C', 'Vidyo1_1280x720_60', 1280, 720, 420, 8, 600, 60, 1],
	['C', 'KristenAndSara_1280x720_60', 1280, 720, 420, 8, 600, 60, 1],
	['C', 'Vidyo3_1280x720_60', 1280, 720, 420, 8, 600, 60, 1],
	['C', 'Vidyo4_1280x720_60', 1280, 720, 420, 8, 600, 60, 1],

	['D', 'ChinaSpeed_1024x768_30', 1024, 768, 420, 8, 500, 30, 1],
	['D', 'SlideShow_1280x720_20', 1280, 720, 420, 8, 500, 20, 1],
	['D', 'SlideEditing_1280x720_30', 1280, 720, 420, 8, 300, 30, 1],

	['E', 'BasketballDrive_1920x1080_50', 1920, 1080, 420, 8, 500, 50, 1],
	['E', 'Kimono1_1920x1080_24', 1920, 1080, 420, 8, 240, 24, 1],
	['E', 'BQTerrace_1920x1080_60', 1920, 1080, 420, 8, 600, 60, 1],
	['E', 'ParkScene_1920x1080_24', 1920, 1080, 420, 8, 240, 24, 1],
	['E', 'Cactus_1920x1080_50', 1920, 1080, 420, 8, 500, 50, 1],
	['E', 'Tennis_1920x1080_24', 1920, 1080, 420, 8, 240, 24, 1],
	['E', 'CrowdRun_1920x1080_25', 1920, 1080, 420, 8, 250, 24, 1],

	['G', 'PeopleOnStreet_2560x1600_30', 2560, 1600, 420, 8, 150, 30, 1],
	['G', 'SteamLocomotiveTrain_2560x1600_60_10bit_crop', 2560, 1600, 420, 10, 300, 60, 1],
	['G', 'Traffic_2560x1600_30', 2560, 1600, 420, 8, 150, 30, 1],

	['H', 'Beauty_3840x2160_120fps_420_10bit_YUV', 3840, 2160, 420, 10, 600, 120, 1],
	['H', 'Bosphorus_3840x2160_120fps_420_10bit_YUV', 3840, 2160, 420, 10, 600, 120, 1],
	['H', 'Cactus_3840x2160_60fps', 3840, 2160, 420, 10, 695, 60, 1],
	['H', 'Coastguard_3840x2160_60fps', 3840, 2160, 420, 10, 500, 60, 1],
	['H', 'Foreman_3840x2160_60fps', 3840, 2160, 420, 10, 515, 60, 1],
	['H', 'HoneyBee_3840x2160_120fps_420_10bit_YUV', 3840, 2160, 420, 10, 600, 120, 1],
	['H', 'Jockey_3840x2160_120fps_420_10bit_YUV', 3840, 2160, 420, 10, 600, 120, 1],
	['H', 'Lips_3840x2160_120fps_10bit', 3840, 2160, 420, 10, 600, 120, 1],
	['H', 'Mobile_3840x2160_60fps', 3840, 2160, 420, 10, 740, 60, 1],
	['H', 'News_3840x2160_60fps', 3840, 2160, 420, 10, 530, 60, 1],
	['H', 'ReadySetGo_3840x2160_120fps_420_10bit_YUV', 3840, 2160, 420, 10, 600, 120, 1],
	['H', 'RollerCoaster_4096x2160_60fps_10bit_420_jvet', 4096, 2160, 420, 10, 300, 60, 1],
	['H', 'ShakeNDry_3840x2160_120fps_420_10bit_YUV', 3840, 2160, 420, 10, 300, 120, 1],
	['H', 'SunBath_3840x2160_50fps_10bit', 3840, 2160, 420, 10, 300, 50, 1],
	['H', 'Suzie_3840x2160_120fps', 3840, 2160, 420, 10, 660, 120, 1],
	['H', 'Suzie_3840x2160_60fps', 3840, 2160, 420, 10, 740, 60, 1],
	['H', 'ToddlerFountain_4096x2160_60fps_10bit_420_jvet', 4096, 2160, 420, 10, 300, 60, 1],
	['H', 'YachtRide_3840x2160_120fps_420_10bit_YUV', 3840, 2160, 420, 10, 600, 120, 1]
]
