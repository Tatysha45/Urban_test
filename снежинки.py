import simple_draw as sd

sd.resolution = (1200, 600)
# length = 200
# point = sd.get_point(300, 300)
#
# v1 = sd.get_vector(start_point=point, angle=0, length=200, width=3)
# v1.draw()
# v2 = sd.get_vector(start_point=v1.end_point, angle=120, length=200, width=3)
# v2.draw()
# v3 = sd.get_vector(start_point=v2.end_point, angle=240, length=200, width=3)
# v3.draw()
#
# length = 200
# point = sd.get_point(300, 300)
#
# def triangle(point, angle=0):
#
#     v1 = sd.get_vector(start_point=point, angle=angle, length=200, width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=200, width=3)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=200, width=3)
#     v3.draw()
#
# point_0 = sd.get_point(300, 300)
#
# for angle in range(0, 360, 30):
#     triangle(point=point_0, angle=angle)

# point_0 = sd.get_point(300, 5)
# v1 = sd.get_vector(start_point=point_0, angle=90, length=100)
# v1.draw()

# def branch(point, angle, length):
#     v1 = sd.get_vector(start_point==point, angle=angle, length=length, width=3)
#     v1.draw()
#     return  v1.end_point

# angle_0 = 90
# length_0 = 200
# next_point = branch(point=point_0, angle=angle_0, length=length_0)
# next_angle = angle_0 - 30
# next_length = length_0 * .75
# next_point = branch(point=next_point, angle=next_angle, length=next_length)
# next_angle = angle_0 - 30
# next_length = length_0 * .75
# next_point = branch(point=next_point, angle=next_angle, length=next_length)
# angle_0 = 90
# length_0 = 200
# next_angle = angle_0
# next_length = length_0
# next_point = point_0
# while next_length > 10:
#     next_point = branch(point=next_point, angle=next_angle, length=next_length)
#     next_angle = next_angle - 30
#     next_length = next_length * 0.75

# def branch(point, angle, length):
#     if length < 1:
#         return
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#     next_point = v1.end_point
#     next_angle = angle - 30
#     next_length = length * .75
#     branch(point=next_point, angle=next_angle, length=next_length)
#
# for length in range(50, 200, 10):
#     branch(point=point_0, angle=90, length=length)
# branch(point=point_0, angle=90, length=50)
# branch(point=point_0, angle=90, length=100)
# branch(point=point_0, angle=90, length=200)
#
# def branch(point, angle, length, delta):
#     if length < 1:
#         return
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#     next_point = v1.end_point
#     next_angle = angle - delta
#     next_length = length * .75
#     branch(point=next_point, angle=next_angle, length=next_length, delta=delta)

# for delta in range(0, 50, 10):
#     branch(point=point_0, angle=90, length=200, delta=30)
#     branch(point=point_0, angle=90, length=200, delta=40)
#     branch(point=point_0, angle=90, length=200, delta=50)
# for delta in range(0, 51, 10):
#     branch(point=point_0, angle=90, length=150, delta=delta)
# for delta in range(-50, 1, 10):
#     branch(point=point_0, angle=90, length=150, delta=delta)


# sd.clear_screen()
# point_0 = sd.get_point(100, 500)
# # sd.snowflake(center=point_0, length=200, factor_a=0.5)
# while True:
#     sd.clear_screen()
#     pass
#     pass
#     pass
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
#
# y = 500
# while True:
#     sd.clear_screen()
#     point = sd.get_point(100, y)
#     sd.snowflake(center=point, length=50)
#     y -= 10
#     if y < 0:
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

y = 500
x = 100

y2 = 450
x2 = 150
while True:
    sd.clear_screen()
    point = sd.get_point(x, y)
    sd.snowflake(center=point, length=50)
    y -= 10
    if y < 50:
        break
    x = x + 10

    point2 = sd.get_point(x2, y2)
    sd.snowflake(center=point2, length=50)
    y2 -= 10
    if y2 < 50:
        break
    x2 = x2 + 28

    sd.sleep(0.1)
    if sd.user_want_exit():
        break


sd.pause()