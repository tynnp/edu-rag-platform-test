import { useState } from "react";
import PinInput from "../components/PinInput";
import { verifyPin } from "../services/api";

interface PinPageProps {
    onSuccess: () => void;
}

export default function PinPage({ onSuccess }: PinPageProps) {
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (pin: string) => {
        setLoading(true);
        setError("");
        try {
            const isValid = await verifyPin(pin);
            if (isValid) {
                onSuccess();
            } else {
                setError("Mã PIN không đúng. Vui lòng thử lại.");
            }
        } catch (err) {
            setError("Có lỗi xảy ra. Vui lòng thử lại sau.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen bg-slate-950 flex items-center justify-center p-4">
            <PinInput onSubmit={handleSubmit} error={error} loading={loading} />
        </div>
    );
}