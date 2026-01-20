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
        <div className="w-full max-w-md p-8 bg-white rounded-2xl shadow-xl border border-gray-200">
            <h2 className="text-2xl font-bold text-center text-gray-800 mb-2">
                Xác thực bảo mật
            </h2>
            <p className="text-center text-gray-500 mb-8 text-sm">
                Vui lòng nhập mã PIN để truy cập hệ thống
            </p>
            <form onSubmit={handleSubmit} className="space-y-6">
                <div>
                    <input
                        type="password"
                        maxLength={6}
                        value={pin}
                        onChange={(e) => setPin(e.target.value.replace(/\D/g, ""))}
                        placeholder="••••••"
                        className="w-full px-4 py-4 text-center text-3xl tracking-[1em] font-bold text-indigo-600 bg-gray-50 border-2 border-gray-200 rounded-xl focus:border-indigo-500 focus:outline-none focus:ring-4 focus:ring-indigo-500/10 transition-all placeholder:text-gray-300"
                        disabled={loading}
                        autoFocus
                    />
                </div>

                {error && (
                    <div className="p-3 bg-red-50 border border-red-200 text-red-600 text-sm text-center rounded-lg animate-pulse">
                        {error}
                    </div>
                )}

                <button
                    type="submit"
                    disabled={pin.length !== 6 || loading}
                    className="w-full py-4 bg-indigo-600 text-white font-semibold rounded-xl hover:bg-indigo-500 disabled:bg-gray-200 disabled:text-gray-400 disabled:cursor-not-allowed transition-all transform active:scale-[0.98] shadow-lg shadow-indigo-500/20"
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