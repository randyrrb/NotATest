import sys, pygame

width = 1300
height = 800

screen = pygame.display.set_mode((width, height))
speed = [0, 0]
light_blue = 173, 216, 230

balloon = pygame.image.load = [pygame.image.load('slam1.png'), pygame.image.load('slam2.png'), pygame.image.load('slam3.png'),
           pygame.image.load('slam4.png'), pygame.image.load('slam5.png'), pygame.image.load('slam6.png'),
           pygame.image.load('slam7.png'), pygame.image.load('slam8.png'), pygame.image.load('slam9.png'),
           pygame.image.load('slam10.png'), pygame.image.load('slam11.png'), pygame.image.load('slam12.png'),
           pygame.image.load('slam13.png'), pygame.image.load('slam14.png'), pygame.image.load('slam15.png'),
           pygame.image.load('slam16.png'), pygame.image.load('slam17.png')]
ball_rect = balloon.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    key = pygame.key.get_pressed()
    ball_rect = ball_rect.move(speed)
    if key[pygame.K_UP]:
        ball_rect = ball_rect.move([0, -1])
    if key[pygame.K_DOWN]:
        ball_rect = ball_rect.move([0, 1])
    if key[pygame.K_LEFT]:
        ball_rect = ball_rect.move([-1, 0])
    if key[pygame.K_RIGHT]:
        ball_rect = ball_rect.move([1, 0])



    screen.fill(light_blue)
    screen.blit(balloon, ball_rect)
    pygame.display.flip()
