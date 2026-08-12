




image white = Solid("#FFF")
image red = Solid("#9f0002")

image ctc_icon:
    "gui/main_ctc_01.png"
    pause CTC_ICON_ANIME_PAUSE

    "gui/main_ctc_02.png"
    pause CTC_ICON_ANIME_PAUSE

    "gui/main_ctc_03.png"
    pause CTC_ICON_ANIME_PAUSE

    "gui/main_ctc_04.png"
    pause CTC_ICON_ANIME_PAUSE

    "gui/main_ctc_05.png"
    pause CTC_ICON_ANIME_PAUSE

    "gui/main_ctc_06.png"
    pause CTC_ICON_ANIME_PAUSE

    repeat

image rclick_buttons_frame = Fixed(
    At(Image("gui/right_click_menu_frame_01.png", align = (0.5, 0.5)), rotate_loop_clockwise(35)),
    At(Image("gui/right_click_menu_frame_02.png", align = (0.5, 0.5)), rotate_loop_counter_clockwise(32)),
    At(Image("gui/right_click_menu_frame_03.png", align = (0.5, 0.5)), rotate_loop_clockwise(30)))

image f001_01_blur01 = "images/others/f001_01_blur01.png"


image smoke = 'images/others/smoke.png'
image smoke_front = 'images/others/smoke_front.png'

image splash_circle_logo = "gui/splash_logo.png"

image title_particle1 = SnowBlossom(
    At("gui/title_particle.png", zoom(0.4)),
    count=150,
    border=50,
    xspeed=(-50, 80),
    yspeed=(-300, -50),
    start=0,
    fast=True,
    horizontal=False)

image title_particle2 = SnowBlossom(
    At("gui/title_particle.png", zoom(0.6)),
    count=100,
    border=50,
    xspeed=(-10, 40),
    yspeed=(-120, -5),
    start=0,
    fast=True,
    horizontal=False)

image title_art = Fixed(
    "gui/title_001.png",
    "title_particle1",
    "title_particle2",
    "gui/title_002.png",
    
    At("gui/title_003.png", title_chara(217, 55, start_delay = 0.3, y_offset = 100)),
    At("gui/title_004.png", title_chara(46, 53, start_delay = 0.6, y_offset = 150)),
    At("gui/title_005.png", title_chara(142, 264, start_delay = 1.0, y_offset = 200)),
    At("gui/title_006.png", title_chara(285, 88, start_delay = 1.4, y_offset = 250)),
    
    At("gui/title_007.png", title_card(50, 200, start_delay = 0.4, slide_time = 3.0, slide_offset = 20)),
    At("gui/title_008.png", title_card(710, 219, start_delay = 0.7, slide_time = 2.8, slide_offset = 20)),
    At("gui/title_009.png", title_card(664, 336, start_delay = 0.9, slide_time = 3.0, slide_offset = 25)),
    At("gui/title_010.png", title_card(46, 420, start_delay = 1.1, slide_time = 3.2, slide_offset = 15)),
    At("gui/title_011.png", title_card(602, 450, start_delay = 1.3, slide_time = 2.5, slide_offset = 15)),
    At("gui/title_012.png", title_card(122, 549, start_delay = 1.5, slide_time = 3.2, slide_offset = 20)),
    At("gui/title_013.png", title_card(505, 582, start_delay = 1.7, slide_time = 2.7, slide_offset = 25)),
    At("gui/title_014.png", title_card(283, 596, start_delay = 1.9, slide_time = 3.1, slide_offset = 20)),
    
    At("gui/title_015.png", title_logo),
    )

image sp_logo_movie = Movie(channel = "sp_logo", play = "movies/sp_logo_reveal.webm")







image ecg girlstalkA1 su1 = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef not.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit su1.png")

image ecg girlstalkA1 tro = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef not.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit tro.png")

image ecg girlstalkA1 nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef not.png",  
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit nor.png")

image ecg girlstalkA1 ang = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef not.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit ang.png")

image ecg girlstalkA1 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef not.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit smi.png")




image ecg girlstalkA2 nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef not.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit nor.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cof.png")

image ecg girlstalkA2 tro = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef not.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit tro.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cof.png")

image ecg girlstalkA2 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef not.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit smi.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cof.png")

image ecg girlstalkA2 ang = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef not.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit ang.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cof.png")




image ecg girlstalkA3 nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit nor.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cookie.png")

image ecg girlstalkA3 tro = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit tro.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cookie.png")

image ecg girlstalkA3 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit smi.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cookie.png")

image ecg girlstalkA3 ang = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit ang.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cookie.png")

image ecg girlstalkA3 sur = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit sur.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cookie.png")

image ecg girlstalkA3 su1 = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit su1.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cookie.png")

image ecg girlstalkA3 que = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit que.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cookie.png")

image ecg girlstalkA3 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit ser.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cookie.png")




image ecg girlstalkA4 nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit nor.png",
    (715, 623), GIRLSTALK_DIR + "ecg girlstalk accessories lef book.png")

image ecg girlstalkA4 tro = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit tro.png",
    (715, 623), GIRLSTALK_DIR + "ecg girlstalk accessories lef book.png")

image ecg girlstalkA4 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit smi.png",
    (715, 623), GIRLSTALK_DIR + "ecg girlstalk accessories lef book.png")

image ecg girlstalkA4 ang = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit ang.png",
    (715, 623), GIRLSTALK_DIR + "ecg girlstalk accessories lef book.png")

image ecg girlstalkA4 sur = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit sur.png",
    (715, 623), GIRLSTALK_DIR + "ecg girlstalk accessories lef book.png")

image ecg girlstalkA4 su1 = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit su1.png",
    (715, 623), GIRLSTALK_DIR + "ecg girlstalk accessories lef book.png")

image ecg girlstalkA4 que = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit que.png",
    (715, 623), GIRLSTALK_DIR + "ecg girlstalk accessories lef book.png")

image ecg girlstalkA4 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit ser.png",
    (715, 623), GIRLSTALK_DIR + "ecg girlstalk accessories lef book.png")




image ecg girlstalkA5 nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit nor.png",
    (715, 623), GIRLSTALK_DIR + "ecg girlstalk accessories lef book.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cof.png",)

image ecg girlstalkA5 tro = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit tro.png",
    (715, 623), GIRLSTALK_DIR + "ecg girlstalk accessories lef book.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cof.png",)

image ecg girlstalkA5 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit smi.png",
    (715, 623), GIRLSTALK_DIR + "ecg girlstalk accessories lef book.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cof.png",)

image ecg girlstalkA5 ang = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit ang.png",
    (715, 623), GIRLSTALK_DIR + "ecg girlstalk accessories lef book.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cof.png",)

image ecg girlstalkA5 sur = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit sur.png",
    (715, 623), GIRLSTALK_DIR + "ecg girlstalk accessories lef book.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cof.png",)

image ecg girlstalkA5 su1 = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit su1.png",
    (715, 623), GIRLSTALK_DIR + "ecg girlstalk accessories lef book.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cof.png",)

image ecg girlstalkA5 que = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit que.png",
    (715, 623), GIRLSTALK_DIR + "ecg girlstalk accessories lef book.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cof.png",)

image ecg girlstalkA5 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk sit ser.png",
    (715, 623), GIRLSTALK_DIR + "ecg girlstalk accessories lef book.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cof.png",)




image ecg girlstalkB1 smi glo = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig not.png",
    (669, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit smi.png",
    (169, 0), GIRLSTALK_DIR + "ecg girlstalk chara mao sit glo.png")

image ecg girlstalkB1 smi blu = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig not.png", 
    (669, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit smi.png",
    (169, 0), GIRLSTALK_DIR + "ecg girlstalk chara mao sit blu.png")



image ecg girlstalkB1 uwa glo = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig not.png",
    (669, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit uwa.png",
    (169, 0), GIRLSTALK_DIR + "ecg girlstalk chara mao sit glo.png")

image ecg girlstalkB1 uwa blu = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig not.png",
    (669, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit uwa.png",
    (169, 0), GIRLSTALK_DIR + "ecg girlstalk chara mao sit blu.png")

image ecg girlstalkB1 uwa nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig not.png",
    (669, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit uwa.png",
    (169, 0), GIRLSTALK_DIR + "ecg girlstalk chara mao sit nor.png")



image ecg girlstalkB1 sur gl1 = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig not.png",
    (669, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit sur.png",
    (169, 0), GIRLSTALK_DIR + "ecg girlstalk chara mao sit gl1.png")

image ecg girlstalkB1 sur nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig not.png",
    (669, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit sur.png",
    (169, 0), GIRLSTALK_DIR + "ecg girlstalk chara mao sit nor.png")

image ecg girlstalkB1 sur glo = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig not.png",
    (669, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit sur.png",
    (169, 0), GIRLSTALK_DIR + "ecg girlstalk chara mao sit glo.png")



image ecg girlstalkB1 tro glo = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig not.png",    
    (669, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit tro.png",
    (169, 0), GIRLSTALK_DIR + "ecg girlstalk chara mao sit glo.png")

image ecg girlstalkB1 tro nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig not.png",
    (669, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit tro.png",
    (169, 0), GIRLSTALK_DIR + "ecg girlstalk chara mao sit nor.png")



image ecg girlstalkB1 nor nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig not.png",
    (669, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit nor.png",
    (169, 0), GIRLSTALK_DIR + "ecg girlstalk chara mao sit nor.png")

image ecg girlstalkB1 nor blu = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig not.png",
    (669, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit nor.png",
    (169, 0), GIRLSTALK_DIR + "ecg girlstalk chara mao sit blu.png")

image ecg girlstalkB1 nor glo = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig not.png",
    (669, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit nor.png",
    (169, 0), GIRLSTALK_DIR + "ecg girlstalk chara mao sit glo.png")



image ecg girlstalkB1 lau nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig not.png",        
    (669, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit lau.png",
    (169, 0), GIRLSTALK_DIR + "ecg girlstalk chara mao sit nor.png")

image ecg girlstalkB1 lau glo = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig not.png",
    (669, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit lau.png",
    (169, 0), GIRLSTALK_DIR + "ecg girlstalk chara mao sit glo.png")




image ecg girlstalkB2 nor nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig not.png",        
    (669, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit nor.png",
    (169, 0), GIRLSTALK_DIR + "ecg girlstalk chara mao sit nor.png",
    (1044, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof.png")



image ecg girlstalkB2 lau nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig not.png",
    (669, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit lau.png",
    (169, 0), GIRLSTALK_DIR + "ecg girlstalk chara mao sit nor.png",
    (1044, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof.png")




image ecg girlstalkB3 nor nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig not.png",
    (669, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit nor.png",
    (169, 0), GIRLSTALK_DIR + "ecg girlstalk chara mao sit nor.png",
    (91, 459), GIRLSTALK_DIR + "ecg girlstalk accessories rig dou.png",
    (1044, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof.png")



image ecg girlstalkB3 lau nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig not.png",
    (669, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit lau.png",
    (169, 0), GIRLSTALK_DIR + "ecg girlstalk chara mao sit nor.png",
    (91, 459), GIRLSTALK_DIR + "ecg girlstalk accessories rig dou.png",
    (1044, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof.png")

image ecg girlstalkB3 lau glo = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig not.png",    
    (669, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit lau.png",
    (169, 0), GIRLSTALK_DIR + "ecg girlstalk chara mao sit glo.png",
    (91, 459), GIRLSTALK_DIR + "ecg girlstalk accessories rig dou.png",
    (1044, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof.png")

image ecg girlstalkB3 lau blu = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig not.png",    
    (669, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit lau.png",
    (169, 0), GIRLSTALK_DIR + "ecg girlstalk chara mao sit blu.png",
    (91, 459), GIRLSTALK_DIR + "ecg girlstalk accessories rig dou.png",
    (1044, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof.png")



image ecg girlstalkB3 smi nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig not.png",
    (669, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit smi.png",
    (169, 0), GIRLSTALK_DIR + "ecg girlstalk chara mao sit nor.png",
    (91, 459), GIRLSTALK_DIR + "ecg girlstalk accessories rig dou.png",
    (1044, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof.png")

image ecg girlstalkB3 smi blu = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig not.png",
    (669, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit smi.png",
    (169, 0), GIRLSTALK_DIR + "ecg girlstalk chara mao sit blu.png",
    (91, 459), GIRLSTALK_DIR + "ecg girlstalk accessories rig dou.png",
    (1044, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof.png")

image ecg girlstalkB3 smi glo = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig not.png",
    (669, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit smi.png",
    (169, 0), GIRLSTALK_DIR + "ecg girlstalk chara mao sit glo.png",
    (91, 459), GIRLSTALK_DIR + "ecg girlstalk accessories rig dou.png",
    (1044, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof.png")



image ecg girlstalkB3 tro blu = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig not.png",
    (669, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit tro.png",
    (169, 0), GIRLSTALK_DIR + "ecg girlstalk chara mao sit blu.png",
    (91, 459), GIRLSTALK_DIR + "ecg girlstalk accessories rig dou.png",
    (1044, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof.png")

image ecg girlstalkB3 tro glo = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig not.png",
    (669, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit tro.png",
    (169, 0), GIRLSTALK_DIR + "ecg girlstalk chara mao sit blu.png",
    (91, 459), GIRLSTALK_DIR + "ecg girlstalk accessories rig dou.png",
    (1044, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof.png")



image ecg girlstalkB3 sur nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig not.png",    
    (669, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit sur.png",
    (169, 0), GIRLSTALK_DIR + "ecg girlstalk chara mao sit nor.png",
    (91, 459), GIRLSTALK_DIR + "ecg girlstalk accessories rig dou.png",
    (1044, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof.png")



image ecg girlstalkB3 uwa glo = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig not.png",    
    (669, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit uwa.png",
    (169, 0), GIRLSTALK_DIR + "ecg girlstalk chara mao sit glo.png",
    (91, 459), GIRLSTALK_DIR + "ecg girlstalk accessories rig dou.png",
    (1044, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof.png")

image ecg girlstalkB3 uwa blu = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig not.png",
    (669, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit uwa.png",
    (169, 0), GIRLSTALK_DIR + "ecg girlstalk chara mao sit blu.png",
    (91, 459), GIRLSTALK_DIR + "ecg girlstalk accessories rig dou.png",
    (1044, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof.png")




image ecg girlstalkC1 nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit nor.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")

image ecg girlstalkC1 tro = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit tro.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")

image ecg girlstalkC1 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit smi.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")

image ecg girlstalkC1 uwa = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit uwa.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")

image ecg girlstalkC1 anx = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit anx.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")

image ecg girlstalkC1 sur = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit sur.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")

image ecg girlstalkC1 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit ser.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")

image ecg girlstalkC1 sad = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit sad.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")

image ecg girlstalkC1 lau = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit lau.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")




image ecg girlstalkC2 nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit nor.png",
    (0, 515), GIRLSTALK_DIR + "ecg girlstalk accessories rcen book.png")

image ecg girlstalkC2 tro = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit tro.png",
    (0, 515), GIRLSTALK_DIR + "ecg girlstalk accessories rcen book.png")

image ecg girlstalkC2 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit smi.png",
    (0, 515), GIRLSTALK_DIR + "ecg girlstalk accessories rcen book.png")

image ecg girlstalkC2 uwa = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit uwa.png",
    (0, 515), GIRLSTALK_DIR + "ecg girlstalk accessories rcen book.png")

image ecg girlstalkC2 anx = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit anx.png",
    (0, 515), GIRLSTALK_DIR + "ecg girlstalk accessories rcen book.png")

image ecg girlstalkC2 sur = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit sur.png",
    (0, 515), GIRLSTALK_DIR + "ecg girlstalk accessories rcen book.png")

image ecg girlstalkC2 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit ser.png",
    (0, 515), GIRLSTALK_DIR + "ecg girlstalk accessories rcen book.png")

image ecg girlstalkC2 sad = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit sad.png",
    (0, 515), GIRLSTALK_DIR + "ecg girlstalk accessories rcen book.png")

image ecg girlstalkC2 lau = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit lau.png",
    (0, 515), GIRLSTALK_DIR + "ecg girlstalk accessories rcen book.png")




image ecg girlstalkC3 nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit nor.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png",
    (0, 515), GIRLSTALK_DIR + "ecg girlstalk accessories rcen book.png")

image ecg girlstalkC3 tro = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit tro.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png",
    (0, 515), GIRLSTALK_DIR + "ecg girlstalk accessories rcen book.png")

image ecg girlstalkC3 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit smi.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png",
    (0, 515), GIRLSTALK_DIR + "ecg girlstalk accessories rcen book.png")

image ecg girlstalkC3 uwa = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit uwa.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png",
    (0, 515), GIRLSTALK_DIR + "ecg girlstalk accessories rcen book.png")

image ecg girlstalkC3 anx = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit anx.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png",
    (0, 515), GIRLSTALK_DIR + "ecg girlstalk accessories rcen book.png")

image ecg girlstalkC3 sur = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit sur.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png",
    (0, 515), GIRLSTALK_DIR + "ecg girlstalk accessories rcen book.png")

image ecg girlstalkC3 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit ser.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png",
    (0, 515), GIRLSTALK_DIR + "ecg girlstalk accessories rcen book.png")

image ecg girlstalkC3 sad = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit sad.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png",
    (0, 515), GIRLSTALK_DIR + "ecg girlstalk accessories rcen book.png")

image ecg girlstalkC3 lau = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom sit lau.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png",
    (0, 515), GIRLSTALK_DIR + "ecg girlstalk accessories rcen book.png")




image ecg girlstalkW1 ge1 = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (8, 0), GIRLSTALK_DIR + "ecg girlstalk chara kik sit ge1.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")

image ecg girlstalkW1 ge2 = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",    
    (8, 0), GIRLSTALK_DIR + "ecg girlstalk chara kik sit ge2.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")

image ecg girlstalkW1 let = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (8, 0), GIRLSTALK_DIR + "ecg girlstalk chara kik sit let.png",    
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")

image ecg girlstalkW1 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (8, 0), GIRLSTALK_DIR + "ecg girlstalk chara kik sit smi.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")

image ecg girlstalkW1 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (8, 0), GIRLSTALK_DIR + "ecg girlstalk chara kik sit ser.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")




image ecg girlstalkH2 nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk02 sit nor.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cof.png")

image ecg girlstalkH2 sur = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",  
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk02 sit sur.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cof.png")

image ecg girlstalkH2 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk02 sit smi.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cof.png")

image ecg girlstalkH2 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk02 sit ser.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cof.png")




image ecg girlstalkX1 smi nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig non.png",
    (161, 0), GIRLSTALK_DIR + "ecg girlstalk chara son sit smi.png",
    (662, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr02 sit nor.png",
    (85, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof.png",
    (1057, 613), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof02.png")

image ecg girlstalkX1 smi smi = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig non.png",
    (161, 0), GIRLSTALK_DIR + "ecg girlstalk chara son sit smi.png",
    (662, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr02 sit smi.png",
    (85, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof.png",
    (1057, 613), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof02.png")

image ecg girlstalkX1 nor smi = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig non.png",
    (161, 0), GIRLSTALK_DIR + "ecg girlstalk chara son sit nor.png",
    (662, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr02 sit smi.png",
    (85, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof.png",
    (1057, 613), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof02.png")

image ecg girlstalkX1 nor nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig non.png",
    (161, 0), GIRLSTALK_DIR + "ecg girlstalk chara son sit nor.png",
    (662, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr02 sit nor.png",
    (85, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof.png",
    (1057, 613), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof02.png")

image ecg girlstalkX1 sm2 nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig non.png",
    (161, 0), GIRLSTALK_DIR + "ecg girlstalk chara son sit sm2.png",
    (662, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr02 sit nor.png",
    (85, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof.png",
    (1057, 613), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof02.png")

image ecg girlstalkX1 ser nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig non.png",
    (161, 0), GIRLSTALK_DIR + "ecg girlstalk chara son sit ser.png",
    (662, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr02 sit nor.png",
    (85, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof.png",
    (1057, 613), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof02.png")

image ecg girlstalkX1 ser smi = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig non.png",
    (161, 0), GIRLSTALK_DIR + "ecg girlstalk chara son sit ser.png",
    (662, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr02 sit smi.png",
    (85, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof.png",
    (1057, 613), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof02.png")

image ecg girlstalkX1 tro smi = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig non.png",
    (161, 0), GIRLSTALK_DIR + "ecg girlstalk chara son sit tro.png",
    (662, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr02 sit smi.png",
    (85, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof.png",
    (1057, 613), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof02.png")

image ecg girlstalkX1 smi tro = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig non.png",
    (161, 0), GIRLSTALK_DIR + "ecg girlstalk chara son sit smi.png",
    (662, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr02 sit tro.png",
    (85, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof.png",
    (1057, 613), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof02.png")

image ecg girlstalkX1 nor tro = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig non.png",
    (161, 0), GIRLSTALK_DIR + "ecg girlstalk chara son sit nor.png",
    (662, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr02 sit tro.png",
    (85, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof.png",
    (1057, 613), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof02.png")

image ecg girlstalkX1 ser tro = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig non.png",
    (161, 0), GIRLSTALK_DIR + "ecg girlstalk chara son sit ser.png",
    (662, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr02 sit tro.png",
    (85, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof.png",
    (1057, 613), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof02.png")

image ecg girlstalkX1 tro nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig non.png",
    (161, 0), GIRLSTALK_DIR + "ecg girlstalk chara son sit tro.png",
    (662, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr02 sit nor.png",
    (85, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof.png",
    (1057, 613), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof02.png")

image ecg girlstalkX1 ele nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rig.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rig non.png",
    (161, 0), GIRLSTALK_DIR + "ecg girlstalk chara son sit ele.png",
    (662, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr02 sit nor.png",
    (85, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof.png",
    (1057, 613), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof02.png")




image ecg girlstalkT2 anx = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom05 sit anx.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")

image ecg girlstalkT2 tro = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom05 sit tro.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")

image ecg girlstalkT2 sur = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom05 sit sur.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")

image ecg girlstalkT2 uwa = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom05 sit uwa.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")

image ecg girlstalkT2 lau = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom05 sit lau.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")

image ecg girlstalkT2 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom05 sit smi.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")

image ecg girlstalkT2 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom05 sit ser.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")

image ecg girlstalkT2 nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom05 sit nor.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")




image ecg girlstalkR2 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit smi.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cof.png")

image ecg girlstalkR2 shy = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit shy.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cof.png")

image ecg girlstalkR2 sur = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit sur.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cof.png")

image ecg girlstalkR2 nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit nor.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cof.png")

image ecg girlstalkR2 que = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit que.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cof.png")




image ecg girlstalkQ2 nor nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef02.png",
    (94, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit nor.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef02 diary.png",
    (643, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr04 sit nor.png",
    (85, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef dou.png")

image ecg girlstalkQ2 nor tro = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef02.png",
    (94, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit nor.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef02 diary.png",
    (643, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr04 sit tro.png",
    (85, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef dou.png")

image ecg girlstalkQ2 ser ser = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef02.png",
    (94, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit ser.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef02 diary.png",
    (643, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr04 sit ser.png",
    (85, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef dou.png")

image ecg girlstalkQ2 ser sad = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef02.png",
    (94, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit ser.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef02 diary.png",
    (643, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr04 sit sad.png",
    (85, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef dou.png")

image ecg girlstalkQ2 tro ser = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef02.png",
    (94, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit tro.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef02 diary.png",
    (643, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr04 sit ser.png",
    (85, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef dou.png")

image ecg girlstalkQ2 nor ser = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef02.png",
    (94, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit nor.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef02 diary.png",    
    (643, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr04 sit ser.png",
    (85, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef dou.png")

image ecg girlstalkQ2 ser nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef02.png",
    (94, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit ser.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef02 diary.png",    
    (643, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr04 sit nor.png",
    (85, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef dou.png")

image ecg girlstalkQ2 smi nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef02.png",
    (94, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit smi.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef02 diary.png",
    (643, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr04 sit nor.png",
    (85, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef dou.png")

image ecg girlstalkQ2 ang nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef02.png",
    (94, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit ang.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef02 diary.png",
    (643, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr04 sit nor.png",
    (85, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef dou.png")




image ecg girlstalkS1 ser ser = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef02.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef02 non.png",
    (94, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit ser.png",
    (643, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr03 sit ser.png")

image ecg girlstalkS1 tro ser = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef02.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef02 non.png",
    (94, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit tro.png",
    (643, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr03 sit ser.png")

image ecg girlstalkS1 ser tro = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef02.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef02 non.png",
    (94, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit ser.png",
    (643, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr03 sit tro.png")




image ecg girlstalkT1 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom05 sit ser.png")

image ecg girlstalkT1 tro = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom05 sit ser.png")

image ecg girlstalkT1 anx = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom05 sit anx.png")

image ecg girlstalkT1 sad = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom05 sit sad.png")

image ecg girlstalkT1 uwa = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom05 sit uwa.png")

image ecg girlstalkT1 sur = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom05 sit uwa.png")




image ecg girlstalkU2 sur = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom06 sit sur.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")

image ecg girlstalkU2 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom06 sit ser.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")

image ecg girlstalkU2 tro = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom06 sit tro.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")

image ecg girlstalkU2 anx = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom06 sit anx.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")

image ecg girlstalkU2 sad = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom06 sit sad.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")

image ecg girlstalkU2 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom06 sit smi.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")

image ecg girlstalkU2 uwa = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom06 sit uwa.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")

image ecg girlstalkU2 lau = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom06 sit lau.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")




image ecg girlstalkP1 sur = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk04 sit sur.png")

image ecg girlstalkP1 que = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk04 sit que.png")




image ecg girlstalkP2 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk04 sit ser.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cof.png")

image ecg girlstalkP2 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk04 sit smi.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cof.png")




image ecg girlstalkV2 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (443, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr04 sit ser.png",
    (838, 591), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof02.png")

image ecg girlstalkV2 tro = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (443, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr04 sit tro.png",    
    (838, 591), GIRLSTALK_DIR + "ecg girlstalk accessories rig cof02.png")




image ecg girlstalkV1 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (443, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr04 sit ser.png")

image ecg girlstalkV1 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen non.png",
    (443, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr04 sit smi.png")




image ecg girlstalkR1 tro = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit tro.png")

image ecg girlstalkR1 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit ser.png")

image ecg girlstalkR1 que = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit que.png")

image ecg girlstalkR1 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit smi.png")

image ecg girlstalkR1 nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef non.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit nor.png")




image ecg girlstalkT3 nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen not.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom05 sit nor.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")

image ecg girlstalkT3 tro = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen not.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom05 sit tro.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")

image ecg girlstalkT3 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen not.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom05 sit smi.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")

image ecg girlstalkT3 uwa = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen not.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom05 sit uwa.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")

image ecg girlstalkT3 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back rcen.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk rcen not.png",
    (440, 0), GIRLSTALK_DIR + "ecg girlstalk chara nom05 sit ser.png",
    (815, 626), GIRLSTALK_DIR + "ecg girlstalk accessories rcen cof.png")




image ecg girlstalkR3 shy = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef not.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit shy.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cof.png")

image ecg girlstalkR3 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef not.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit ser.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cof.png")

image ecg girlstalkR3 que = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef not.png",
    (323, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit que.png",
    (314, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef cof.png")




image ecg girlstalkS2 que nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef02.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef02 non.png",
    (94, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit que.png",
    (643, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr03 sit nor.png",
    (85, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef dou.png")

image ecg girlstalkS2 que sad = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef02.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef02 non.png",
    (94, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit que.png",
    (643, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr03 sit sad.png",
    (85, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef dou.png")

image ecg girlstalkS2 ser ser = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef02.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef02 non.png",
    (94, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit ser.png",
    (643, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr03 sit ser.png",
    (85, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef dou.png")

image ecg girlstalkS2 ser nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef02.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef02 non.png",
    (94, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit ser.png",
    (643, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr03 sit nor.png",
    (85, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef dou.png")

image ecg girlstalkS2 ser smi = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef02.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef02 non.png",
    (94, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit ser.png",
    (643, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr03 sit smi.png",
    (85, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef dou.png")

image ecg girlstalkS2 ser tro = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef02.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef02 non.png",
    (94, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit ser.png",
    (643, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr03 sit tro.png",
    (85, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef dou.png")

image ecg girlstalkS2 smi smi = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef02.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef02 non.png",
    (94, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk03 sit smi.png",
    (643, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr03 sit smi.png",
    (85, 593), GIRLSTALK_DIR + "ecg girlstalk accessories lef dou.png")




image ecg girlstalkO2 nor nor = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef02.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef02 non.png", 
    (94, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk04 sit nor.png",
    (643, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr04 sit nor.png")

image ecg girlstalkO2 que smi = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef02.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef02 non.png", 
    (94, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk04 sit que.png",
    (643, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr04 sit smi.png")

image ecg girlstalkO2 que ser = LiveComposite(SCREEN_SIZE,
    (0, 0), GIRLSTALK_DIR + "ecg girlstalk back lef02.png",
    (0, 467), GIRLSTALK_DIR + "ecg girlstalk desk lef02 non.png", 
    (94, 0), GIRLSTALK_DIR + "ecg girlstalk chara rnk04 sit que.png",
    (643, 0), GIRLSTALK_DIR + "ecg girlstalk chara mhr04 sit ser.png")







image ecg familyrestaurantA1 nor = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back lef.png",
    
    (454, 0), FAMILYRES_DIR + "ecg familyrestaurant chara rnk sit nor.png")

image ecg familyrestaurantA1 tro = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back lef.png",
    
    (454, 0), FAMILYRES_DIR + "ecg familyrestaurant chara rnk sit tro.png")

image ecg familyrestaurantA1 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back lef.png",
    
    (454, 0), FAMILYRES_DIR + "ecg familyrestaurant chara rnk sit smi.png")

image ecg familyrestaurantA1 ang = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back lef.png",
    
    (454, 0), FAMILYRES_DIR + "ecg familyrestaurant chara rnk sit ang.png")

image ecg familyrestaurantA1 sur = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back lef.png",
    
    (454, 0), FAMILYRES_DIR + "ecg familyrestaurant chara rnk sit sur.png")

image ecg familyrestaurantA1 su1 = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back lef.png",
    
    (454, 0), FAMILYRES_DIR + "ecg familyrestaurant chara rnk sit su1.png")

image ecg familyrestaurantA1 que = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back lef.png",
    
    (454, 0), FAMILYRES_DIR + "ecg familyrestaurant chara rnk sit que.png")

image ecg familyrestaurantA1 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back lef.png",
    
    (454, 0), FAMILYRES_DIR + "ecg familyrestaurant chara rnk sit ser.png")




image ecg familyrestaurantA2 nor = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back lef.png",
    
    (454, 0), FAMILYRES_DIR + "ecg familyrestaurant chara rnk sit nor.png",
    
    (923, 437), FAMILYRES_DIR + "ecg familyrestaurant accessories lef emp.png")

image ecg familyrestaurantA2 tro = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back lef.png",
    
    (454, 0), FAMILYRES_DIR + "ecg familyrestaurant chara rnk sit tro.png")

image ecg familyrestaurantA2 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back lef.png",
    
    (454, 0), FAMILYRES_DIR + "ecg familyrestaurant chara rnk sit smi.png",
    
    (923, 437), FAMILYRES_DIR + "ecg familyrestaurant accessories lef emp.png")

image ecg familyrestaurantA2 ang = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back lef.png",
    
    (454, 0), FAMILYRES_DIR + "ecg familyrestaurant chara rnk sit ang.png")

image ecg familyrestaurantA2 sur = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back lef.png",
    
    (454, 0), FAMILYRES_DIR + "ecg familyrestaurant chara rnk sit sur.png",
    
    (923, 437), FAMILYRES_DIR + "ecg familyrestaurant accessories lef emp.png")

image ecg familyrestaurantA2 su1 = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back lef.png",
    
    (454, 0), FAMILYRES_DIR + "ecg familyrestaurant chara rnk sit su1.png",
    
    (923, 437), FAMILYRES_DIR + "ecg familyrestaurant accessories lef emp.png")

image ecg familyrestaurantA2 que = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back lef.png",
    
    (454, 0), FAMILYRES_DIR + "ecg familyrestaurant chara rnk sit que.png",
    
    (923, 437), FAMILYRES_DIR + "ecg familyrestaurant accessories lef emp.png")

image ecg familyrestaurantA2 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back lef.png",
    
    (454, 0), FAMILYRES_DIR + "ecg familyrestaurant chara rnk sit ser.png",
    
    (923, 437), FAMILYRES_DIR + "ecg familyrestaurant accessories lef emp.png")




image ecg familyrestaurantB1 nor = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit nor.png")

image ecg familyrestaurantB1 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit smi.png")

image ecg familyrestaurantB1 sm2 = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit sm2.png")

image ecg familyrestaurantB1 ele = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit ele.png")

image ecg familyrestaurantB1 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit ser.png")

image ecg familyrestaurantB1 que = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit que.png")

image ecg familyrestaurantB1 tor = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit tro.png")

image ecg familyrestaurantB1 men = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit men.png")

image ecg familyrestaurantB1 hun = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit hun.png")




image ecg familyrestaurantB2 nor = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit nor.png",
    
    (645, 626), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl1.png",
    
    (54, 643), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl2.png")

image ecg familyrestaurantB2 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit smi.png",
    
    (645, 626), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl1.png",
    
    (54, 643), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl2.png")

image ecg familyrestaurantB2 sm2 = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit sm2.png",
    
    (645, 626), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl1.png",
    
    (54, 643), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl2.png")

image ecg familyrestaurantB2 ele = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit ele.png",
    
    (645, 626), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl1.png",
    
    (54, 643), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl2.png")

image ecg familyrestaurantB2 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit ser.png",
    
    (645, 626), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl1.png",
    
    (54, 643), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl2.png")

image ecg familyrestaurantB2 que = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit que.png",
    
    (645, 626), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl1.png",
    
    (54, 643), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl2.png")

image ecg familyrestaurantB2 tor = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit tro.png",
    
    (645, 626), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl1.png",
    
    (54, 643), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl2.png")

image ecg familyrestaurantB2 men = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit men.png",
    
    (645, 626), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl1.png",
    
    (54, 643), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl2.png")

image ecg familyrestaurantB2 hun = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit hun.png",
    
    (645, 626), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl1.png",
    
    (54, 643), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl2.png")




image ecg familyrestaurantB3 nor = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit nor.png",
    
    (645, 626), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl1.png",
    
    (54, 643), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl2.png",
    
    (889, 558), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl3.png")

image ecg familyrestaurantB3 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit smi.png",
    
    (645, 626), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl1.png",
    
    (54, 643), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl2.png",
    
    (889, 558), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl3.png")

image ecg familyrestaurantB3 sm2 = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit sm2.png",
    
    (645, 626), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl1.png",
    
    (54, 643), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl2.png",
    
    (889, 558), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl3.png")

image ecg familyrestaurantB3 ele = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit ele.png",
    
    (645, 626), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl1.png",
    
    (54, 643), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl2.png",
    
    (889, 558), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl3.png")

image ecg familyrestaurantB3 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit ser.png",
    
    (645, 626), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl1.png",
    
    (54, 643), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl2.png",
    
    (889, 558), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl3.png")

image ecg familyrestaurantB3 que = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit que.png",
    
    (645, 626), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl1.png",
    
    (54, 643), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl2.png",
    
    (889, 558), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl3.png")

image ecg familyrestaurantB3 tor = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit tro.png",
    
    (645, 626), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl1.png",
    
    (54, 643), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl2.png",
    
    (889, 558), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl3.png")

image ecg familyrestaurantB3 men = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit men.png",
    
    (645, 626), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl1.png",
    
    (54, 643), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl2.png",
    
    (889, 558), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl3.png")

image ecg familyrestaurantB3 hun = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit hun.png",
    
    (645, 626), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl1.png",
    
    (54, 643), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl2.png",
    
    (889, 558), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl3.png")




image ecg familyrestaurantB4 nor = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit nor.png",
    
    (645, 626), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl1.png",
    
    (54, 643), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl2.png",
    
    (889, 558), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl3.png",
    
    (540, 463), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl4.png")

image ecg familyrestaurantB4 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit smi.png",
    
    (645, 626), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl1.png",
    
    (54, 643), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl2.png",
    
    (889, 558), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl3.png",
    
    (540, 463), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl4.png")

image ecg familyrestaurantB4 sm2 = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit sm2.png",
    
    (645, 626), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl1.png",
    
    (54, 643), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl2.png",
    
    (889, 558), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl3.png",
    
    (540, 463), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl4.png")

image ecg familyrestaurantB4 ele = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit ele.png",
    
    (645, 626), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl1.png",
    
    (54, 643), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl2.png",
    
    (889, 558), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl3.png",
    
    (540, 463), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl4.png")

image ecg familyrestaurantB4 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit ser.png",
    
    (645, 626), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl1.png",
    
    (54, 643), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl2.png",
    
    (889, 558), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl3.png",
    
    (540, 463), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl4.png")

image ecg familyrestaurantB4 que = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit que.png",
    
    (645, 626), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl1.png",
    
    (54, 643), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl2.png",
    
    (889, 558), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl3.png",
    
    (540, 463), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl4.png")

image ecg familyrestaurantB4 tor = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit tro.png",
    
    (645, 626), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl1.png",
    
    (54, 643), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl2.png",
    
    (889, 558), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl3.png",
    
    (540, 463), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl4.png")

image ecg familyrestaurantB4 men = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit men.png",
    
    (645, 626), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl1.png",
    
    (54, 643), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl2.png",
    
    (889, 558), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl3.png",
    
    (540, 463), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl4.png")

image ecg familyrestaurantB4 hun = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (217, 0), FAMILYRES_DIR + "ecg familyrestaurant chara son sit hun.png",
    
    (645, 626), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl1.png",
    
    (54, 643), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl2.png",
    
    (889, 558), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl3.png",
    
    (540, 463), FAMILYRES_DIR + "ecg familyrestaurant accessories rig dl4.png")




image ecg familyrestaurantH2 nor = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (210, 0), FAMILYRES_DIR + "ecg familyrestaurant chara mhr04 sit nor.png",
    
    (578, 643), FAMILYRES_DIR + "ecg familyrestaurant accessories rig ome.png")

image ecg familyrestaurantH2 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (210, 0), FAMILYRES_DIR + "ecg familyrestaurant chara mhr04 sit smi.png",
    
    (578, 643), FAMILYRES_DIR + "ecg familyrestaurant accessories rig ome.png")

image ecg familyrestaurantH2 shy = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back rig.png",
    
    (210, 0), FAMILYRES_DIR + "ecg familyrestaurant chara mhr04 sit shy.png",
    
    (578, 643), FAMILYRES_DIR + "ecg familyrestaurant accessories rig ome.png")




image ecg familyrestaurantG2 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back lef.png",
    
    (454, 0), FAMILYRES_DIR + "ecg familyrestaurant chara rnk04 sit smi.png",
    
    (464, 634), FAMILYRES_DIR + "ecg familyrestaurant accessories lef ham.png")

image ecg familyrestaurantG2 shy = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back lef.png",
    
    (454, 0), FAMILYRES_DIR + "ecg familyrestaurant chara rnk04 sit shy.png",
    
    (464, 634), FAMILYRES_DIR + "ecg familyrestaurant accessories lef ham.png")

image ecg familyrestaurantG2 que = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back lef.png",
    
    (454, 0), FAMILYRES_DIR + "ecg familyrestaurant chara rnk04 sit que.png",
    
    (464, 634), FAMILYRES_DIR + "ecg familyrestaurant accessories lef ham.png")

image ecg familyrestaurantG2 sur = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back lef.png",
    
    (454, 0), FAMILYRES_DIR + "ecg familyrestaurant chara rnk04 sit sur.png",
    
    (464, 634), FAMILYRES_DIR + "ecg familyrestaurant accessories lef ham.png")

image ecg familyrestaurantG2 tro = LiveComposite(SCREEN_SIZE,
    (0, 0), FAMILYRES_DIR + "ecg familyrestaurant back lef.png",
    
    (454, 0), FAMILYRES_DIR + "ecg familyrestaurant chara rnk04 sit tro.png",
    
    (464, 634), FAMILYRES_DIR + "ecg familyrestaurant accessories lef ham.png")




image ecg nighttalkA2 nor = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back lef.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk lef non.png",
    (323, 0), NIGHTALK_DIR + "ecg nighttalk chara rnk sit nor.png",
    (314, 593), NIGHTALK_DIR + "ecg nighttalk accessories lef cof.png")

image ecg nighttalkA2 tro = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back lef.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk lef non.png",
    (323, 0), NIGHTALK_DIR + "ecg nighttalk chara rnk sit tro.png",
    (314, 593), NIGHTALK_DIR + "ecg nighttalk accessories lef cof.png")

image ecg nighttalkA2 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back lef.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk lef non.png",
    (323, 0), NIGHTALK_DIR + "ecg nighttalk chara rnk sit smi.png",
    (314, 593), NIGHTALK_DIR + "ecg nighttalk accessories lef cof.png")

image ecg nighttalkA2 ang = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back lef.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk lef non.png",
    (323, 0), NIGHTALK_DIR + "ecg nighttalk chara rnk sit ang.png",
    (314, 593), NIGHTALK_DIR + "ecg nighttalk accessories lef cof.png")

image ecg nighttalkA2 sur = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back lef.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk lef non.png",
    (323, 0), NIGHTALK_DIR + "ecg nighttalk chara rnk sit sur.png",
    (314, 593), NIGHTALK_DIR + "ecg nighttalk accessories lef cof.png")

image ecg nighttalkA2 su1 = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back lef.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk lef non.png",
    (323, 0), NIGHTALK_DIR + "ecg nighttalk chara rnk sit su1.png",
    (314, 593), NIGHTALK_DIR + "ecg nighttalk accessories lef cof.png")

image ecg nighttalkA2 que = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back lef.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk lef non.png",
    (323, 0), NIGHTALK_DIR + "ecg nighttalk chara rnk sit que.png",
    (314, 593), NIGHTALK_DIR + "ecg nighttalk accessories lef cof.png")

image ecg nighttalkA2 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back lef.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk lef non.png",
    (323, 0), NIGHTALK_DIR + "ecg nighttalk chara rnk sit ser.png",
    (314, 593), NIGHTALK_DIR + "ecg nighttalk accessories lef cof.png")

image ecg nighttalkA2 sad = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back lef.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk lef non.png",
    (323, 0), NIGHTALK_DIR + "ecg nighttalk chara rnk sit sad.png",
    (314, 593), NIGHTALK_DIR + "ecg nighttalk accessories lef cof.png")




image ecg nighttalkA3 nor = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back lef.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk lef non.png",
    (323, 0), NIGHTALK_DIR + "ecg nighttalk chara rnk sit nor.png",
    (469, 398), NIGHTALK_DIR + "ecg nighttalk accessories lef piz.png")

image ecg nighttalkA3 tro = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back lef.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk lef non.png",
    (323, 0), NIGHTALK_DIR + "ecg nighttalk chara rnk sit tro.png",
    (469, 398), NIGHTALK_DIR + "ecg nighttalk accessories lef piz.png")

image ecg nighttalkA3 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back lef.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk lef non.png",
    (323, 0), NIGHTALK_DIR + "ecg nighttalk chara rnk sit smi.png",
    (469, 398), NIGHTALK_DIR + "ecg nighttalk accessories lef piz.png")

image ecg nighttalkA3 ang = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back lef.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk lef non.png",
    (323, 0), NIGHTALK_DIR + "ecg nighttalk chara rnk sit ang.png",
    (469, 398), NIGHTALK_DIR + "ecg nighttalk accessories lef piz.png")

image ecg nighttalkA3 sur = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back lef.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk lef non.png",
    (323, 0), NIGHTALK_DIR + "ecg nighttalk chara rnk sit sur.png",
    (469, 398), NIGHTALK_DIR + "ecg nighttalk accessories lef piz.png")

image ecg nighttalkA3 su1 = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back lef.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk lef non.png",
    (323, 0), NIGHTALK_DIR + "ecg nighttalk chara rnk sit su1.png",
    (469, 398), NIGHTALK_DIR + "ecg nighttalk accessories lef piz.png")

image ecg nighttalkA3 que = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back lef.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk lef non.png",
    (323, 0), NIGHTALK_DIR + "ecg nighttalk chara rnk sit que.png",
    (469, 398), NIGHTALK_DIR + "ecg nighttalk accessories lef piz.png")

image ecg nighttalkA3 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back lef.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk lef non.png",
    (323, 0), NIGHTALK_DIR + "ecg nighttalk chara rnk sit ser.png",
    (469, 398), NIGHTALK_DIR + "ecg nighttalk accessories lef piz.png")




image ecg nighttalkB2 nor = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rcen.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rcen.png",
    (464, 0), NIGHTALK_DIR + "ecg nighttalk chara son sit nor.png",
    (842, 490), NIGHTALK_DIR + "ecg nighttalk accessories rcen mil.png")

image ecg nighttalkB2 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rcen.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rcen.png",
    (464, 0), NIGHTALK_DIR + "ecg nighttalk chara son sit smi.png",
    (842, 490), NIGHTALK_DIR + "ecg nighttalk accessories rcen mil.png")

image ecg nighttalkB2 sm2 = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rcen.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rcen.png",
    (464, 0), NIGHTALK_DIR + "ecg nighttalk chara son sit sm2.png",
    (842, 490), NIGHTALK_DIR + "ecg nighttalk accessories rcen mil.png")

image ecg nighttalkB2 ele = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rcen.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rcen.png",
    (464, 0), NIGHTALK_DIR + "ecg nighttalk chara son sit ele.png",
    (842, 490), NIGHTALK_DIR + "ecg nighttalk accessories rcen mil.png")

image ecg nighttalkB2 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rcen.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rcen.png",
    (464, 0), NIGHTALK_DIR + "ecg nighttalk chara son sit ser.png",
    (842, 490), NIGHTALK_DIR + "ecg nighttalk accessories rcen mil.png")

image ecg nighttalkB2 que = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rcen.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rcen.png",
    (464, 0), NIGHTALK_DIR + "ecg nighttalk chara son sit que.png",
    (842, 490), NIGHTALK_DIR + "ecg nighttalk accessories rcen mil.png")

image ecg nighttalkB2 tor = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rcen.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rcen.png",
    (464, 0), NIGHTALK_DIR + "ecg nighttalk chara son sit tro.png",
    (842, 490), NIGHTALK_DIR + "ecg nighttalk accessories rcen mil.png")

image ecg nighttalkB2 men = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rcen.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rcen.png",
    (464, 0), NIGHTALK_DIR + "ecg nighttalk chara son sit men.png",
    (842, 490), NIGHTALK_DIR + "ecg nighttalk accessories rcen mil.png")

image ecg nighttalkB2 hun = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rcen.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rcen.png",
    (464, 0), NIGHTALK_DIR + "ecg nighttalk chara son sit hun.png",
    (842, 490), NIGHTALK_DIR + "ecg nighttalk accessories rcen mil.png")




image ecg nighttalkC2 nor nor = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rig.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rig non.png",
    (161, 0), NIGHTALK_DIR + "ecg nighttalk chara son sit nor.png",
    (669, 0), NIGHTALK_DIR + "ecg nighttalk chara mhr sit nor.png",
    (75, 401), NIGHTALK_DIR + "ecg nighttalk accessories rig piz.png")

image ecg nighttalkC2 smi nor = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rig.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rig non.png",
    (161, 0), NIGHTALK_DIR + "ecg nighttalk chara son sit smi.png",
    (669, 0), NIGHTALK_DIR + "ecg nighttalk chara mhr sit nor.png",
    (75, 401), NIGHTALK_DIR + "ecg nighttalk accessories rig piz.png")

image ecg nighttalkC2 nor tro = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rig.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rig non.png",
    (161, 0), NIGHTALK_DIR + "ecg nighttalk chara son sit nor.png",
    (669, 0), NIGHTALK_DIR + "ecg nighttalk chara mhr sit tro.png",
    (75, 401), NIGHTALK_DIR + "ecg nighttalk accessories rig piz.png")

image ecg nighttalkC2 que smi = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rig.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rig non.png",
    (161, 0), NIGHTALK_DIR + "ecg nighttalk chara son sit que.png",
    (669, 0), NIGHTALK_DIR + "ecg nighttalk chara mhr sit smi.png",
    (75, 401), NIGHTALK_DIR + "ecg nighttalk accessories rig piz.png")

image ecg nighttalkC2 smi smi = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rig.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rig non.png",
    (161, 0), NIGHTALK_DIR + "ecg nighttalk chara son sit smi.png",
    (669, 0), NIGHTALK_DIR + "ecg nighttalk chara mhr sit smi.png",
    (75, 401), NIGHTALK_DIR + "ecg nighttalk accessories rig piz.png")

image ecg nighttalkC2 que nor = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rig.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rig non.png",
    (161, 0), NIGHTALK_DIR + "ecg nighttalk chara son sit que.png",
    (669, 0), NIGHTALK_DIR + "ecg nighttalk chara mhr sit nor.png",
    (75, 401), NIGHTALK_DIR + "ecg nighttalk accessories rig piz.png")

image ecg nighttalkC2 ele nor = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rig.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rig non.png",
    (161, 0), NIGHTALK_DIR + "ecg nighttalk chara son sit ele.png",
    (669, 0), NIGHTALK_DIR + "ecg nighttalk chara mhr sit nor.png",
    (75, 401), NIGHTALK_DIR + "ecg nighttalk accessories rig piz.png")




image ecg nighttalkD2 nor = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rcen.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rcen.png",
    (443, 0), NIGHTALK_DIR + "ecg nighttalk chara mhr sit nor.png",
    (838, 591), NIGHTALK_DIR + "ecg nighttalk accessories rcen cof02.png")

image ecg nighttalkD2 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rcen.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rcen.png",
    (443, 0), NIGHTALK_DIR + "ecg nighttalk chara mhr sit smi.png",
    (838, 591), NIGHTALK_DIR + "ecg nighttalk accessories rcen cof02.png")

image ecg nighttalkD2 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rcen.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rcen.png",
    (443, 0), NIGHTALK_DIR + "ecg nighttalk chara mhr sit ser.png",
    (838, 591), NIGHTALK_DIR + "ecg nighttalk accessories rcen cof02.png")

image ecg nighttalkD2 sad = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rcen.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rcen.png",
    (443, 0), NIGHTALK_DIR + "ecg nighttalk chara mhr sit sad.png",
    (838, 591), NIGHTALK_DIR + "ecg nighttalk accessories rcen cof02.png")

image ecg nighttalkD2 tro = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rcen.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rcen.png",
    (443, 0), NIGHTALK_DIR + "ecg nighttalk chara mhr sit tro.png",
    (838, 591), NIGHTALK_DIR + "ecg nighttalk accessories rcen cof02.png")




image ecg nighttalkO2 glo = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rcen.png",
    
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rcen.png",
    
    (370, 0), NIGHTALK_DIR + "ecg nighttalk chara ode sit glo.png",
    
    (165, 590), NIGHTALK_DIR + "ecg nighttalk accessories rcen cof.png")

image ecg nighttalkO2 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rcen.png",
    
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rcen.png",
    
    (370, 0), NIGHTALK_DIR + "ecg nighttalk chara ode sit ser.png",
    
    (165, 590), NIGHTALK_DIR + "ecg nighttalk accessories rcen cof.png")

image ecg nighttalkO2 puc = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rcen.png",
    
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rcen.png",
    
    (370, 0), NIGHTALK_DIR + "ecg nighttalk chara ode sit puc.png",
    
    (165, 590), NIGHTALK_DIR + "ecg nighttalk accessories rcen cof.png")




image ecg nighttalkN2 sur = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back lef.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk lef non.png",
    (323, 0), NIGHTALK_DIR + "ecg nighttalk chara rnkmos sit sur.png",
    
    
    (314, 593), NIGHTALK_DIR + "ecg nighttalk accessories lef cof.png")

image ecg nighttalkN2 que = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back lef.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk lef non.png",
    (323, 0), NIGHTALK_DIR + "ecg nighttalk chara rnkmos sit que.png",
    (314, 593), NIGHTALK_DIR + "ecg nighttalk accessories lef cof.png")

image ecg nighttalkN2 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back lef.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk lef non.png",
    (323, 0), NIGHTALK_DIR + "ecg nighttalk chara rnkmos sit ser.png",
    (314, 593), NIGHTALK_DIR + "ecg nighttalk accessories lef cof.png")

image ecg nighttalkN2 cla = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back lef.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk lef non.png",
    (323, 0), NIGHTALK_DIR + "ecg nighttalk chara rnkmos sit cla.png",
    (314, 593), NIGHTALK_DIR + "ecg nighttalk accessories lef cof.png")




image ecg nighttalkT1 anx = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rcen.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rcen.png",
    (440, 0), NIGHTALK_DIR + "ecg nighttalk chara nom05 sit anx.png")

image ecg nighttalkT1 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rcen.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rcen.png",
    (440, 0), NIGHTALK_DIR + "ecg nighttalk chara nom05 sit smi.png")

image ecg nighttalkT1 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rcen.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rcen.png",
    (440, 0), NIGHTALK_DIR + "ecg nighttalk chara nom05 sit ser.png")

image ecg nighttalkT1 tro = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rcen.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rcen.png",
    (440, 0), NIGHTALK_DIR + "ecg nighttalk chara nom05 sit tro.png")

image ecg nighttalkT1 uwa = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rcen.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rcen.png",
    (440, 0), NIGHTALK_DIR + "ecg nighttalk chara nom05 sit uwa.png")




image ecg nighttalkS1 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back lef.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk lef non.png",
    (323, 0), NIGHTALK_DIR + "ecg nighttalk chara rnk03 sit ser.png")

image ecg nighttalkS1 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back lef.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk lef non.png",
    (323, 0), NIGHTALK_DIR + "ecg nighttalk chara rnk03 sit smi.png")

image ecg nighttalkS1 sur = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back lef.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk lef non.png",
    (323, 0), NIGHTALK_DIR + "ecg nighttalk chara rnk03 sit sur.png")

image ecg nighttalkS1 que = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back lef.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk lef non.png",
    (323, 0), NIGHTALK_DIR + "ecg nighttalk chara rnk03 sit que.png")

image ecg nighttalkS1 nor = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back lef.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk lef non.png",
    (323, 0), NIGHTALK_DIR + "ecg nighttalk chara rnk03 sit nor.png")




image ecg nighttalkU1 nor = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rcen.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rcen.png",
    (440, 0), NIGHTALK_DIR + "ecg nighttalk chara nom06 sit nor.png")

image ecg nighttalkU1 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back rcen.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk rcen.png",
    (440, 0), NIGHTALK_DIR + "ecg nighttalk chara nom06 sit smi.png")




image ecg nighttalkR1 smi smi = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back lef02.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk lef02 non.png",
    (94, 0), NIGHTALK_DIR + "ecg nighttalk chara rnk04 sit smi.png",
    (643, 0), NIGHTALK_DIR + "ecg nighttalk chara mhr04 sit smi.png")

image ecg nighttalkR1 ser nor = LiveComposite(SCREEN_SIZE,
    (0, 0), NIGHTALK_DIR + "ecg nighttalk back lef02.png",
    (0, 467), NIGHTALK_DIR + "ecg nighttalk desk lef02 non.png",
    (94, 0), NIGHTALK_DIR + "ecg nighttalk chara rnk04 sit ser.png",
    (643, 0), NIGHTALK_DIR + "ecg nighttalk chara mhr04 sit nor.png")







image ecg raintalkA2 sur = LiveComposite(SCREEN_SIZE,
    (0, 0), RAINTALK_DIR + "ecg raintalk back lef.png",
    (0, 467), RAINTALK_DIR + "ecg raintalk desk lef non.png",
    (323, 0), RAINTALK_DIR + "ecg raintalk chara rnkmos sit sur.png",
    (314, 593), RAINTALK_DIR + "ecg raintalk accessories lef cof.png")

image ecg raintalkA2 sad = LiveComposite(SCREEN_SIZE,
    (0, 0), RAINTALK_DIR + "ecg raintalk back lef.png",
    (0, 467), RAINTALK_DIR + "ecg raintalk desk lef non.png",
    (323, 0), RAINTALK_DIR + "ecg raintalk chara rnkmos sit sad.png",
    (314, 593), RAINTALK_DIR + "ecg raintalk accessories lef cof.png")

image ecg raintalkA2 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), RAINTALK_DIR + "ecg raintalk back lef.png",
    (0, 467), RAINTALK_DIR + "ecg raintalk desk lef non.png",
    (323, 0), RAINTALK_DIR + "ecg raintalk chara rnkmos sit ser.png",
    (314, 593), RAINTALK_DIR + "ecg raintalk accessories lef cof.png")

image ecg raintalkA2 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), RAINTALK_DIR + "ecg raintalk back lef.png",
    (0, 467), RAINTALK_DIR + "ecg raintalk desk lef non.png",
    (323, 0), RAINTALK_DIR + "ecg raintalk chara rnkmos sit smi.png",
    (314, 593), RAINTALK_DIR + "ecg raintalk accessories lef cof.png")




image ecg raintalkB2 smi = LiveComposite(SCREEN_SIZE,
    (0, 0), RAINTALK_DIR + "ecg raintalk back rig.png",
    (0, 467), RAINTALK_DIR + "ecg raintalk desk rcen non.png",
    (483, 0), RAINTALK_DIR + "ecg raintalk chara mao sit smi.png",
    (815, 626), RAINTALK_DIR + "ecg raintalk accessories rcen cof.png")

image ecg raintalkB2 tro = LiveComposite(SCREEN_SIZE,
    (0, 0), RAINTALK_DIR + "ecg raintalk back rig.png",
    (0, 467), RAINTALK_DIR + "ecg raintalk desk rcen non.png",
    (483, 0), RAINTALK_DIR + "ecg raintalk chara mao sit tro.png",
    (815, 626), RAINTALK_DIR + "ecg raintalk accessories rcen cof.png")

image ecg raintalkB2 ser = LiveComposite(SCREEN_SIZE,
    (0, 0), RAINTALK_DIR + "ecg raintalk back rig.png",
    (0, 467), RAINTALK_DIR + "ecg raintalk desk rcen non.png",
    (483, 0), RAINTALK_DIR + "ecg raintalk chara mao sit ser.png",
    (815, 626), RAINTALK_DIR + "ecg raintalk accessories rcen cof.png")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
