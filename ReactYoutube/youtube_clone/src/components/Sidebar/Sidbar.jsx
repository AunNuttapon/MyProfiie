import './SidebarStyle.css';
function Sidbar() {
  return <section id="side">
    <div className="side-pmr">
      <a href="#!" className="-item">
        <div className="-icon">
          <img src="https://via.placeholder.com/24x24" alt="" />
        </div>
        <div className="-text">หน้าแรก</div>
      </a>
      <a href="#!" className="-item">
        <div className="-icon">
          <img src="https://via.placeholder.com/24x24" alt="" />
        </div>
        <div className="-text">Shorts</div>
      </a>
      <a href="#!" className="-item">
        <div className="-icon">
          <img src="https://via.placeholder.com/24x24" alt="" />
        </div>
        <div className="-text">การติดตาม</div>
      </a>
    </div>
  </section>;
}

export default Sidbar;
