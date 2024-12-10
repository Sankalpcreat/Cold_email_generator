import React from "react";
import { Card, CardContent, CardHeader, CardTitle } from "../components/ui/card";
import { Button } from "../components/ui/button";
import { Copy } from "lucide-react";

interface OutputCardProps {
    title: string;
    content: string;
}

const OutputCard: React.FC<OutputCardProps> = ({ title, content }) => {
    const handleCopy = () => {
        navigator.clipboard.writeText(content);
    };

    return (
        <Card className="w-full shadow-lg">
            <CardHeader className="flex flex-row items-center justify-between">
                <CardTitle className="text-lg font-semibold text-primary">
                    {title}
                </CardTitle>
                <Button
                    variant="outline"
                    size="sm"
                    onClick={handleCopy}
                    className="flex items-center gap-2"
                >
                    <Copy className="h-4 w-4" />
                    Copy
                </Button>
            </CardHeader>
            <CardContent>
                <pre className="bg-gray-50 p-4 rounded-lg text-sm overflow-x-auto whitespace-pre-wrap">
                    {content}
                </pre>
            </CardContent>
        </Card>
    );
};

export default OutputCard;