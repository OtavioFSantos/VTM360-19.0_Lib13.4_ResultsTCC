import numpy as np
import scipy.interpolate

def BD_PSNR(R1, PSNR1, R2, PSNR2, piecewise=0):
    lR1 = np.log(R1)
    lR2 = np.log(R2)

    # Use interpolação cúbica
    interp1 = scipy.interpolate.CubicSpline(lR1, PSNR1)
    interp2 = scipy.interpolate.CubicSpline(lR2, PSNR2)

    # integration interval
    min_int = max(min(lR1), min(lR2))
    max_int = min(max(lR1), max(lR2))

    # find integral
    int1 = interp1.integral(min_int, max_int)
    int2 = interp2.integral(min_int, max_int)

    # find avg diff
    avg_diff = (int2 - int1) / (max_int - min_int)

    return avg_diff

def BD_RATE(R1, PSNR1, R2, PSNR2, piecewise=0):
    lR1 = np.log(R1)
    lR2 = np.log(R2)

    # Use interpolação cúbica
    interp1 = scipy.interpolate.CubicSpline(PSNR1, lR1)
    interp2 = scipy.interpolate.CubicSpline(PSNR2, lR2)

    # integration interval
    min_int = max(min(PSNR1), min(PSNR2))
    max_int = min(max(PSNR1), max(PSNR2))

    # find integral
    int1 = interp1.integral(min_int, max_int)
    int2 = interp2.integral(min_int, max_int)

    # find avg diff
    avg_exp_diff = (int2 - int1) / (max_int - min_int)
    avg_diff = (np.exp(avg_exp_diff) - 1) * 100

    return avg_diff
