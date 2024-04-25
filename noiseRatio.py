import math

def MSE(SourceData, CompareData):
    if len(SourceData) != len(CompareData):
        raise Exception(f"wrong data length : {len(SourceData)},  {len(CompareData)}")
    n = len(SourceData)
    return sum((x - y) ** 2 for x, y in zip(SourceData, CompareData)) / n


def PSNR(SourceData, CompareData):
    mse = MSE(SourceData, CompareData)
    mse = max(mse, 0.0001)
    return 20 * math.log10(max(SourceData) / math.sqrt(mse))