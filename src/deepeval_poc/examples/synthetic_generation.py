from typing import List
from deepeval.synthesizer import Synthesizer
from deepeval.synthesizer.config import StylingConfig, EvolutionConfig
from deepeval.synthesizer.types import Evolution
from deepeval.dataset.golden import Golden
from deepeval.models import GPTModel
import deepeval_poc


def main():
    model = GPTModel(model="gpt-4o")

    styling_config = StylingConfig(
        scenario="Healthcare virtual assistant helping patients with medical records and appointments",
        task="Handle patient inquiries about medical history, medications, appointments, test results, and billing while maintaining HIPAA compliance and verifying patient identity",
        input_format="Patient questions about their medical records, prescriptions, appointments, insurance, and health information",
        expected_output_format="Professional, HIPAA-compliant responses that verify identity before sharing sensitive information, provide accurate medical data, and maintain patient confidentiality"
    )

    evolution_config = EvolutionConfig(
        evolutions={
            Evolution.REASONING: 0.25,
            Evolution.MULTICONTEXT: 0.2,
            Evolution.CONCRETIZING: 0.15,
            Evolution.CONSTRAINED: 0.15,
            Evolution.COMPARATIVE: 0.1,
            Evolution.HYPOTHETICAL: 0.1,
            Evolution.IN_BREADTH: 0.05,
        }
    )

    synthesizer = Synthesizer(
        model=model,
        async_mode=True,
        styling_config=styling_config,
        evolution_config=evolution_config
    )

    contexts = [
        [
            "Patient: Sarah Chen, DOB: 03/15/1985, MRN: 2024-45678. "
            "Current Medications: Metformin 500mg twice daily, Lisinopril 10mg once daily. "
            "Recent Visit: Annual checkup on 12/10/2023 with Dr. James Wilson. "
            "Lab Results: HbA1c 6.2%, Blood Pressure 125/80, Cholesterol 190 mg/dL. "
            "Upcoming: Follow-up appointment February 15, 2024 at 2:00 PM."
        ],
        [
            "Patient: Michael Torres, DOB: 08/22/1972, MRN: 2024-89012. "
            "Diagnosis: Hypertension Stage 2, Type 2 Diabetes. "
            "Allergies: Penicillin (severe), Sulfa drugs (moderate). "
            "Recent Procedure: Cardiac stress test on 11/30/2023 - Results: Normal. "
            "Prescriptions: Insulin glargine 20 units bedtime, Atorvastatin 40mg evening. "
            "Insurance: BlueCross Policy #BC-334455, $30 specialist copay."
        ],
        [
            "Patient: Jennifer Park, DOB: 06/18/1990, MRN: 2024-23456. "
            "Surgical History: Appendectomy 2015, C-section 2020. "
            "Current Conditions: Postpartum hypothyroidism, managed well. "
            "Medications: Levothyroxine 75mcg daily. "
            "Recent Labs (01/05/2024): TSH 2.1 mIU/L (normal), Free T4 1.3 ng/dL (normal). "
            "Billing: Last visit $150, Insurance paid $120, Patient owes $30."
        ],
        [
            "Patient: Robert Lee, DOB: 11/30/1968, MRN: 2024-67890. "
            "Chief Complaint: Chronic lower back pain, managed with physical therapy. "
            "Medications: Ibuprofen 600mg as needed, Gabapentin 300mg three times daily. "
            "Recent MRI (12/20/2023): Mild disc degeneration L4-L5, no herniation. "
            "Referrals: Physical therapy - 12 sessions authorized, 8 remaining. "
            "Next appointment: Pain management consultation January 25, 2024."
        ],
        [
            "Patient: Amanda Rodriguez, DOB: 09/05/1995, MRN: 2024-34567. "
            "Preventive Care: Flu shot administered 10/15/2023. "
            "Upcoming: Mammogram screening due (turned 30), schedule by March 2024. "
            "Family History: Mother - breast cancer at age 52, Father - heart disease. "
            "Recent screening: Cholesterol panel normal, recommended annual monitoring. "
            "Portal access: Username amanda.r2024, security setup required."
        ],
    ]

    print("\nGenerating test cases...")

    goldens = synthesizer.generate_goldens_from_contexts(
        contexts=contexts,
        max_goldens_per_context=20,
        include_expected_output=True
    )

    print(f"Generated {len(goldens)} medical conversation test cases")

    print("Sample test cases:\n")
    for i, golden in enumerate(goldens[:5], 1):
        print(f"{i}. INPUT: {golden.input}")
        print(f"   OUTPUT: {golden.expected_output[:100]}...")
        print()

    print(f"\nTotal test cases ready for evaluation: {len(goldens)}")


if __name__ == "__main__":
    main()
