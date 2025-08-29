import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def create_system_prompt():
    return """You are a medical AI assistant specializing in UTI diagnosis and treatment. You must:

1. **Safety First**: Always prioritize patient safety
2. **Follow Guidelines**: Use established clinical guidelines for UTI treatment
3. **Be Conservative**: When in doubt, recommend medical evaluation
4. **Provide Reasoning**: Explain your clinical reasoning
5. **Consider Contraindications**: Check for drug allergies and contraindications

**UTI Symptoms**: frequent urination, burning during urination, urgent need to urinate, cloudy urine, strong smelling urine, pelvic pain, lower back pain

**Emergency Symptoms**: fever, chills, nausea, vomiting, severe pain, blood in urine, confusion, dizziness, shortness of breath

**Available Antibiotics**:
- Nitrofurantoin: 100mg twice daily for 5 days (contraindicated in pregnancy, kidney disease, allergies)
- Trimethoprim: 200mg twice daily for 3 days (contraindicated in pregnancy, allergies)
- Ciprofloxacin: 250mg twice daily for 3 days (contraindicated in pregnancy, allergies)

**Safety Rules**:
- Patients under 18: Refer to doctor
- Emergency symptoms: Immediate medical attention
- Pregnancy: Refer to doctor
- Diabetes/kidney disease: Refer to doctor
- Drug allergies: Avoid contraindicated medications

Respond with a JSON object containing:
{
    "safety_status": "safe/unsafe/emergency",
    "diagnosis": "UTI likely/UTI unlikely/Needs medical evaluation",
    "treatment": "antibiotic_name or null",
    "dosage": "dosage_info or null",
    "duration": "duration_info or null",
    "escalation_reason": "reason for escalation or null",
    "follow_up": "follow-up instructions",
    "confidence_score": 0.0-1.0,
    "reasoning": "clinical reasoning"
}"""

def create_user_prompt(patient_info):
    
    return f"""Patient Information:
- Age: {patient_info['age']}
- Gender: {patient_info['gender']}
- Symptoms: {patient_info['symptoms']}
- Allergies: {patient_info['allergies']}
- Current Medications: {patient_info['medications']}
- Medical Conditions: {patient_info['medical_conditions']}
- Pregnancy Status: {patient_info['pregnancy_status']}

Analyze this patient using the clinical algorithm and provide a recommendation."""

def get_recommendation(patient_info):
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return {
                "error": "OpenAI API key not found. Please set OPENAI_API_KEY environment variable."
            }
        
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": create_system_prompt()},
                {"role": "user", "content": create_user_prompt(patient_info)}
            ],
            temperature=0.1,
            max_tokens=800
        )
        
        content = response.choices[0].message.content
        start_idx = content.find('{')
        end_idx = content.rfind('}') + 1
        json_str = content[start_idx:end_idx]
        result = json.loads(json_str)
        
        return result
        
    except Exception as e:
        return {
            "safety_status": "unsafe",
            "diagnosis": "Needs evaluation",
            "treatment": "Refer to doctor",
            "dosage": "",
            "duration": "",
            "escalation_reason": "System error occurred",
            "follow_up": "Please consult a healthcare provider immediately",
            "confidence_score": 0.0,
            "reasoning": f"System error: {str(e)}"
        }
