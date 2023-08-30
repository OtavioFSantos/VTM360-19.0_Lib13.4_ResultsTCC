import os

#./bin/EncoderAppStatic -c cfg/encoder_intra_vtm.cfg -c cfg-360Lib/encoder_360_ERP.cfg -c cfg-360Lib/per-sequence/360/360test_Harbor.cfg -c cfg-360Lib/per-sequence/360/360test_Harbor_Viewports.cfg --SphFile=cfg-360Lib/360Lib/sphere_655362.txt --InputFile=/home/otavio/Downloads/videos/Harbor_8192x4096_30fps_8bit_420_erp.yuv --CodingFaceWidth=4096 --CodingFaceHeight=2048 -b Harbor_QP37.bin --QP=37 --FramesToBeEncoded=8

frames = "80"
caminho_noHorizontalBlocks = "/home/ofsantos/noHorizontalBlocks/bin/EncoderAppStatic"
caminho_noVerticalBlocks  = "/home/ofsantos/noVerticalBlocks/bin/EncoderAppStatic"
cfg_all_intra = "/home/ofsantos/original/cfg/encoder_intra_vtm.cfg"
cfg_360_original = "/home/ofsantos/original/cfg-360Lib/encoder_360_ERP.cfg"
cfg_360_noHorizontalBlocks = "/home/ofsantos/noHorizontalBlocks/cfg-360Lib/encoder_360_ERP.cfg"
cfg_360_noVerticalBlocks = "/home/ofsantos/noVerticalBlocks/cfg-360Lib/encoder_360_ERP.cfg"
caminho_cfg_videos = "/home/ofsantos/original/cfg-360Lib/per-sequence/360/360test_"
caminho_videos = "/home/media/360_videos/4096p/"
caminho_resultados = "/home/ofsantos/resultados/"
videos = ["ChairliftRide_8192x4096_30fps_10bit_420_erp.yuv", "Gaslamp_8192x4096_30fps_8bit_420_erp.yuv", "Harbor_8192x4096_30fps_8bit_420_erp.yuv", "KiteFlite_8192x4096_30fps_8bit_420_erp.yuv", "SkateboardInLot_8192x4096_30fps_10bit_420_erp.yuv", "SkateboardTrick_le_8192x4096_60fps_8bit_420_erp.yuv", "Train_le_8192x4096_60fps_8bit_420_erp.yuv", "Trolley_8192x4096_30fps_8bit_420_erp.yuv"]
pastas_resultados = ["ChairliftRide/", "Gaslamp/", "Harbor/", "KiteFlite/", "SkateboardInLot/", "SkateboardTrick/", "Train/", "Trolley/"] 
cfg_videos = ["ChairliftRide.cfg", "GasLamp.cfg", "Harbor.cfg", "KiteFlite.cfg", "SkateboardInLot.cfg", "SkateboardTrick.cfg", "Train.cfg", "Trolley.cfg"]
viewports_videos = ["ChairliftRide_Viewports.cfg", "GasLamp_Viewports.cfg", "Harbor_Viewports.cfg", "KiteFlite_Viewports.cfg", "SkateboardInLot_Viewports.cfg", "SkateboardTrick_Viewports.cfg", "Train_Viewports.cfg", "Trolley_Viewports.cfg"]
sphfile_path = "/home/ofsantos/original/cfg-360Lib/360Lib/sphere_655362.txt"
qps = ["22","27","32","37"]

for video, cfg, cfg_viewport, pasta_resultado in zip(videos, cfg_videos, viewports_videos, pastas_resultados):
    	for qp in qps:
		comando_noHorizontalBlocks = "taskset -c 0 " + caminho_noHorizontalBlocks + " -c " + cfg_all_intra + " -c " + cfg_360_noHorizontalBlocks + " -c " + caminho_cfg_videos + cfg + " -c " + caminho_cfg_videos + cfg_viewport + " --SphFile=" + sphfile_path + " --InputFile=" + caminho_videos + video + " --CodingFaceWidth=4096 --CodingFaceHeight=2048 " + " -b noHorizontalBlocks.bin " + " --QP=" + qp + " --FramesToBeEncoded=" + frames + " > noHorizontalBlocks.txt"
		
		comando_noVerticalBlocks = "taskset -c 0 " + caminho_noVerticalBlocks + " -c " + cfg_all_intra + " -c " + cfg_360_noVerticalBlocks + " -c " + caminho_cfg_videos + cfg + " -c " + caminho_cfg_videos + cfg_viewport + " --SphFile=" + sphfile_path + " --InputFile=" + caminho_videos + video + " --CodingFaceWidth=4096 --CodingFaceHeight=2048 " + " -b noVerticalBlocks.bin " + " --QP=" + qp + " --FramesToBeEncoded=" + frames + " > noVerticalBlocks.txt"
		
		os.chdir(caminho_resultados + pasta_resultado + qp)
		
		print(comando_noHorizontalBlocks)
		os.system(comando_noHorizontalBlocks)
		
		print(comando_noVerticalBlocks)
		os.system(comando_noVerticalBlocks)
		
		print("== All commands executed for video " + video + " and " + qp + "! ==")
	
	print("== All commands executed for video " + video + "! ==")       
        
print("== All commands executed! ==")
