const API_BASE_URL = "http://localhost:8000/api";

export async function verifyPin(pin: string): Promise<boolean> {
    const res = await fetch(`${API_BASE_URL}/verify-pin`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ pin }),
    });
    return res.ok;
}

export async function chatWithRag(message: string): Promise<string> {
    const res = await fetch(`${API_BASE_URL}/chat/rag`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message }),
    });
    const data = await res.json();
    return data.answer;
}

export async function chatWithoutRag(message: string): Promise<string> {
    const res = await fetch(`${API_BASE_URL}/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message }),
    });
    const data = await res.json();
    return data.answer;
}