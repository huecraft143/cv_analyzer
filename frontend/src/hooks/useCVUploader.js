import { useState } from "react";

export default function useCVUploader() {
    const [data, setData] = useState(null);
    const [cvFile, setCVFile] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const uploadCV = async (file) => {
        setLoading(true);
        setError(null);
        setData(null);
        const formData = new FormData();
        formData.append("file", file);

        try {
            const response = await fetch("http://localhost:8000/api/upload", {
                method: "POST",
                body: formData,
            });

            if (!response.ok) {
                throw new Error("Failed to upload CV");
            }
            const data = await response.json();
            setCVFile(data.file);
            setData(data);
        }
        catch(error) {
            setError(error.message);
        } finally {
            setLoading(false);
        }
    };
        return {
            data,
            loading,
            error,
            uploadCV
        };
}