from bjontegaard_metric import *
import numpy as np
import sys

QP22=0
QP27=1
QP32=2
QP37=3

refsFile = sys.argv[1]#'BitratePSNR_Original.csv'
modsFile = sys.argv[2]#'BitratePSNR_5Bv2.csv'
nFiles =   int(sys.argv[3])
nLines = nFiles*4+1
modsLines = open(modsFile).readlines()

# nFiles = 9

QP22 = 0
QP27 = 1
QP32 = 2
QP37 = 3

bitrate = 1
PSNR = 2
WSPSNR = 3

# for i in xrange(0,nFiles):
# 	print(refs[i])
# 	print(mods[i])

refs = np.genfromtxt(refsFile, delimiter=',', skip_header=1)
mods = np.genfromtxt(modsFile, delimiter=',', skip_header=1)

for i in range(0,nFiles):

	ref = refs[:][i*4:i*4+4]
	mod = mods[:][i*4:i*4+4]
	# print(ref)
	# print(mod)

	Rref = np.array([ref[QP22][bitrate], ref[QP27][bitrate], ref[QP32][bitrate], ref[QP37][bitrate]])
	PSNRref = np.array([ref[QP22][PSNR], ref[QP27][PSNR], ref[QP32][PSNR], ref[QP37][PSNR]])
	# SPSNR_NNref = np.array([ref[QP22][3], ref[QP27][3], ref[QP32][3], ref[QP37][3]])
	WSPSNRref = np.array([ref[QP22][WSPSNR], ref[QP27][WSPSNR], ref[QP32][WSPSNR], ref[QP37][WSPSNR]])
	# # C_SPSNR_NNref = np.array([ref[QP22][3], ref[QP27][3], ref[QP32][3], ref[QP37][3]])
	# # E2ESPSNR_NNref = np.array([ref[QP22][4], ref[QP27][4], ref[QP32][4], ref[QP37][4]])
	# # E2EWSPSNRref = np.array([ref[QP22][5], ref[QP27][5], ref[QP32][5], ref[QP37][5]])
	# # PSNR_DYN_VP0ref = np.array([ref[QP22][6], ref[QP27][6], ref[QP32][6], ref[QP37][6]])
	# # PSNR_DYN_VP1ref = np.array([ref[QP22][7], ref[QP27][7], ref[QP32][7], ref[QP37][7]])
	# # CFPSNR_NNref = np.array([ref[QP22][8], ref[QP27][8], ref[QP32][8], ref[QP37][8]])
	# # CFCPPPSNR_NNref = np.array([ref[QP22][9], ref[QP27][9], ref[QP32][9], ref[QP37][9]])


	Rmod = np.array([mod[QP22][bitrate], mod[QP27][bitrate], mod[QP32][bitrate], mod[QP37][bitrate]])
	#PSNRmod = np.array([mod[QP22][PSNR], mod[QP27][PSNR], mod[QP32][PSNR], mod[QP37][PSNR]])
	# SPSNR_NNmod = np.array([mod[QP22][3], mod[QP27][3], mod[QP32][3], mod[QP37][3]])
	WSPSNRmod = np.array([mod[QP22][WSPSNR], mod[QP27][WSPSNR], mod[QP32][WSPSNR], mod[QP37][WSPSNR]])
	# # C_SPSNR_NNmod = np.array([mod[QP22][3], mod[QP27][3], mod[QP32][3], mod[QP37][3]])
	# # E2ESPSNR_NNmod = np.array([mod[QP22][4], mod[QP27][4], mod[QP32][4], mod[QP37][4]])
	# # E2EWSPSNRmod = np.array([mod[QP22][5], mod[QP27][5], mod[QP32][5], mod[QP37][5]])
	# # PSNR_DYN_VP0mod = np.array([mod[QP22][6], mod[QP27][6], mod[QP32][6], mod[QP37][6]])
	# # PSNR_DYN_VP1mod = np.array([mod[QP22][7], mod[QP27][7], mod[QP32][7], mod[QP37][7]])
	# # CFPSNR_NNmod = np.array([mod[QP22][8], mod[QP27][8], mod[QP32][8], mod[QP37][8]])
	# # CFCPPPSNR_NNmod = np.array([mod[QP22][9], mod[QP27][9], mod[QP32][9], mod[QP37][9]])

	print(modsLines[i*4+1].split(',')[0])
	# print(Rref)
	# print(PSNRref)
	# print(WSPSNRref)
	# print(Rmod)
	# print(PSNRmod)
	# print(WSPSNRmod)

	#print('BD-PSNR: ', BD_PSNR(Rref, PSNRref, Rmod, PSNRmod))
	#print('BD-RATE: ', BD_RATE(Rref, PSNRref, Rmod, PSNRmod))

	# print 'BD-SPSNR_NN: ', BD_PSNR(Rref, SPSNR_NNref, Rmod, SPSNR_NNmod)
	# print 'BD-RATE: ', BD_RATE(Rref, SPSNR_NNref, Rmod, SPSNR_NNmod)

	print('BD-WSPSNR: ', BD_PSNR(Rref, WSPSNRref, Rmod, WSPSNRmod))
	print('BD-RATE: ', BD_RATE(Rref, WSPSNRref, Rmod, WSPSNRmod))
