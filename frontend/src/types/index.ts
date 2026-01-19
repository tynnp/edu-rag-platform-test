export interface Message {
    role: "user" | "bot";
    content: string;
}

export interface ChatRequest {
    message: string;
}

export interface ChatResponse {
    answer: string;
    context?: string;
    use_rag: boolean;
}