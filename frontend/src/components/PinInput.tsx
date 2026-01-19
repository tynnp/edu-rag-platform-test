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
        <div className="w-full max-w-md p-8 bg-slate-800 rounded-2xl shadow-xl border border-slate-700">
            <h2 className="text-2xl font-bold text-center text-slate-100 mb-2">
                Xác thực bảo mật
            </h2>
            <p className="text-center text-slate-400 mb-8 text-sm">
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
                        className="w-full px-4 py-4 text-center text-3xl tracking-[1em] font-bold text-indigo-400 bg-slate-900 border-2 border-slate-700 rounded-xl focus:border-indigo-500 focus:outline-none focus:ring-4 focus:ring-indigo-500/10 transition-all placeholder:text-slate-700"
                        disabled={loading}
                        autoFocus
                    />
                </div>

                {error && (
                    <div className="p-3 bg-red-500/10 border border-red-500/20 text-red-400 text-sm text-center rounded-lg animate-pulse">
                        {error}
                    </div>
                )}

                <button
                    type="submit"
                    disabled={pin.length !== 6 || loading}
                    className="w-full py-4 bg-indigo-600 text-white font-semibold rounded-xl hover:bg-indigo-500 disabled:bg-slate-700 disabled:text-slate-500 disabled:cursor-not-allowed transition-all transform active:scale-[0.98] shadow-lg shadow-indigo-500/20"
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