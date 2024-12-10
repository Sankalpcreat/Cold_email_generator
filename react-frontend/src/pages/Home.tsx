import React, { useState } from "react";
import JobInputForm from "../components/JobInputForm";
import OutputCard from "../components/OutputCard";
import Loader from "../components/Loader";
import { parseJobDescription, generateColdEmail } from "../services/api";
import { Card, CardContent } from "../components/ui/card";

const Home: React.FC = () => {
    const [jobDescription, setJobDescription] = useState<string | null>(null);
    const [coldEmail, setColdEmail] = useState<string | null>(null);
    const [loading, setLoading] = useState(false);

    const handleJobUrlSubmit = async (url: string) => {
        setLoading(true);
        try {
            const description = await parseJobDescription(url);
            setJobDescription(JSON.stringify(description, null, 2));

            const email = await generateColdEmail(url);
            setColdEmail(JSON.stringify(email, null, 2));
        } catch (error) {
            console.error("Error generating email:", error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen bg-gray-50">
            <div className="container mx-auto px-4 py-8">
                <div className="max-w-4xl mx-auto space-y-8">
                    <div className="text-center space-y-2">
                        <h1 className="text-4xl font-bold text-primary">
                            Cold Email Generator
                        </h1>
                        <p className="text-gray-600">
                            Generate personalized cold emails based on job descriptions
                        </p>
                    </div>

                    <JobInputForm onSubmit={handleJobUrlSubmit} />

                    {loading ? (
                        <Card>
                            <CardContent>
                                <Loader />
                            </CardContent>
                        </Card>
                    ) : (
                        <div className="grid grid-cols-1 gap-6">
                            {jobDescription && (
                                <OutputCard
                                    title="Job Description Analysis"
                                    content={jobDescription}
                                    className="flex flex-col"
                                />
                            )}
                            {coldEmail && (
                                <OutputCard
                                    title="Generated Cold Email"
                                    content={coldEmail}
                                    className="flex flex-col"
                                />
                            )}
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default Home;