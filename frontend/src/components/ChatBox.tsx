import { useState, useRef, useEffect } from "react";
import ReactMarkdown from 'react-markdown';
import type { Message } from "../types";
import { Send, Bot, User, MessageSquare, Network } from "lucide-react";

interface ChatBoxProps {
    messages: Message[];
    onSend: (message: string) => void;
    loading: boolean;
    useRag: boolean;
    onToggleRag: (value: boolean) => void;
}

export default function ChatBox({ messages, onSend, loading, useRag, onToggleRag }: ChatBoxProps) {
    const [input, setInput] = useState("");
    const messagesEndRef = useRef<HTMLDivElement>(null);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    };

    useEffect(() => {
        scrollToBottom();
    }, [messages]);

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        if (input.trim() && !loading) {
            onSend(input);
            setInput("");
        }
    };

    return (
        <div className="flex flex-col h-full bg-gray-50/50">
            {/* Header */}
            <div className="sticky top-0 z-10 bg-white/80 backdrop-blur-md border-b border-gray-200/50 px-4 py-3">
                <div className="max-w-6xl mx-auto flex items-center justify-between">
                    <div className="flex items-center gap-3">
                        <div className="p-2 bg-blue-600/10 rounded-xl">
                            <Network className="w-6 h-6 text-blue-600" />
                        </div>
                        <div>
                            <h1 className="text-lg font-bold text-gray-800">EDU RAG Platform test</h1>
                        </div>
                    </div>

                    <div className="flex items-center bg-gray-100 p-1 rounded-lg">
                        <button
                            onClick={() => onToggleRag(false)}
                            className={`px-4 py-1.5 rounded-md text-sm font-medium transition-all ${!useRag ? "bg-white text-gray-800 shadow-sm" : "text-gray-500 hover:text-gray-700"
                                }`}
                        >
                            Chat thường
                        </button>
                        <button
                            onClick={() => onToggleRag(true)}
                            className={`px-4 py-1.5 rounded-md text-sm font-medium transition-all ${useRag ? "bg-blue-600 text-white shadow-sm" : "text-gray-500 hover:text-gray-700"
                                }`}
                        >
                            RAG Mode
                        </button>
                    </div>
                </div>
            </div>

            {/* Messages */}
            <div className="flex-1 overflow-y-auto">
                <div className="max-w-5xl mx-auto px-4 py-8 space-y-8">
                    {messages.length === 0 && (
                        <div className="flex flex-col items-center justify-center h-[60vh] text-gray-400">
                            <div className="p-4 bg-white rounded-full shadow-sm mb-4">
                                <MessageSquare className="w-8 h-8 text-blue-600/50" />
                            </div>
                            <h2 className="text-xl font-semibold text-gray-700 mb-2">Xin chào!</h2>
                            <p className="text-gray-500">Tôi có thể giúp gì cho bạn về nội quy lớp học hôm nay?</p>
                        </div>
                    )}

                    {messages.map((msg, idx) => (
                        <div
                            key={idx}
                            className={`flex gap-4 ${msg.role === "user" ? "justify-end" : "justify-start"}`}
                        >
                            {msg.role === "bot" && (
                                <div className="flex-shrink-0 w-8 h-8 rounded-full bg-white border border-gray-200 flex items-center justify-center mt-1 shadow-sm">
                                    <Bot className="w-5 h-5 text-blue-600" />
                                </div>
                            )}

                            <div
                                className={`max-w-[85%] sm:max-w-[75%] rounded-2xl px-6 py-4 shadow-sm ${msg.role === "user"
                                    ? "bg-blue-600 text-white"
                                    : "bg-white border border-gray-100 text-gray-800"
                                    }`}
                            >
                                <div className={`prose prose-sm max-w-none ${msg.role === "user" ? "prose-invert" : ""}`}>
                                    <ReactMarkdown>
                                        {msg.content}
                                    </ReactMarkdown>
                                </div>
                            </div>

                            {msg.role === "user" && (
                                <div className="flex-shrink-0 w-8 h-8 rounded-full bg-gray-800 flex items-center justify-center mt-1 shadow-sm">
                                    <User className="w-5 h-5 text-white" />
                                </div>
                            )}
                        </div>
                    ))}

                    {loading && (
                        <div className="flex justify-start gap-4">
                            <div className="flex-shrink-0 w-8 h-8 rounded-full bg-white border border-gray-200 flex items-center justify-center shadow-sm">
                                <Bot className="w-5 h-5 text-blue-600" />
                            </div>
                            <div className="bg-white border border-gray-100 rounded-2xl px-6 py-4 shadow-sm">
                                <div className="flex gap-1.5">
                                    <div className="w-2 h-2 bg-blue-600 rounded-full animate-bounce"></div>
                                    <div className="w-2 h-2 bg-blue-600 rounded-full animate-bounce [animation-delay:-0.15s]"></div>
                                    <div className="w-2 h-2 bg-blue-600 rounded-full animate-bounce [animation-delay:-0.3s]"></div>
                                </div>
                            </div>
                        </div>
                    )}
                    <div ref={messagesEndRef} />
                </div>
            </div>

            {/* Input */}
            <div className="bg-white/80 backdrop-blur-md border-t border-gray-200/50 p-4 pb-6">
                <div className="max-w-5xl mx-auto relative">
                    <form onSubmit={handleSubmit} className="relative shadow-lg rounded-2xl bg-white border border-gray-200 hover:border-blue-400 transition-colors focus-within:border-blue-500 focus-within:ring-4 focus-within:ring-blue-500/10 outline-none">
                        <input
                            type="text"
                            value={input}
                            onChange={(e) => setInput(e.target.value)}
                            placeholder="Nhập câu hỏi của bạn..."
                            className="w-full pl-6 pr-14 py-4 bg-transparent border-none focus:ring-0 text-gray-800 placeholder:text-gray-400 outline-none"
                            disabled={loading}
                        />
                        <button
                            type="submit"
                            disabled={!input.trim() || loading}
                            className="absolute right-2 top-2 p-2 bg-blue-600 text-white rounded-xl hover:bg-blue-700 disabled:bg-gray-100 disabled:text-gray-300 disabled:cursor-not-allowed transition-all active:scale-95"
                        >
                            <Send className="w-5 h-5" />
                        </button>
                    </form>
                    <p className="text-center text-xs text-gray-400 mt-3">
                        Hệ thống có thể mắc lỗi. Vui lòng kiểm tra lại thông tin quan trọng.
                    </p>
                </div>
            </div>
        </div>
    );
}