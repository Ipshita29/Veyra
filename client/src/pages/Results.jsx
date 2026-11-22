import "../css/Results.css";
import Navbar from "../components/Navbar.jsx";
import VideoPlayer from "../components/VideoPlayer.jsx";
import LanguageSelector from "../components/LanguageSelector.jsx";
import Summary from "../components/Summary.jsx";
import Chapters from "../components/Chapters.jsx";
import Transcript from "../components/Transcript.jsx";

export default function Results() {
  return (
    <div className="results">
      <Navbar />
      <VideoPlayer />
      <LanguageSelector />
      <Summary />
      <Chapters />
      <Transcript />
    </div>
  );
}
