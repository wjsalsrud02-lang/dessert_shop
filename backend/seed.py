from app import app
from models import db, Dessert

with app.app_context():
    db.create_all()

    desserts = [
        Dessert(
            name="핑크 스프링 도넛",
            price=3800,
            description="딸기 초콜릿 코팅 위에 알록달록 스프링클을 더한 달콤한 시그니처 도넛",
            image_url="/images/도넛1.png",
            category="donut"
        ),
        Dessert(
            name="블루 슈가 도넛",
            price=3800,
            description="하늘빛 슈가 글레이즈와 바삭한 스프링클이 어우러진 상큼한 도넛",
            image_url="/images/도넛2.png",
            category="donut"
        ),
        Dessert(
            name="카라멜 크런치 도넛",
            price=4200,
            description="부드러운 카라멜 코팅 위에 초콜릿 드리즐을 더한 달콤쌉싸름한 도넛",
            image_url="/images/도넛3.png",
            category="donut"
        ),
        Dessert(
            name="레드 벨벳 크럼 도넛",
            price=4200,
            description="레드벨벳 크럼이 듬뿍 올라간 깊고 진한 초콜릿 풍미의 도넛",
            image_url="/images/도넛4.png",
            category="donut"
        ),
        Dessert(
            name="초코 쉐도우 도넛",
            price=4000,
            description="다크 초콜릿 코팅과 초코 스프링클이 어우러진 클래식한 초코 도넛",
            image_url="/images/도넛5.png",
            category="donut"
        ),
        Dessert(
            name="레인보우 스위티 초코 도넛",
            price=4000,
            description="컬러풀한 스프링클이 가득 올라간 달콤하고 경쾌한 초코 도넛",
            image_url="/images/도넛6.png",
            category="donut"
        ),
        Dessert(
            name="너티 허니 도넛",
            price=4200,
            description="고소한 견과류와 꿀 코팅이 조화로운 바삭달콤 도넛",
            image_url="/images/도넛7.png",
            category="donut"
        ),
        Dessert(
            name="핑크 밀키 도넛",
            price=3800,
            description="부드러운 밀크 글레이즈에 핑크 코팅을 더한 크리미한 도넛",
            image_url="/images/도넛8.png",
            category="donut"
        ),
        Dessert(
            name="다크 초코 크런치 도넛",
            price=4300,
            description="초콜릿 크런치가 가득 올라간 진한 초코 매니아용 도넛",
            image_url="/images/도넛9.png",
            category="donut"
        ),
        Dessert(
            name="화이트 드리즐 도넛",
            price=4100,
            description="화이트 초콜릿 드리즐로 마무리한 깔끔하고 달콤한 도넛",
            image_url="/images/도넛10.png",
            category="donut"
        ),
        Dessert(
            name="초코 브라우니 도넛",
            price=4500,
            description="브라우니 크럼이 듬뿍 올라간 묵직하고 진한 디저트 도넛",
            image_url="/images/도넛11.png",
            category="donut"
        ),
        Dessert(
            name="퍼플 크림 도넛",
            price=4200,
            description="은은한 퍼플 글레이즈와 부드러운 크림 풍미가 매력적인 도넛",
            image_url="/images/도넛12.png",
            category="donut"
        ),
        Dessert(
            name="클래식 버터 마들렌",
            price=3200,
            description="프랑스 전통 레시피로 구워낸 깊은 버터 향과 촉촉한 식감의 기본 마들렌",
            image_url="/images/마들렌1.png",
            category="madeleine"
        ),
        Dessert(
            name="레드 벨벳 마들렌",
            price=3500,
            description="부드러운 코코아 풍미와 크림치즈 글레이즈가 어우러진 달콤한 레드 벨벳 마들렌",
            image_url="/images/마들렌2.png",
            category="madeleine"
        ),
        Dessert(
            name="피스타치오 마들렌",
            price=3800,
            description="고소한 피스타치오 페이스트와 화이트 초콜릿 코팅의 균형 잡힌 풍미",
            image_url="/images/마들렌3.png",
            category="madeleine"
        ),
        Dessert(
            name="말차 그린티 마들렌",
            price=3800,
            description="쌉싸름한 말차 향이 은은하게 퍼지는 일본식 녹차 마들렌",
            image_url="/images/마들렌4.png",
            category="madeleine"
        ),
        Dessert(
            name="커피 모카 마들렌",
            price=3800,
            description="진한 에스프레소와 초콜릿이 어우러진 어른스러운 풍미",
            image_url="/images/마들렌5.png",
            category="madeleine"
        ),
        Dessert(
            name="레인보우 스프링클 마들렌",
            price=3500,
            description="알록달록한 스프링클로 즐거움을 더한 달콤한 마들렌",
            image_url="/images/마들렌6.png",
            category="madeleine"
        ),
        Dessert(
            name="레몬 글레이즈 마들렌",
            price=3800,
            description="상큼한 레몬 아이싱으로 마무리한 산뜻한 마들렌",
            image_url="/images/마들렌7.png",
            category="madeleine"
        ),
        Dessert(
            name="솔티드 카라멜 마들렌",
            price=3800,
            description="달콤한 카라멜과 소금의 조화가 매력적인 깊은 맛",
            image_url="/images/마들렌8.png",
            category="madeleine"
        ),
        Dessert(
            name="초콜릿 마블 마들렌",
            price=3800,
            description="바닐라와 초콜릿 반죽이 어우러진 클래식 마블 스타일",
            image_url="/images/마들렌9.png",
            category="madeleine"
        ),
        Dessert(
            name="프룻 마들렌",
            price=4100,
            description="제철 과일을 듬뿍 올려 화사하게 즐기는 마들렌",
            image_url="/images/마들렌10.png",
            category="madeleine"
        ),
        Dessert(
            name="라즈베리 크리스탈 마들렌",
            price=3900,
            description="라즈베리 코팅과 설탕 크리스탈의 상큼한 식감의 마들렌",
            image_url="/images/마들렌11.png",
            category="madeleine"
        ),
        Dessert(
            name="라벤더 글레이즈 마들렌",
            price=4000,
            description="은은한 라벤더 향으로 완성한 플로럴 무드의 마들렌",
            image_url="/images/마들렌12.png",
            category="madeleine"
        ),
        Dessert(
            name="화이트 초콜릿 마들렌",
            price=3800,
            description="화이트 초콜릿과 시트러스 제스트가 조화로운 부드러운 마들렌",
            image_url="/images/마들렌13.png",
            category="madeleine"
        ),
        Dessert(
            name="크리스탈 슈가 마들렌",
            price=3400,
            description="겉은 바삭, 속은 촉촉한 설탕 코팅 클래식",
            image_url="/images/마들렌14.png",
            category="madeleine"
        ),
        Dessert(
            name="다크 세서미 마들렌",
            price=3900,
            description="고소한 흑임자 풍미가 매력적인 동양적인 마들렌",
            image_url="/images/마들렌15.png",
            category="madeleine"
        ),
        Dessert(
            name="바닐라 마카롱",
            price=2800,
            description="부드러운 바닐라 크림이 가득한 클래식 마카롱",
            image_url="/images/마카롱1.png",
            category="macaron"
        ),
        Dessert(
            name="오렌지 초콜릿 마카롱",
            price=3000,
            description="상큼한 오렌지와 다크 초콜릿의 조화가 잘 어울리는 마카롱",
            image_url="/images/마카롱2.png",
            category="macaron"
        ),
        Dessert(
            name="피스타치오 마카롱",
            price=3200,
            description="고소한 피스타치오 크림의 깊은 풍미가 가득한 마카롱",
            image_url="/images/마카롱3.png",
            category="macaron"
        ),
        Dessert(
            name="스트로베리 마카롱",
            price=3000,
            description="상큼한 딸기 크림이 살아있는 달콤한 마카롱",
            image_url="/images/마카롱4.png",
            category="macaron"
        ),
        Dessert(
            name="라벤더 & 레몬 마카롱",
            price=3200,
            description="플로럴한 라벤더와 레몬의 산뜻한 밸런스의 마카롱",
            image_url="/images/마카롱5.png",
            category="macaron"
        ),
        Dessert(
            name="코코넛 망고 마카롱",
            price=3200,
            description="열대 과일의 달콤함의 코코넛 맛을 담은 마카롱",
            image_url="/images/마카롱6.png",
            category="macaron"
        ),
        Dessert(
            name="카라멜 마카롱",
            price=3000,
            description="부드럽고 진한 솔티드 카라멜 크림이 물씬 느껴지는 마카롱",
            image_url="/images/마카롱7.png",
            category="macaron"
        ),
        Dessert(
            name="헤이즐넛 마카롱",
            price=3200,
            description="고소한 헤이즐넛 프랄린 풍미가 느껴지는 마카롱",
            image_url="/images/마카롱8.png",
            category="macaron"
        ),
        Dessert(
            name="로즈 라즈베리 마카롱",
            price=3200,
            description="장미 향과 라즈베리의 우아한 조화가 느껴지는 마카롱",
            image_url="/images/마카롱9.png",
            category="macaron"
        ),
        Dessert(
            name="레몬 마카롱",
            price=2800,
            description="상큼함이 돋보이는 클래식 레몬 마카롱",
            image_url="/images/마카롱10.png",
            category="macaron"
        ),
        Dessert(
            name="말차 피스타치오 마카롱",
            price=3900,
            description="말차의 쌉싸름함과 피스타치오의 고소함을 동시에 느낄 수 있는 마카롱",
            image_url="/images/마카롱11.png",
            category="macaron"
        ),
        Dessert(
            name="밀크 초코 마카롱",
            price=3000,
            description="달콤한 밀크 초콜릿 크림의 안정적인 맛 마카롱",
            image_url="/images/마카롱12.png",
            category="macaron"
        ),
        Dessert(
            name="초콜릿 마카롱",
            price=3800,
            description="진한 다크 초콜릿 가나슈 필링이 들어있는 마카롱",
            image_url="/images/마카롱13.png",
            category="macaron"
        ),
        Dessert(
            name="세서미 & 레드빈 마카롱",
            price=3200,
            description="흑임자와 팥의 조화로운 동양적인 풍미가 느껴지는 마카롱",
            image_url="/images/마카롱14.png",
            category="macaron"
        ),
        Dessert(
            name="얼그레이 코코넛 마카롱",
            price=3900,
            description="얼그레이 향과 코코넛의 부드러운 조화가 어우러지는 마카롱",
            image_url="/images/마카롱15.png",
            category="macaron"
        ),
        Dessert(
            name="블루베리 마카롱",
            price=3000,
            description="상큼한 블루베리 크림의 깔끔한 마카롱",
            image_url="/images/마카롱16.png",
            category="macaron"
        ),
        Dessert(
            name="코튼 캔디 마카롱",
            price=3200,
            description="달콤한 추억을 떠올리게 하는 솜사탕 맛 마카롱",
            image_url="/images/마카롱17.png",
            category="macaron"
        ),
        Dessert(
            name="로즈 & 리치 마카롱",
            price=3300,
            description="리치의 달콤함과 로즈 향이 어우러진 고급스러운 마카롱",
            image_url="/images/마카롱18.png",
            category="macaron"
        ),
    ]

    db.session.add_all(desserts)
    db.session.commit()
