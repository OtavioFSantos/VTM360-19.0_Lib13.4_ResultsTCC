
VVCSoftware: VTM Encoder Version 19.0 [Linux][GCC 11.3.0][64 bit] [SIMD=AVX2] 

CompactCodingFPFormat is automatically disabled for source video because it is only supported for OHP and ISP
CompactCodingFPFormat is automatically disabled for output video because it is only supported for OHP and ISP
TOOL CFG: IBD:1 HAD:1 RDQ:1 RDQTS:1 RDpenalty:0 LQP:0 SQP:0 ASR:0 MinSearchWindow:8 RestrictMESampling:0 FEN:1 ECU:0 FDM:1 ESD:0 TransformSkip:1 TransformSkipFast:1 TransformSkipLog2MaxSize:5 ChromaTS:1 BDPCM:0 Tiles: 1x1 Slices: 1 MCTS:0 SAO:1 ALF:1 CCALF:1 MaxNumALFAPS 8 AlfapsIDShift 0 ConstantJointCbCrSignFlagWPP:0 WPB:0 PME:2  WaveFrontSynchro:0 WaveFrontSubstreams:1 ScalingList:0 TMVPMode:1  DQ:1  SignBitHidingFlag:0 RecalQP:0 
TOOL CFG: LFNST:1 MMVD:1 Affine:1 AffineType:1 AdaptBypassAffineMe:0 PROF:0 SbTMVP:1 DualITree:1 IMV:1 BIO:0 LMChroma:1 HorCollocatedChroma:1 VerCollocatedChroma:0 MTS:1(explicit intra) SBT:1 ISP:1 SMVD:0 CompositeLTReference:0 Bcw:0 BcwFast:0 LADF:0 CIIP:0 Geo:0 AllowDisFracMMVD:1 AffineAmvr:0 AffineAmvrEncOpt:0 AffineAmvp:1 DMVR:0 MmvdDisNum:8 JointCbCr:1 ACT:0 PLT:0 IBC:0 HashME:0 WrapAround:0 VirtualBoundariesEnabledFlag:0 VirtualBoundariesPresentInSPSFlag:1 vertical virtual boundaries:[ ] horizontal virtual boundaries:[ ] Reshape:1 (Signal:SDR Opt:0 CSoffset:2) MRL:1 MIP:1 EncDbOpt:0 
FAST TOOL CFG: LCTUFast:1 FastMrg:1 PBIntraFast:1 IMV4PelFast:1 MTSMaxCand: 4(intra) 4(inter) ISPFast:1 FastLFNST:1 AMaxBT:1 E0023FastEnc:1 ContentBasedFastQtbt:0 UseNonLinearAlfLuma:1 UseNonLinearAlfChroma:1 MaxNumAlfAlternativesChroma:8 FastMIP:1 TTFastSkip:31 TTFastSkipThr:1.075 FastLocalDualTree:0 RPR:0 TemporalFilter:4/4 SEI CTI:0 BIM:0 SEI FGC:0 SEI processing Order:0 

-----360Lib software version [13.1]-----
-----360 video parameters----
SphereVideo:1
InputGeometryType: Equirectangular 
ChromaFormat:1 Resolution:8192x4096xF1 FPStructure:1x1 | Id_0(R_0)  | 
Compact type: 0
InputPERP: 0

CodingGeometryType: Equirectangular 
ChromaFormat:1 Resolution:4096x2048xF1 FPStructure:1x1 | Id_0(R_0)  | 
Compact type: 0
CodingPERP: 0

Packed frame resolution: 4096x2048 (Input face resolution:4096x2048)
Interpolation method for luma: 5, interpolation method for chroma: 4
ChromaSampleLocType: 0
CodingChromaSampleLocType: 0
Input ChromaFormatIDC: 1; Internal ChromaFormatIDC: 1; Output ChromaFormatIDC: 1
Internal bit depth for projection conversion: 10, output bit depth from pejction conversion: 10

End to end S-PSNR-NN is enabled; SphFile file: cfg-360Lib/360Lib/sphere_655362.txt
Codec S-PSNR-NN is enabled; SphFile file: cfg-360Lib/360Lib/sphere_655362.txt
WS-PSNR is enabled
End to end WS-PSNR is enabled
ViewPort parameters for static ViewPort PSNR calculation:
Number of viewports: 2, Resolutoin:1816x1816
Global viewport setting: 75.00 75.00 -38.00 -41.00
Global viewport setting: 75.00 75.00 -95.00 27.00
ViewPort parameters for dynamic ViewPort PSNR calculation:
Number of viewports: 2, Resolutoin:1920x1080
Dyanmic viewport 0, hFOV:78.10, vFOV:49.10
Start viewport setting(POC_0): -45.00 -15.00; End viewport setting(POC_299): 45.00 15.00
Dyanmic viewport 1, hFOV:78.10, vFOV:49.10
Start viewport setting(POC_0): -135.00 -15.00; End viewport setting(POC_299): -45.00 15.00
Cross-format S-PSNR-NN is enabled; SphFile file: cfg-360Lib/360Lib/sphere_655362.txt
Cross-format CPP-PSNR is enabled
Rotation in 1/100 degrees: (yaw:0  pitch:0  roll:0)
-----360 video parameters----



 started @ Wed Jul 19 15:18:01 2023
POC    0 LId:  0 TId: 0 ( IDR_N_LP, I-SLICE, QP 37 )     399008 bits [Y 36.6129 dB    U 46.5499 dB    V 46.9740 dB] [Y-WSPSNR 35.7496 dB   U-WSPSNR 45.5512 dB   V-WSPSNR 46.1028 dB] [Y-C_SPSNR_NN 35.7370 dB   U-C_SPSNR_NN 45.5721 dB   V-C_SPSNR_NN 46.1086 dB] [Y-E2ESPSNR_NN 35.6824 dB   U-E2ESPSNR_NN 45.4405 dB   V-E2ESPSNR_NN 45.9522 dB] [Y-E2EWSPSNR 35.6913 dB   U-E2EWSPSNR 45.4327 dB   V-E2EWSPSNR 45.9535 dB] [Y-PSNR_VP0 35.5971 dB   U-PSNR_VP0 45.5177 dB   V-PSNR_VP0 46.1263 dB] [Y-PSNR_VP1 36.4428 dB   U-PSNR_VP1 45.8498 dB   V-PSNR_VP1 45.4986 dB] [Y-PSNR_DYN_VP0 33.9981 dB   U-PSNR_DYN_VP0 43.6540 dB   V-PSNR_DYN_VP0 44.1139 dB] [Y-PSNR_DYN_VP1 34.8147 dB   U-PSNR_DYN_VP1 45.1849 dB   V-PSNR_DYN_VP1 45.5216 dB] [Y-CFSPSNR_NN 35.6822 dB   U-CFSPSNR_NN 45.4404 dB   V-CFSPSNR_NN 45.9521 dB] [Y-CFCPPPSNR 35.6828 dB   U-CFCPPPSNR 45.5168 dB   V-CFCPPPSNR 46.0614 dB] [ET   140 ] [L0] [L1]

LayerId  0
	Total Frames |  Bitrate      Y-PSNR   U-PSNR   V-PSNR   YUV-PSNR Y-WSPSNR U-WSPSNR V-WSPSNR Y-C_SPSNR_NN U-C_SPSNR_NN V-C_SPSNR_NN Y-E2ESPSNR_NN U-E2ESPSNR_NN V-E2ESPSNR_NN Y-E2EWSPSNR U-E2EWSPSNR V-E2EWSPSNR Y-PSNR_VP U-PSNR_VP V-PSNR_VP Y-PSNR_VP U-PSNR_VP V-PSNR_VP Y-PSNR_DYN_VP U-PSNR_DYN_VP V-PSNR_DYN_VP Y-PSNR_DYN_VP U-PSNR_DYN_VP V-PSNR_DYN_VP Y-CFSPSNR_NN U-CFSPSNR_NN V-CFSPSNR_NN Y-CFCPPPSNR U-CFCPPPSNR V-CFCPPPSNR 
	1            a  1496.2800    36.6129  46.5499  46.9740  38.1687  35.7496  45.5512  46.1028  35.7370      45.5721      46.1086      35.6824       45.4405       45.9522       35.6913     45.4327     45.9535     35.5971   45.5177   46.1263   36.4428   45.8498   45.4986   33.9981       43.6540       44.1139       34.8147       45.1849       45.5216       35.6822      45.4404      45.9521      35.6828     45.5168     46.0614     

 finished @ Wed Jul 19 15:20:34 2023
 Total Time:      153.325 sec. [user]      153.375 sec. [elapsed]
