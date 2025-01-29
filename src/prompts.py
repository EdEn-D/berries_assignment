

diarization_prompt=\
'''This is a conversation between a therapist and his patient. Add speaker labels for the conversation. Note that there is no clear distinction in the text below for which speaker is who this will have to be inferred from the context.

example:
input text: So before we get started, I just wanted to talk about a couple of things. Okay, I am ready. Great so the first rule is that everything said here is confidential. Alright, I understand

output text:
Therapist: So before we get started, I just wanted to talk about a couple of things.
Patient:  Okay, I am ready.
Therapist: Great so the first rule is that everything said here is confidential.
Patient: Alright, I understand

Below is the conversation transcript:
'''

notes_prompts=\
'''You are a scribe for a therapist. Your task is to take notes on the transcript of the session. In your notes you must concisely, clearly and professionally take notes on the conversation focusing on  information directly related to the session’s objectives, treatment goals, or concerns raised by the patient. You must record facts and you may use the patients quotes as well. Outline the notes in the SOAP format:

1. Subjective (S):
Capture the patient’s reported feelings, concerns, or symptoms in their own words.
Example: "I feel like I’m not making progress at work."
2. Objective (O):
Document observable facts or therapist observations (e.g., demeanor, tone of voice, body language).
Example: The patient appeared anxious, frequently fidgeting with their hands.
3. Assessment (A):
Note the therapist’s interpretation or insights based on the session. Tie these to therapy goals.
Example: Anxiety levels appear higher than last session, possibly due to the new job role.
4. Plan (P):
Include goals, interventions discussed, or homework assigned to the patient.
Example: The patient will practice grounding exercises and reflect on three positive work interactions this week.

Below is the conversation transcript:
'''

notes_formatting=\
'''
Write the notes with the guidelines you provided in the first answer. 

HTML Output Formatting: 
 - The generated notes should be outputted as HTML that can be rendered in a React app. 
 - Each section (e.g., Subjective, Objective, etc.) and subsection should be in bold. 
 - Direct quotes from the client should also be in bold. 
'''