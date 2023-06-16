import os
from collections import OrderedDict

PATH = os.environ['WEBSITE_ROOT']
RELATIVE_PATH = '/photos'
PHOTO_PATH = PATH + RELATIVE_PATH




def DSCF(images):
    return [ f'DSCF{i}.jpg' for i in images]

photos = OrderedDict({


    'Home':
    DSCF(['4220', '4380-1', '4330', '4324', '4263',
          '4374', '4256', '4243', '3458', '3460-2']) +
    ['24.jpg',
     '25.jpg', '27.jpg',
     '28.jpg', '29.jpg',
     '33.jpg', '35.jpg',
     '38.jpg', '39.jpg', '40.jpg', '41.jpg','42.jpg', '43.jpg'],
    
    'Green and Yellow':
    DSCF(['4395', '4396',   '4322', '4294', '4289', '4347',
          '4319', '4349',   '4394', '4379', '4268', '4337',
          '4338', '4363-1', '3800', '3805', '4011', '3962',
          '3947']),

    'Red':
    DSCF(['4332', '4333', '4355', '4358', '4366', '4367',
          '4369', '4372', '4317', '4387', '4299', '4295',
          '4298', '4296', '4270', '4269', '3973', '4218',
          '4214', '4206', '4188'])
})


