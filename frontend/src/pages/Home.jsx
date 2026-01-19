import "./Home.css";
import MySwiper from "../components/MySwiper";


function Home() {
  return (
    <main className="home">
      <MySwiper />

      <section className="top-banner">
        <div className="top-banner-box">
          <h2>CREAMYDAY’</h2>
          <p>
            매일이 달콤해지는 순간,<br />
            크리미한 디저트를 만나보세요.
          </p>
        </div>
      </section>

      <section className="product-section">
        <div className="product1"></div>
        <div className="product2"></div>
        <div className="product3"></div>
        <div className="product4"></div>
      </section>

      <section className="bottom-banner">
        <p>Everyday is Creamy 🍰</p>
      </section>
    </main>
  );
}

export default Home;
