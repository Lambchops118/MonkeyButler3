
#Monkey Butler Vector Art
#Part of Monkey Butler 3

import arcade

def head(self, dx, dy): #Vector lines for the head. dx and dy allow input to move entire head on screen together

        dx = dx
        dy = dy

        color = arcade.color.GREEN

        #NOSE
        arcade.draw_circle_filled(dx+465, dy+325, 1, arcade.color.GREEN)#Top point, left, 1
        arcade.draw_line(dx+465, dy+325, dx+470, dy+310, color, 1)
        arcade.draw_circle_filled(dx+495, dy+325, 1, arcade.color.GREEN)#Top point, left, 9

        arcade.draw_circle_filled(dx+470, dy+310, 1, arcade.color.GREEN) #bottleneck left, 2
        arcade.draw_line(dx+470, dy+310, dx+465, dy+270, color, 1)
        arcade.draw_circle_filled(dx+490, dy+310, 1, arcade.color.GREEN) #bottleneck right 8
        arcade.draw_line(dx+490, dy+310, dx+495, dy+325, color, 1)

        arcade.draw_circle_filled(dx+475, dy+280, 1, arcade.color.GREEN) #inner corner left 4
        arcade.draw_line(dx+475, dy+280, dx+480, dy+270, color, 1)
        arcade.draw_circle_filled(dx+485, dy+280, 1, arcade.color.GREEN) #inner corner right 6
        arcade.draw_line(dx+485, dy+280, dx+495, dy+270, color, 1)

        arcade.draw_circle_filled(dx+465, dy+270, 1, arcade.color.GREEN) #bottom point left 3
        arcade.draw_line(dx+465, dy+270, dx+475, dy+280, color, 1)
        arcade.draw_circle_filled(dx+480, dy+270, 1, color) #bottom point mid 5
        arcade.draw_line(dx+480, dy+270, dx+485, dy+280, color, 1)
        arcade.draw_circle_filled(dx+495, dy+270, 1, color) #bottom point right 7
        arcade.draw_line(dx+495, dy+270, dx+490, dy+310, color, 1)


        #HEAD
        arcade.draw_circle_filled(dx+365, dy+340, 1, color) #top head vec left 1
        arcade.draw_line(dx+365, dy+340, dx+365, dy+305, color, 1)
        arcade.draw_circle_filled(dx+595, dy+340, 1, color) #top head vec right 13

        arcade.draw_circle_filled(dx+365, dy+305, 1, color)#2
        arcade.draw_line(dx+365, dy+305, dx+380, dy+300, color, 1)
        arcade.draw_circle_filled(dx+595, dy+305, 1, color)#12
        arcade.draw_line(dx+595, dy+305, dx+595, dy+340, color ,1)

        arcade.draw_circle_filled(dx+380, dy+300, 1, color)#3
        arcade.draw_line(dx+380, dy+300, dx+380, dy+240, color, 1) #SIDE
        arcade.draw_circle_filled(dx+580, dy+300, 1, color)#11
        arcade.draw_line(dx+580, dy+300, dx+595, dy+305, color ,1)

        arcade.draw_circle_filled(dx+380, dy+240, 1, color)#4
        arcade.draw_line(dx+380, dy+240, dx+430, dy+215, color, 1)
        arcade.draw_circle_filled(dx+580, dy+240, 1, color)#10
        arcade.draw_line(dx+580, dy+240, dx+580, dy+300, color ,1) #SIDE

        arcade.draw_circle_filled(dx+430, dy+215, 1, color)#5
        arcade.draw_line(dx+430, dy+215, dx+430, dy+200, color, 1)
        arcade.draw_circle_filled(dx+530, dy+215,1, color)#9
        arcade.draw_line(dx+530, dy+215, dx+580, dy+240, color ,1)

        arcade.draw_circle_filled(dx+430, dy+200, 1, color)#6
        arcade.draw_line(dx+430, dy+200, dx+480, dy+190, color, 1)
        arcade.draw_circle_filled(dx+530, dy+200, 1, color)#8
        arcade.draw_line(dx+530, dy+200, dx+530, dy+215, color ,1)

        arcade.draw_circle_filled(dx+480, dy+190, 1, color) #chin tip 7
        arcade.draw_line(dx+480, dy+190, dx+530, dy+200, color ,1)


        #SNOUT
        #brow
        arcade.draw_circle_filled(dx+440,dy+385, 1, color) #1
        arcade.draw_line(dx+440, dy+385, dx+460, dy+380, color ,1)
        arcade.draw_circle_filled(dx+460, dy+380, 1, color)#2
        arcade.draw_line(dx+460, dy+380, dx+480, dy+375, color ,1)
        arcade.draw_circle_filled(dx+480, dy+375, 1, color) #center
        arcade.draw_line(dx+480, dy+375, dx+500, dy+380, color ,1)
        arcade.draw_circle_filled(dx+500, dy+380, 1, color)# 4
        arcade.draw_line(dx+500, dy+380, dx+520, dy+385, color, 1)
        arcade.draw_circle_filled(dx+520, dy+385, 1, color)#5

        #muzzle and mouth
        arcade.draw_circle_filled(dx+455, dy+310, 1, color)#6
        arcade.draw_line(dx+455, dy+310, dx+435, dy+265, color ,1)
        arcade.draw_circle_filled(dx+505, dy+310, 1, color)#7

        arcade.draw_circle_filled(dx+435, dy+265, 1, color)#8
        arcade.draw_line(dx+435, dy+265, dx+435,dy+250, color ,1)
        arcade.draw_circle_filled(dx+525, dy+265, 1, color)#7
        arcade.draw_line(dx+525, dy+265, dx+505, dy+310, color, 1)

        arcade.draw_circle_filled(dx+435, dy+250, 1, color)#10
        arcade.draw_line(dx+435, dy+250, dx+455, dy+225, color ,1)
        arcade.draw_circle_filled(dx+525, dy+250, 1, color)
        arcade.draw_line(dx+525, dy+250, dx+525, dy+265, color ,1)
        arcade.draw_line(dx+525, dy+250, dx+495, dy+255, color, 1)#mouth

        arcade.draw_circle_filled(dx+455, dy+225, 1, color)#12
        arcade.draw_line(dx+455, dy+225, dx+480, dy+220, color, 1)
        arcade.draw_circle_filled(dx+505, dy+225, 1, color)#13
        arcade.draw_line(dx+505, dy+225, dx+480, dy+220, color ,1)
        arcade.draw_circle_filled(dx+480, dy+220, 1, color)#14
        arcade.draw_line(dx+505, dy+225, dx+525, dy+250, color, 1)

        #mouth
        arcade.draw_circle_filled(dx+465, dy+255, 1, color)#15
        arcade.draw_circle_filled(dx+495, dy+255, 1, color)#16

        arcade.draw_line(dx+465, dy+255, dx+435, dy+250, color, 1)
        arcade.draw_line(dx+465, dy+255, dx+495, dy+255, color ,1)

        #HAIR
        arcade.draw_circle_filled(dx+480, dy+425, 1, color)#top middle
        arcade.draw_line(dx+480, dy+425, dx+460, dy+435, color, 1)
        arcade.draw_circle_filled(dx+460, dy+435, 1, color)#2
        arcade.draw_line(dx+460, dy+435, dx+400, dy+415, color ,1)
        arcade.draw_circle_filled(dx+400, dy+415, 1, color)#3
        arcade.draw_line(dx+400, dy+415, dx+365, dy+370, color ,1)

        arcade.draw_circle_filled(dx+365, dy+370, 1, color)#4
        arcade.draw_line(dx+365, dy+370, dx+345, dy+370, color, 1)
        arcade.draw_circle_filled(dx+345, dy+370, 1, color)#5
        arcade.draw_line(dx+345, dy+370, dx+365, dy+340, color, 1)
        arcade.draw_circle_filled(dx+365, dy+340, 1, color)#6 connects head and hair
        arcade.draw_line(dx+365, dy+340, dx+400, dy+350, color, 1)
        arcade.draw_circle_filled(dx+400, dy+350, 1, color)#7
        arcade.draw_line(dx+400, dy+350, dx+440, dy+385, color, 1)
        arcade.draw_circle_filled(dx+440, dy+385, 1, color)#8 connects brow and hair
        arcade.draw_line(dx+440, dy+385, dx+480, dy+400, color, 1)
        arcade.draw_circle_filled(dx+480, dy+400, 1, color)#9 bottom of middle
        arcade.draw_line(dx+480, dy+400, dx+520, dy+385, color, 1)

        arcade.draw_circle_filled(dx+520, dy+385, 1, color)#10 connects brow and hair
        arcade.draw_line(dx+520, dy+385, dx+575, dy+350, color, 1)
        arcade.draw_circle_filled(dx+575, dy+350, 1, color)#11
        arcade.draw_line(dx+575, dy+350, dx+595, dy+340, color, 1)
        arcade.draw_circle_filled(dx+595, dy+340, 1, color)#12 connects head and hair
        arcade.draw_line(dx+595, dy+340, dx+640, dy+370, color, 1)
        arcade.draw_circle_filled(dx+640, dy+370, 1, color)#13
        arcade.draw_line(dx+640, dy+370, dx+610, dy+385, color, 1)
        arcade.draw_circle_filled(dx+610, dy+385, 1, color)#14
        arcade.draw_line(dx+610, dy+385, dx+560, dy+430, color, 1)
        arcade.draw_circle_filled(dx+560, dy+430, 1, color)#15
        arcade.draw_line(dx+560, dy+430, dx+535, dy+430, color, 1)
        arcade.draw_circle_filled(dx+535, dy+430 ,1, color)#16
        arcade.draw_line(dx+535, dy+430, dx+480, dy+425, color, 1 )

        #GLASSES
        #lenses
        arcade.draw_circle_outline(dx+430, dy+335, 36, color)#left
        arcade.draw_circle_outline(dx+530,dy+335, 36, color)#rght


        #bridge and sides
        arcade.draw_line(dx+430, dy+335, dx+530, dy+335, color, 1)
        arcade.draw_line(dx+430, dy+325, dx+365, dy+340, color, 1)
        arcade.draw_line(dx+530, dy+325, dx+595, dy+340, color, 1)

        #code
        arcade.draw_circle_filled(dx+430, dy+335, 35, arcade.color.BLACK)
        arcade.draw_circle_filled(dx+530, dy+335, 35, arcade.color.BLACK)

        #left
        arcade.draw_line(dx+405, dy+350, dx+430, dy+350, color, 1)
        arcade.draw_line(dx+405, dy+342, dx+445, dy+342, color, 1)
        arcade.draw_line(dx+405, dy+334, dx+425, dy+334, color, 1)
        arcade.draw_line(dx+405, dy+326, dx+450, dy+326, color, 1)
        arcade.draw_line(dx+405, dy+318, dx+415, dy+318, color, 1)
        arcade.draw_line(dx+430, dy+318, dx+445, dy+318, color, 1)

        #Right
        #Cube
        #arcade.draw_line(dx+505, dy+345, dx+520, dy+340, color, 1) #Top Left Front
        #arcade.draw_line(dx+505, dy+330, dx+520, dy+325, color, 1) #Bottom Left Front
        #arcade.draw_line(dx+520, dy+325, dx+520, dy+340, color, 1) #Middle Vertical
        #arcade.draw_line(dx+505, dy+345, dx+505, dy+330, color, 1) #Left vertical
        #arcade.draw_line(dx+520, dy+340, dx+535, dy+345, color, 1) #Top Right Front
        #arcade.draw_line(dx+520, dy+325, dx+535, dy+330, color, 1) #Bottom Right Front
        #arcade.draw_line(dx+535, dy+330, dx+535, dy+345, color, 1)#Right Vertical
        #arcade.draw_line(dx+505, dy+345, dx+520, dy+350, color, 1)#Top Back Right
        #arcade.draw_line(dx+520, dy+350, dx+535, dy+345, color, 1) #Top Back left

        #Code
        arcade.draw_line(dx+515, dy+360, dx+530, dy+360, color, 1)
        arcade.draw_line(dx+515, dy+352, dx+525, dy+352, color, 1)
        arcade.draw_line(dx+515, dy+344, dx+535, dy+344, color, 1)
        arcade.draw_line(dx+515, dy+336, dx+530, dy+336, color, 1)
        arcade.draw_line(dx+540, dy+336, dx+550, dy+336, color, 1)
        arcade.draw_line(dx+515, dy+328, dx+530, dy+328, color, 1)
        arcade.draw_line(dx+515, dy+320, dx+535, dy+320, color, 1)
        arcade.draw_line(dx+515, dy+312, dx+530, dy+312, color, 1)




        #DRIP
        arcade.draw_line(dx+580, dy+260, dx+675, dy+240, color, 1) #Right shoulder
        arcade.draw_line(dx+380, dy+260, dx+290, dy+240, color, 1) #left shoulder

