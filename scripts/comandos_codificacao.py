import os

#./bin/EncoderAppStatic -c cfg/encoder_intra_vtm.cfg -c cfg-360Lib/encoder_360_ERP.cfg -c cfg-360Lib/per-sequence/360/360test_Harbor.cfg -c cfg-360Lib/per-sequence/360/360test_Harbor_Viewports.cfg --SphFile=cfg-360Lib/360Lib/sphere_655362.txt --InputFile=/home/otavio/Downloads/videos/Harbor_8192x4096_30fps_8bit_420_erp.yuv --CodingFaceWidth=4096 --CodingFaceHeight=2048 -b Harbor_QP37.bin --QP=37 --FramesToBeEncoded=8

frames = "80"
caminho_original = "/home/ofsantos/original/bin/EncoderAppStatic"
caminho_noHorizontalModes  = "/home/ofsantos/noHorizontalModes/bin/EncoderAppStatic"
caminho_noVerticalModes  = "/home/ofsantos/noVerticalModes/bin/EncoderAppStatic"
cfg_all_intra = "/home/ofsantos/original/cfg/encoder_intra_vtm.cfg"
cfg_360_original = "/home/ofsantos/original/cfg-360Lib/encoder_360_ERP.cfg"
cfg_360_noHorizontalModes = "/home/ofsantos/noHorizontalModes/cfg-360Lib/encoder_360_ERP.cfg"
cfg_360_noVerticalModes = "/home/ofsantos/noVerticalModes/cfg-360Lib/encoder_360_ERP.cfg"
caminho_cfg_videos = "/home/ofsantos/original/cfg-360Lib/per-sequence/360/360test_"
caminho_videos = "/home/media/360_videos/4096p/"
caminho_resultados = "/home/ofsantos/resultados/"
videos = ["Harbor_8192x4096_30fps_8bit_420_erp.yuv", "KiteFlite_8192x4096_30fps_8bit_420_erp.yuv", "SkateboardInLot_8192x4096_30fps_10bit_420_erp.yuv", "SkateboardTrick_le_8192x4096_60fps_8bit_420_erp.yuv", "Train_le_8192x4096_60fps_8bit_420_erp.yuv", "Trolley_8192x4096_30fps_8bit_420_erp.yuv"]
pastas_resultados = ["Harbor/", "KiteFlite/", "SkateboardInLot/", "SkateboardTrick/", "Train/", "Trolley/"] 
cfg_videos = ["Harbor.cfg", "KiteFlite.cfg", "SkateboardInLot.cfg", "SkateboardTrick.cfg", "Train.cfg", "Trolley.cfg"]
viewports_videos = ["Harbor_Viewports.cfg", "KiteFlite_Viewports.cfg", "SkateboardInLot_Viewports.cfg", "SkateboardTrick_Viewports.cfg", "Train_Viewports.cfg", "Trolley_Viewports.cfg"]
sphfile_path = "/home/ofsantos/original/cfg-360Lib/360Lib/sphere_655362.txt"
qps = ["22","27","32","37"]

for video, cfg, cfg_viewport, pasta_resultado in zip(videos, cfg_videos, viewports_videos, pastas_resultados):
    	for qp in qps:
		comando_original = "taskset -c 0 " + caminho_original + " -c " + cfg_all_intra + " -c " + cfg_360_original + " -c " + caminho_cfg_videos + cfg + " -c " + caminho_cfg_videos + cfg_viewport + " --SphFile=" + sphfile_path + " --InputFile=" + caminho_videos + video + " --CodingFaceWidth=4096 --CodingFaceHeight=2048 " + " -b original.bin " + " --QP=" + qp + " --FramesToBeEncoded=" + frames + " > original.txt"
		
		comando_noHorizontalModes = "taskset -c 0 " + caminho_noHorizontalModes + " -c " + cfg_all_intra + " -c " + cfg_360_noHorizontalModes + " -c " + caminho_cfg_videos + cfg + " -c " + caminho_cfg_videos + cfg_viewport + " --SphFile=" + sphfile_path + " --InputFile=" + caminho_videos + video + " --CodingFaceWidth=4096 --CodingFaceHeight=2048 " + " -b noHorizontalModes.bin " + " --QP=" + qp + " --FramesToBeEncoded=" + frames + " > noHorizontalModes.txt"
		
		comando_noVerticalModes = "taskset -c 0 " + caminho_noVerticalModes + " -c " + cfg_all_intra + " -c " + cfg_360_noVerticalModes + " -c " + caminho_cfg_videos + cfg + " -c " + caminho_cfg_videos + cfg_viewport + " --SphFile=" + sphfile_path + " --InputFile=" + caminho_videos + video + " --CodingFaceWidth=4096 --CodingFaceHeight=2048 " + " -b noVerticalModes.bin " + " --QP=" + qp + " --FramesToBeEncoded=" + frames + " > noVerticalModes.txt"
		
		os.chdir(caminho_resultados + pasta_resultado + qp)
		
		print(comando_original)
		os.system(comando_original)
		
		print(comando_noHorizontalModes)
		os.system(comando_noHorizontalModes)
		
		print(comando_noVerticalModes)
		os.system(comando_noVerticalModes)
		
		print("== All commands executed for video " + video + " and " + qp + "! ==")
	
	print("== All commands executed for video " + video + "! ==")       
        
print("== All commands executed! ==")
