knowledge_base = {
    "Rule1": {
        "fever": "yes",
        "mucous": "no",
        "cough": "yes",
        "sore throat": "yes",
        "runny or stuffy nose": "yes",
        "body aches": "yes",
        "head aches": "yes",
        "fatigue or tiredness": "yes",
        "vomiting": "yes",
        "shortness of breath": "no",
        "sharp chest pain that gets worse with deep breathing": "no",
        "loss of appetite": "no",
        "confusion": "no",
        "whisteling sound when breathing": "no"
    },
    "Rule2": {
        "fever": "yes",
        "cough": "yes",
        "mucous": "yes",
        "sore throat": "no",
        "runny or stuffy nose": "no",
        "body aches": "no",
        "head aches": "no",
        "fatigue or tiredness": "yes",
        "vomiting": "yes",
        "shortness of breath": "yes",
        "sharp chest pain that gets worse with deep breathing or cough": "yes",
        "loss of appetite": "yes",
        "confusion": "yes",
        "whisteling sound when breathing": "no"
    },
    "Rule3": {
        "fever": "yes",
        "cough": "yes",
        "mucous": "no",
        "sore throat": "no",
        "runny or stuffy nose": "yes",
        "body aches": "no",
        "head aches": "no",
        "fatigue or tiredness": "yes",
        "vomiting": "no",
        "shortness of breath": "yes",
        "sharp chest pain that gets worse with deep breathing or cough": "no",
        "loss of appetite": "no",
        "confusion": "no",
        "whisteling sound when breathing": "yes"
    },
    "action": {
        "action1": "Disease : flu ; Remedy: Drink plenty of water to avoid dehydration, take rest, take paracetamol",
        "action2": "Disease : Pneumonia ; Remedy : antibiotics/antiviral, rest, stay hydrated",
        "action3": "Disease : Bronchitis, Remedy : Tests: Nasal swabs, Chest X-ray, Blood tests, Sputum test, Pulmonary function tests"
    }
}

fever = input("Suffering from Fever?")
cough = input("Suffering from Cough?")
mucous = input("Having Green or yellowish or bloody mucous in cough?")
soreThroat = input("Having Sore Throat?")
runnyNose = input("Having Runny nose?")
bodyAche = input("Having body aches?")
headAche = input("Having headaches")
fatigue = input("Facing fatigue or tiredness?")
vomiting = input("Facing vomiting?")
breathShort = input("Facing shortness of breath?")
chestPain = input(
    "Having sharp chest pain that gets worse with deep breathing or coughing?")
appetite = input("Facing loss of appetite?")
confusion = input("Facing confusion in old age? ")
whisteling = input("Having whisteling sound when breathing?")


def inferenceEngine():
    if (
        fever == knowledge_base['Rule1']['fever'] and
        cough == knowledge_base['Rule1']['cough'] and
        mucous == knowledge_base['Rule1']['mucous'] and
        soreThroat == knowledge_base['Rule1']['sore throat'] and
        runnyNose == knowledge_base['Rule1']['runny or stuffy nose'] and
        bodyAche == knowledge_base['Rule1']['body aches'] and
        headAche == knowledge_base['Rule1']['head aches'] and
        fatigue == knowledge_base['Rule1']['fatigue or tiredness'] and
        vomiting == knowledge_base['Rule1']['vomiting'] and
        breathShort == knowledge_base['Rule1']['shortness of breath'] and
        chestPain == knowledge_base['Rule1']['sharp chest pain that gets worse with deep breathing'] and
        appetite == knowledge_base['Rule1']['loss of appetite'] and
        confusion == knowledge_base['Rule1']['confusion'] and
        whisteling == knowledge_base['Rule1']['whisteling sound when breathing']
    ):
        print(knowledge_base['action']['action1'])
    elif (
        fever == knowledge_base['Rule2']['fever'] and
        cough == knowledge_base['Rule2']['cough'] and
        mucous == knowledge_base['Rule2']['mucous'] and
        soreThroat == knowledge_base['Rule2']['sore throat'] and
        runnyNose == knowledge_base['Rule2']['runny or stuffy nose'] and
        bodyAche == knowledge_base['Rule2']['body aches'] and
        headAche == knowledge_base['Rule2']['head aches'] and
        fatigue == knowledge_base['Rule2']['fatigue or tiredness'] and
        vomiting == knowledge_base['Rule2']['vomiting'] and
        breathShort == knowledge_base['Rule2']['shortness of breath'] and
        chestPain == knowledge_base['Rule2']['sharp chest pain that gets worse with deep breathing or cough'] and
        appetite == knowledge_base['Rule2']['loss of appetite'] and
        confusion == knowledge_base['Rule2']['confusion'] and
        whisteling == knowledge_base['Rule2']['whisteling sound when breathing']
    ):
        print(knowledge_base['action']['action2'])
    elif (
        fever == knowledge_base['Rule3']['fever'] and
        cough == knowledge_base['Rule3']['cough'] and
        mucous == knowledge_base['Rule3']['mucous'] and
        soreThroat == knowledge_base['Rule3']['sore throat'] and
        runnyNose == knowledge_base['Rule3']['runny or stuffy nose'] and
        bodyAche == knowledge_base['Rule3']['body aches'] and
        headAche == knowledge_base['Rule3']['head aches'] and
        fatigue == knowledge_base['Rule3']['fatigue or tiredness'] and
        vomiting == knowledge_base['Rule3']['vomiting'] and
        breathShort == knowledge_base['Rule3']['shortness of breath'] and
        chestPain == knowledge_base['Rule3']['sharp chest pain that gets worse with deep breathing or cough'] and
        appetite == knowledge_base['Rule3']['loss of appetite'] and
        confusion == knowledge_base['Rule3']['confusion'] and
        whisteling == knowledge_base['Rule3']['whisteling sound when breathing']
    ):
        print(knowledge_base['action']['action3'])
    else:
        print("No matching rule found.")


# Example usage
inferenceEngine()
