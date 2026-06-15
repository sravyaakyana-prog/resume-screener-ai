document.addEventListener("DOMContentLoaded", () => {

    const btn = document.getElementById("btn");

    // 🌐 YOUR RENDER BACKEND URL
    const API_URL = "https://resume-screener-backend-t6pd.onrender.com";

    btn.addEventListener("click", async () => {

        const fileInput = document.getElementById("resume");
        const jdInput = document.getElementById("jd");
        const output = document.getElementById("output");

        if (!fileInput.files.length) {
            alert("Upload PDF first");
            return;
        }

        if (!jdInput.value.trim()) {
            alert("Enter Job Description");
            return;
        }

        output.innerText = "⏳ Analyzing resume...";

        const formData = new FormData();

        // ⚠️ MUST MATCH FASTAPI BACKEND
        formData.append("file", fileInput.files[0]);
        formData.append("jd", jdInput.value);

        try {
            const res = await fetch(`${API_URL}/analyze`, {
                method: "POST",
                body: formData
            });

            if (!res.ok) {
                throw new Error("Server error: " + res.status);
            }

            const data = await res.json();

            const matched = Array.isArray(data.matched_skills)
                ? data.matched_skills.join(", ")
                : "None";

            const missing = Array.isArray(data.missing_skills)
                ? data.missing_skills.join(", ")
                : "None";

            output.innerText =
`📊 Score: ${data.score}

✅ Matched Skills:
${matched}

❌ Missing Skills:
${missing}

🧠 Reason:
${data.reason || data.feedback || "N/A"}`;

        } catch (err) {
            output.innerText = "❌ Error: " + err.message;
        }
    });

});