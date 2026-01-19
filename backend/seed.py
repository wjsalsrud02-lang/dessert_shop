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
    ]

    db.session.add_all(desserts)
    db.session.commit()
