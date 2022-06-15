# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
init:
    #===========캐릭터=============
    define b = Character("블루헨", color="#c8ffc8", image = "bluehen")
    define r = Character("리히터", color="#24FCFF", image = "richter")
    define e = Character("에테르세이지", color="#DD7EFF", image = "ether")
    define d = Character("둠브링어", color = "#7112FF", image = "doom")
    define db = Character("데이브레이커", color = "#ABF200", image = "db")
    define c = Character("코크", color = "#FFBB00", image = "c")
    define ba = Character("깡패들", color = "#000000", image = "bad")
    define ra = Character("라디언트소울", color="#FFB2D9", image = "radiant")
    define n = Character("니샤", color="#002266", image = "nisha")
    define v = Character("비천", color="#FFBB00", image = "vi")
    #===========이미지=============
    #배경
    image bg street_day = "거리_아침.png"
    image bg street_night = "거리_노을.png"
    image bg park = "공원.png"
    image bg park_night = "공원밤.png"
    image bg backstreet1 = "뒷골목깊은곳.png"
    image bg backstreet2 = "뒷골목얕은곳.png"
    image bg room = "방 안.png"
    image bg room_night = "방 안_밤.png"
    image bg fountain_day = "분수대_낮.png"
    image bg fountain_night = "분수대_밤.png"
    image bg office_day = "사무실_낮.png"
    image bg office_night = "사무실_노을.png"
    image bg market = "시장.png"
    image bg policeoffice = "경찰서.png"
    image bg river = "이스마엘강.png"
    image bg river_night = "이스마엘강밤.png"
    image bg gameover = "gameover.png"
    image bg gameset = "평범엔딩.png"
    image black = "black.png"
    image white = "white.png"
    image bg school = "2일학교.png"
    image bg school_third = "3일학교.png"
    image bg school_1 = "본관.png"
    image bg school_2 = "온실.png"
    image bg school_3 = "별관.png"
    image bg school_4 = "운동장.png"
    image bg school_5 = "기숙사.png"
    image bg school_6 = "강당.png"
    image bg school_7 = "귀신의집.png"
    image bg school_night = "학교밤.png"
    image bg market_night = "시장밤.png"
    image bg school_2_night = "온실밤.png"
    image bg mansion = "저택.png"
    image bg raso = "라소방.png"

    image bg edra = "엔딩_라소.png"
    image bg eddo = "엔딩_둠브.png"
    image bg edco = "엔딩_코크.png"
    image bg edri = "엔딩_리히터.png"

    #재판
    image bg lawcourt = "재판장1.png"
    image bg lawcourt2 = "재판끝.png"
    image bg bluehenlaw = "재판블루헨기본.png"
    image bg bluehenlaw1 = "재판블루헨찡그림.png"
    image bg bluehenlaw2 = "재판블루헨흰털.png"
    image bg bluehenlaw3 = "재판블루헨방울.png"
    image bg teacherlaw = "재판선생.png"
    image bg teacherlaw2 = "재판선생흰털.png"
    image bg vilaw = "재판비천.png"
    image bg claw = "재판코크.png" # 당황
    image bg claw1 = "재판코크1.png" # 웃는거
    image bg judge = "재판재판장.png"
    image bg judge2 = "재판무죄.png"
    image bg judge3 = "재판유죄.png"

    #잡
    image paper = "paper.png"
    image carrotc = "당근.png" #c붙어잇습니다제발잘해주세
    image fur = "땡털.png"
    image tu = "튜튜2.png"
    image bell = "땡털방울.png"
    image blood = "피.png"
    #캐릭터

    #리히터
    image richter normal = "리히터_보통.png"
    image richter angry = "리히터_눈감음.png"
    image richter say = "리히터_대화.png"
    image richter wink = "리히터_웃음.png"
    image richter ask = "리히터_놀람.png"

    #블루헨
    image bluehen normal = "블루헨_미소.png"
    image bluehen say = "블루헨_대화.png"
    image bluehen angry= "블루헨_한심.png"
    image bluehen wink = "블루헨_미소2.png"
    image bluehen ask = "블루헨_놀람.png"
    image bluehen angryy = "블루헨_찡그림.png"

    #에세
    image ether normal = "에세_기본.png"
    image ether say = "에세_대화.png"
    image ether angry= "에세_어이.png" #대충어이없는표정인데앵그리로함
    image ether wink = "에세_윙크.png"
    image ether ask = "에세_의문.png"

    #둠브
    image doom black = "애드_블랙.png"
    image doom normal = "애드_기본.png"
    image doom angry = "애드_화남.png"
    image doom say = "애드_왜눈감노.png" #둠브는 말하는걸 눈감는걸로하겟습니다
    image doom wink = "애드_쑥쓰.png"
    image doom ask = "애드_당황.png"
    image doom smile = "애드_비웃음.png"
    image doom askask = "애드_매우당황.png"
    #데브
    image db normal = "데브_땡글.png"

    #코크
    image c normal = "코크_미소.png"
    image c say = "코크_대화.png"
    image c angry= "코크_놀람.png"
    image c wink = "코크_당황.png"
    image c ask = "코크_의문.png"
    image c winkk = "코크_볼.png"

    #라디언트소울
    image radiant normal = "라소_기본.png"
    image radiant say = "라소_대화.png"
    image radiant angry = "라소_당황.png" #화나지않았지만당황하는겁니다
    image radiant wink = "라소_정박.png"
    image radiant ask = "라소_걱정.png"
    image radiant cry = "라소_울먹.png"
    #라디언트소울오른쪽
    image radiant normalr = "라소_기본_반전.png"
    image radiant sayr = "라소_대화_반전.png"
    image radiant angryr = "라소_당황_반전.png" #화나지않았지만당황하는겁니다
    image radiant winkr = "라소_정박_반전.png"
    image radiant askr = "라소_걱정_반전.png"
    image radiant cryr = "라소_울먹_반전.png"

    #니샤오른쪽
    image nisha black = "니샤_실루엣.png"
    image nisha normalr = "니샤_기본.png"
    image nisha sayr = "니샤_대화.png"
    image nisha askr = "니샤_얹짢.png"
    #니샤
    image nisha normal = "니샤_기본_반전.png"
    image nisha say = "니샤_대화_반전.png"
    image nisha ask = "니샤_얹짢_반전.png"

    #잡
    image vii = "비천.png"
    image docsol = "doc.png"
    image bad = "깡패_땡글.png"
    image bad1 = "플로_땡글.png"
    image bad2 = "가게주인_땡글.png"
    image bad3 = "학생_땡글.png"
    image bad4 = "경비원_땡글.png"
    image bad5 = "어쌔신_땡글.png"
    image bad6 = "어쌔신땡글2.png"
    image bad7 = "사회자땡글.png"
    image black1 = "black1.png"
    image black2 = "black2.png"
    #일러
    image utac = "일러_코크1.png"
    image ildo = "일러_둠브.png"
    image ilra = "일러_라소.png"
    #===========호감도=============
    # 리히터 호감도
    $ Richter_point = 0
    # 둠브링어 호감도
    $ doom_point = 0
    # 라디언트소울 호감도
    $ Radiant_point = 0
    # 코크 호감도
    $ c_point = 0
    #==========분기==================
    $ doc = 0 # 0일때는 독솔로기 안주운거
    $ police = 0 # 0일때는 경찰서에 안가본거
    $ dname = 0 # 0일때는 둠브이름모름
    $ request = 0 # 첫째날 의뢰 거절 = 0 , 수락 = 1

    #첫째날 분기
    $ fone = 0 # 분수대 분기 0 = 안간거 1 = 간거
    $ ftwo = 0 # 공원 분기
    $ fthree = 0
    $ ffour = 0
    $ ffive = 0
    $ fsix = 0

    $ one = 0 # 분수대 분기 0 = 안간거 1 = 간거
    $ two = 0 # 공원 분기
    $ three = 0
    $ four = 0
    $ five = 0
    $ six = 0
    $ count = 0 # 문제 한번에 정답 = 0 , 1이상은 아닌거
    $ carrot = 0 # 당근 0은 안가져간거 1은 가져간거

    # 3일차 분기
    $ sone = 0 # 본관 분기 0 = 안간거 1 = 간거
    $ stwo = 0 # 별관 분기
    $ sthree = 0
    $ sfour = 0
    $ ans = 0 # 0은 틀린거 1은 맞은거

    #============Shake 함수=================
    python:
        import math
        dissolve2 = Dissolve(2)
        dissolve4 = Dissolve(4)
        class Shaker(object):
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x
                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor

                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)

            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)
    #
#
transform rotation:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate -300
    linear 1 rotate 360
label start:
    stop music fadeout 1.0
    #==============================첫째날================================
    $ doc = 0 # 0일때는 독솔로기 안주운거
    $ police = 0 # 0일때는 경찰서에 안가본거
    $ dname = 0 # 0일때는 둠브이름모름
    $ request = 0 # 첫째날 의뢰 거절 = 0 , 수락 = 1

    #첫째날 분기
    $ fone = 0 # 분수대 분기 0 = 안간거 1 = 간거
    $ ftwo = 0 # 공원 분기
    $ fthree = 0
    $ ffour = 0
    $ ffive = 0
    $ fsix = 0

    $ one = 0 # 분수대 분기 0 = 안간거 1 = 간거
    $ two = 0 # 공원 분기
    $ three = 0
    $ four = 0
    $ five = 0
    $ six = 0
    $ count = 0 # 문제 한번에 정답 = 0 , 1이상은 아닌거
    $ carrot = 0 # 당근 0은 안가져간거 1은 가져간거

    # 3일차 분기
    $ sone = 0 # 본관 분기 0 = 안간거 1 = 간거
    $ stwo = 0 # 별관 분기
    $ sthree = 0
    $ sfour = 0
    $ ans = 0 # 0은 틀린거 1은 맞은거
    #암전
    "... ... 눈이 부셔요."
    "왜 이렇게 머리가 아플까요?"
    scene bg room with fade
    show richter normal with fade #기본표정 ???(리히터)
    play music "audio/도입.ogg"
    '???' "이제 일어났나요, 블루헨."
    '???' "일어났으면 씻고 와요."

    "어? 이사람은..."
    $ renpy.block_rollback()
    #선택지 1
    menu:
        "알겠어요. 갔다올게요.":
                '???' "이상하게 오늘따라 말을 잘 듣네요. 불길하군요."
                $ Richter_point = Richter_point + 1
        "귀찮아요. 세숫물 좀 받아다 주면 안 되나요?":
                show richter angry with dissolve
                '???' "건방지기 짝이 없네요. 너의 일은 스스로 하도록 하세요."
                "쳇..."
    $ renpy.block_rollback()
    "대충 씻고 나오니 아까 전의 그 사람이 보인다."
    "이 사람은 얼마 전에 내 탐정 사무소에 조수로 취직한, 리히터라고 하는 사람이었지."
    "솔직히 그가 온 뒤로 일주일에 한번 들어올까 말까였던 일거리가 거의 매일 생기고 있다."
    "내 사무실의 경제생활이 많이 나아졌다고 해야 할까."
    "왜 이런 작은 사무실에 리히터씨 같은 엘리트가 취직한 지 모르겠지만, 나로서는 다행이다."
    show richter normal with dissolve
    r "... 오늘도 오후 1시에 기상했군요. 도대체 어제 뭘 하다 잔 거죠?"
    r "지금은 도착한 의뢰서가 없어요."
    r "안에만 있지 말고 밖에 바람이라도 좀 쐬고 오는 게 낫겠군요."

    "그렇게까지 말한다면 어쩔 수 없이 밖에 나갔다 와야겠는걸..."
    "대충 주위를 둘러보다 오자."
    scene bg street_day with dissolve
    stop music fadeout 1.0
    play music "audio/거리.ogg"
    show bluehen normal #기본표정 블루헨
    b "날씨가 좋네요. 어딜 가볼까요?"
    hide bluehen normal with dissolve
    $ renpy.block_rollback()
    #선택지2
    while True:
        scene bg street_day with dissolve
        menu:
            "분수대":
                $ renpy.block_rollback()
                scene bg fountain_day with dissolve
                "이 분수대에 동전을 던지면 소원이 이루어진다고 한다."
            #이쪽도 첨간거 두번째간거 해주면 좋을것같음===============================
            "경찰서":
                $ renpy.block_rollback()
                $ fone = fone + 1
                if fone == 1 : #처음 방문 했을때
                    scene bg policeoffice with dissolve
                    show ether say at right with dissolve #말하는표정 에테르세이지
                    e "어? 또 무슨 일이야 탐정씨. 사건이라도 터졌어?"
                    show bluehen normal at left with dissolve#눈감고웃는표정 블루헨
                    b "하하, 경찰씨는 꼭 내가 사건을 몰고 다니는 것처럼 말하네요?"
                    e "그야... 아니다. 미안, 난 지금 좀 바빠서. 저 녀석을 취조해야 해. 다음에 보자."
                    hide ether say with dissolve
                    hide bluehen normal with dissolve
                    "그녀가 가리킨 곳엔 껄렁거리는 남자가 짜장면을 먹으며 앉아있었다."
                    show doom black #실루엣 ??? (둠브링어)
                    $ police = police + 1
                    '???' "아앙?! 뭘 봐! 눈깔 돌려."
                    hide doom black with dissolve
                    show doom black at left with dissolve
                    show ether angry at right with dissolve#화내는표정 에테르세이지
                    e "시끄러워, 이 깡패!" with Shake((0, 0, 0, 0), 1.0, dist=30)
                    '???' "아악! 뭐 하는 거야, 이 애송이가! 이몸의 머리를 치다니, 제정신이냐!"
                    "... 여기에 더 있어봤자 기분만 나빠질 것 같다."
                    hide doom black with dissolve
                    hide ether angry with dissolve
                else :
                    $ renpy.block_rollback()
                    scene bg policeoffice with dissolve
                    "그들은 아직도 싸우는 중이다."
                    "더 있어봤자 기분만 나빠질 것 같다. 돌아가자."
            #이쪽도 첨간거 두번째간거 해주면 좋을것같음===============================
            "공원" :
                $ renpy.block_rollback()
                $ ftwo = ftwo + 1
                if ftwo == 1 : #처음 방문 했을때
                    scene bg park with dissolve
                    "햇볕이 내리쬐고 있다."
                    "마음이 절로 들뜨는 기분인걸."
                    "풀밭에 서 있자 발 밑에 무언가가 굴러왔다."
                    $ renpy.block_rollback()
                    menu:
                        "줍는다":
                            $ renpy.block_rollback()
                            show docsol at rotation with moveinleft
                            "뭐지? 이상한 걸 주웠다."
                            $ doc = 1 # 독솔로긩주움
                            hide docsol with dissolve
                            play sound "audio/GetItem_Unique.wav"
                            "[독솔로기]를 획득했다."
                        "줍지 않는다":
                            $ renpy.block_rollback()
                            "빨리 사무실로 돌아가도록 하자."
                else :
                    $ renpy.block_rollback()
                    "빨리 사무실로 돌아가도록 하자."
            "뒷골목":
                stop music fadeout 1.0
                play music "audio/뒷골목.ogg"
                $ renpy.block_rollback()
                scene bg backstreet2 with dissolve
                "아무도 없다. 대낮인데도 어두컴컴하다."
                $ renpy.block_rollback()
                with Shake((0, 0, 0, 0), 1.0, dist=30)
                $ renpy.block_rollback()
                "윽! 뭐지."
                $ renpy.block_rollback()
                stop music fadeout 1.0
                play sound "audio/게임오버.ogg"
                scene bg gameover with dissolve2
                $ renpy.block_rollback()
                $ renpy.pause(4.0)
                $ renpy.block_rollback()
                $ renpy.full_restart()
                #게임오버댐
            "시장":
                $ renpy.block_rollback()
                scene bg market with dissolve
                "사람이 많은 곳에 오면 항상 기분이 좋아진다."
            "학교":
                $ renpy.block_rollback()
                stop music fadeout 1.0
                play music "audio/학교.ogg"
                scene bg school with dissolve #학교
                "수업 중인 듯 오가는 사람은 아무도 없다."
                stop music fadeout 1.0
                play music "audio/거리.ogg"
            "이스마엘 강":
                stop music fadeout 1.0
                play music "audio/이스마엘강.ogg"
                $ renpy.block_rollback()
                scene bg river with dissolve
                "이 강에만 오면 항상 기분이 이상해진다."
                "나도 모르게 신을 찾아야 할 것 같은 느낌이다."
                stop music fadeout 1.0
                play music "audio/거리.ogg"
            "탐정 사무소":
                stop music fadeout 1.0
                play music "audio/보통.ogg"
                $ renpy.block_rollback()
                jump next
    label next :
        $ renpy.block_rollback()
        scene bg room with dissolve
        show richter normal with dissolve
        r "네가 나갔다 오는 동안 의뢰서가 도착했어요."
        r "한번 읽어보도록 하세요."

        "나는 리히터가 건네는 종이를 받았다."
        #말하는표정 리히터
        show richter say with dissolve
        r "뒷골목은 위험한 곳이니 신중히 생각하도록 하세요."
        "심부름 하기?"
        "이 정도면 쉽게 할 수 있을 것 같다."
        hide richter say with dissolve
        $ renpy.block_rollback()
        menu:
            "의뢰를 수락한다":
                $ request = 1
                "좋은 예감이 드는군. 어디 한번 가볼까?"
                show richter say with dissolve #말하는표정 리히터
                r "다녀오세요."
                hide richter say with dissolve
                "서류 전달이라... 장소는 뒷골목이군."
                #(뒷골목 화면 강제 전환)
                $ renpy.block_rollback()
                scene bg backstreet2 with dissolve
                stop music fadeout 1.0
                play music "audio/뒷골목.ogg"
                $ renpy.pause(2.0)
                $ renpy.block_rollback()
                if police == 1: #둠브를 경찰서에서 만났다면
                    $ renpy.block_rollback()
                    with Shake((0, 0, 0, 0), 1.0, dist=30)
                    show doom normal at right with dissolve #기본표정 ???(둠브)
                    $ doom_point = doom_point + 1 #둠 호감도 1
                    '???' "어어?! 네 녀석은 아까 경찰서에 왔던 그..."
                    "불쾌한 인물과 마주했다."
                    "신경 쓰지 말고 의뢰를 완수하러 가도록 하자."
                    '???' "이봐, 잠깐 기다려."
                    show doom smile at right with dissolve #비웃는표정 ???(둠브)
                    '???' "이렇게 만난 것도 인연인데, 술이나 한잔 사지그래?"
                    show bluehen angry at left with dissolve #블루헨 정색표정
                    $ renpy.block_rollback()
                    #선택지3 (결과는 같음)
                    menu :
                        "싫은데요, 깡패 씨?" :
                            $ renpy.block_rollback()
                            b "싫은데요, 깡패 씨?"
                            show doom angry at right with dissolve #소리 지르는 표정 ???(둠브)
                            '???' "뭐라고 이 자식?! 사람 보고 깡패라니!"
                            d "내 이름은 애드다! 잘 기억해 둬."
                            $ dname = 1
                            show bluehen say at left with dissolve #눈감고웃는표정 블루헨
                            b "볼일이 없으면 어서 비키도록 해요. 날이 점점 어두워지는데
                            객사하지 않으려면 집에 빨리 들어가야 하지 않겠어요? 난 바쁘답니다. 그럼 이만."
                            d "뭐야! 이봐, 야! 내 말 아직 안 끝났다고!"
                            $ renpy.block_rollback()
                            hide doom say with dissolve
                            hide bluehen normal with dissolve
                        "내가 왜 그래야 하는지 모르겠네요. 비켜요 깡패 씨.":
                            $ renpy.block_rollback()
                            b "내가 왜 그래야 하는지 모르겠네요. 비켜요 깡패 씨."
                            show doom angry at right with dissolve #소리 지르는 표정 ???(둠브)
                            '???' "뭐라고 이 자식?! 사람보고 깡패라니!"
                            d "내 이름은 둠브링어다! 잘 기억해 둬."
                            $ dname = 1
                            show bluehen say at left with dissolve #눈감고웃는표정 블루헨
                            b "볼일이 없으면 어서 비키도록 해요. 날이 점점 어두워지는데
                            객사 하지 않으려면 집에 빨리 들어가야하지 않겠어요? 난 바쁘답니다. 그럼 이만."
                            d "뭐야! 이봐, 야! 내 말 아직 안끝났다고!"
                            $ renpy.block_rollback()
                            hide doom angry with dissolve
                            hide bluehen normal with dissolve
                else: # 둠브 안만났다면
                    $ renpy.block_rollback()
                    show doom normal at right with dissolve #기본표정 ???(둠브)
                    '???' "네 녀석은 뭐냐?"
                    '???' "오늘은 내 기분이 안 좋으니까, 여길 조용히 지나갈 거란 생각은 버려라."
                    $ renpy.pause(2.0)
                    "시끄럽고 경박한 자이군."
                    "신경 쓰지 말고 의뢰를 완수하러 가도록 하자."
                    show doom angry at right with dissolve #소리 지르는 표정 ???(둠브)
                    '???' "뭐야! 이봐, 야! 내 말 아직 안 끝났다고!"
                    hide doom angry with dissolve
                    hide bluehen normal with dissolve
                $ renpy.block_rollback()
                "빠른 걸음으로 그곳을 벗어나자 시끄러운 소리가 점점 멀어졌다."
                scene bg backstreet1 with dissolve #으슥한 뒷골목 화면 강제전환
                "똑똑"
                show bluehen normal at left with dissolve #기본표정 블루헨
                b "어서 문 열어요. 엘더가 22번지의 에코라는 인간이 네게 보낸 서류에요."
                show bad1 at right with dissolve #실루엣 ??? (플로)
                '???' "오옷, 고마워! 너 진짜 친절하구나?"
                '???' "하핫! 잘 가!"
                hide bluehen normal with dissolve
                hide bad1 with dissolve
                with dissolve2
                "서류를 무사히 전달했다."
                "사무실로 돌아가려는데 누군가 내 어깨를 붙잡았다."
                $ renpy.block_rollback()
                if dname == 0 : #둠브 이름을 안봤을때
                    show doom smile at right with dissolve #비웃는표정 ???(둠브)
                    '???' "아하, 너 탐정이었군. 나도 네녀석에게 의뢰나 하나 할까 하는데, 어때. 할 생각 있나?"
                    show bluehen normal at left with dissolve #기본표정 블루헨
                    b "의뢰는 사무실에 내 조수를 통해 전달하도록 해요."
                    b "물론 받을지 말지는 의뢰 내용을 들어본 다음 생각해 보도록 할게요."
                    show doom normal at right with dissolve #기본표정 ???(둠브)
                    '???' "아앙? 그럼 지금 같이 사무실로 가면 되겠네. 앞장서라 탐정."
                    b "뭐, 알겠어요. 당신 같은 손님이라도 받아서 나쁠 것은 없죠."
                    b "하지만 사무실에서 행패 부리는 순간 바로 쫓아낼 거예요?"
                    show doom angry at right with dissolve #소리지르는표정 ???(둠브)
                    '???' "누, 누가 행패를 부린다고 그래?!"
                    '???' "빨리 앞장서기나 해!"
                else : #둠브 이름을 봤을때
                    $ renpy.block_rollback()
                    show doom smile at right with dissolve #비웃는표정 둠브
                    d "아하, 너 탐정이었군. 나도 네녀석에게 의뢰나 하나 할까 하는데, 어때. 할 생각 있나?"
                    show bluehen normal at left with dissolve #기본표정 블루헨
                    b "의뢰는 사무실에 내 조수를 통해 전달하도록 해요."
                    b "물론 받을지 말지는 의뢰 내용을 들어본 다음 생각해 보도록 할게요."
                    show doom normal at right with dissolve #기본표정 둠브
                    d "아앙? 그럼 지금 같이 사무실로 가면 되겠네. 앞장서라 탐정."
                    b "뭐, 알겠어요. 당신 같은 손님이라도 받아서 나쁠 것은 없죠."
                    b "하지만 사무실에서 행패 부리는 순간 바로 쫓아낼 거예요?"
                    show doom angry at right with dissolve #소리지르는표정 표정 둠브
                    d "누, 누가 행패를 부린다고 그래?!"
                    d "빨리 앞장서기나 해!"
                $ renpy.block_rollback()
                hide bluehen normal with dissolve
                hide doom angry with dissolve
                "시끄러운 예비 의뢰인과 함께 걸으니 골목길에 있던 인간 무리들이 힐끗대며 시선을 보내는 것 같다."
                "착각이 아니었는지 인간 무리는 예비 의뢰인에게 가까이 다가와 말을 걸었다."
                show bad at right with dissolve #실루엣 뒷골목 깡패들
                ba "하하, 둠브링어. 무슨 배짱으로 여기까지 왔지?"
                ba "네놈이 오늘 경찰서에서 우리 아지트를 분 거지?"
                ba "그래놓고 여기까지 제 발로 찾아오다니. 목숨이 두 개인가? 아니면 죽고 싶어 환장했던가."
                show doom smile at left with dissolve #비웃는표정 둠브
                d "하, 내가 왜 그딴 걸 경찰에게 말했다고 생각하지?"
                d "뭔가 착각하는 모양인데, 그런 쓰레기 정보는 뇌에 담아둘 필요조차 느끼지 않아."
                ba "이자식! 시치미를 떼시겠다..."
                ba "오늘 박살을 내버리겠어!!!"
                with Shake((0, 0, 0, 0), 1.0, dist=30)

                hide bad normal with dissolve
                hide doom normal with dissolve
                "서로 치고받고 싸우는 게 마치 동물의 왕국 같군요."
                "이만 사무실로 가고 싶지만, 예비 의뢰인을 버려두고 가면 또 잔소리를 듣겠죠."
                "어느 한쪽이 쓰러질 때까지 기다려야겠네요."
                with dissolve2
                show doom normal at right with dissolve #다친 표정 둠브
                d "하아, 하아..."
                d "뭐야, 아직 안 갔어?"
                d "... 바로 도망쳤어야지. 몸도 비실비실하게 생겨선 애송이가."
                show bluehen normal at left with dissolve #기본표정 블루헨
                b "많이 다친 것 같네요? 싸움 실력은 별로인가 봐요."
                d "크윽, 이 자식이...? 시비걸 거면 가라."
                b "어쩔 수 없군요. 따라와요."
                scene bg room_night with dissolve2 #사무실 안 강제전환
                stop music fadeout 1.0
                play music "audio/보통.ogg"
                show bluehen normal at left with dissolve #기본표정 블루헨
                b "너무 늦게 와서 내 조수는 가버렸네요."
                b "이게 다 깡패씨 때문이에요."
                show doom ask at right with dissolve #당황하는 표정 둠브
                d "하아? 깡패가 아니라 애드라고!"
                b "깡패씨 이름은 관심 없어요."
                b "뭐해요? 어서 쇼파에 앉도록 해요. 대충 약이라도 발라야 의뢰서를 쓸 것 아니에요?"
                show doom wink at right with dissolve #당황볼빨사표정 둠브링어
                d "뭐?! 윽... 알겠어."
                $ renpy.block_rollback()
                menu :
                    "약을 대충 바른다":
                        $ renpy.block_rollback()
                        $ doom_point = doom_point + 2 # 둠 호감도 2
                        "약을 대충 발라주었다."
                    "사심을 담아 실수인 척 상처부위를 세게 누른다":
                        $ renpy.block_rollback()
                        show doom angry at right with dissolve #다친소리지르는표정 둠브링어
                        d "아악! 이게 미쳤나!!"
                        show bluehen say at left with dissolve #눈감고웃는표정 블루헨
                        b "하하, 미안해요? 실수했네요. 이젠 실수하지 않을게요."
                #(선택지 관계없이 둠브링어에게 약을 발라주는 블루헨 일러스트 뜸)
                scene ildo with dissolve2
                $ renpy.pause(2.0)
                scene bg room_night with dissolve2
                #(일러스트 클릭 시 다시 사무실 안으로 장면전환) 스탠딩지우고 씬으로하면될듯
                $ renpy.block_rollback()
                show doom wink at right with dissolve #치료된볼빨간기본표정 둠브링어
                d "... 너 의외로 좋은 놈이구나."
                d "그, 그... 난 이만 가봐야겠다?"
                d "뭐... 다음에 의뢰할 게 있으면 찾아올...지도..."
                d "어쨌든 가보겠다고!!"
                "(쾅!)" with Shake((0, 0, 0, 0), 1.0, dist=10)
                hide doom wink with dissolve
                "문이 세차게 닫겼다."
                "얼마나 세게 닫았으면 문고리가 그만 떨어져 나가버렸다."
                "아아, 정말... 어이가 없는 인간이네요. 한숨밖에 나오지 않아요."
                "사무실의 보안을 위해서 오늘도 여기서 자야 하겠네요."
                scene black with fade
                $ renpy.pause(1.0)
                $ renpy.block_rollback()
                #이때 까매지는 화면 넣으면 좋을듯
                stop music fadeout 1.0
                #====암전=====
            "의뢰를 수락하지 않는다":
                $ Richter_point = Richter_point + 2
                "그래도 오늘은 조금 쉬고 싶다. 바깥 날씨가 좋던데 리히터에게 나가자고 할까."
                show bluehen say at left with dissolve #눈감고웃는표정 블루헨
                b "리히터, 오늘 날씨가 좋던데 공원에 나가보는 건 어때요?"
                b "가끔씩은 휴식도 필요하대요."
                show richter angry at right with dissolve#눈감은표정 리히터
                r "항상 놀면서 말은 잘하는군요."
                r "... 그래요. 나가도록 합시다."
                hide bluehen say with dissolve
                hide richter angry with dissolve

                scene bg park with dissolve#공원
                stop music fadeout 1.0
                play music "audio/거리.ogg"
                show bluehen normal at left with dissolve#기본표정 블루헨
                b "날씨가 너무 좋은걸요."
                b "이렇게 기분전환 하니 리히터도 좋죠?"
                show richter normal at right with dissolve #기본표정 리히터
                r "... ..."
                hide bluehen normal with dissolve
                hide richter normal with dissolve
                # ========독솔로기 주웠을때=========
                if doc == 1 :
                    show db normal at right #실루엣 ??? (체육복 데이브레이커)
                    '???' "어머! 손에 들고 계시는 건 혹시...?"
                    show bluehen normal at left with dissolve
                    show docsol with dissolve2
                    hide docsol with dissolve
                    b "하하, 이것 말인가요? 아까 공원에서 주웠어요. 네 건가요? 줄게요."
                    '???' "맞아요! 제 공이에요. 주워주셔서 감사해요. 잃어버린 줄로만 알았지 뭐예요."
                    '???' "후후후, 혹시 심심하시면 공놀이하실래요? 혼자서는 도저히 재미가 없어서 말이죠."
                    b "그래요. 할 것도 없었는데 마침 잘 됐네요."
                    "이상한 엘프와 공놀이를 잠시 했다."
                    hide db normal with dissolve
                    hide bluehen normal with dissolve

                    scene bg room with dissolve2 #사무실 안 전환
                    show bluehen normal at left with dissolve#기본표정 블루헨
                    b "오늘 정말 재미있었어요. 안 그런가요?"
                    show richter normal at right with dissolve#기본표정 리히터
                    r "글쎄요."
                    r "나는 이만 가야겠어요. 또 사무실에서 잠들지 말고 곱게 집에 가도록 하세요."
                    hide richter normal with dissolve
                    "잔소리가 심하군."
                    hide bluehen normal with dissolve
                    show bluehen say with dissolve#눈감고 웃는표정 블루헨
                    b "알겠어요. 내일 봐요, 리히터!"
                    hide bluehen say with dissolve
                    "리히터가 나가자마자 담요를 덮고 소파에 누웠다."
                    "나는 눕자마자 잠에 빠져들었다..."
                    scene black with fade
                    $ renpy.pause(1.0)
                    stop music fadeout 1.0
                    #이때 까매지는 화면 넣으면 좋을듯
                else :
                    stop music fadeout 1.0
                    scene black with fade
                    $ renpy.pause(1.0)
                    #이때 까매지는 화면 넣으면 좋을듯
    #==============================첫째날끝================================


    #==============================둘째날================================
    scene bg room with dissolve2 #사무실 안 전환
    "오늘도 날이 밝았네요."
    "슬슬 일어나 볼까요?"
    play music "audio/보통.ogg"
    if request == 0 : #첫째날 의뢰 거절 했을 시 -리히터 호감도 2
        $ Richter_point = Richter_point + 2
        show richter normal at right with dissolve#기본표정 리히터
        r "일어났나요."
        r "사무실에서 잠들지 말라고 했을 텐데요."
        "그의 표정이 조금 난처해 보인다."
        "... 착각일까?"
    else : #첫째날 의뢰 수락 했을 시
        show richter say at right with dissolve#말하는표정 리히터
        r "블루헨. 대체 어제 뭘 한 거죠?"
        r "사무실의 문고리가 부서졌어요."
        show bluehen normal at left with dissolve#기본표정 블루헨
        b "아, 문고리요?"
        b "난 잘 모르겠어요. 이상하다, 이게 왜 떨어져 있지?"
        r "..."
        r "수리기사를 불러야겠군요."
        hide richter say with dissolve
        hide bluehen normal with dissolve

    $ renpy.pause(2.0)
    show richter say with dissolve#말하는표정 리히터
    r "네가 자고 있는 동안 의뢰인이 방문했어요."
    r "지금 응접실에 있을 겁니다. 아, 이건 네 앞으로 온 편지예요."
    r "보낸 사람은 적혀있지 않네요."
    "나는 리히터가 건네는 종이를 받았다."
    #(편지1장그림)(큰 독백 혹은 종이에 글자가 쓰인 일러스트)
    "나는 편지를 뜯었다."
    hide richter say with dissolve
    show paper at truecenter with dissolve

    "... ?"
    "편지를 읽는데 앞에 있던 리히터가 편지를 휙 빼앗아갔다."
    #기본표정 리히터
    show richter normal at right with dissolve#기본표정 리히터
    r "스팸 편지군요."
    r "이건 내가 처리할게요."
    hide paper
    "리히터는 찡그린 표정으로 편지를 찢어 쓰레기통에 버렸다."
    "무슨 편지였을까?"
    hide richter normal with dissolve
    show bluehen normal at left with dissolve#기본표정 블루헨
    b "하하, 일단 의뢰인을 만나러 가 볼까요."
    "응접실의 문을 열자 의뢰인이 보였다."
    b "반가워요 의뢰인씨. 여긴 무슨 일로 찾아온거죠?"
    show radiant normalr at right with dissolve#기본표정 라디언트소울
    ra "후힛! 안녕!"
    ra "라비는... 라비의 친구를 찾으러 왔어!"
    b "누군가 실종된 건가요? 그렇군요. 네 친구가 실종된 당시의 정황을 기억나는 대로 자세히 말해봐요."
    show radiant askr at right with dissolve#시무룩한표정 라디언트소울
    ra "니샤는... 언제나 나랑 함께 있었어."
    ra "쭉 함께였는데... 니샤가 오늘 아침 갑자기 사라졌어."
    b "저런, 안타깝네요."
    b "경찰서에 실종 신고는 해 봤나요?"
    ra "그게... 경찰서란 곳을 찾아갔는데 라비의 친구를 찾아주지 않겠대."
    ra "라비, 너무 슬펐는데 누군가가 여기를 찾아가 보라 했어!"
    b "그 인간들이 나빴네요. 그런 일은 경찰이 하지 않으면 누가 하는 거죠?"
    b "어쨌든 잘 왔어요. 내가 의뢰인씨의 친구를 찾아주도록 할게요."
    b "의뢰인씨의 친구에 대해 알려줘요."
    show radiant normalr at right with dissolve#기본표정 라디언트소울
    ra "후힛! 니샤는... 니샤야!"
    ra "니샤는 라비를 제일 좋아해!"
    ra "라비도 니샤를 제일 좋아해!"
    b "... 그게 다 인가요?"
    ra "뭐가 더 필요한거야? 우움... 라비 잘 모르겠어."
    b "일단 밖으로 나가보죠."
    b "기억나는 정보가 있으면 바로바로 말해봐요."
    ra "응! 알겠어!"
    hide radiant normal with dissolve
    hide bluehen normal with dissolve

    scene bg street_day with dissolve2 #(거리 화면)
    stop music fadeout 1.0
    play music "audio/거리.ogg"
    if request == 1 : #첫째날 의뢰 수락 했을 시
        show doom ask at right with dissolve #볼빨간기본표정 둠브링어
        d "어? 안... 안... 크흠. 어디가냐?"
        show bluehen normal at left with dissolve#기본표정 블루헨
        b "아아... 너는"
        menu :
            "깡패씨군요?" :
                $ doom_point = doom_point + 1 # 둠 호감도 1
                b "깡패씨군요?"
            "깡패씨군요?" :
                $ doom_point = doom_point + 1 # 둠 호감도 1
                b "깡패씨군요?"
            "우리 사무실 문고리를 부수고 간 깡패씨군요?" :
                $ doom_point = doom_point + 1 # 둠 호감도 1
                b "우리 사무실 문고리를 부수고 간 깡패씨군요?"
        show doom angry at right with dissolve #소리지르는표정 둠브링어
        d "뭐야?! 이게 기껏 아는 척 해줬더니... 건방지게!"
        b "그래서 무슨 일인가요? 용건이 없으면 비켜줬으면 좋겠네요. 나는 일을 하러 가야 돼서 바쁘거든요."
        show doom normal at right with dissolve #기본표정 둠브링어
        d "크윽... 그, 그래. 나도 네 녀석에게 의뢰를 맡겨야 할 테니 오늘은 네놈의 일 처리를 한번 보도록 하지."
        show doom smile at right with dissolve #비웃는표정 둠브링어
        d "시원찮으면 장사 접을 생각해야 할 거야."
        hide doom smile with dissolve
        hide bluehen normal with dissolve
        "하아... 귀찮게 됐네요."
    else : #첫째날 의뢰 거절 시
        with Shake((0, 0, 0, 0), 1.0, dist=20)
        show doom normal at left with dissolve #기본표정 둠브링어
        d "크윽!"
        d "사람을 쳐 놓고 시치미를 뚝 떼고 지나가시겠다?"
        d "가뜩이나 짜증 나 죽겠는데..."
        show radiant normalr at right with dissolve #시무룩한표정 라디언트소울
        ra "앗! 미안! 라비가 친거야?"
        ra "라비의 실수야..."
        d "... 뭐, 그렇게까지 빈다면야 어쩔 수 없지."
        d "원래 정신적 피해 보상으로 3억 ED를 내야 하는데, 사과를 했으니 특별히 반으로 깎아주마."
        ra "우움, 하지만 라비는 지금 바쁜걸?"
        ra "친구를 찾으러 가야 해서, 이따가 줄게!"
        show doom smile at left with dissolve #비웃는표정 둠브링어
        d "하, 내가 네 녀석의 뭘 믿고?"
        d "앞에선 그렇게 말을 하고선 슬그머니 도망가려는 놈들 많이 봤지."
        d "네 녀석이 정신적 피해 보상비를 갚을 때까지 계속 옆에서 감시해야겠다."
        d "공교롭게도 나는 시간이 많거든. 크크크큭..."
        "완전 깡패나 다름 없는 인간이네요. 귀찮게 된 것 같군요."
        hide doom angry with dissolve
        hide radiant normal with dissolve
    $ one = 0 # 분수대 분기 0 = 안간거 1 = 간거
    $ two = 0 # 공원 분기
    $ three = 0
    $ four = 0
    $ five = 0
    $ six = 0
    #선택지3
    while True:
        scene bg street_day with dissolve
        menu:
            "분수대":
                $ one = one + 1
                if one == 1 : #처음 방문 했을때
                    scene bg fountain_day with dissolve
                    show radiant normalr at right with dissolve #기본표정 라디언트소울
                    ra "와! 정말 예뻐. 근데 저기 떨어진 반짝반짝한 것들은 뭐야?"
                    show bluehen normal at left with dissolve #기본표정 블루헨
                    b "저 분수대에 동전을 던지면 소원이 이루어 진다는 속설을 믿는 자들이 던진 동전이에요."
                    ra "동전...? 라비는 동전이 없는데. 어떡하지...?"
                    hide bluehen normal with dissolve
                    show doom normal at left with dissolve #기본표정 둠브링어
                    d "왜 날 보냐, 애송이?"
                    d "... ..."
                    d "하... 자, 여기 있다. 됐냐?"
                    ra "후힛!"
                    ra "고마워!"
                    show radiant askr at right with dissolve #시무룩한표정 라디언트소울
                    ra "니샤를 찾게 해주세요..."
                    hide doom normal with dissolve
                    hide radiant ask with dissolve
                    "의뢰인은 눈을 감고 소원을 빌었다."
                    "인간은 정말 저런 걸 믿는군요. 신기하네요."
                    if one>=1:
                        if two>=1:
                            if three>=1:
                                if four>=1:
                                    if five>=1:
                                        if six>=1:
                                            jump next6
                else :
                    scene bg fountain_day with dissolve
                    "이 분수대는 하루에 두번씩 특별한 분수쇼를 연다고 한다."
            "공원" :
                $ two = two + 1 # 첫 방문은 two가 1이고 두번째 이상은 2이상이 됩니다
                if two == 1: # 처음 방문 했을때
                    scene bg park with dissolve
                    show radiant normalr at right with dissolve #기본표정 라디언트소울
                    ra "와, 풀이다!"
                    ra "그러고보니 니샤가 저번에 이런 말을 했어."
                    ra "나는 10년간 라비를 찾아 헤맸어."
                    ra "네 나이의 딱 3분의 2배의 시간을 썼지."
                    ra "너무 늦어서 미안해. 하지만 괜찮아, 이렇게 다시 만났으니까."
                    ra "후힛, 니샤가 그랬는데 니샤는 라비 나이보다 2배 더 많대!"
                    show doom normal at left with dissolve #기본표정 둠브링어
                    d "도대체 네녀석 친구는 뭐 하는 놈이냐..."
                    hide doom normal with dissolve
                    hide radiant normal with dissolve
                    show bluehen normal with dissolve #기본표정 블루헨
                    b "그 말에 따르면 네 친구의 나이는..."
                    # 문제 1
                    while True:
                        $ answer = renpy.input('<나이 기입>') #로그를 보게 시키면됩니다
                        if (answer == "30"):
                            jump next2
                        else:
                            $ count = count + 1
                            "아닌 것 같은데? 다시 한번 생각해보자."
                    # next2 : 정답 맞췄을때
                    label next2 :
                        if count == 0: # 한번에 맞췄을때
                            $ Radiant_point = Radiant_point + 1 #라소 호감도 1올라감
                        hide bluehen normal with dissolve
                        show bluehen normal at left with dissolve #기본표정 블루헨
                        b "의뢰인씨 친구의 나이는 30살이군요?"
                        show radiant normalr at right with dissolve #기본표정 라디언트소울
                        ra "라비는 잘 모르겠어!"
                        b "그래요. 다른 장소로 가 봅시다."
                        hide bluehen normal with dissolve
                        hide radiant normal with dissolve
                        if one>=1:
                            if two>=1:
                                if three>=1:
                                    if four>=1:
                                        if five>=1:
                                            if six>=1:
                                                jump next6
                else: # 공원 재방문 시
                    scene bg park with dissolve
                    "다른 곳도 둘러보자"
            "뒷골목":
                $ three = three + 1
                scene bg backstreet2 with dissolve
                stop music fadeout 1.0
                play music "audio/뒷골목.ogg"
                show doom normal at right with dissolve #기본표정 둠브링어
                d "하, 네놈의 친구 녀석이 여기 왔다면 내 눈에 띄었겠지."
                d "분명 건방진 놈 친구니 똑같이 건방지겠지?"
                d "만났으면 내가 이미 묵사발을 내 줬을 텐데."
                d "요 일주일간은 들락거리는 짭새들 말곤 새 인물은 없었다고."
                show bluehen normal at left with dissolve #기본표정 블루헨
                b "그래요? 아무래도 여긴 없는 것 같군요. 다른 장소로 가요."
                stop music fadeout 1.0
                play music "audio/거리.ogg"
                if one>=1:
                    if two>=1:
                        if three>=1:
                            if four>=1:
                                if five>=1:
                                    if six>=1:
                                        jump next6
            "시장":
                $ four = four + 1 # 첫 방문은 two가 1이고 두번째 이상은 2이상이 됩니다
                if four == 1: # 처음 방문 했을때
                    scene bg market with dissolve
                    show radiant normalr at right with dissolve #기본표정 라디언트소울
                    ra "사람이 엄청 많아!"
                    ra "앗, 저게 뭐지?"
                    ra "라비가 제일 좋아하는 만두야!"
                    #꼬르륵소리잇으면좋겟네어케넣을까
                    show radiant askr at right with dissolve #시무룩한표정 라디언트소울
                    ra "라비, 배고파..."
                    show doom normal at left with dissolve #기본표정 둠브링어
                    d "왜 날 보냐, 애송이?"
                    d "...하, 참나. 진짜 어이가 없네. 알겠다고."
                    d "이봐, 거기 네 놈. 만두 몇 개 내놔 보시지."
                    hide radiant normal with dissolve
                    show bad2 at right with dissolve #실루엣 만두가게 사장
                    '만두가게 사장' "우리 집 만두가 정말 맛있긴 하지!"
                    '만두가게 사장' "하지만 우리 집 만두는 이 문제를 맞추는 사람들만 사 갈 수 있다고."
                    '만두가게 사장' "우리 가게엔 만두가 20개가 들어가는 찜기가 5개 있지."
                    '만두가게 사장' "이걸 봉투에 대충 반씩 나누어 담았더니 10개의 만두 봉투가 생겼어."
                    '만두가게 사장' "이때 봉투에 담은 만두 갯수의 평균이 10개가 될 확률은 몇 퍼센트일까?"
                    show doom angry at left with dissolve #소리지르는표정 둠브링어
                    hide bad2 with dissolve
                    d "이녀석이 미쳤나..."
                    d "죽고싶어?"
                    show radiant askr at right with dissolve #시무룩한표정 라디언트소울
                    ra "라비, 배가 고파서 죽을 것 같아."
                    ra "으악, 라비 죽는다!"
                    hide doom angry with dissolve
                    hide radiant ask with dissolve
                    show bluehen normal with dissolve #기본표정 블루헨
                    b "깡패 씨, 의뢰인씨가 죽으면 다 네탓이에요."
                    b "어서 의뢰인씨가 배가 고파 죽어버리기 전에 만두를 사 오세요."
                    hide bluehen normal with dissolve

                    # 문제 2
                    $ count = 0
                    while True:
                        $ answer = renpy.input('<정답 기입>') #로그를 보게 시키면됩니다
                        if (answer == "100"):
                            jump next3
                        else:
                            $ count = count + 1
                            show bad2 at right with dissolve #실루엣 만두가게 사장
                            '만두가게 사장' "다시 잘 생각해보라구."
                            show doom angry at left with dissolve #화난표정 둠브링어
                            d "크윽!" #여기화면흔들릴수도있구요보고결정
                            hide bad2 with dissolve
                            hide doom angry with dissolve
                    # next3 : 정답 맞췄을때
                    label next3 :
                        if count == 0: # 한번에 맞췄을때
                            $ Radiant_point = Radiant_point + 1 #라소 호감도 1올라감
                        show bad2 at right with dissolve #실루엣 만두가게 사장
                        '만두가게 사장' "하하, 젊은 친구가 수수께끼를 좋아하는구만!"
                        '만두가게 사장' "자, 여기 만두 한 봉지 있다네."
                        '만두가게 사장' "3만ED라고. 정말 싸지?"
                        show doom normal at left with dissolve #기본표정 둠브링어
                        d "진짜 어이가 없네..."
                        hide bad2 with dissolve
                        hide doom normal with dissolve
                        show bluehen normal with dissolve #기본표정 블루헨
                        b "자, 의뢰인씨의 배도 채웠으니 다른 장소에 가 볼까요?"
                        hide bluehen normal with dissolve
                        if one>=1:
                            if two>=1:
                                if three>=1:
                                    if four>=1:
                                        if five>=1:
                                            if six>=1:
                                                jump next6
                else :
                    scene bg market with dissolve# 시장 배경
                    show doom normal at left with dissolve #기본표정 둠브링어
                    d "... 여기를 또 둘러보고 싶진 않은데. 다른 곳으로 가지?"
            "학교":
                $ five = five + 1 # 첫 방문은 five가 1이고 두번째 이상은 2이상이 됩니다
                if five == 1: # 처음 방문 했을때
                    stop music fadeout 1.0
                    play music "audio/학교.ogg"
                    scene bg school with dissolve #학교
                    show radiant normalr at right with dissolve #기본표정 라디언트소울
                    ra "여기는 어디야?"
                    ra "다들 똑같은 옷을 입고 있어."
                    show bluehen normal at left with dissolve #기본표정 블루헨
                    b "여기는 학교라는 곳이에요."
                    b "다같이 모여서 공부를 하는 곳이죠."
                    hide radiant normal with dissolve
                    show bad4 at right with dissolve #실루엣 경비원
                    '경비원' "저기요, 여긴 아무나 마음대로 들어올 수 없는 곳이에요."
                    '경비원' "들어오시려면 문제를 풀어야 합니다."
                    b "그래요? 그럼 어디 한번 내봐요."
                    '경비원' "최고차항의 계수가 양수인 삼차함수 f(x)가 다음 조건을 만족시킨다.
                    (가) 방정식 f(x)-x=0의 서로 다른 실근의 개수는 2이다.
                    (나) 방정식 f(x)+x=0의 서로 다른 실근의 개수는 2이다.
                    f(0)=0, f'(1)=1일때, f(3)의 값은?"
                    b "이 정도는 당연히 알죠?"
                    b "깡패 씨, 대답해봐요."
                    hide bad4 with dissolve
                    show doom normal at right with dissolve #기본표정 둠브링어
                    d "무, 뭐?"
                    d "뭔데...?"
                    # 문제 3
                    $ count = 0
                    hide bluehen normal with dissolve
                    while True:
                        $ answer = renpy.input('<정답 기입>') #로그를 보게 시키면됩니다
                        if (answer == "51"):
                            jump next4
                        else:
                            $ count = count + 1
                            show bad4 at left with dissolve #실루엣 경비원
                            '경비원' "당신들은 여기 들어 올 수 없어요."
                            '경비원' "여긴 선택받은 엘리트들만 밟을 수 있는 땅이거든요."
                            '경비원' "죄송하지만 이만 나가주세요."
                            show doom angry at right with dissolve #당황한표정 둠브링어
                            d "아니, 아니아니! 이봐, 실수라고. 정답은..."
                            hide bad4 with dissolve
                            hide doom ask with dissolve
                    # next4 : 정답 맞췄을때
                    label next4 :
                        if count == 0: # 한번에 맞췄을때
                            $ Radiant_point = Radiant_point + 1 #라소 호감도 1올라감
                        hide doom normal with dissolve
                        show doom normal at left with dissolve #기본표정 둠브링어
                        show bad4 at right with dissolve #실루엣 경비원
                        '경비원' "이 학교에 들어올 최소한의 자격은 되는 것 같군요."
                        '경비원' "출입해도 좋아요. 대신, 기숙사 쪽으론 가면 안 됩니다."
                        hide bad4 with dissolve
                        hide doom normal with dissolve
                        scene bg school_1 with dissolve#(본관 화면 전환)
                        show bluehen normal at left with dissolve #기본표정 블루헨
                        b "여기가 학교라는 곳이군요."
                        b "안까지 들어온 건 처음이에요."
                        show bad3 at right with dissolve #실루엣 학생
                        '학생' "거기 외부인 분들! 제 얘기를 잠시 들어주세요."
                        '학생' "오늘 저희 반의 우산 꽂이에 우산이 3개 꽂혀 있었어요."
                        '학생' "그 우산이 세개 다 비슷하게 생겨서 언뜻 봐선 구분이 잘 안가요."
                        '학생' "우산 주인들이 이름을 확인하지 않고 우산을 무작위로 가져갔을때
                        2명만 자신의 우산을 제대로 가져갔을 확률은 몇 퍼센트 일까요?"
                        hide bad3 with dissolve
                        show doom angry at right with dissolve #소리지르는표정 둠브링어
                        d "이 애송이는 또 뭐야?!"
                        b "너무 쉬운걸요. 나는 알겠는데, 설마 깡패씨는 모르겠나요?"
                        hide bluehen angry with dissolve
                        show radiant normal at left with dissolve #기본표정 라디언트소울
                        ra "후힛! 이건 라비도 알겠어!"
                        d "이것들이...! 내가 맞춰주지. 정답은..."
                        # 문제 4
                        $ count = 0
                        hide radiant normal with dissolve
                        while True:
                            $ answer = renpy.input('<정답 기입>') #로그를 보게 시키면됩니다
                            if (answer == "0"):
                                jump next5
                            else:
                                $ count = count + 1
                                show bad3 at left with dissolve #실루엣 학생
                                '학생' "정답만큼의 지능이네요."
                                '학생' "어떻게 들어오셨죠?"
                                '학생' "역시 제가 잘못 들은 거겠죠? 다시 한번 얘기해주세요."
                                hide bad with dissolve
                        # next5 : 정답 맞췄을때
                        label next5 :
                            if count == 0: # 한번에 맞췄을때
                                $ Radiant_point = Radiant_point + 1 #라소 호감도 1올라감
                            show bad3 at left with dissolve #실루엣 학생
                            '학생' "이 정도도 못 맞추면 고개를 들고 살 수조차 없죠."
                            '학생' "그럼 이만."
                            hide bad3 with dissolve
                            show doom angry at right with dissolve #소리지르는표정 둠브링어
                            d "뭐, 뭐야?!"
                            d "다들 지금 뭐하자는 거야?"
                            show bluehen normal at left with dissolve #기본표정 블루헨
                            b "이 학교에도 의뢰인 친구 씨는 없네요."
                            b "다른 장소로 가 봅시다."
                            if one>=1:
                                if two>=1:
                                    if three>=1:
                                        if four>=1:
                                            if five>=1:
                                                if six>=1:
                                                    jump next6
                else : # 학교에 재방문했을시
                    scene bg school with dissolve #학교
                    stop music fadeout 1.0
                    play music "audio/학교.ogg"
                    "이곳엔 없는 듯 하다."
                    stop music fadeout 1.0
                    play music "audio/거리.ogg"
            "이스마엘 강":
                $ six = six + 1
                if six == 1:
                    scene bg river with dissolve
                    stop music fadeout 1.0
                    play music "audio/이스마엘강.ogg"
                    "항상 이곳에 오면 이상한 기분이 드는군."
                    "마치 내 존재 이유를 부정당하는 느낌..."
                    show radiant normal at left with dissolve #기본표정 라디언트소울
                    ra "우움, 여긴 없는 것 같아."
                    ra "도대체 니샤는 어디 있는거지...?"
                    ra "니~ 샤~!! 있으면 대답해줘!!!"
                    show doom normal at right with dissolve #기본표정 둠브링어
                    d "물에다 대고 소리 질러봤자 물귀신이 아닌 이상 나타날 리 없잖아."
                    d "딱 봐도 아무도 없구만, 괜히 왔네."
                    hide doom normal with dissolve
                    hide radiant normal with dissolve
                    stop music fadeout 1.0
                    play music "audio/거리.ogg"
                    if one>=1:
                        if two>=1:
                            if three>=1:
                                if four>=1:
                                    if five>=1:
                                        if six>=1:
                                            jump next6
    label next6:
        #선택지 전부 클릭 시 (다클릭안하면겜진행안댐)
        #(노을진 거리 화면 전환)
        scene bg street_night with dissolve
        stop music fadeout 1.0
        $ renpy.pause(1.0)
        show bluehen normal at left with dissolve #기본표정 블루헨
        play music "audio/밤거리.ogg"
        b "벌써 날이 저물었네요."
        b "이정도면 찾아볼 수 있는 곳까지 모두 가본 것 같은데, 아무래도 마을엔 없는 것 같군요."
        b "어쩌면 이미 다른 곳으로 갔을 수도 있겠네요."
        show radiant cryr at right with dissolve #시무룩한표정 라디언트소울
        ra "니샤가 날 두고...?"
        ra "그럴리가 없는데..."
        ra "니샤는 항상 내 곁에 있어준다고 했어."
        ra "라비한테 약속했단 말이야..."
        hide bluehen normal with dissolve
        show doom askask at left with dissolve #당황하는표정 둠브링어
        d "야, 야... 너 우냐...?"
        hide doom ask with dissolve
        hide radiant cryr with dissolve
        show nisha black at right with dissolve #실루엣 ??? (니샤)
        '???' "라비."
        show radiant angry at left with dissolve #놀란표정 라디언트소울
        ra "어?"
        show nisha normalr at right with dissolve #기본표정 ??? (니샤)
        '???' "라비, 어디 갔었어. 사라져서 깜짝 놀랐잖아."
        show radiant cry at left with dissolve #울먹이는표정 라디언트소울
        ra "니샤, 작은 니샤가... 작은 니샤가 사라졌어."
        n "... 그 거울이라면 여기 있어."
        n "잠시 거울을 닦으려고 가져갔었는데 사라진 줄 알았던 거야?"
        n "미안해. 미리 말하지 않은 내 탓이야."
        show radiant wink at left with dissolve #웃는표정 라디언트소울
        ra "아니야! 라비 오늘 재미있었어."
        ra "무~지무지 맛있는 만두도 먹었어!"
        show nisha askr at right with dissolve #어두운표정 니샤
        n "그래, 라비가 재미있었다니 나도 기분이 좋네."
        n "그런데 저것들은...?"
        show radiant normal at left with dissolve #놀란표정 라디언트소울
        ra "응! 오늘 라비를 도와준 아주아주 착한 사람들이야!"
        hide radiant normal with dissolve
        show doom normal at left with dissolve #기본표정 둠브링어
        d "저것들이라니! 건방진 애송이 녀석, 시비냐?"
        hide doom normal with dissolve
        if request == 0 : #첫째날 의뢰 거절 했을 시
            show radiant angry at left with dissolve #놀란표정 라디언트소울
            ra "헉! 맞다, 나... 돈 줘야 하는거 있는데... 까먹고 있었어."
            show nisha askr at right with dissolve #어두운표정 니샤
            n "라비. 돈이라니?"
            show radiant normal at left with dissolve #기본표정 라디언트소울
            ra "으응, 삐죽머리한테 돈 줘야해! 원래 3억 ED인데, 라비가 사과 했으니까 반으로 깎아 준댔어!"
            n "네가 라비를 협박한거니?"
            hide radiant normal with dissolve
            show doom angry at left with dissolve
            d "으윽...! 그게 아니고..."
            d "오히려 난 이 애송이한테 뜯기기만..."
            n "... 정말 불쾌하네."
            n "라비, 이런 것들이랑 상종하면 안돼."
            n "라비를 위해서니까. 어서 빨리 집에 가자."
            hide nisha askr with dissolve
            hide doom angry with dissolve
        else : #의뢰 수행 시
            show nisha askr at right with dissolve #어두운표정 니샤
            n "... ..."
            show nisha normalr at right with dissolve #기본표정 니샤
            n "그 거울이 그렇게 소중하다니, 조금 질투해 버릴 것 같네."
            n "후후, 이제 그만 집에 가자."
            show radiant normal at left with dissolve #기본표정 라디언트소울
            ra "응! 나중에 봐! 오늘 고마웠어!"
            hide radiant normal with dissolve
            hide nisha normalr with dissolve
            scene ilra with dissolve2
            $ renpy.pause(2.0)
            #(노을진 거리에서 블루헨과 둠브한테 손 흔드는 라소 일러스트)
        scene bg street_night with dissolve
        show bluehen normal at left with dissolve #기본표정 블루헨
        b "의뢰인씨의 친구가 거울인 줄은 몰랐네요."
        b "사실 집 안에 있었다니, 헤지호그 밑이 어둡다는 속담이 사실인가봐요."
        show doom normal at right with dissolve #기본표정 둠브링어
        d "그딴 속담은 처음 들어보는데..."
        d "하, 그렇게 찾아댔는데 거울 따위였다니. 힘빠졌어. 이만 간다."
        b "그래요. 잘 가고 다신 만나지 말아요."
        hide doom normal with dissolve
        hide bluehen normal with dissolve

        #(사무실 화면 전환)
        scene bg room_night with dissolve
        show richter normal at right with dissolve #기본표정 리히터
        stop music fadeout 1.0
        play music "audio/보통.ogg"
        r "의뢰는 잘 다녀왔나요."
        show bluehen normal at left with dissolve #기본표정 블루헨
        b "네. 그런데 의뢰인씨의 친구가 사실 거울이었지 뭐예요. 이러니 경찰서에서 받아주지 않았죠."
        r "그래서 의뢰비는 받아왔나요?"
        b "어? 흠... 어라? 리히터가 받은 거 아니었나요?"
        r "... ..."
        r "일단 그 저택으로 의뢰비를 청구 해야겠군요."
        b "저택이라면..."
        b "설마 얼마 전에 그 음산한 저택을 사들인 의문의 인간이 이번 의뢰인씨였나요?"
        r "그런 듯 합니다. 자신의 집 주소가 그곳이라고 하더군요."
        r "난 이만 퇴근해야겠어요."
        if request == 0 : #첫째날 의뢰 거절 했을 시
            r "오늘은 얌전히 집으로 가도록 하세요."
            r "멀쩡히 집도 있으면서 왜 이곳에서 자는 지 모르겠네요."
            "리히터는 한숨을 쉬곤 퇴근했다."
            "벌써 밤이군. 내일은 꼭 일찍 일어나야겠다."
        else : # 수락
            r "문고리는 수리가 다 되었으니 오늘은 집으로 가도록 하세요."
            "리히터는 언짢은 표정으로 퇴근했다."
            "벌써 밤이군. 내일은 꼭 일찍 일어나야겠다."
        scene black with fade
        $ renpy.pause(1.0)
        stop music fadeout 3.0
        #이때 까매지는 화면 넣으면 좋을듯
#========================================둘째 끝==============================================

#========================================셋째 시작============================================
    scene black with fade
    $ renpy.pause(1.0)
    #다끝나고 여기 블헨이나튜튜얼굴추가했으면좋겠다는생각이들기도하고요어려우면안해도됨
    "하하, 참 이상한 동물이군요."
    "왜 바닥에다가 자꾸 침을 뱉는 거죠?"
    "... ..."
    "저기, 흰 털 동물씨. 너 침을 너무 많이 뱉는군요."
    "이대로 갔다간 내 사무실이 침으로 가득 차버리겠어요."
    "... ..."
    "어느새 침이 허리까지..."
    "안돼..."

    scene bg room with dissolve2 #사무실 안 전환
    "헉!"
    "... ..."
    "꿈이었나..."
    show richter normal at right with dissolve
    play music "audio/보통.ogg"
    r "안색이 창백하군요, 블루헨."
    r "설마 악몽을 꾼 건가요?"
    show bluehen ask at left with dissolve
    b "으으... 머리가 너무 아파요."
    r "... ..."
    r "꿈은 어디까지나 꿈일 뿐이죠."
    r "어서 나갈 준비를 하세요. 의뢰가 들어왔습니다."
    show bluehen normal at left with dissolve
    b "그렇네요. 이런 건 금방 잊어버리는 게 낫겠어요."
    b "무슨 의뢰인가요?"
    r "학교에서 온 의뢰입니다. 자세한 건 학교로 가서 들어보세요."
    r "기다리고 있는 사람이 있을겁니다."
    r "아, 그리고 난 이번 의뢰가 끝나면 이 일을 그만두니 그리 알고 있도록 하세요."
    show bluehen ask at left with dissolve
    b "응? 진짜요?"
    show bluehen say at left with dissolve
    b "하하, 네 입에서 그만둔다는 말이 나오니 신기하네요."
    b "그래요, 좋아요. 요즘 일거리가 너무 많아져서 나도 당분간 문을 닫고 쉬려고 했거든요."
    b "그런데 왜 관두는 거예요? 뭔가 문제가 생겼나요?"
    r "... 네가 알 필요 없어요. 일단은 그렇게 알고 있으세요."
    r "지금 학교로 가면 선생이라는 자가 교문 앞에서 기다리고 있을거예요. 갔다 오세요."
    show bluehen normal at left with dissolve
    b "처음부터 금방 관둘 거라고 했었지만... 막상 간다고 하니 아쉽네요."
    b "가끔씩은 놀러 와요? 너라면 50퍼센트 싸게 해줄 생각도 있어요."
    b "그러고 보니 탁자 위의 저 당근은 뭐죠? 어제 못 보던 건데. 참 귀엽게도 생겼네요?"
    show carrotc with dissolve #(당근사진)
    r "글쎄요. 나도 못보던 것이군요. 네 건줄 알았는데, 아닌가요?"
    r "네가 가져온 게 아니라면... 내가 처리할 테니 놔두세요."
    "당근이 참 귀엽게도 생겼다. 가져가볼까?"
    menu :
        "가져간다":
            $ carrot = 1
            "가져가서 바깥에 잘 심어보자."
            play sound "audio/GetItem_Unique.wav"
            "[당근]을 획득했다."
        "가져가지 않는다":
            "역시 귀찮다. 여기에 내버려 두면 리히터가 잘 치워주겠지?"
    hide carrotc with dissolve #(당근사진)
    b "그래요, 다녀올게요!"
    #(학교 화면)
    scene bg school_third with dissolve2 #축제학교
    scene bg school_1 with dissolve2 #학교
    stop music fadeout 1.0
    play music "audio/3일학교.ogg"
    #실루엣 대머리선생님
    show bad3 at right with dissolve2 #실루엣 대머리선생님 이것도 나중에 바꾸기
    '선생님' "아이고, 안녕하십니까 탐정님. 잘 오셨습니다."
    '선생님' "저희 학교가 지금 축제 준비 중이라 어수선한데... 시끄러워도 좀 참아주세요. 허허."
    show bluehen normal at left with dissolve #기본표정 블루헨
    b "하하, 괜찮아요."
    '선생님' "다름이 아니고 저희 학교 온실을 누군가가 파헤치는 바람에..."
    '선생님' "정말이지 피해가 막심하답니다. 일단 온실로 가실까요."
    b "뭐, 그래요. 안내해봐요."
    scene bg school_2 with dissolve2 #(온실 화면)
    show bluehen ask at left with dissolve #놀란표정 블루헨
    b "이건... 뭔가요? 정말이지 대단하군요."
    show bad3 at right with dissolve2 #실루엣 대머리선생님
    '선생님' "간밤에 누가 학교 온실을 다 이 모양으로 만들어 놓는 바람에 놀라서 경찰서에도 신고했지만..."
    '선생님' "마을에 살인사건이 나서 지금 당장 조사는 불가능하다고 하더군요."
    '선생님' "더군다나 제가 아끼던 분재에 흙을 갈려고 잠시 온실에 놔뒀는데 엉망이 되어버렸어요."
    '선생님' "그것 때문에 제 머리가 반이나 빠졌지 뭡니까."
    '선생님' "곧 오후에 학교 축제가 있을 예정이라 외부인들도 오시는 마당에 정말이지 어떤 놈이...!"
    '선생님' "범인을 꼭 잡아주셨으면 합니다!"
    show bluehen normal at left with dissolve #기본표정 블루헨
    b "좋아요. 온실을 이렇게 만든 인간을 잡으면 되는 거죠? 흠... 또 다른 정보는 없나요?"
    '선생님' "아, 도와줄 학생 하나를 불렀습니다. 저기 있네요. 저 친구가 도와줄 겁니다. 진짜 착한 학생이거든요."
    hide bluehen normal with dissolve
    show c normal at left with dissolve #기본표정 코크
    c "안녕하세요, 선생님. 급한 일이 생겼다고 들었어요."
    '선생님' "이 학생은 청이라고 하는 친군데요, 학교 구석구석을 무척이나 잘 압니다."
    '선생님' "자세한 건 제가 다 얘기 해놨으니... 어이쿠, 저희 반에 빨리 가봐야 해서. 그럼 실례하겠습니다."
    hide bad3 with dissolve
    hide c with dissolve
    "대머리는 사라졌다."
    show bluehen normal at left with dissolve #기본표정 블루헨
    show c normal at right with dissolve #기본표정 코크
    show c say at right with dissolve #기본표정 코크
    c "안녕하세요 탐정님! 저는 이 학교의 수호자, 청이라고 합니다! 궁금한 게 있으면 언제든 물어봐 주세요!"
    b "하하, 캐릭터가 참 특이하네요. 그래요 수호자씨. 우리끼리 범인을 잘 잡아봐요?"
    c "네! 그럼 어디부터 둘러보실 건가요?"
    b "일단 이 곳부터 살펴보죠."
    "무참하게 짓밟힌 꽃들이 있다."
    b "이건...?"
    "구석에서 무엇인가를 발견했다."
    show fur #(흰털사진)
    $ renpy.pause(2.0)
    b "이게..뭐죠?"
    b "잘은 모르겠지만 증거가 될 수도 있겠네요"
    b "다음 장소로 가 볼까요."
    c "네!"
    $ renpy.pause(1.0)
    play sound "audio/GetItem_Unique.wav"
    "증거품 : [흰 털]을 획득했다."
    #선택지
    while True:
        scene bg school_third with dissolve
        menu :
            "온실":
                scene bg school_2 with dissolve
                #재 입장 시
                "이곳에서는 더 이상 증거를 발견할 수 없을 것 같다."
            "본관":
                $ sone = sone + 1
                if sone == 1 : #처음 방문 했을때
                    scene bg school_1 with dissolve
                    show c normal at right with dissolve #기본표정 코크
                    c "지금 학교가 축제 중이라 각 반마다 부스가 설치되어 있어요. 저희 반은 귀신의 집을 하는데, 보러 가실래요?"
                    show bluehen normal at left with dissolve #기본표정 블루헨
                    b "좋아요. 재미있겠네요. 어디 한번 가볼까요?"
                    "2-3이라 적혀있는 교실에 입장료를 내고 들어갔다."
                    stop music fadeout 0.5
                    scene bg school_7 with dissolve #귀신의집
                    show c wink at right with dissolve #놀란표정 코크 이것도보고바뀔수도
                    c "헉... 너무 어두운 것 같아요."
                    #(귀신의집 교실 배경에 어쌔신땡글이가 나타났다 사라짐)
                    scene bg school_7 with dissolve #귀신의집
                    show bad5 with easeinleft  #어쌔신땡글이로 나중에 바꿈
                    scene bg school_7 with dissolve #귀신의집
                    "저게 뭐지...? 알 수 없는 생물체다."
                    scene bg school_1 with dissolve
                    play music "audio/3일학교.ogg"
                    show c normal at right with dissolve #기본표정 코크
                    c "후! 드디어 빠져나왔네요. 괜찮으세요?"
                    show bluehen normal at left with dissolve #기본표정 블루헨
                    b "수호자씨야말로 괜찮은 건가요? 안색이 창백하네요."
                    b "그런데 아까 전 이상한 흰 생물 같은 것을 보지 못했나요?"
                    show c wink at right with dissolve #웃는표정 코크로 나중에 바뀔수도있습니다
                    c "에이, 장난치지 마세요. 저는 그런 걸 보지 못했는걸요?"
                    "흠... 설마...?"
                    b "그래요. 장난이었어요. 나름 재미있네요. 다른 곳에도 한번 가볼까요?"
                    show c normal at right with dissolve #기본표정 코크
                    c "네!"
                    if sone>=1:
                        if stwo>=1:
                            if sthree>=1:
                                if sfour>=1:
                                    jump next7
                else : #(재 입장 시)
                    scene bg school_1 with dissolve
                    "이곳에서는 더 이상 증거를 발견할 수 없을 것 같다."
            "별관":
                $ stwo = stwo + 1
                if stwo == 1 : #처음 방문 했을때
                    scene bg school_3 with dissolve
                    show c normal at right with dissolve #기본표정 코크
                    show bluehen normal at left with dissolve #기본표정 블루헨
                    c "여긴 학교 별관이에요. 저희 학교 별관에는 음악실과 미술실, 어학실과 컴퓨터실이 있어요. "
                    c "사실 고학년이 되면 별관에서 하는 수업이 없어서 잘 사용하지는 않는데..."
                    show c say at right with dissolve #웃는표정 코크
                    c "조금 부끄럽지만 저는 음악실에서 노래하는 것도 무척 좋아해서 자주 와요... 헤헤."
                    show c normal at right with dissolve #기본표정 코크
                    c "사실 오늘 5시에 강당에서 노래를 부르는데 혹시 시간이 나신다면 보러 와 주실 수 있을까요?"
                    b "그럼요. 기대할게요."
                    show c say at right with dissolve #웃는표정 코크
                    c "네! 멋진 무대를 선보이겠습니다!"
                    $ renpy.pause(1.0)
                    "저건...?"
                    "별관 복도에서 볼펜을 발견했다."
                    show c say at right with dissolve #웃는표정 코크
                    c "엇! 이건 아라 누나 것이네요."
                    c "아라 누나는 물건에 이름을 꼭 쓰시는데도 자주 잃어버려요. 가져가서 돌려드려야겠어요."
                    b "그래요."
                    $ renpy.pause(1.0)
                    play sound "audio/GetItem_Unique.wav"
                    "증거품 : [볼펜]을 획득했다."
                    if sone>=1:
                        if stwo>=1:
                            if sthree>=1:
                                if sfour>=1:
                                    jump next7
                else : #(재 입장 시)
                    scene bg school_3 with dissolve
                    "이곳에서는 더 이상 증거를 발견할 수 없을 것 같다."
            "운동장":
                $ sthree = sthree + 1
                if sthree == 1 : #처음 방문 했을때
                    scene bg school_4 with dissolve
                    "축제라 운동장 여기저기에 설치된 부스가 보인다."
                    show c angry at right with dissolve #놀란표정 코크
                    c "앗! 저건...!"
                    show bluehen normal at left with dissolve #기본표정 블루헨
                    b "응? 뭔가요?"
                    show c normal at right with dissolve #기본표정 코크
                    c "축제 때 밖에 먹을 수 없는 전설의 떡꼬치예요! 정말 맛이 뛰어나다고 해요. 저도 소문으로만 전해 들었지만요."
                    b "아하, 그래요? 그럼 한번 맛보러 가볼까요? 근데 줄이 정말 길군요."
                    c "이럴 수가... 주변 사람들도 점점 몰려들고 있어요. 일단 주문을 미리 하죠."
                    hide c normal with dissolve
                    hide bluehen normal with dissolve
                    "떡꼬치 두 개만 주세요!!!" with Shake((0, 0, 0, 0), 1.0, dist=40)
                    $ renpy.pause(1.0)
                    show bluehen ask at left with dissolve #놀란표정 블루헨
                    b "이럴 수가... 주변 사람들이 모두 기절해버렸네요."
                    show c wink at right with dissolve #당황표정 코크
                    c "앗! 저도 모르게 소리를 질러버렸네요... 죄송해요!!!"
                    show bluehen normal at left with dissolve #기본표정 블루헨
                    "쓰러진 사람들을 제치고 떡꼬치 두 개를 집었다. "
                    "장사하는 학생들도 모두 쓰러져 돈을 받을 사람이 없기에 부스 위에 대충 놓았다."
                    c "죄송해요... 정말 죄송해요!!!"
                    b "언제까지 사과할 건가요? 자, 이거 받아요. 떡꼬치예요."
                    show c normal at right with dissolve #기본표정 코크
                    c "앗... 감사합니다!"
                    "떡꼬치는 그저 그런 맛이었다. 하지만 수호자씨는 정말 감탄하며 떡꼬치를 먹었다."
                    "꼬치를 버리러 쓰레기통에 가는 길에 이상한 것을 발견했다."
                    # (방울에 흰 털이 묻어있는 사진)
                    show bell with dissolve
                    $ renpy.pause(2.0)
                    c "어...? 이건 방울? 이런 게 왜 쓰레기통에 있을까요? 앗, 방울에 털이 조금 붙어있네요."
                    b "그러고 보니 이 털, 온실에서 발견한 털과 상당히 유사하군요."
                    show c angry at right with dissolve #놀란표정 코크
                    c "엇! 그러네요!"
                    b "일단 가지고 있도록 하죠."
                    $ renpy.pause(1.0)
                    play sound "audio/GetItem_Unique.wav"
                    "증거품 : [털이 묻은 방울]을 획득했다."
                    if sone>=1:
                        if stwo>=1:
                            if sthree>=1:
                                if sfour>=1:
                                    jump next7
                else : # (재 입장 시)
                    scene bg school_4 with dissolve
                    "이곳에서는 더 이상 증거를 발견할 수 없을 것 같다."
            "기숙사":
                $ sfour = sfour + 1
                if sfour == 1 : #처음 방문 했을때
                    scene bg school_5 with dissolve
                    show c normal at right with dissolve #기본표정 코크
                    c "기숙사는 원래 외부인들은 출입 금지 구역이지만 혹시 모르니 안에는 들어가지 말고 바깥만 잠깐 둘러봐요!"
                    show bluehen normal at left with dissolve #기본표정 블루헨
                    b "그래요."
                    "기숙사 뒤편에서 방석과 밥그릇을 발견했다."
                    b "이건 뭔가요?"
                    show c wink at right with dissolve #당황표정 코크
                    c "아앗! 이건... 사실 아라 누나가 키우시는 은이라는 고양이가 있어요. 원래 키우면 안 되지만..."
                    show c say at right with dissolve #웃는표정 코크
                    c "절대 떨어질 수 없다고 몰래 바깥에서 키우고 계세요. 헤헤. 비밀이에요."
                    b "그렇군요. 알겠어요."
                    "주변을 돌다 이상한 것을 발견했다."
                    show c angry at right with dissolve #놀란표정 코크
                    c "어..? 이건 뜯겨진 꽃 무더기예요. 기숙사 뒤에 누가 이런걸..."
                    "꽃 무더기 사이에서 비녀를 발견했다."
                    c "이건...!"
                    b "혹시 아는 물건인가요?"
                    show c wink at right with dissolve #당황표정 코크
                    c "네. 아라 누나가 며칠 전에 잃어버린 비녀예요."
                    b "흠... 그렇군요. 일단 갖고 가 보도록 해요."
                    c "네..."
                    show c ask at right with dissolve #울상표정 코크
                    $ renpy.pause(1.0)
                    play sound "audio/GetItem_Unique.wav"
                    "증거품 : [비녀]를 획득했다."
                    if sone>=1:
                        if stwo>=1:
                            if sthree>=1:
                                if sfour>=1:
                                    jump next7
                else :
                    scene bg school_5 with dissolve
                    "이곳에서는 더 이상 증거를 발견할 수 없을 것 같다."
    label next7: #(전부 클릭 시)
        $ renpy.pause(1.0)
        show bluehen normal at left with dissolve #기본표정 블루헨
        b "이제 둘러볼 곳은 다 둘러본 것 같군요. 다시 온실에 가볼까요?"
        show c normal at right with dissolve #기본표정 코크
        c "네. 좋아요!"
        scene bg school_2 with dissolve #(온실 화면 전환)
        with Shake((0, 0, 0, 0), 1.0, dist=40)
        if carrot == 1: #(당근을 가져올 시)
            $ renpy.block_rollback()
            show c angry at right with dissolve #당황표정 코크
            $ renpy.block_rollback()
            stop music fadeout 1.0
            "거대한 무언가가 나에게로 돌진했다."
            $ renpy.block_rollback()
            scene white
            show tu with zoomin
            $ renpy.block_rollback()
            "쿵!!!" with hpunch
            $ renpy.block_rollback()
            stop music fadeout 1.0
            play sound "audio/게임오버.ogg"
            scene bg gameover with dissolve2
            $ renpy.block_rollback()
            $ renpy.pause(4.0)
            $ renpy.block_rollback()
            $ renpy.full_restart()
        else :
            show c wink at right with dissolve #당황표정 코크
            c "아앗! 진정해. 이 녀석!"
            "거대한 무언가가 수호자씨에게로 돌진했다."
            "수호자씨는 땅에 놓인 긴 막대기로 그것을 간단하게 막았다."
            c "튜튜, 당번이 밥을 주지 않은 거야? 왜 이렇게 화가 나 있어?"
            "이런 난폭한 동물을 풀어놓고 사육하고 있다니. 이 학교도 알만하군. 빨리 처리하고 여길 떠나야겠어."
            show c normal at right with dissolve #기본표정 코크
            c "착하지? 내가 밥 줄게. 따라와, 튜튜."
            "기분 나쁜 흰 털 동물은 그대로 수호자를 따라갔다."
            hide c normal with dissolve
            "수호자씨가 밥을 주고 돌아오는 동안 잠시 생각에 빠졌다."
            "모든 증거품이 하나의 답을 가리키는 것을 느꼈다."
            show bluehen normal at left with dissolve #기본표정 블루헨
            show c normal at right with dissolve #기본표정 코크
            b "수호자씨, 당신도 느꼈죠?"
            c "... 네."
            b "아무래도 범인을 찾은 것 같네요. 모두를 불러오죠."

            #(갑분재판)
            #(검사 대머리선생 변호사 블루헨 조수 코크 판사 땡글이 재판화면)
            $ count = 0
            $ renpy.pause(2.0)
            scene bg lawcourt with dissolve
            $ renpy.pause(1.0)
            $ renpy.block_rollback()
            stop music fadeout 1.0
            play music "audio/재판시작.mp3"
            "4월 1일 오후 4시 학급 재판소 제1법정"
            scene bg teacherlaw with dissolve
            '선생님' "범인을 찾았다니 다행입니다. 그럼 어디 한번 들어볼까요... 그 범인이라는 것이 누군지."
            scene bg bluehenlaw with dissolve
            b "일단 재판장씨. 증인 소환을 신청할게요. 아라 한이라는 학생씨를 불러줄래요?"
            scene bg judge with dissolve
            '재판관' "인정합니다."
            scene bg vilaw with dissolve
            $ renpy.pause(1.0)
            v "소... 소녀의 힘이 필요하신가요...?"
            $ renpy.pause(1.0)
            scene bg bluehenlaw with dissolve
            scene bg bluehenlaw2 with dissolve2 #블루헨 흰털
            b "우리는 온실 구석에서 이런 걸 발견했어요."
            scene bg teacherlaw2 with dissolve #선생흰털
            '선생님' "이건..."
            scene bg bluehenlaw with dissolve
            b "아마도 온실을 망가뜨린 이는"
            $ renpy.block_rollback()
            while True:
                menu :
                    "사람이다.":
                        $ ans = 0
                    "짐승이다.":
                        $ ans = 1
                        jump next8
                    "식물이다.":
                        $ ans = 0
                if ans == 0 :
                    $ renpy.block_rollback()
                    $ count = count + 1
                    scene bg teacherlaw with dissolve
                    '선생님' "네...?"
                    scene bg claw with dissolve
                    c "그건... 아닌 것 같아요."
                    scene bg bluehenlaw with dissolve
            label next8 :
                $ renpy.block_rollback()
                if (count == 0):
                    $ c_point = c_point + 1
                scene bg bluehenlaw with dissolve
                b "그래요. 이 털은 온실을 망가뜨린 게 짐승이라는 것을 뜻하고 있는 거예요."
                scene bg teacherlaw with dissolve
                '선생님' "네?! 그럼 화단을 망가뜨린 놈이 짐승이란 말입니까..."
                scene bg bluehenlaw with dissolve
                b "그래요. 그것도 아주 포악한 야생성을 가진 짐승이죠."
                scene bg bluehenlaw3 with dissolve2 #블루헨방울
                b "그리고 운동장 구석에 있는 쓰레기통에서도 똑같은 털이 붙어있는 방울을 발견했어요."
                b "이건 그 짐승이 쓰레기통에 갔다는 걸 뜻하죠. 그 짐승은..."
                $ count = 0
                $ renpy.block_rollback()
                while True:
                    $ ans = 0
                    menu :
                        "너무 굶주려서 쓰레기통을 뒤지러 갔다.":
                            $ ans = 0
                        "무언가를 버리러 갔다.":
                            $ ans = 0
                        "무언가를 찾으러 갔다.":
                            $ ans = 1
                            jump next9
                    if ans == 0 :
                        $ renpy.block_rollback()
                        $ count = count + 1
                        scene bg teacherlaw with dissolve
                        '선생님' "네...?"
                        scene bg claw with dissolve
                        c "그건... 아닌 것 같아요."
                        scene bg bluehenlaw with dissolve
                label next9 :
                    $ renpy.block_rollback()
                    if (count == 0):
                        $ c_point = c_point + 1
                    scene bg bluehenlaw with dissolve
                    b "바로 무언가를 찾으러 간 거죠. 무엇을 찾으러 갔을까요? 내 생각엔..."
                    $ count = 0
                    $ renpy.block_rollback()
                    while True:
                        $ ans = 0
                        menu :
                            "비녀":
                                $ ans = 1
                                jump next10
                            "볼펜":
                                $ ans = 0
                            "꽃":
                                $ ans = 0
                        if ans == 0 :
                            $ renpy.block_rollback()
                            $ count = count + 1
                            scene bg teacherlaw with dissolve
                            '선생님' "네...?"
                            scene bg claw with dissolve
                            c "그건... 아닌 것 같아요."
                            scene bg bluehenlaw with dissolve
                    label next10 :
                        $ renpy.block_rollback()
                        if (count == 0):
                            $ c_point = c_point + 1
                        scene bg bluehenlaw with dissolve
                        b "그래요. 바로 학생씨의 비녀를 찾으러 간 거예요."
                        scene bg teacherlaw with dissolve
                        '선생님' "뭐야?! 증거 있어, 변호사?"
                        scene bg bluehenlaw with dissolve
                        b "증거는 당연히 있죠. 이걸 보세요."
                        b "이 비녀는 우리가 조사하면서 기숙사 뒤편에서 발견한 학생씨의 비녀예요."
                        b "그런데 온실에서 꺾인 꽃 무더기 속에 파묻혀있었죠."
                        scene bg vilaw with dissolve
                        v "아앗! 그것은... 소녀의 비녀가 맞사옵니다!"
                        scene bg teacherlaw with dissolve
                        '선생님' "이건...! 하지만 그것만으로는 비녀를 찾으러 갔다고 할 수 없을 텐데? 그렇게 따지면 오히려 아라 학생이 범인일 가능성이 더 높지 않나?"
                        scene bg bluehenlaw with dissolve
                        b "이걸 봐요. 우리가 별관에서 발견한 학생씨의 볼펜이에요."
                        b "하지만 별관은 갈 일이 잘 없는 3학년의 물건이 어째서 별관에 있었을까요? 그 이유는..."
                        $ count = 0
                        $ renpy.block_rollback()
                        while True:
                            $ ans = 0
                            menu :
                                "아라가 범인이다.":
                                    $ ans = 0
                                "범인은 아라와 관련이 없다.":
                                    $ ans = 0
                                "누군가가 아라의 물건을 자꾸 훔친다.":
                                    $ ans = 1
                                    jump next11
                            if ans == 0 :
                                $ renpy.block_rollback()
                                $ count = count + 1
                                scene bg teacherlaw with dissolve
                                '선생님' "네...?"
                                scene bg claw with dissolve
                                c "그건... 아닌 것 같아요."
                                scene bg bluehenlaw with dissolve
                        label next11 :
                            $ renpy.block_rollback()
                            if (count == 0):
                                $ c_point = c_point + 1
                            scene bg bluehenlaw with dissolve
                            stop music fadeout 3.0
                            b "그래요."
                            play music "audio/재판추리.mp3"
                            b "학생씨의 물건을 자꾸 훔쳐 가는 사람이 있다는 겁니다."
                            scene bg teacherlaw with dissolve
                            '선생님' "헉!"
                            scene bg vilaw with dissolve
                            v "헉!!!"
                            scene bg bluehenlaw1 with dissolve
                            b "그것도 한두 번이 아니라 여러 번을 훔친 것 같군요."
                            scene bg bluehenlaw with dissolve
                            b "지금까지 물건을 계속 잃어버렸던 게 과연 학생씨만의 탓일까요?"
                            b "그리고 학생씨는 물건을 자주 잃어버려서 모든 물건에 이름을 쓴다고 들었어요."
                            b "하지만 이 비녀에는 이름이 쓰여있지 않죠. 왜일까요?"
                            b "항상 머리에 착용하는 것에다 굳이 이름을 쓸 이유가 없기 때문이죠."
                            b "그러니, 누군가가 고의로 학생씨의 방에 침입해 이 비녀를 훔쳐 갔다는 소리입니다."
                            b "어떤가요, 학생씨?"
                            scene bg vilaw with dissolve
                            v "아앗! 그러고 보니 제가 가장 아끼는 비녀를 기숙사 침대맡에 놓고 잤는데 없어졌사옵니다..."
                            scene bg bluehenlaw with dissolve
                            b "그래요. 학생씨의 비녀를 훔친 누군가는 그걸 쓰레기통에 버려버린 거죠."
                            b "하지만 누군가는 몰랐던 겁니다."
                            b "그 비녀를 찾는 짐승이 있단걸..."
                            b "그 짐승씨는 비녀를 갖고 가 기숙사에 숨겼던 거예요."
                            b "하지만 증거품인 방울을 쓰레기통에 떨어뜨렸죠. 범인이 화단을 망친 이유는..."
                            $ count = 0
                            $ renpy.block_rollback()
                            while True:
                                $ ans = 0
                                menu :
                                    "튜튜가 싫어서 그랬다.":
                                        $ ans = 0
                                    "비녀를 숨기기 위해 그랬다.":
                                        $ ans = 1
                                        jump next12
                                    "너무 배고파서 꽃을 먹었다.":
                                        $ ans = 0
                                if ans == 0 :
                                    $ renpy.block_rollback()
                                    $ count = count + 1
                                    scene bg teacherlaw with dissolve
                                    '선생님' "네...?"
                                    scene bg claw with dissolve
                                    c "그건... 아닌 것 같아요."
                                    scene bg bluehenlaw with dissolve
                            label next12 :
                                $ renpy.block_rollback()
                                if (count == 0):
                                    $ c_point = c_point + 1
                                scene bg bluehenlaw with dissolve
                                b "그래요. 화단을 망친 이유는 화단의 꽃을 뜯어 이 비녀를 숨기려고 했기 때문이에요."
                                b "학생씨의 물건을 훔치는 자의 눈을 피해 학생씨에게 전달하기 위해서죠."
                                scene bg teacherlaw with dissolve
                                '선생님' "그럼... 범인은..."
                                scene bg bluehenlaw1 with dissolve
                                $ count = 0
                                $ renpy.block_rollback()
                                while True:
                                    $ ans = 0
                                    menu :
                                        "튜튜":
                                            $ ans = 0
                                        "은":
                                            $ ans = 1
                                            jump next13
                                        "땡글이":
                                            $ ans = 0
                                        "내가 어떻게 아냐?":
                                            $ ans = 0
                                    #(2번 틀릴시)
                                    if count == 1 :
                                        stop music fadeout 1.0
                                        play music "audio/재판시작.mp3"
                                        $ renpy.block_rollback()
                                        scene bg claw with dissolve
                                        c "점점..재판이 이상해지는것 같아요."
                                        $ renpy.block_rollback()
                                        scene bg judge with dissolve
                                        '재판관' "재판이고 뭐고 당신은 그냥 엘소드나 하시는게 나을것 같군요."
                                        $ renpy.block_rollback()
                                        '재판관' "이 재판은..."
                                        $ renpy.block_rollback()
                                        $ renpy.pause(1.0)
                                        scene bg judge3 with dissolve2
                                        $ renpy.block_rollback()
                                        $ renpy.pause(2.0)
                                        $ renpy.block_rollback()
                                        with Shake((0, 0, 0, 0), 1.0, dist=30)
                                        $ renpy.block_rollback()
                                        stop music fadeout 1.0
                                        play sound "audio/게임오버.ogg"
                                        scene bg gameover with dissolve2
                                        $ renpy.block_rollback()
                                        $ renpy.pause(4.0)
                                        $ renpy.block_rollback()
                                        $ renpy.full_restart()
                                        #게임오버댐
                                    if ans == 0 :
                                        stop music fadeout 3.0
                                        play music "audio/재판선택지.mp3"
                                        $ renpy.block_rollback()
                                        $ count = count + 1
                                        scene bg teacherlaw with dissolve
                                        '선생님' "네...?"
                                        scene bg claw with dissolve
                                        c "그건... 아닌 것 같아요."
                                        scene bg bluehenlaw1 with dissolve
                                label next13 :
                                    stop music fadeout 3.0
                                    play music "audio/재판선택지2.mp3"
                                    $ renpy.block_rollback()
                                    if (count == 0):
                                        $ c_point = c_point + 1
                                    scene bg bluehenlaw with dissolve
                                    b "화단을 망친 범인은 바로, 학생씨의 고양이 은이에요."
                                    scene bg vilaw with dissolve
                                    v "아앗!! 그 이름은 어찌 아시는지...! 몰래 모시고 있었는데...!"
                                    scene bg claw1 with dissolve
                                    c "하핫. 미안해요, 아라 누나."
                                    scene bg vilaw with dissolve
                                    v "청님... 정말 너무하시옵니다!"
                                    stop music fadeout 1.0
                                    scene bg judge with dissolve
                                    '재판관' "그럼 판결을 내리도록 하겠습니다. 판결은..."
                                    $ renpy.pause(1.0)
                                    scene bg judge2 with dissolve2
                                    $ renpy.pause(2.0)
                                    jump next14
    label next14 :
        stop music fadeout 1.0
        play music "audio/재판후.mp3"
        $ renpy.block_rollback()
        scene bg lawcourt2 with dissolve2
        "재판이 무사히 끝났다."
        show c normal at right with dissolve #기본표정 코크
        c "역시 대단하세요!"
        show bluehen normal at left with dissolve #기본표정 블루헨
        b "이 정도는 가뿐하죠. 자, 그럼 온실을 망친 범인에게 데려다주겠나요, 학생씨?"
        scene bg lawcourt2 with dissolve2
        show vii at left with dissolve #비천
        v "네, 알겠사옵니다. 이것도 저의 업보이니... 달게 받겠어요."
        show bad3 at right with dissolve #선생님
        '선생님' "아라 이 녀석 학교에서 몰래 고양이를 키우다니... 설마 기숙사에 들여보낸 건 아니겠지?"
        # (기숙사화면전환)
        stop music fadeout 1.0
        play music "audio/학교.ogg"
        scene bg school_5 with dissolve2
        show vii at left with dissolve #비천
        v "기숙사 뒤편 수풀에 은님을 위한 거주공간을 만들었사와요. 저, 절대 기숙사 안까지 오신적은 없사옵니다!"
        show bad3 at right with dissolve #선생님
        '선생님' "하긴. 들키면 그 깐깐한 데니프 선생에게 붙잡혀 5시간 설교를 들을지도 모르는 일이니..."
        '선생님' "그런데 네 물건을 훔쳐 가는 사람이 있다고?"
        v "네, 은님이 제 비녀를 지켜주셨다니 다행이에요. 정말 저에게 소중한 물건이옵니다."
        v "누가 제 물건을 훔쳐 가는 것일까요..."
        hide vii with dissolve
        hide bad3 with dissolve
        show bluehen normal at left with dissolve #기본표정 블루헨
        b "저런, 나는 잠시 동안 사무실 문을 닫는 데 말이에요. 경찰에 연락하도록 해요."
        b "그럼 범인을 찾았으니 온실 손해배상은 고양이씨에게 청구하도록 하세요."
        b "뒷일은 알아서 잘 처리하도록 해요. 난 이만 가볼게요. 잘 있어요?"
        hide bluehen normal with dissolve
        show c normal with dissolve #기본표정 코크
        c "아앗! 저도 강당에 공연하러 가야 하는데... 저도 이만 가볼게요!"
        hide c normal with dissolve
        show bad3 with dissolve #선생님
        '선생님' "내... 내 분재가... 으아악! 머리가 빠진다!!!"

        # (강당 화면 전환)
        $ renpy.block_rollback()
        stop music fadeout 3.0
        scene bg school_6 with dissolve2
        show bad7 with dissolve #실루엣 사회자
        play music "audio/공연.ogg"
        '사회자' "다음 순서는! 우리 학교의 자랑이죠! 밴드부의 공연입니다!"
        scene utac with dissolve2
        $ renpy.pause(3.0)
        "수호자씨가 이쪽을 보고 손을 흔들었다."
        "그나저나, 모두 귀를 막고 고통스러워하는데 괜찮을까."

        stop music fadeout 1.0
        scene bg room_night with dissolve2
        "전부 정리하고 갔는지 사무실은 싸늘하다."
        "그는 아마... ..."
        "일단 자고 일어나서 생각하자."
        scene black with dissolve2
        $ renpy.block_rollback()
#=======================3일째 끝========================================================
#=======================4일째 시작======================================================
    scene black
    $ renpy.block_rollback()
    $ renpy.pause(2.0)
    "...지금이 몇 시죠?"
    "왠지 바깥이 어두운데..."
    scene bg room_night with dissolve2 #(불 꺼진 사무실)
    show bluehen normal with dissolve #기본표정 블루헨
    play music "audio/도입.ogg"
    b "몇 시간 잔 것 같지 않은데 이상하게 몸이 찌뿌둥하네요."
    b "...어라? 다음날이었네요? 내가 이렇게 오래 자다니..."
    b "리히터!"
    $ renpy.pause(1.0)
    "아... 맞다. 그는 일을 그만두었지. 그리고 나도 당분간 문을 닫기로 했었다."
    b "빈자리 때문일까요... 그새 익숙해진 모양이에요."
    b "기분전환이라도 하러 밖에 나갔다 올까요."
    stop music fadeout 2.0
    $ renpy.block_rollback()
    #선택지
    while True:
        scene bg street_night with dissolve2 #(거리 화면전환)
        play music "audio/평범엔딩.ogg"
        menu:
            "분수대":
                scene bg fountain_night with dissolve
                $ renpy.block_rollback()
                "분수대에 가자 쇼가 시작된 듯 형형색색의 물을 뿜고 있었다."
                $ renpy.block_rollback()
                "은은한 달빛 아래 펼쳐지는 화려한 쇼가 기분을 나아지게 했다."
                $ renpy.block_rollback()
                show bluehen normal with dissolve #기본표정 블루헨
                b "이런 것도 나쁘지 않네요."
                $ renpy.block_rollback()
                b "앞으로도 이 평안한 하루가 계속 이어졌으면 좋겠어요."
                $ renpy.block_rollback()
                b "이제 내일을 준비하러 가볼까요?"
                $ renpy.block_rollback()
                $ renpy.pause(1.0)
                $ renpy.block_rollback()
                scene bg gameset with dissolve2
                $ renpy.block_rollback()
                $ renpy.pause(5.0)
                $ renpy.block_rollback()
                $ renpy.full_restart()
            "경찰서":
                scene bg street_night with dissolve
                $ renpy.block_rollback()
                "이 늦은 밤에 경찰서에는 가봤자 불이 꺼져 있을 것이다."
                $ renpy.block_rollback()
                "사무소에 가 밥이나 먹어야겠다. 뭔가 허무한걸..."
                $ renpy.block_rollback()
                $ renpy.pause(1.0)
                $ renpy.block_rollback()
                scene bg gameset with dissolve2
                $ renpy.block_rollback()
                $ renpy.pause(5.0)
                $ renpy.block_rollback()
                $ renpy.full_restart()
            "공원" :
                $ renpy.block_rollback()
                scene bg park_night with dissolve # 밤 공원 이미지로 바꿈
                "밤의 공원은 어쩐지 스산했다."
                "경치를 구경하는데 발치에서 무언가가 굴러왔다."
                show docsol at rotation with moveinleft
                hide docsol with dissolve
                show bluehen normal at left with dissolve #기본표정 블루헨
                show docsol at right with dissolve
                b "아, 너는..."
                b "너, 심심하면 나랑 같이 갈래요?"
                #$ renpy.pause(1.0)
                show docsol at right with vpunch
                "그것은 알아들은 듯 끄덕였다."
                show bluehen say at left with dissolve #웃는표정 블루헨
                b "좋아요. 오늘부터 네 이름은 독솔로기예요. 너도 좋다고요? 하하."
                "독솔로기를 들고 사무소에 돌아갔다."
                #(독솔로기엔딩)
                $ renpy.block_rollback()
                $ renpy.pause(1.0)
                $ renpy.block_rollback()
                scene bg gameset with dissolve2
                $ renpy.block_rollback()
                $ renpy.pause(5.0)
                $ renpy.block_rollback()
                $ renpy.full_restart()
            "뒷골목":
                scene bg backstreet2 with dissolve
                if doom_point >= 3 : #3이상일때 (3, 4)
                    $ renpy.block_rollback()
                    show doom normal at right with dissolve
                    d "...너. 왜 이제서야 나돌아다니냐? 한참 찾았잖아. 오늘 도통 보이질 않더라니..."
                    show bluehen normal at left with dissolve #기본표정 블루헨
                    b "응? 깡패씨가 왜 날 찾아요?"
                    show doom wink at right with dissolve
                    d "그거야..."
                    d "다름이 아니라... 그..."
                    d "... ..."
                    $ renpy.pause(2.0)
                    #(일러스트)
                    scene bg eddo with dissolve
                    $ renpy.pause(3.0)
                    d "내가 널 조... 조조 조... 좋아! 하니까..."
                    d "... 그래서 찾았어. 됐냐?"
                    d "너도 나 좋으면, 꽃 받아주든가 말든가..."
                    scene bg backstreet2 with dissolve
                    show bluehen angryy at left with dissolve #화난표정 블루헨
                    b "갑자기 뭐죠?"
                    show doom wink at right with dissolve
                    d "쳇. 빨리 받으라고... 팔 떨어지겠으니까."
                    b "싫은데요?"
                    stop music fadeout 2.0
                    show doom angry at right with dissolve
                    d "... 뭐?"
                    show bluehen wink at left with dissolve #화난표정 블루헨
                    b "싫다고요."
                    play music "audio/당황.ogg"
                    d "뭐... 뭐?!"
                    b "내가 왜 깡패씨같은 시끄럽고 경박한 인간을... 좋아한다고 생각할 수 있죠?"
                    b "정말 이해가 안 되네요."
                    b "나는 이만 가볼게요. 여기서 조금이라도 더 머물기 싫네요."
                    b "그럼."
                    hide bluehen angryy with dissolve
                    show doom angry at right with dissolve
                    d "뭐라고?! 이 자식... 너!!! 내 마음을 갖고 놀았겠다!!! 거기 서!!!" with Shake((0, 0, 0, 0), 1.0, dist=40)
                    hide doom angry with dissolve
                    "괜히 뒷골목에 갔다가 기분만 나빠졌다."
                    "사무실에 돌아가야겠군..."
                    #(둠브엔딩)
                    scene bg eddo with dissolve2
                    $ renpy.pause(2.0)
                    "-둠브링어 ENDING-"
                    $ renpy.full_restart()
                else : # 둠포인트 1, 2
                    $ renpy.block_rollback()
                    show bad with dissolve #깡패 땡글이들
                    $ renpy.block_rollback()
                    ba "어이, 형씨. 이런 야밤에 어두~컴컴한 뒷골목엔 오면 안 된다는 거 못 배웠나 봐?"
                    $ renpy.block_rollback()
                    ba "크크크... 돈 좀 있나 뒤져볼까? 아, 물론 죽인 채로 말이지~"
                    $ renpy.block_rollback()
                    with Shake((0, 0, 0, 0), 1.0, dist=40)
                    $ renpy.block_rollback()
                    "뒤에서 무언가가 내 머리를 강하게 타격했다."
                    $ renpy.block_rollback()
                    $ renpy.pause(1.0)
                    $ renpy.block_rollback()
                    stop music fadeout 1.0
                    play sound "audio/게임오버.ogg"
                    scene bg gameover with dissolve2
                    $ renpy.block_rollback()
                    $ renpy.pause(5.0)
                    $ renpy.block_rollback()
                    $ renpy.full_restart()
                    #게임오버댐
            "시장":
                scene bg market_night with dissolve
                $ renpy.block_rollback()
                show bluehen normal with dissolve #기본표정 블루헨
                $ renpy.block_rollback()
                b "이 가게만 문을 열었네요. 한번 들어가 볼까요?"
                $ renpy.block_rollback()
                hide bluehen normal with dissolve
                show bad2 with dissolve #가게사장땡글
                $ renpy.block_rollback()
                '가게사장' "어서 오세요. 손님!"
                $ renpy.block_rollback()
                hide bad2 with dissolve
                show bluehen normal with dissolve
                $ renpy.block_rollback()
                "김밥을 시켜서 맛있게 먹었다."
                $ renpy.block_rollback()
                b "배부르네요. 그럼 이제 사무실로 돌아가 볼까요~"
                $ renpy.block_rollback()
                $ renpy.pause(1.0)
                $ renpy.block_rollback()
                scene bg gameset with dissolve2
                $ renpy.block_rollback()
                $ renpy.pause(5.0)
                $ renpy.block_rollback()
                $ renpy.full_restart()
            "학교":
                scene bg school_night with dissolve #학교
                if c_point >= 6 :
                    stop music fadeout 1.0
                    $ renpy.block_rollback()
                    show c normal at right with dissolve #기본표정 코크
                    c "어? 안녕하세요, 탐정님!"
                    show bluehen normal at left with dissolve #기본표정 블루헨
                    b "응? 아, 너는 수호자씨군요."
                    c "학교엔 어쩐 일로 오셨어요?"
                    b "그냥 기분전환 겸 주변을 둘러보고 있었어요."
                    show c angry at right with dissolve #당황표정 코크
                    c "탐정님도 기분이 안 좋으실 때가 있군요..."
                    show c normal at right with dissolve #기본표정 코크
                    c "아, 그럼 학교에 잠깐 들어오세요! 경비원분들도 제가 이야기하면 살짝 눈감아주실 거예요."
                    show c say at right with dissolve #웃는표정 코크
                    c "하하. 교칙을 어겨본 적이 처음이라 조금 두근거리기도 하네요."
                    c "그리고 온실이 지금 엄청 멋지게 복구되었답니다! 보러 가실래요?"
                    b "그럴까요? 그럼 안내해 줘요."
                    scene bg school_2_night with dissolve2 #온실
                    play music "audio/코크엔딩.ogg"
                    show c normal at right with dissolve #기본표정 코크
                    c "어때요, 탐정님! 꽃이 거의 다 심어졌죠? 조금 좁지만, 여기 앉아보실래요?"
                    c "저도 기분이 우울할 때 온실에 와서 자주 별을 구경해요."
                    c "별을 보면서 제가 나아가야 할 목표를 다시 되새겨요. 그때의 다짐이 약해지지 않게..."
                    show c angry at right with dissolve #놀란표정 코크
                    c "앗! 저기 보세요. 별똥별이에요!"
                    #(일러스트)
                    $ renpy.pause(2.0)
                    scene bg edco with dissolve2
                    $ renpy.pause(3.0)
                    "나의 목표..."
                    c "정말 멋져요! 별똥별은 처음 봐요."
                    b "... 그렇네요. 나도 처음 봐요."
                    c "별똥별을 보았으니 소원을 빌어야겠어요! 탐정님도 어서 비세요!"
                    "소원... 소원이라."
                    "나와 수호자씨는 잠시 눈을 감고 소원을 빌었다."
                    $ renpy.pause(2.0)
                    scene bg school_night with dissolve #학교
                    show bluehen normal at left with dissolve #기본표정 블루헨
                    b "오늘 고마웠어요. 덕분에 기분전환이 좀 된 것 같아요."
                    show c normal at right with dissolve #웃는표정 코크
                    c "다행이에요! 아, 어디서 지내세요? 집까지 바래다 드릴게요."
                    b "그건 됐어요. 나 혼자서 갈 수 있답니다."
                    c "아니에요. 얼마 전 마을에 살인사건이 일어나신 거 모르시나요?"
                    b "그럼 네가 더 위험한 거 아닌가요? 학생이잖아요."
                    b "뭐... 네가 정 원한다면 그렇게 하도록 해요."
                    c "네! 가요! 맞다, 혹시..."
                    b "응?"
                    show c winkk at right with dissolve #볼빨간 코크가 필요한듯합니다
                    c "실례가 안된다면 형이라고 불러도 될까요...?"
                    show bluehen say at left with dissolve #웃는표정 블루헨
                    b "그럼요. 오늘 좋은 걸 보여준 기념으로 허락할게요."
                    show c say at right with dissolve #웃는 코크
                    c "...네, 형!"
                    $ renpy.pause(1.0)
                    "그와 함께 밤길을 걸어갔다."
                    #(코크 엔딩)
                    stop music fadeout 2.0
                    scene bg edco with dissolve2
                    $ renpy.pause(2.0)
                    "-코멧 크루세이더 ENDING-"
                    $ renpy.full_restart()
                else : #(콬포인트 4이하일시)
                    $ ttang = 1
                    $ renpy.block_rollback()
                    show bad4 with dissolve
                    $ renpy.block_rollback()
                    '경비원' "어이어이, 네놈 학교 주변은 왜 알짱거리지?"
                    $ renpy.block_rollback()
                    play music "audio/땡글엔딩.ogg"
                    '경비원' "내 애완견이 널 물어뜯고 싶어 하는군..."
                    $ renpy.block_rollback()
                    '경비원' "후후, 땡글. 저놈을 잡아 죽여!"
                    $ renpy.block_rollback()
                    scene bg school_night
                    $ renpy.block_rollback()
                    play sound "audio/훅.wav"
                    show bad5 with easeinright
                    play sound "audio/HitEveWeapon1.wav"
                    hide bad5 with Shake((0, 0, 0, 0), 0.3, dist=10)
                    $ renpy.block_rollback()
                    play sound "audio/훅.wav"
                    show bad6 with easeinleft
                    play sound "audio/HitEveWeapon1.wav"
                    hide bad6 with Shake((0, 0, 0, 0), 0.3, dist=10)
                    $ renpy.block_rollback()
                    play sound "audio/훅.wav"
                    show bad5 with easeinright
                    play sound "audio/HitEveWeapon1.wav"
                    hide bad5 with Shake((0, 0, 0, 0), 0.3, dist=10)
                    $ renpy.block_rollback()
                    play sound "audio/훅.wav"
                    show bad6 with easeinleft
                    play sound "audio/HitEveWeapon1.wav"
                    hide bad6 with Shake((0, 0, 0, 0), 0.3, dist=10)
                    $ renpy.block_rollback()
                    $ renpy.pause(1.0)
                    $ renpy.block_rollback()
                    scene bg gameover with dissolve2
                    $ renpy.block_rollback()
                    $ renpy.pause(5.0)
                    $ renpy.block_rollback()
                    $ renpy.full_restart()
                    #게임오버댐
            "의문의 저택":
                scene bg mansion with dissolve
                if Radiant_point >= 4: #(랏포인트 4이상일시)
                    stop music fadeout 1.0
                    $ renpy.block_rollback()
                    "저택은 그 흔한 경비원 한 명도 없었다."
                    "초인종을 누르자 의뢰인씨의 목소리가 들렸다."
                    ra "어? 라비 친구다!"
                    $ renpy.pause(1.0)
                    "이윽고 저택의 문이 열렸다."
                    show radiant say with dissolve
                    play music "audio/라소엔딩.ogg"
                    ra "라비 친구, 어서 와! 라비랑 놀러 온 거야? 라비 너무 좋아!"
                    show radiant wink with dissolve
                    "의뢰인씨는 내 손을 붙들고 저택의 계단을 올라갔다."
                    "그 메이드는 당혹스러운 듯 입을 열었으나 신난 의뢰인씨의 콧노래에 다시 닫았다."
                    scene bg raso with dissolve#(라비의 방 화면)이 추가된다면 추가하겟습니당 ㅋ
                    show radiant normalr at right with dissolve
                    ra "나랑 인형놀이하자! 인형이 말랑말랑해! 구름이도 새 친구 좋아할 거야. 그때 찾아준 작은니샤도!"
                    show bluehen normal at left with dissolve
                    b "그건 내가 찾아준 게 아닌데요? 네 메이드 씨가 찾아줬잖아요."
                    show radiant winkr at right with dissolve
                    ra "우웅... 그런가? 그래도 좋아할 거야! 모두 사이좋게 지내!"
                    "의뢰인씨는 인형을 내 손에 쥐여주곤 해맑게 웃었다."
                    #(일러스트)
                    $ renpy.block_rollback()
                    scene bg edra with dissolve2
                    $ renpy.pause(3.0)
                    ra "콰과과광! 비행기에 탄 곰돌이가 여객선을 터뜨렸다!"
                    $ renpy.pause(1.0)
                    $ renpy.block_rollback()
                    scene bg mansion with dissolve#(저택화면)
                    show radiant normalr at right with dissolve
                    ra "오늘 재미있었어! 또 놀러 와!"
                    show bluehen normal at left with dissolve
                    b "그래요. 다음에 봐요."
                    $ renpy.pause(1.0)
                    scene bg mansion with dissolve
                    "차디찬 밤공기에 따뜻해진 손이 금세 식었다."
                    "하지만 왠지 아까의 그 기분은... 아직 남아있을지도."
                    #(라소엔딩)
                    stop music fadeout 2.0
                    scene bg edra with dissolve2
                    $ renpy.pause(2.0)
                    "-라디언트 소울 ENDING-"
                    $ renpy.full_restart()
                else : #(랏포인트 3이하일 시)
                    stop music fadeout 1.0
                    $ renpy.block_rollback()
                    "저택은 그 흔한 경비원 한 명도 없었다."
                    $ renpy.block_rollback()
                    "...그렇다고 생각했으나 나는 이윽고 알 수 없는 냄새를 맡고 쓰러졌다."
                    $ renpy.block_rollback()
                    scene white with dissolve2 #(암전)
                    scene black
                    play music "audio/바람.mp3"
                    $ renpy.pause(1.0)
                    $ renpy.block_rollback()
                    "눈을 떠 보니 그때 봤던 메이드가 보인다."
                    $ renpy.block_rollback()
                    show nisha sayr with dissolve #정색 니샤
                    $ renpy.block_rollback()
                    n "너, 라비한테 접근하는 이유가 뭐야?"
                    $ renpy.block_rollback()
                    n "... 하긴, 이제 와서 그런 걸 들을 필요는 없지."
                    $ renpy.block_rollback()
                    n "안 그래도 잘 됐어. 네 옆에 있던 그 자... 내 기분을 아주 거슬리게 했거든."
                    $ renpy.block_rollback()
                    n "받았으면 되돌려줘야겠지?"
                    $ renpy.block_rollback()
                    n "또 땅을 더럽히게 생겼어. 요 근래 처리할 게 많네."
                    $ renpy.block_rollback()
                    hide nisha sayr with dissolve
                    $ renpy.block_rollback()
                    show bluehen angryy with dissolve
                    $ renpy.block_rollback()
                    b "또라니. 설마 어저께 일어난 살인사건... 네 짓인가요?"
                    $ renpy.block_rollback()
                    hide bluehen angryy with dissolve
                    $ renpy.block_rollback()
                    show nisha askr with dissolve #정색 니샤
                    $ renpy.pause(2.0)
                    show nisha sayr with dissolve #정색 니샤
                    $ renpy.block_rollback()
                    n "..."
                    $ renpy.pause(1.0)
                    $ renpy.block_rollback()
                    n "그러면, 어쩌게?"
                    $ renpy.block_rollback()
                    show nisha askr with dissolve #정색 니샤
                    $ renpy.pause(1.0)
                    n "잘 가, 방해되는 인간."
                    $ renpy.block_rollback()
                    hide nisha askr with dissolve
                    $ renpy.block_rollback()
                    play sound "audio/sword.wav"
                    with Shake((0, 0, 0, 0), 1.0, dist=30)
                    $ renpy.block_rollback()
                    scene bg gameover with dissolve2
                    $ renpy.block_rollback()
                    $ renpy.pause(5.0)
                    $ renpy.block_rollback()
                    $ renpy.full_restart()
                    #게임오버댐
            "이스마엘 강":
                scene bg river_night with dissolve
                play music "audio/이스마엘강.ogg"
                if Richter_point >= 5: #(맇포인트 5이상일 시)
                    $ renpy.block_rollback()
                    "누군가 다리에 서 있는 것 같다."
                    $ renpy.block_rollback()
                    "...이상한 기분이 든다."
                    menu :
                        "다리" :
                            $ renpy.block_rollback()
                            $ renpy.pause(1.0)
                            $ renpy.block_rollback()
                            show bluehen normal with dissolve
                            b "리히터..."
                            "섣불리 말을 꺼낼 수가 없어 머뭇거렸다. 그는 아마..."
                            scene bg river_night with dissolve
                            show bluehen normal at left with dissolve
                            show richter normal at right with dissolve
                            b "넌, 천계에서 온 거죠?"
                            show richter angry at right with dissolve
                            r "..."
                            show richter normal at right with dissolve
                            r "그래요. 알고 있었군요."
                            b "며칠 전부터 눈치챘어요. 너는 나를 없애러 온 건가요?"
                            show richter say at right with dissolve
                            r "글쎄요."
                            b "내가 인간이 된 것 때문에..."
                            b "불완전한, 천족도 인간도 아닌 나를 세계에서 제거하고 싶어 하는 자들이 많다는 것쯤은 알아요."
                            show bluehen wink at left with dissolve
                            b "하지만 네가 나를 죽이려고 했다면 벌써 죽었겠죠. 난 지금 나약한 인간이니까."
                            b "여기에 온 이유가 뭔가요?"
                            b "일을 갑자기 그만둔 것도... 천계로 돌아가기 위해선가요?"
                            show richter angry at right with dissolve
                            r "처음엔 감시하기 위함이었어요."
                            r "하지만 너와 같이 지내면서 내 안의 무언가가 달라지고 있다는 느낌이 들었어요."
                            r "이 강한 이끌림..."
                            show richter say at right with dissolve
                            r "너와 같은 아인이라 그런 걸까요?"
                            show bluehen ask at left with dissolve
                            $ renpy.pause(1.0)
                            b "!!!"
                            b "그 이름은..."
                            r "난 언제나 널 주시하고 있어요."
                            show richter wink at right with dissolve
                            r "... 너의 선택을 존중합니다, 블루헨."
                            #(일러스트)
                            scene bg edri with dissolve2
                            $ renpy.pause(3.0)
                            scene bg river_night with dissolve #리히터 캐릭터없이 스크립트만
                            $ renpy.pause(3.0)
                            r "그럼 안녕히."
                            $ renpy.pause(1.0)
                            "그는 애초에 없었던 것처럼 사라졌다."
                            "나를 혼란스럽게 만든 채..."
                            "나는 한동안 그 자리를 떠나지 못하다 날이 밝아오고 나서야 발을 뗐다."
                            "마치 꿈을 꾼 것 같다."
                            "하지만 꿈 따위가 아닌 것을 누구보다 잘 알고 있다."
                            show bluehen wink with dissolve
                            b "언젠가 또다시 만날 날을 기다릴게요, 리히터."
                            #(리히터 엔딩)
                            stop music fadeout 2.0
                            scene bg edri with dissolve2
                            $ renpy.pause(2.0)
                            "-리히터 ENDING-"
                            $ renpy.full_restart()
                else :
                    $ renpy.block_rollback()
                    "누군가 다리에 서 있는 것 같다."
                    $ renpy.block_rollback()
                    "...이상한 기분이 든다."
                    menu :
                        "다리" :
                            $ renpy.block_rollback()
                            $ renpy.pause(1.0)
                            "다리에는 아무도 없었다. 착각이었나."
                            $ renpy.block_rollback()
                            "나는 왠지 모를 공허한 기분을 안고 사무실로 돌아갔다."
                            $ renpy.block_rollback()
                            "내일을 위해 억지로라도 잠을 청해 봐야겠다."
                            $ renpy.pause(1.0)
                            $ renpy.block_rollback()
                            scene bg gameset with dissolve2
                            $ renpy.block_rollback()
                            $ renpy.pause(5.0)
                            $ renpy.block_rollback()
                            $ renpy.full_restart()
                #jump next
    #label next :
