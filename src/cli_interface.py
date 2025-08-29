from colorama import Fore, Style
from .llm_agent import get_recommendation

def print_header(text):
    print(f"\n{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{text:^50}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")

def collect_patient_info():
    print_header("Patient Information")
    
    print("Please provide the following information:")
    
    #Patient Information
    age = int(input("Age: "))
    gender = input("Gender (male/female/other): ")
    print("\nDescribe your symptoms in detail:")
    symptoms = input("Symptoms: ")
    print("\nMedical Information:")
    allergies = input("Drug allergies (or 'none'): ")
    medications = input("Current medications (or 'none'): ")
    medical_conditions = input("Medical conditions (or 'none'): ")
    pregnancy_status = input("Pregnancy status (pregnant/not pregnant/not applicable): ")
    
    return {
        "age": age,
        "gender": gender,
        "symptoms": symptoms,
        "allergies": allergies,
        "medications": medications,
        "medical_conditions": medical_conditions,
        "pregnancy_status": pregnancy_status
    }

def display_result(recommendation):
    print_header("AI Recommendation")
    
    if "error" in recommendation:
        print(f"{Fore.RED}Error: {recommendation['error']}{Style.RESET_ALL}")
        return
    
    print(f"Diagnosis: {recommendation.get('diagnosis', 'Unknown')}")
    print(f"Safety Status: {recommendation.get('safety_status', 'Unknown').upper()}")
    
    confidence = recommendation.get('confidence_score', 0)
    if confidence:
        print(f"Confidence: {confidence:.1%}")
    
    treatment = recommendation.get('treatment', '')
    if treatment and treatment != "Refer to doctor":
        print(f"Treatment: {treatment}")
        dosage = recommendation.get('dosage', '')
        duration = recommendation.get('duration', '')
        if dosage:
            print(f"Dosage: {dosage}")
        if duration:
            print(f"Duration: {duration}")
    else:
        print(f"Treatment: {treatment}")
        escalation_reason = recommendation.get('escalation_reason', '')
        if escalation_reason:
            print(f"Reason: {escalation_reason}")
    
    print(f"\n{Fore.CYAN}Clinical Reasoning:{Style.RESET_ALL}")
    print(recommendation.get('reasoning', 'No reasoning provided'))

    print(f"\n{Fore.YELLOW}Follow-up:{Style.RESET_ALL}")
    print(recommendation.get('follow_up', 'Please consult a healthcare provider'))

def start_consultation():
    try:
        print(f"{Fore.CYAN}=== Simple LLM UTI Agent ==={Style.RESET_ALL}")
        print(f"{Fore.YELLOW}This is a prototype system.{Style.RESET_ALL}\n")
        
        patient_info = collect_patient_info()
        
        print(f"\n{Fore.GREEN}Analyzing your information...{Style.RESET_ALL}")
        recommendation = get_recommendation(patient_info)
        
        display_result(recommendation)
        
        print(f"\n{Fore.YELLOW}Disclaimer: This is for educational purposes only.{Style.RESET_ALL}")
        
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Consultation cancelled.{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}Error: {e}{Style.RESET_ALL}")
