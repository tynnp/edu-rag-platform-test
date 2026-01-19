import { useState } from "react";
import PinPage from "./pages/PinPage";
import ChatPage from "./pages/ChatPage";

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  if (!isAuthenticated) {
    return <PinPage onSuccess={() => setIsAuthenticated(true)} />;
  }

  return <ChatPage />;
}

export default App;
