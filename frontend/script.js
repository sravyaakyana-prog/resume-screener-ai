document.addEventListener("DOMContentLoaded", () => {

    const btn = document.getElementById("btn");

    btn.addEventListener("click", async () => {

        const fileInput = document.getElementById("resume");
        const jdInput = document.getElementById("jd");
        const output = document.getElementById("output");

        console.log("✅ Button clicked");

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
        formData.append("file", fileInput.files[0]);
        formData.append("jd", jdInput.value);

        try {
            const res = await fetch("http://127.0.0.1:8000/analyze", {
                method: "POST",
                body: formData
            });

            if (!res.ok) {
                throw new Error("Server error: " + res.status);
            }

            const data = await res.json();

            console.log("🔥 BACKEND RESPONSE:", data);

            // ✅ FIX: ensure arrays are properly joined
            const matched = Array.isArray(data.matched_skills)
                ? data.matched_skills.join(", ")
                : "None";

            const missing = Array.isArray(data.missing_skills)
                ? data.missing_skills.join(", ")
                : "None";

            const suggestions = Array.isArray(data.suggestions)
                ? data.suggestions.join("\n")
                : "None";

            output.innerText =
`📊 Score: ${data.score}

✅ Matched Skills:
${matched || "None"}

❌ Missing Skills:
${missing || "None"}

🧠 Reason:
${data.reason}

💡 Suggestions:
${suggestions || "None"}`;

        } catch (err) {
            console.error("❌ ERROR:", err);
            output.innerText = "❌ Error: " + err.message;
        }
    });

});