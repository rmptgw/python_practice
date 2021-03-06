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
# 캐릭터 이동 좌표 설정
character_to_x = 0
character_to_y = 0
# 캐릭터 이동 속도 설정
character_speed = 0.5

# 무기 설정
weapon     = pygame.image.load( os.path.join(image_path,"weapon.png") )
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
# 무기는 여러발 발사 가능
weapons = []
# 무기 속도 설정
weapon_speed = 10

# 공 만들기(4개 크기에 대해 따로 처리)
ball_images = [
    pygame.image.load( os.path.join(image_path, "balloon1.png") ),
    pygame.image.load( os.path.join(image_path, "balloon2.png") ),
    pygame.image.load( os.path.join(image_path, "balloon3.png") ),
    pygame.image.load( os.path.join(image_path, "balloon4.png") )
]
# 공 크기에 따른 최초 속도
ball_speed_y = [-18, -15, -12, -9] # index 0, 1, 2, 3 에 해당하는 값
# 공들
balls = []
balls.append({
    "pos_x" : 50,   # 공의 x좌표
    "pos_y" : 50,   # 공의 y좌표
    "img_idx" : 0,  # 공의 이미지 인덱스
    "to_x" : 3,     # x축 이동 방향, -는 좌측, +는 우측
    "to_y" : -6,    # y축 이동 방향
    "init_spd_y" : ball_speed_y[0] # y 최초 속도
})

weapon_to_remove =  -1
ball_to_remove = -1

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(30) # 게임 화면의 초당 프레임 수 설정
    print("fps : " + str(clock.get_fps()))

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
    
    # 공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val['pos_x']
        ball_pos_y = ball_val['pos_y']
        ball_img_idx = ball_val['img_idx']
        
        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # 가로벽에 닿았을 때, 공 이동위치 변경(튕겨 나오는 효과)
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val['to_x'] = ball_val['to_x'] * -1

        # 세로위치
        # 스테이지에 튕겨서 올라가는 처리
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val['to_y'] = ball_val['init_spd_y']
        else : # 그 외의 모든 경우에는 속도를 증가
            ball_val['to_y'] += 0.5

        ball_val['pos_x'] += ball_val['to_x']
        ball_val['pos_y'] += ball_val['to_y']
    


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

    # 캐릭터 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top  = character_y_pos

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val['pos_x']
        ball_pos_y = ball_val['pos_y']
        ball_img_idx = ball_val['img_idx']
        
        # 공 rect 정보 업데이트
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        # 공과 캐릭터 충돌처리
        if character_rect.colliderect(ball_rect):
            running = False
            break
        
        # 공과 무기들 충돌처리
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            # 무기 rect 정보 업데이트
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

            # 충돌체크
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx # 해당 무기 없애기 위한 값 설정
                ball_to_remove = ball_idx # 해당 공 없애기 위한 값 설정
                break
    # 충돌된 공 or 무기 없애기
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1
    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1


    # 5. 화면에 그리기
    screen.blit( background, (0,0) ) # 배경화면 구현

    # 무기 구현
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val['pos_x']
        ball_pos_y = val['pos_y']
        ball_img_idx = val['img_idx']
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    screen.blit( stage,      ( 0, screen_height - stage_height ) )  # 스테이지 구현
    screen.blit( character,  ( character_x_pos, character_y_pos ) )  # 캐릭터 구현
    
    pygame.display.update() # 게임 화면 다시 그리기!

# pygame 종료
pygame.quit()

############################################################ㄴ
