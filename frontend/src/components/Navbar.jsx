import "./Navbar.css";

function Navbar() {
  return (
    <header className="navbar">
      <nav className="nav-inner">
        <ul className="nav-left">
          <li>HOME</li>
          <li>DESSERT</li>
          <li>REVEIW</li>
          <li>Q&A</li>
        </ul>


        <div className="nav-right">
          <img src="/images/search.png" alt="search" />
          <img src="/images/user.png" alt="profile" />
          <img src="/images/cart.png" alt="cart" />
        </div>
      </nav>
    </header>
  );
}

export default Navbar;
