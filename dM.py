from groq import Groq
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def llm_response(symptoms):
    completion = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """You are an AI medical assistant designed to assist patients by analyzing their symptoms. When presented with the following symptoms: '{symptoms}', respond with empathy and recommend relevant laboratory tests that may help in diagnosing their condition. Ensure your response can accommodate symptoms in both Swahili and English.
                Instructions:
                1. **Empathetic Acknowledgment:** Start your response with a sympathetic remark regarding the symptoms the patient is experiencing.
                2. **List Potential Diseases:** Based on the symptoms, list possible diseases that could be indicated.
                3. **Focus on Provided Symptoms:** Use only the symptoms listed in '{symptoms}' to determine appropriate lab tests.
                4. **Concise Suggestions:** Recommend specific lab tests that are directly related to these symptoms, without adding explanations or diagnoses.
                5. **No Extra Content:** Provide only the names of suggested lab tests without additional comments or text.
                6. **Conclusion with Takeaway:** End your response with a takeaway statement, advising the patient to upload an image of their test results for further assistance.
                7. **Language Response :** in English ;
                8. ** Responses format:** the response should be in - - and the response list should be in the following format "\n 1.,\n 2.,\n 3

                Your response should demonstrate care and professionalism while clearly listing potential diseases, the necessary lab tests, and a concluding statement about uploading test results."""
            },
            {
                "role": "user",
                "content": f"symptoms: {symptoms}"
            },
        ],
        temperature=0.5,
        max_tokens=1024,
        top_p=0.65,
        stream=True,
        stop=None,
    )
    result=[]
    for chunk in completion:
        res=chunk.choices[0].delta.content or ""
        result.append(res.replace("\n", ""))
    return "\n".join(result)


# llm_response("Fever")

