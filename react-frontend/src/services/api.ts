import axios from "axios";

const API_BASE_URL = "http://localhost:8000"; 
export const parseJobDescription = async (jobUrl: string) => {
    const response = await axios.post(`${API_BASE_URL}/job-description-parser`, {
        job_url: jobUrl,
    });
    return response.data;
};

export const generateColdEmail = async (jobUrl: string) => {
    const response = await axios.post(`${API_BASE_URL}/cold-email-generator`, {
        job_url: jobUrl,
    });
    return response.data;
};