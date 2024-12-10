import React, { useState } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "../components/ui/card";
import { Input } from "../components/ui/input";
import { Button } from "../components/ui/button";
import { LinkIcon } from "lucide-react";

interface JobInputFormProps {
    onSubmit: (url: string) => void;
}

const JobInputForm: React.FC<JobInputFormProps> = ({ onSubmit }) => {
    const [url, setUrl] = useState("");

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        if (url) onSubmit(url);
    };

    return (
        <Card className="w-full shadow-lg">
            <CardHeader>
                <CardTitle className="text-2xl font-bold text-primary">
                    Generate Cold Email
                </CardTitle>
            </CardHeader>
            <CardContent>
                <form onSubmit={handleSubmit} className="space-y-4">
                    <div className="flex flex-col space-y-2">
                        <label htmlFor="jobUrl" className="text-sm font-medium text-gray-700">
                            Job Posting URL
                        </label>
                        <div className="flex space-x-2">
                            <div className="relative flex-1">
                                <LinkIcon className="absolute left-3 top-3 h-5 w-5 text-gray-400" />
                                <Input
                                    id="jobUrl"
                                    type="url"
                                    value={url}
                                    onChange={(e) => setUrl(e.target.value)}
                                    className="pl-10"
                                    placeholder="https://example.com/job-posting"
                                    required
                                />
                            </div>
                            <Button type="submit" className="bg-primary hover:bg-primary/90">
                                Generate
                            </Button>
                        </div>
                    </div>
                </form>
            </CardContent>
        </Card>
    );
};

export default JobInputForm;