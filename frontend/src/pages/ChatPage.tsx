import { useState } from "react";
import { FileText, X, PanelLeft } from "lucide-react";
import ChatBox from "../components/ChatBox";
import { chatWithRag, chatWithoutRag } from "../services/api";
import type { Message } from "../types";

export default function ChatPage() {
    const [messages, setMessages] = useState<Message[]>([]);
    const [loading, setLoading] = useState(false);
    const [useRag, setUseRag] = useState(true);
    const [showPdf, setShowPdf] = useState(true);

    const handleSend = async (message: string) => {
        setMessages((prev) => [...prev, { role: "user", content: message }]);
        setLoading(true);

        try {
            const apiCall = useRag ? chatWithRag : chatWithoutRag;
            const answer = await apiCall(message);
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
        <div className="h-screen w-full flex bg-gray-100">
            {/* PDF Viewer - Left Side */}
            {showPdf && (
                <div className="w-[45%] h-full border-r border-gray-300 bg-white flex flex-col">
                    <div className="p-3 bg-indigo-600 text-white flex justify-between items-center">
                        <span className="font-semibold flex items-center gap-2">
                            <FileText size={18} />
                            Tài liệu gốc
                        </span>
                        <button
                            onClick={() => setShowPdf(false)}
                            className="text-white hover:text-gray-200"
                        >
                            <X size={20} />
                        </button>
                    </div>
                    <iframe
                        src="/document.pdf"
                        className="flex-1 w-full"
                        title="PDF Viewer"
                    />
                </div>
            )}

            {/* Chat - Right Side */}
            <div className={`h-full flex flex-col ${showPdf ? 'w-[55%]' : 'w-full'}`}>
                {!showPdf && (
                    <button
                        onClick={() => setShowPdf(true)}
                        className="absolute top-4 left-4 bg-indigo-600 text-white px-4 py-2 rounded-lg shadow-lg hover:bg-indigo-700 z-10 flex items-center gap-2"
                    >
                        <PanelLeft size={18} />
                        Xem tài liệu
                    </button>
                )}
                <ChatBox
                    messages={messages}
                    onSend={handleSend}
                    loading={loading}
                    useRag={useRag}
                    onToggleRag={setUseRag}
                />
            </div>
        </div>
    );
}