import { useState } from "react";
import ChatBox from "../components/ChatBox";
import { chatWithRag, chatWithoutRag } from "../services/api";
import type { Message } from "../types";

export default function ChatPage() {
    const [messages, setMessages] = useState<Message[]>([]);
    const [loading, setLoading] = useState(false);
    const [useRag, setUseRag] = useState(true);

    const handleSend = async (message: string) => {
        // Thêm tin nhắn người dùng
        setMessages((prev) => [...prev, { role: "user", content: message }]);
        setLoading(true);

        try {
            const apiCall = useRag ? chatWithRag : chatWithoutRag;
            const answer = await apiCall(message);

            // Thêm phản hồi của LLM
            setMessages((prev) => [...prev, { role: "bot", content: answer }]);
        } catch (error) {
            setMessages((prev) => [
                ...prev,
                { role: "bot", content: "Xin lỗi, đã có lỗi xảy ra khi xử lý yêu cầu của bạn." },
            ]);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="h-screen w-full bg-white">
            <ChatBox
                messages={messages}
                onSend={handleSend}
                loading={loading}
                useRag={useRag}
                onToggleRag={setUseRag}
            />
        </div>
    );
}