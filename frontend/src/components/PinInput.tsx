import { useState } from "react";
import { Loader2 } from "lucide-react";

interface PinInputProps {
    onSubmit: (pin: string) => void;
    error?: string;
    loading?: boolean;
}

export default function PinInput({ onSubmit, error, loading }: PinInputProps) {
    const [pin, setPin] = useState("");

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        if (pin.length === 6) {
            onSubmit(pin);
        }
    };

    return (
        <div className="w-full max-w-md p-8 bg-white rounded-2xl shadow-xl">
            <h2 className="text-2xl font-bold text-center text-gray-800 mb-6">
                Nhập mã PIN
            </h2>
            <form onSubmit={handleSubmit} className="space-y-6">
                <div>
                    <input
                        type="password"
                        maxLength={6}
                        value={pin}
                        onChange={(e) => setPin(e.target.value.replace(/\D/g, ""))}
                        placeholder="••••••"
                        className="w-full px-4 py-4 text-center text-3xl tracking-[1em] font-bold text-gray-700 border-2 border-gray-200 rounded-xl focus:border-blue-500 focus:outline-none transition-colors"
                        disabled={loading}
                        autoFocus
                    />
                </div>

                {error && (
                    <div className="p-3 bg-red-50 text-red-500 text-sm text-center rounded-lg animate-pulse">
                        {error}
                    </div>
                )}

                <button
                    type="submit"
                    disabled={pin.length !== 6 || loading}
                    className="w-full py-4 bg-blue-600 text-white font-semibold rounded-xl hover:bg-blue-700 disabled:bg-gray-300 disabled:cursor-not-allowed transition-all transform active:scale-[0.98]"
                >
                    {loading ? (
                        <span className="flex items-center justify-center gap-2">
                            <Loader2 className="animate-spin h-5 w-5" />
                            Đang xác thực...
                        </span>
                    ) : (
                        "Truy cập"
                    )}
                </button>
            </form>
        </div>
    );
}