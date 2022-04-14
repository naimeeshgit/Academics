import { BrowserRouter, Routes, Route, Outlet } from "react-router-dom";
import "./App.css";

import UsersList from "./components/users/UsersList";
import Home from "./components/common/Home";
import Register from "./components/common/Register";
import Navbar from "./components/templates/Navbar";
import Profile from "./components/users/Profile";
import Login from "./components/common/Login";
import ProfileBuyer from "./components/common/ProfileBuyer";

import Enter from "./components/common/enter";
import Results from "./components/common/results";

// const Layout = () => {
//   return (
//     <div>
//       <Navbar />
//       <div className="container">
//         <Outlet />
//       </div>
//     </div>
//   );
// };

//Remove the nav bar and give appropriate spacing or margin to the content / Leave the nav bar as it as just remove the buttons from it
function App() {
  return (
    <BrowserRouter>
      <Routes>
        
          <Route path="/" element={<Home />} />
          <Route path="users" element={<UsersList />} />
          <Route path="register" element={<Register />} />
          <Route path="login" element={<Login />} />
          <Route path="profile" element={<Profile />} />
          <Route path="profileBuyer" element={<ProfileBuyer />} />
          <Route path="enter" element={<Enter />} />
          <Route path="results" element={<Results />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
