import pygame

pygame.init() # 초기화(반드시 필요)

# 화면 크기 설정
screen_width  = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("D:/pythonWorkspace/pygame_basic/tmp.background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("D:/pythonWorkspace/pygame_basic/tmp.character.png")
character_size = character.get_rect().size # 이미지 크기 구함
character_width = character_size[0]     # 캐릭터의 가로 크기
character_height = character_size[1]    # 캐릭터의 세로 크기
character_x_pos = ( screen_width  / 2 ) - ( character_width / 2 )     # ( 가로 위치 )
character_y_pos = screen_height - character_height # ( 세로 위치 )

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6


# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임 화면의 초당 프레임 수 설정
    # print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get():  # 사용자의 입력을 감지
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였나?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:    # 키보드 눌렸는지 확인
            if event.key == pygame.K_LEFT: # 왼쪽
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:  # 오른쪽
                to_x += character_speed
            elif event.key == pygame.K_UP: # 위쪽
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:   # 아래쪽
                to_y += character_speed

        if event.type == pygame.KEYUP: # 키보드가 눌리지 않으면
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    # dt를 곱함으로 프레임에 관계없이 속도 보정을 해줌
    character_x_pos += to_x * dt 
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > ( screen_width - character_width ):
        character_x_pos = screen_width - character_width

    # 가로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > ( screen_height - character_height ):
        character_y_pos = screen_height - character_height
    
    screen.blit(background, (0, 0)) # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    pygame.display.update() # 게임 화면 다시 그리기!

# pygame 종료
pygame.quit()