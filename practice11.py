# 패키지
#import travel.thailand
# import travel.thailand.ThailandPackage
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

#########################################
# __all__
# from travel import *
# #trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()


from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()
import inspect
import random

print(inspect.getfile(random))
print(inspect.getfile(thailand))
