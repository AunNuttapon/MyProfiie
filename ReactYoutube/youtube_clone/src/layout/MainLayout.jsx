import Contents from "../components/Contents/Contents";
import Nav from "../components/Nav/Nav";
import Sidbar from "../components/Sidebar/Sidbar";

function MainLayout() {
  return (
    <section id="main-layout">
      <Nav></Nav>
      <Sidbar></Sidbar>
      <Contents></Contents>
    </section>
  );
}

export default MainLayout;
