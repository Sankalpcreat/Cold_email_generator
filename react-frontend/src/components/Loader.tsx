import React from "react";
import { Loader2 } from "lucide-react";

const Loader: React.FC = () => {
    return (
        <div className="flex flex-col items-center justify-center p-8 space-y-4">
            <Loader2 className="h-8 w-8 animate-spin text-primary" />
            <p className="text-sm text-gray-500">Generating your email...</p>
        </div>
    );
};

export default Loader;