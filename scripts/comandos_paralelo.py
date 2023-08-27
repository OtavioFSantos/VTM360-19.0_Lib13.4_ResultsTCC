import os
import multiprocessing

#./bin/EncoderAppStatic -c cfg/encoder_intra_vtm.cfg -c cfg-360Lib/encoder_360_ERP.cfg -c cfg-360Lib/per-sequence/360/360test_Harbor.cfg -c cfg-360Lib/per-sequence/360/360test_Harbor_Viewports.cfg --SphFile=cfg-360Lib/360Lib/sphere_655362.txt --InputFile=/home/otavio/Downloads/videos/Harbor_8192x4096_30fps_8bit_420_erp.yuv --CodingFaceWidth=4096 --CodingFaceHeight=2048 -b Harbor_QP37.bin --QP=37 --FramesToBeEncoded=8

frames = "8"
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
videos = ["Gaslamp_8192x4096_30fps_8bit_420_erp.yuv"]
pastas_resultados = ["Gaslamp/"] 
cfg_videos = ["GasLamp.cfg"]
viewports_videos = ["GasLamp_Viewports.cfg"]
sphfile_path = "/home/ofsantos/original/cfg-360Lib/360Lib/sphere_655362.txt"
qps = ["22","27","32","37"]

num_cores = 9
pool = multiprocessing.Pool(processes=num_cores)

def run_command_with_taskset(command, core):
	taskset_cmd = f"taskset -c {core} {command}"
	os.system(taskset_cmd)

def execute_commands(video, cfg, cfg_viewport, pasta_resultado, qp):
	comando_original = caminho_original + " -c " + cfg_all_intra + " -c " + cfg_360_original + " -c " + caminho_cfg_videos + cfg + " -c " + caminho_cfg_videos + cfg_viewport + " --SphFile=" + sphfile_path + " --InputFile=" + caminho_videos + video + " --CodingFaceWidth=4096 --CodingFaceHeight=2048 " + " -b original.bin " + " --QP=" + qp + " --FramesToBeEncoded=" + frames + " > original.txt"
        
	comando_noHorizontalModes = caminho_noHorizontalModes + " -c " + cfg_all_intra + " -c " + cfg_360_noHorizontalModes + " -c " + caminho_cfg_videos + cfg + " -c " + caminho_cfg_videos + cfg_viewport + " --SphFile=" + sphfile_path + " --InputFile=" + caminho_videos + video + " --CodingFaceWidth=4096 --CodingFaceHeight=2048 " + " -b noHorizontalModes.bin " + " --QP=" + qp + " --FramesToBeEncoded=" + frames + " > noHorizontalModes.txt"
        
        comando_noVerticalModes = caminho_noVerticalModes + " -c " + cfg_all_intra + " -c " + cfg_360_noVerticalModes + " -c " + caminho_cfg_videos + cfg + " -c " + caminho_cfg_videos + cfg_viewport + " --SphFile=" + sphfile_path + " --InputFile=" + caminho_videos + video + " --CodingFaceWidth=4096 --CodingFaceHeight=2048 " + " -b noVerticalModes.bin " + " --QP=" + qp + " --FramesToBeEncoded=" + frames + " > noVerticalModes.txt"

	resultado_dir = os.path.join(caminho_resultados, pasta_resultado, qp)
	os.makedirs(resultado_dir, exist_ok=True)
	os.chdir(resultado_dir)

	commands = [comando_original, comando_noHorizontalModes, comando_noVerticalModes]
	command_core_pairs = zip(commands, range(num_cores))
	pool.starmap(run_command_with_taskset, command_core_pairs)

	print("== All commands executed for video " + video + " and " + qp + "! ==")

# Iterate over your videos and other variables
for video, cfg, cfg_viewport, pasta_resultado in zip(videos, cfg_videos, viewports_videos, pastas_resultados):
	for qp in qps:
		execute_commands(video, cfg, cfg_viewport, pasta_resultado, qp)

	print("== All commands executed for video " + video + "! ==")

pool.close()
pool.join()

print("== All commands executed for all videos! ==")
