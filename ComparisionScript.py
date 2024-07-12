import numpy as np
import numpy.linalg as linalg
import insightface
import insightface.app as app
import skimage.io as io
import cv2 as cv
from insightface.data import get_image
from PIL import Image
import os
from openpyxl import Workbook


class ComparisionScript:
    fa = app.FaceAnalysis() 
    fa.prepare(ctx_id = -1, det_size = (640, 640))

    def dotProduct(img, img2):
        image = io.imread(img)
        image2 = io.imread(img2)
        result1 = fa.get(image)
        result2 = fa.get(image2)

        
        w=0
        if len(result2) > 0 and len(result1) > 0:
        
            norm1 = linalg.norm(result1[0]["embedding"])
            norm2 = linalg.norm(result2[0]["embedding"])

            unitVector1 = result1[0]["embedding"]/norm1
            unitVector2 = result2[0]["embedding"]/norm2

            print(np.dot(unitVector1, unitVector2))
            w = np.dot(unitVector1, unitVector2)
        else:
            w = 200
        return w



    passport_imgs = os.listdir("C:/Users/6on/ngsi-summer-2024/Airport3/PassportImages")

    airport_imgs = os.listdir("C:/Users/6on/ngsi-summer-2024/Airport3/AirportImages")


    # def create_worksheet(workbook_name, sheet_name, sheet_num, image_set_one, image_set_two):
    #     row_one = {0,0}
    #     row_after = {}
    #     wb = Workbook()
    #     worksheet = wb.create_sheet(sheet_name,sheet_num)
    #     row_one.append(image_set_two)
    #     wb.save(workbook_name)
    #     worksheet.append(row_one)
    #     for i in image_set_one:
    #         row_after[1] = i 
    #         for w in image_set_two:
    #             row_after[2 + image_set_two.index(w)] = (i, w)
    #         worksheet.append(row_after)
    #         wb.save(workbook_name)
        
    #     wb.save(workbook_name)
    