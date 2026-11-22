import "../css/Home.css";
import Navbar from "../components/Navbar.jsx";
import VideoUploader from "../components/VideoUploader.jsx";

export default function Home() {
  return (
    <div className="home">
      <Navbar />
      <VideoUploader />
    </div>
  );
}
