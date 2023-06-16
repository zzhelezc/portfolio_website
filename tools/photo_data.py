import os
from collections import OrderedDict

PATH = os.environ['WEBSITE_ROOT']
RELATIVE_PATH = '/photos'
PHOTO_PATH = PATH + RELATIVE_PATH




def DSCF(images):
    return [ f'DSCF{i}.jpg' for i in images]

photos = OrderedDict({
    
    'Home':
    DSCF(['4395', '4396',   '4322', '4294', '4289', '4347',
          '4319', '4349',   '4394', '4379', '4268', '4337',
          '4338', '4363-1', '3800', '3805', '4011', '3962',
          '3947']),

    'Red':
    DSCF(['4332', '4333', '4355', '4358', '4366', '4367',
          '4369', '4372', '4317', '4387', '4299', '4295',
          '4298', '4296', '4270', '4269', '3973', '4218',
          '4214', '4206', '4188']),

    'Ordinary Places':
    DSCF(['4220', '4380-1', '4341', '4330', '4324', '4263',
          '4374', '4256', '4243']),

    "Places and Things": [('DSCF3460-2.jpg', 'DSCF3458.jpg'),'23.jpg', '24.jpg',
                          '25.jpg', '26.jpg', '27.jpg',
                          '28.jpg', '29.jpg', '30.jpg', '31.jpg', '32.jpg',
                          '33.jpg', '34.jpg', '35.jpg', '36.jpg', '37.jpg',
                          '38.jpg', '39.jpg', '40.jpg', '41.jpg', ('42.jpg', '43.jpg')],

    'Boats':
    DSCF(['4189', '4164', '4165', '4168', '4183',
          '4292', '4306', '4307', '4300', '4305',
          '4303', '4360', '4362', '4344', '4365']),
    
    
    "People": ['0.jpg', '1.jpg', '2.jpg', '3.jpg', '4.jpg',
               '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg',
               '10.jpg', '11.jpg', '12.jpg', '13.jpg', '14.jpg',
               '15.jpg', '16.jpg', '17.jpg', '18.jpg', '19.jpg',
                 '20.jpg', '21.jpg', '22.jpg'],
})


