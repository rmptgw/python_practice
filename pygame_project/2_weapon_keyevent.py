# Project) 오락실 Pang 게임 만들기

# [게임조건]
# 1. 캐릭터는 화면 아래에 위치, 좌우로만 이동가능
# 2. 스페이스를 누르면 무기를 쏘아올림
# 3. 큰 공 1개가 나타나서 바운스
# 4. 무기에 닿으면 공은 작은 크기 2갤 분할, 가장 작은 크기의 공은 사라짐
# 5. 모든 공을 없애면 게임 종료(성공)
# 6. 캐릭터는 공에 닿으면 게임 종료(실패)
# 7. 시간제한 99초, 초과 시 게임 종료(실패)
# 8. FPS는 30으로 고정(필요시 speed 값을 조정)

# [게임 이미지]
# 1. 배경 : 640 * 480(가로 세로) - background.png
# 2. 무대 : 640 * 50 - stage.png
# 3. 캐릭터 : 60 * 33 - character.png
# 4. 무기 : 20 * 430 - weapon.png
# 5. 공 : 160 * 160, 80 * 80, 40 * 40, 20 * 20 - balloon1.png ~ balloon4.png

import pygame
import os
############################################################
# 기본 초기화(반드시 해야 하는 것들)

pygame.init() # 초기화(반드시 필요)

# 화면 크기 설정
screen_width  = 640 # 가로 크기
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Project) 오락실 Pang 게임 만들기") # 게임 이름

# FPS
clock = pygame.time.Clock()
############################################################
# 1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 폰트, 속도 등 )
# 배경 및 이미지 지정
# 작업 디렉토리 지정
current_path = os.path.dirname(__file__)
# 이미지 디렉토리 지정
image_path = os.path.join(current_path, "images")
# 배경 설정
background = pygame.image.load( os.path.join(image_path, "background.png") )

# 스테이지 이미지 지정
stage      = pygame.image.load( os.path.join(image_path, "stage.png") )
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# 캐릭터 설정
character  = pygame.image.load( os.path.join(image_path,"character.png") )
character_size   = character.get_rect().size
character_width  = character_size[0]
character_height = character_size[1]
character_x_pos  = ( screen_width  / 2 ) - ( character_width  / 2 )
character_y_pos  = screen_height - character_height - stage_height


# 무기 설정
weapon     = pygame.image.load( os.path.join(image_path,"weapon.png") )
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
# 무기는 여러발 발사 가능
weapons = []

# 무기 속도 설정
weapon_speed = 10


balloon1   = pygame.image.load( os.path.join(image_path, "balloon1.png") )
balloon2   = pygame.image.load( os.path.join(image_path, "balloon2.png") )
balloon3   = pygame.image.load( os.path.join(image_path, "balloon3.png") )
balloon4   = pygame.image.load( os.path.join(image_path, "balloon4.png") )


# 이동할 좌표 설정
character_to_x = 0
character_to_y = 0

# 이동 속도 설정
character_speed = 0.5

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(30) # 게임 화면의 초당 프레임 수 설정
    # print("fps : " + str(clock.get_fps()))

    # 2. 이벤트 처리( 키보드, 마우스 등 )
    for event in pygame.event.get():  # 사용자의 입력을 감지
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였나?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:    # 키보드 눌렸는지 확인
            if event.key == pygame.K_LEFT: # 방향키 왼쪽 / 좌측으로 이동
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:  # 방향키 오른쪽 / 우측으로 이동
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE: # 스페이스 / 무기발사
                weapon_x_pos = character_x_pos + ( character_width / 2 ) - ( weapon_width / 2 )
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])


            
        if event.type == pygame.KEYUP: # 키보드가 눌리지 않으면
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    
    # 3. 게임 캐릭터 위치 정의
    # 무기 위치 조정
    # 무기 발사시 x값은 변동 없고 y값은 변동됨
    weapons = [ [ w[0], w[1] - weapon_speed ] for w in weapons ]
    
    # 천장에 닿은 무기 없애기
    weapons = [ [ w[0], w[1] ] for w in weapons if w[1] > 0 ]
    
    # dt를 곱함으로 프레임에 관계없이 속도 보정을 해줌
    character_x_pos += character_to_x * dt 
    character_y_pos += character_to_y * dt

    # 가로 경계값 처리
    if  character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > ( screen_width - character_width ):
         character_x_pos = screen_width - character_width

    # 세로 경계값 처리 -
    if  character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > ( screen_height - character_height ):
         character_y_pos = screen_height - character_height
    
    # 4. 충돌 처리
    # 충돌 처리를 위한 rect 정보 업데이트
    # get_rect = rectangle 정보를 가져옴
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top  = character_y_pos

    # 충돌 체크
    # if character_rect.colliderect( enemy_rect ):
    #     print('충돌했어요')
    #     running = False

    # 5. 화면에 그리기
    screen.blit( background, (0,0) ) # 배경화면 구현

    # 무기 구현
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    screen.blit( stage,      ( 0, screen_height - stage_height ) )  # 스테이지 구현
    screen.blit( character,  ( character_x_pos, character_y_pos ) )  # 캐릭터 구현
    
    pygame.display.update() # 게임 화면 다시 그리기!

# pygame 종료
pygame.quit()

############################################################ㄴ
