# Product Requirements Document (PRD)
# Personal AI Assistant Desk Robot

**Project Name:** Personal AI Assistant Robot  
**Version:** Version 1 Planning Draft  
**Owner:** Alex Pham  
**Document Type:** Product Requirements Document  
**Status:** Draft  
**Last Updated:** 2026-06-18  

---

## 1. Product Summary

The Personal AI Assistant Desk Robot is a beginner-friendly hardware and software project. The goal is to build a small, cute, 3D-printed desk robot that acts as a physical host for an AI assistant.

The robot will not be a fully functional moving robot in Version 1. Instead, it will behave more like a custom smart assistant device. The user should be able to speak to it, ask useful questions, and receive spoken responses. A small screen should display helpful information when needed, such as the assistant status, today's calendar events, weather, reminders, or a simple robot face.

The project is also a learning project. It should help the builder learn electronics, microcontrollers, Raspberry Pi or similar small computers, basic wiring, displays, microphones, speakers, APIs, and eventually 3D-printed enclosure design.

Version 1 should prioritize building a simple working assistant over building a polished robot body. The physical robot shell can come after the main electronics and software are proven to work.

---

## 2. Problem Statement

The builder wants a personal AI assistant that feels more personal and physical than using ChatGPT on a phone or computer. Instead of opening an app, the builder wants a small desk companion that can be asked questions out loud.

The assistant should eventually answer questions like:

- “What do I have to do today?”
- “What is on my Google Calendar?”
- “What is the weather today?”
- “Do I have any important emails?”
- “Remind me what I should focus on next.”

The challenge is that the builder is new to electronics and robotics. The project must therefore be designed in a way that is beginner-friendly, safe, affordable, and expandable.

---

## 3. Target User

### Primary User

The primary user is the builder, Alex, who wants to learn electronics and build a useful personal assistant device.

### User Skill Level

Assume the user:

- Has very little electronics experience.
- Owns a simple Arduino starter kit.
- Has programming experience but may not know hardware programming well.
- Needs clear explanations for wiring, components, power, APIs, and setup.
- Wants to understand why each decision is being made.

### User Needs

The user needs:

- Step-by-step guidance.
- Safe beginner-friendly hardware choices.
- Clear explanations of each component.
- A realistic budget-conscious plan.
- A project structure that allows progress in small wins.
- A system that can grow over time.

---

## 4. Product Vision

The long-term vision is to create a small personal AI desk companion that can help with daily planning, communication, and information retrieval.

In the future, the robot may have:

- A cute 3D-printed body.
- A screen-based animated face.
- Voice conversation.
- Calendar summaries.
- Gmail summaries.
- Weather reports.
- LED status lights.
- Buttons or touch input.
- Optional movement, such as a moving head or arms.
- A modular software system for adding more services.

Version 1 should lay the foundation for this vision without becoming too complicated.

---

## 5. Version 1 Scope

Version 1 should focus on the simplest useful version of the robot assistant.

### Version 1 Must Include

1. A main computing device that can connect to Wi-Fi.
2. A microphone or voice input method.
3. A speaker or audio output method.
4. A small screen for visual information.
5. Basic assistant software that can receive a question and respond.
6. A simple status display.
7. A software structure that can later support Google Calendar, Gmail, weather, and other tools.
8. Beginner-safe power setup.

### Version 1 Should Include If Budget Allows

1. Google Calendar integration.
2. Weather integration.
3. A simple robot face or expression display.
4. LED status lights.
5. A button for push-to-talk.
6. A basic 3D-printed or temporary enclosure.

### Version 1 Does Not Need

1. Movement.
2. Wheels.
3. Robotic arms.
4. Walking.
5. Battery power.
6. Custom circuit boards.
7. Advanced wake word detection.
8. Full always-listening voice assistant behavior.
9. Fully polished 3D-printed body.
10. Complex animation.

---

## 6. Goals

### Product Goals

- Build a working desk assistant that feels like a physical AI companion.
- Allow the user to ask questions using voice.
- Allow the assistant to respond using speech.
- Show useful information on a screen.
- Create a foundation for personal app integrations.
- Keep the first version realistic and affordable.

### Learning Goals

The project should teach the user:

- What Arduino is good for.
- What Raspberry Pi or a similar mini-computer is good for.
- Why different boards are used for different jobs.
- How microphones, speakers, and displays connect to a computer.
- How APIs work at a basic level.
- How Google Calendar and Gmail integrations may be added.
- How to test electronics safely.
- How to build a project in phases.

### Budget Goal

The target budget for Version 1 is around **$150**. This is a target, not a strict maximum. If the best beginner-friendly version costs more, the project documentation should explain why and identify cheaper alternatives.

---

## 7. Non-Goals

The following are intentionally out of scope for Version 1:

- Building a robot that walks, drives, or moves around.
- Creating a humanoid robot with arms and joints.
- Building a battery-powered portable device.
- Designing custom printed circuit boards.
- Training a custom AI model.
- Building a fully offline AI assistant.
- Creating a commercial product.
- Supporting multiple users.
- Handling sensitive Gmail actions like sending, deleting, or replying to emails automatically.
- Making the robot autonomous.

These may be considered in future versions only after Version 1 works reliably.

---

## 8. Recommended Product Strategy

The project should be built in layers.

### Layer 1: Learn the Basics

Use the existing Arduino kit to learn simple electronics:

- Turn an LED on and off.
- Read a button press.
- Use a sensor.
- Understand basic wiring.
- Understand power, ground, resistors, and breadboards.

This layer is for learning, not for powering the whole AI assistant.

### Layer 2: Build the Assistant Core

Use a Raspberry Pi or similar mini-computer as the main brain because the assistant needs Wi-Fi, software, APIs, microphone input, speaker output, and display support.

This layer should prove that the assistant can:

- Boot up.
- Connect to Wi-Fi.
- Run a simple program.
- Display text or graphics.
- Play audio.
- Capture voice or audio input.

### Layer 3: Add AI Behavior

Add software that allows the user to ask a question and receive an answer.

Early versions can use a simple typed input first, then move to voice input.

### Layer 4: Add Personal Tools

Add integrations one at a time:

1. Weather.
2. Google Calendar.
3. Gmail summaries.
4. Other future apps.

### Layer 5: Build the Robot Body

After the electronics are tested, design or choose a 3D-printed body that fits the actual parts.

This avoids the common mistake of printing a body first and later realizing the electronics do not fit.

---

## 9. Key Product Requirements

### 9.1 Voice Input

The robot should allow the user to ask questions using voice.

#### Requirements

- The system should support a microphone.
- The user should be able to trigger input in a beginner-friendly way.
- Push-to-talk is acceptable for Version 1.
- Always-listening wake word detection is optional and not required.

#### Acceptance Criteria

- The user can speak a short question.
- The system can capture the question clearly enough to process it.
- The system gives feedback that it is listening or processing.

#### Notes

A push-to-talk button is often simpler and more private than an always-listening device. Always-listening behavior can be added later.

---

### 9.2 Spoken Output

The robot should respond out loud.

#### Requirements

- The system should support a speaker.
- The assistant should be able to read responses aloud.
- The audio should be loud enough for desk use.

#### Acceptance Criteria

- The assistant can speak a short response.
- The user can understand the audio from normal desk distance.
- The audio output does not require the user to manually open a computer app.

---

### 9.3 Screen Display

The robot should include a small screen to display useful information.

#### Requirements

- The screen should show assistant status, such as idle, listening, thinking, or speaking.
- The screen should display calendar or weather information when needed.
- The screen may also show a simple face or expression.

#### Acceptance Criteria

- The screen turns on and displays a test message.
- The screen updates based on assistant state.
- The screen can show at least one useful information card, such as weather or calendar events.

---

### 9.4 Calendar Integration

The assistant should eventually connect to Google Calendar.

#### Requirements

- The user should be able to ask what is scheduled today.
- The assistant should summarize upcoming events.
- The assistant should avoid exposing private calendar details unnecessarily.

#### Acceptance Criteria

- The assistant can retrieve the user's events for the current day.
- The assistant can summarize event times and titles.
- The screen can display the next event or today’s schedule.

#### Example Interaction

User: “What do I have today?”  
Assistant: “You have three events today. Your first event is Biology lab at 10:00 AM. Later, you have a meeting at 2:00 PM and dinner at 7:00 PM.”

---

### 9.5 Weather Integration

The assistant should be able to report the weather.

#### Requirements

- The assistant should fetch current weather or a daily forecast.
- The assistant should speak a short summary.
- The screen should optionally show temperature and condition.

#### Acceptance Criteria

- The user can ask for weather.
- The assistant returns a useful weather summary.
- The screen displays the main weather information.

---

### 9.6 Gmail Integration

Gmail integration should be added carefully because email can contain private information.

#### Requirements

- Version 1 should treat Gmail as a future or later-stage integration.
- The assistant should summarize important emails, not read everything by default.
- The assistant should ask before performing sensitive actions.
- Sending, deleting, archiving, or replying to emails should not happen automatically.

#### Acceptance Criteria

- The assistant can identify recent important emails.
- The assistant can summarize sender, subject, and high-level content.
- The assistant does not send, delete, or modify emails unless a later version explicitly supports it with confirmation.

---

### 9.7 Assistant Personality

The assistant should feel friendly and helpful, but not overly complicated.

#### Requirements

- The assistant should explain what it is doing when helpful.
- The assistant should keep responses concise for voice.
- The assistant should provide more detail on the screen or when asked.
- The assistant should admit when it cannot access something.

#### Acceptance Criteria

- Responses are understandable when spoken aloud.
- The assistant avoids long walls of text during voice output.
- The assistant can give more detailed explanations when asked.

---

## 10. User Stories

### Core User Stories

1. **As the builder, I want to ask the robot what I have today so that I can hear my schedule without opening my calendar.**
2. **As the builder, I want the robot to tell me the weather so that I can quickly plan my day.**
3. **As the builder, I want the robot to speak answers out loud so that it feels like a real assistant.**
4. **As the builder, I want the robot to show information on a small screen so that I can glance at details.**
5. **As the builder, I want to learn the electronics step by step so that I understand what I am building.**
6. **As the builder, I want a beginner-safe setup so that I do not damage parts or create unsafe wiring.**
7. **As the builder, I want the project to stay expandable so that I can add Gmail, LEDs, buttons, or movement later.**

### Future User Stories

1. **As the builder, I want the robot to show a cute animated face so that it feels more alive.**
2. **As the builder, I want the robot to use LEDs to show status so that I can tell when it is listening or thinking.**
3. **As the builder, I want to ask about important emails so that I can avoid missing something.**
4. **As the builder, I want to add a physical button so that I can control when the robot listens.**
5. **As the builder, I want to place the electronics inside a 3D-printed body so that the project looks finished.**

---

## 11. Example Interactions

### Calendar

User: “What do I have today?”  
Assistant: “Today you have two events. At 9:00 AM, you have class. At 3:00 PM, you have a project meeting. Your next event is class at 9:00 AM.”  
Screen: Shows today’s schedule.

### Weather

User: “What’s the weather today?”  
Assistant: “Today is expected to be warm with a high around 88 degrees. You may want to bring water if you’ll be outside.”  
Screen: Shows temperature, condition, and high/low.

### General AI Question

User: “Explain what a resistor does.”  
Assistant: “A resistor limits how much electrical current flows through a circuit. It is kind of like a narrow part of a pipe that slows water down.”  
Screen: Shows the word “Resistor” and a short definition.

### Gmail Future Example

User: “Do I have any important emails?”  
Assistant: “You have two recent emails that may be important. One is from your professor about lab access, and one is from Chase about your account. I can summarize either one.”  
Screen: Shows sender and subject only.

---

## 12. Functional Requirements

| ID | Requirement | Priority | Version |
|---|---|---:|---|
| FR-001 | Device can boot and connect to Wi-Fi | Must Have | V1 |
| FR-002 | Device can display a basic status screen | Must Have | V1 |
| FR-003 | Device can play spoken audio | Must Have | V1 |
| FR-004 | Device can capture voice input or accept temporary typed input | Must Have | V1 |
| FR-005 | Assistant can answer basic questions | Must Have | V1 |
| FR-006 | Assistant can show simple visual responses | Must Have | V1 |
| FR-007 | Assistant can fetch weather | Should Have | V1 |
| FR-008 | Assistant can fetch today’s Google Calendar events | Should Have | V1 or V1.1 |
| FR-009 | Assistant can summarize Gmail safely | Could Have | V1.2+ |
| FR-010 | Device can use LED status indicators | Could Have | V1.1+ |
| FR-011 | Device can use a push-to-talk button | Could Have | V1.1+ |
| FR-012 | Device can fit inside a 3D-printed desk robot body | Should Have | V1.2+ |

---

## 13. Non-Functional Requirements

### Usability

- The system should be easy to use from a desk.
- The user should not need to type commands after setup for normal use.
- The assistant should make it clear when it is idle, listening, thinking, or speaking.

### Beginner Friendliness

- The system should use common, well-documented parts.
- The first version should avoid soldering if possible.
- Wiring should be simple and easy to inspect.
- Setup should be broken into small testable steps.

### Safety

- The project should use safe low-voltage electronics.
- The project should avoid unsafe batteries in Version 1.
- The user should unplug power before changing wires.
- The enclosure should allow ventilation if the main board gets warm.
- Power supplies should match the device requirements.

### Privacy

- The assistant should not always listen by default unless the user intentionally enables that feature.
- Calendar and Gmail data should be handled carefully.
- Secrets, API keys, and tokens should not be hardcoded into public code.
- Gmail actions should be read-only at first.

### Maintainability

- Code should be organized into simple modules.
- Each integration should be added separately.
- The project should include clear notes for setup and debugging.

### Expandability

- The architecture should allow future modules, including Gmail, reminders, LEDs, buttons, and movement.
- Arduino can be added later for physical electronics control.

---

## 14. Hardware Requirements

### Main Computer

The project should use a small computer that can run a normal operating system, connect to Wi-Fi, run Python, use APIs, and connect to audio/display devices.

A Raspberry Pi or similar device is recommended because it is better suited than Arduino for internet-connected AI assistant behavior.

### Microphone

The microphone should be beginner-friendly. A USB microphone may be easier than wiring a raw microphone module.

### Speaker

The speaker should be simple to connect. A USB speaker, 3.5 mm speaker, or small amplified speaker may be used depending on the main board.

### Display

The screen should be small enough to fit into a desk robot body but large enough to show readable information. It could be an OLED, LCD, or small HDMI display.

### Arduino Kit

The Arduino kit should be used for learning and optional future add-ons, such as:

- LEDs.
- Buttons.
- Sensors.
- Simple status lights.

Arduino should not be expected to handle the main AI assistant features by itself.

### Enclosure

The final body should be a cute desk robot shell. It should have room for:

- Main board.
- Screen.
- Speaker.
- Microphone opening.
- Power cable.
- Ventilation.
- Optional LED/button holes.

---

## 15. Software Requirements

### Core Software Modules

The software should eventually be organized into these modules:

1. **Input Module**  
   Handles typed input, button input, or voice input.

2. **Speech-to-Text Module**  
   Converts the user's spoken question into text.

3. **Assistant Brain Module**  
   Sends the user’s request to an AI model or local logic and decides how to respond.

4. **Text-to-Speech Module**  
   Converts the assistant response into spoken audio.

5. **Display Module**  
   Updates the screen with status or useful information.

6. **Calendar Module**  
   Connects to Google Calendar and fetches schedule data.

7. **Weather Module**  
   Fetches weather data.

8. **Gmail Module**  
   Later connects to Gmail in a privacy-conscious way.

9. **Configuration Module**  
   Stores settings, API keys, preferences, and environment variables.

---

## 16. Suggested Version Milestones

### Milestone 0: Planning and Parts Decision

Goal: Decide the first hardware setup.

Deliverables:

- Parts list.
- Budget estimate.
- Board decision.
- Display decision.
- Audio input/output decision.

Success means the user knows what to buy and why.

### Milestone 1: Electronics Learning

Goal: Use the Arduino kit to understand basic electronics.

Deliverables:

- LED blink test.
- Button input test.
- Basic sensor test if available.

Success means the user understands basic wiring, power, ground, and simple code upload.

### Milestone 2: Main Computer Setup

Goal: Set up Raspberry Pi or selected board.

Deliverables:

- Operating system installed.
- Wi-Fi working.
- SSH or local access working.
- Python environment ready.

Success means the user can run a basic Python script on the board.

### Milestone 3: Screen Test

Goal: Connect and test the display.

Deliverables:

- Screen powers on.
- Screen shows text or a simple face.
- Screen can update status.

Success means the display can be controlled by code.

### Milestone 4: Audio Test

Goal: Test microphone and speaker.

Deliverables:

- Speaker can play a test sound.
- Microphone can record audio.
- Optional speech-to-text test.

Success means the robot can hear and speak at a basic level.

### Milestone 5: Basic Assistant Loop

Goal: Build the first working assistant interaction.

Deliverables:

- User asks a question.
- Assistant processes the question.
- Assistant responds with text and speech.
- Screen shows status.

Success means the system feels like a basic voice assistant.

### Milestone 6: Weather Integration

Goal: Add a low-risk external data integration.

Deliverables:

- Weather API connected.
- Assistant can answer weather questions.
- Screen shows weather card.

Success means the system can fetch real-time external information.

### Milestone 7: Google Calendar Integration

Goal: Add personal schedule support.

Deliverables:

- Google Calendar authentication working.
- Assistant can fetch today’s events.
- Assistant can summarize schedule.
- Screen shows next event.

Success means the user can ask what they have today.

### Milestone 8: Physical Robot Body

Goal: Put the working electronics into a cute desk robot body.

Deliverables:

- Chosen or designed 3D model.
- Electronics layout plan.
- Cable routing plan.
- Ventilation plan.
- Final assembly checklist.

Success means the assistant looks like a desk robot instead of loose electronics.

### Milestone 9: Gmail Integration

Goal: Add cautious email summarization.

Deliverables:

- Gmail authentication working.
- Read-only email fetching.
- Safe summary behavior.
- No automatic sending/deleting.

Success means the assistant can identify important emails without unsafe actions.

---

## 17. Success Metrics

Version 1 will be considered successful if:

- The device turns on reliably.
- The device connects to Wi-Fi.
- The screen displays assistant status.
- The speaker works.
- The microphone or input method works.
- The assistant can answer at least basic questions.
- The assistant can speak responses out loud.
- The system can be extended without starting over.
- The user understands the major parts and why they are used.

A later version will be successful if:

- The assistant can summarize calendar events.
- The assistant can report weather.
- The assistant can safely summarize Gmail.
- The electronics fit neatly inside a 3D-printed body.

---

## 18. Risks and Mitigations

| Risk | Impact | Likelihood | Mitigation |
|---|---|---:|---|
| Budget exceeds $150 | Medium | High | Prioritize core parts first; delay body, LEDs, and advanced display |
| Raspberry Pi availability or price changes | Medium | Medium | Consider alternate small computers or used parts |
| Audio setup is harder than expected | High | Medium | Start with USB microphone/speaker instead of raw modules |
| Display setup is confusing | Medium | Medium | Choose well-documented display; test before mounting |
| Google API setup is frustrating | Medium | Medium | Add Google integrations after local assistant works |
| Gmail privacy issues | High | Medium | Use read-only access first; summarize safely; avoid sending/deleting |
| 3D-printed body does not fit parts | Medium | Medium | Do not print final body until exact hardware dimensions are known |
| User gets overwhelmed | High | High | Break work into small phases with one next step at a time |
| Power problems damage parts | High | Low/Medium | Use proper power supplies; unplug before rewiring; avoid batteries early |

---

## 19. Privacy and Security Requirements

Because the assistant may access personal calendar and email data, privacy must be considered from the beginning.

### Requirements

- Store API keys and tokens outside of public code.
- Do not commit secrets to GitHub.
- Use read-only permissions whenever possible.
- Ask for confirmation before any action that changes user data.
- Do not enable always-listening mode by default.
- Prefer push-to-talk or manual activation in early versions.
- Make it clear when the device is listening.

### Gmail-Specific Safety Rules

The Gmail integration should initially be read-only.

The assistant should not:

- Send emails automatically.
- Delete emails automatically.
- Archive emails automatically.
- Mark emails as read automatically.
- Reply to emails automatically.

Any of those features should require a future explicit design decision.

---

## 20. Open Questions

These questions should be answered before or during the next planning stage:

1. What exact main board should be used?
2. Should the first screen be OLED, LCD, or HDMI?
3. Should the first microphone be USB or a module?
4. Should the first speaker be USB, Bluetooth, 3.5 mm, or wired amplifier?
5. Should the assistant use push-to-talk first?
6. Should the robot body be custom designed or based on an existing model?
7. Does the user have access to a 3D printer?
8. Should the first version be powered only by wall power?
9. What AI service should be used for the assistant brain?
10. Should the project use Python as the main software language?

---

## 21. Recommended Version 1 Product Definition

The recommended Version 1 product is:

A wall-powered cute desk assistant prototype using a small computer as the main brain, with a microphone, speaker, and small display. It should first work as a basic voice assistant on a desk before being placed inside a 3D-printed body. It should support weather first, then Google Calendar, then Gmail later.

The recommended Version 1 build order is:

1. Learn basic Arduino electronics separately.
2. Choose and buy the main board and core parts.
3. Set up the main board.
4. Test the display.
5. Test the speaker.
6. Test the microphone.
7. Build a simple assistant loop.
8. Add weather.
9. Add Google Calendar.
10. Plan the 3D-printed body.
11. Add Gmail only after the assistant foundation is stable.

---

## 22. Product Decision Notes

### Arduino vs Raspberry Pi

Arduino is useful for learning electronics and controlling simple parts like LEDs, buttons, motors, and sensors. However, Arduino is not the best choice for the main AI assistant because the assistant needs internet access, APIs, audio processing, display handling, and more complex software.

A Raspberry Pi or similar mini-computer is better for the main assistant because it behaves more like a small computer. It can connect to Wi-Fi, run Python, use APIs, connect to displays, and handle audio more easily.

The recommended approach is:

- Use Raspberry Pi or similar as the main brain.
- Use Arduino later as an optional helper for LEDs, buttons, sensors, or movement.

### Push-to-Talk vs Always Listening

Push-to-talk is recommended for Version 1 because it is simpler and more private. Always-listening wake word detection can be added later, but it adds complexity.

### Wall Power vs Battery

Wall power is recommended for Version 1 because it is safer and simpler. Batteries add complexity around charging, current draw, heat, and safety.

### Physical Body Timing

The body should come after the electronics plan is clear. The body must fit the actual screen, board, speaker, microphone, cables, and power connector.

---

## 23. Out-of-Scope Future Ideas

These are good future ideas but should not distract from Version 1:

- Moving head.
- Moving arms.
- Wheels.
- Touchscreen interface.
- Custom wake word.
- Offline AI model.
- Camera vision.
- Face recognition.
- Home automation.
- Mobile app companion.
- Custom PCB.
- Battery-powered portable version.

---

## 24. Final PRD Summary

This project should start as a simple, working AI desk assistant and grow into a cute physical robot over time. The first priority is not movement or appearance. The first priority is proving the assistant can listen, think, speak, and display useful information.

The project should stay beginner-friendly, safe, modular, and budget-conscious. Every hardware and software choice should help the user learn while moving toward a working Version 1 assistant.
