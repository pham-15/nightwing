# Engineering Roadmap

**Project:** Project Nightwing
**Document:** Engineering Roadmap  
**Version:** 1.0  
**Target Version:** Version 1 beginner build  
**Budget Goal:** Around $150 for core prototype when possible  
**Primary User:** Alex, beginner electronics learner  
**Last Updated:** 2026-06-19

---

## 1. Purpose of This Roadmap

This roadmap explains how to build the personal AI assistant robot in a realistic engineering order. The goal is not to build the final cute robot shell first. The goal is to first prove that each important system works separately, then combine them into one reliable desk robot.

The Version 1 robot should:

- Sit on a desk.
- Listen to voice input.
- Respond out loud through a speaker.
- Show simple information on a small screen.
- Connect to Wi-Fi.
- Eventually connect to Google Calendar, weather, and Gmail.
- Avoid movement for now.
- Stay beginner-friendly and safe.

This roadmap is written for a beginner. Each phase includes what to build, why it matters, what parts or tools are involved, what skills are learned, how to test it, and what counts as done.

---

## 2. Engineering Strategy

### 2.1 Build in Layers

The project should be built in layers instead of all at once.

The basic order is:

1. Learn tiny electronics skills.
2. Set up the main computer.
3. Test each device separately.
4. Build the assistant in software only.
5. Add voice input/output.
6. Add screen output.
7. Add outside app integrations.
8. Put the working electronics into a robot body.

This avoids the beginner mistake of buying everything, wiring everything together, and then not knowing which part is causing problems.

### 2.2 Desk Prototype First, Robot Body Later

The first working version should be built on a desk with loose parts. The 3D-printed robot body should come later.

Reason:

- The screen size may change.
- The speaker size may change.
- The microphone placement may matter.
- The Raspberry Pi may need airflow.
- Wires may need more space than expected.
- Ports need to remain accessible.

Once the electronics work, the robot shell can be designed around the real parts.

### 2.3 Keep Version 1 Simple

Version 1 should prioritize a working assistant over fancy robotics.

Do not focus on:

- Walking.
- Wheels.
- Arms.
- Servo motors.
- Battery power.
- Complicated custom circuit boards.
- Advanced wake-word detection.
- Complex 3D modeling too early.

The first win is: **ask the robot a question and hear it answer.**

---

## 3. Recommended Version 1 Architecture

### 3.1 Main Brain

Use a Raspberry Pi as the main brain.

The main brain handles:

- Wi-Fi.
- Python code.
- API calls.
- AI assistant requests.
- Google Calendar/Gmail/weather integration.
- Screen output.
- Microphone input.
- Speaker output.

### 3.2 Arduino Role

Use the Arduino kit for learning and optional simple electronics.

Arduino is good for:

- LEDs.
- Buttons.
- Sensors.
- Simple input/output.
- Learning basic circuits.

Arduino is not ideal for:

- Running an AI assistant.
- Connecting to Google Calendar directly.
- Handling Gmail APIs.
- Running a modern screen UI.
- Processing voice assistant logic.

For Version 1, Arduino is optional. It can be used in early learning phases and later add-ons.

### 3.3 High-Level System Diagram

```text
User pushes physical button
   ↓
Raspberry Pi 4 GPIO detects button press
   ↓
USB microphone records voice
   ↓
Assistant software
   ↓
External services when needed
   - AI model
   - Google Calendar
   - Gmail
   - Weather API
   ↓
Response
   ├── Speaker: spoken answer
   └── Screen: visual info/status
```

Optional later:

```text
Raspberry Pi
   ↓ USB or serial
Arduino
   ↓
LED eyes / buttons / sensors
```

---

## 4. Roadmap Summary

| Phase | Name                          | Main Goal                           | Core Output                              |
| ----: | ----------------------------- | ----------------------------------- | ---------------------------------------- |
|     0 | Project Setup and Decisions   | Decide the first build path         | Clear Version 1 plan and parts list      |
|     1 | Beginner Electronics Practice | Learn basic Arduino/wiring concepts | LED/button/sensor confidence             |
|     2 | Main Computer Setup           | Set up Raspberry Pi or equivalent   | Bootable device with Wi-Fi and Python    |
|     3 | Screen Prototype              | Display simple text/status          | Working screen output                    |
|     4 | Audio Prototype               | Test microphone and speaker         | Record and play audio successfully       |
|     5 | Text Assistant Prototype      | Build assistant without voice       | Typed question → typed answer            |
|     6 | Voice Assistant Loop          | Add speech input/output             | Spoken question → spoken answer          |
|     7 | Local Dashboard UI            | Show useful screen states           | Idle/listening/thinking/answer screens   |
|     8 | Calendar Integration          | Connect Google Calendar             | “What do I have today?” works            |
|     9 | Weather Integration           | Add weather responses               | Weather answer and screen card           |
|    10 | Gmail Integration             | Add limited email support           | Safe email summary/checking              |
|    11 | Physical Robot Planning       | Choose/design shell                 | Dimensions and mounting plan             |
|    12 | Integration Build             | Put electronics in shell            | Working desk robot prototype             |
|    13 | Polish and Reliability        | Make it easier to use               | Auto-start, error handling, cleanup      |
|    14 | Future Expansion              | Add optional features               | LEDs, buttons, wake word, movement later |

---

## 5. Phase 0: Project Setup and Decisions

### Goal

Create a clear beginner-friendly Version 1 plan before buying many parts.

### Why This Phase Matters

A lot of beginner electronics projects fail because the builder buys random parts that do not work together. This phase prevents that.

### Main Decisions

- Which main computer to use.
- Which screen size to use.
- Which microphone type to use.
- Which speaker type to use.
- Whether Arduino is needed in Version 1.
- Whether the first assistant will use button activation, typed input, or always-listening voice.
- Whether the 3D body will be downloaded from an existing model or custom-designed.

### Recommended Default Decisions

| Decision    | Recommended Default                       | Reason                                                         |
| ----------- | ----------------------------------------- | -------------------------------------------------------------- |
| Main brain  | Raspberry Pi 4                            | Best beginner path for Wi-Fi, Python, APIs, display, and audio |
| Arduino     | Optional, not required for core assistant | Better used for learning or later LEDs/buttons                 |
| Screen      | Small HDMI                                | Easier to show status and information                          |
| Mic         | USB microphone                            | Easier than raw microphone wiring                              |
| Speaker     | USB speaker                               | Easier than building an amplifier circuit                      |
| Movement    | No movement                               | Keeps Version 1 realistic                                      |
| Battery     | Wall power only                           | Safer and simpler                                              |
| Robot shell | Later                                     | Electronics should work before enclosure design                |

### Tasks

- [ ] Review PRD.
- [ ] Review budget/BOM document.
- [ ] Decide the Version 1 main computer.
- [ ] Decide the first display type.
- [ ] Decide the first microphone/speaker approach.
- [ ] Decide whether to use wall power only.
- [ ] Create a project folder on your computer.
- [ ] Create a simple decision log entry for every major hardware decision.

### Deliverables

- Version 1 parts list.
- Version 1 architecture sketch.
- Decision log updated.
- List of known unknowns.

### Skills Learned

- Difference between microcontrollers and small computers.
- How to compare hardware parts.
- Why compatibility matters.
- How to plan a prototype before buying.

### Done Means

Phase 0 is done when you know what parts you are buying first and why each part is needed.

---

## 6. Phase 1: Beginner Electronics Practice with Arduino

### Goal

Use the Arduino kit to learn the basics of wiring and electronics before connecting more expensive parts.

### Why This Phase Matters

Even if Arduino is not the main brain, it is a great learning tool. You can safely practice basic electronics concepts before touching the Raspberry Pi setup.

### Scope

This phase is for learning only. It does not need to become part of the final robot yet.

### Tasks

- [ ] Install the Arduino IDE.
- [ ] Connect Arduino to your computer.
- [ ] Upload the Blink example.
- [ ] Wire one LED on a breadboard.
- [ ] Learn what a resistor does.
- [ ] Wire a button input.
- [ ] Read button state in code.
- [ ] Try one simple sensor from the kit if available.
- [ ] Document what each wire does.

### Beginner Concepts

| Concept     | Simple Meaning                                        |
| ----------- | ----------------------------------------------------- |
| Breadboard  | A board that lets you connect wires without soldering |
| LED         | A small light that only works one direction           |
| Resistor    | A part that limits electrical current                 |
| Digital pin | A pin that is basically ON or OFF                     |
| Ground/GND  | The shared return path in the circuit                 |
| 5V/3.3V     | Power levels used by electronics                      |

### Safety Notes

- Unplug power before changing wires.
- Do not connect power directly to ground.
- Use resistors with LEDs.
- Do not connect Arduino 5V signals directly to Raspberry Pi GPIO later without checking voltage compatibility.

### Deliverables

- Working blinking LED.
- Working button input.
- Notes explaining the circuit.
- Optional: simple sensor reading.

### Done Means

Phase 1 is done when you can confidently upload code to Arduino and wire a basic LED/button circuit without guessing.

---

## 7. Phase 2: Main Computer Setup

### Goal

Set up the Raspberry Pi or selected main computer so it can run code, connect to Wi-Fi, and become the assistant brain.

### Why This Phase Matters

The main computer is the core of the project. Everything else depends on it.

### Tasks

- [ ] Buy or choose the main computer.
- [ ] Prepare the storage device, usually a microSD card.
- [ ] Install the operating system.
- [ ] Connect keyboard/mouse/monitor or set up remote access.
- [ ] Connect to Wi-Fi.
- [ ] Update system packages.
- [ ] Install Python.
- [ ] Create a project folder.
- [ ] Confirm internet access from the device.
- [ ] Confirm the device can run a simple Python script.

### Software Setup Checklist

- [ ] Operating system installed.
- [ ] Wi-Fi working.
- [ ] Python working.
- [ ] Git installed if needed.
- [ ] Code editor available or remote editing set up.
- [ ] Project folder created.
- [ ] Virtual environment created if using Python.

### Deliverables

- Main computer boots successfully.
- Wi-Fi works.
- Python runs.
- Project folder exists.
- Basic `hello world` script runs.

### Testing

Run a simple script that prints:

```text
Robot assistant setup is working.
```

Then confirm the device can access the internet.

### Done Means

Phase 2 is done when the main computer is ready to run your assistant software.

---

## 8. Phase 3: Screen Prototype

### Goal

Connect the small screen and display simple text or graphics.

### Why This Phase Matters

The screen gives the robot a face/status display and lets it show useful information without speaking everything.

### Screen Use Cases

- Idle face.
- Listening status.
- Thinking status.
- Answer summary.
- Calendar list.
- Weather card.
- Error messages.
- Setup status.

### Tasks

- [ ] Connect the screen.
- [ ] Confirm the operating system detects it.
- [ ] Show the desktop or terminal on it.
- [ ] Create a simple display test.
- [ ] Show text: “Hello, Alex.”
- [ ] Show a simple robot face or status message.

### Deliverables

- Working screen.
- Simple Python display test or browser-based UI.
- Notes on screen resolution and size.

### Testing

Test these screen states:

| State     | Expected Display                   |
| --------- | ---------------------------------- |
| Idle      | Robot face or “Ready”              |
| Listening | “Listening…”                       |
| Thinking  | “Thinking…”                        |
| Speaking  | “Speaking…”                        |
| Error     | Short understandable error message |

### Done Means

Phase 3 is done when the screen can reliably show simple status messages.

---

## 9. Phase 4: Audio Prototype

### Goal

Test the microphone and speaker separately before building the full voice assistant.

### Why This Phase Matters

Voice assistants fail if the audio setup is bad. It is easier to test microphone and speaker separately before adding AI.

### Tasks

- [ ] Connect microphone.
- [ ] Confirm the device recognizes the microphone.
- [ ] Record a short audio sample.
- [ ] Play the recording back.
- [ ] Connect speaker.
- [ ] Play a test sound.
- [ ] Adjust input/output volume.
- [ ] Test audio from a normal speaking distance.

### Deliverables

- Microphone records audio.
- Speaker plays audio.
- Basic volume settings documented.
- Audio test notes.

### Testing

Perform these tests:

| Test                    | Expected Result                           |
| ----------------------- | ----------------------------------------- |
| Record voice            | Audio file contains understandable speech |
| Playback                | Speaker plays clearly                     |
| Normal distance         | Robot can hear from desk distance         |
| Quiet room              | Speech is clear                           |
| Slight background noise | Speech is still somewhat usable           |

### Common Issues

| Problem                | Likely Cause             | Fix Direction                   |
| ---------------------- | ------------------------ | ------------------------------- |
| No microphone detected | Driver/device issue      | Check USB/device settings       |
| Recording is silent    | Wrong input selected     | Choose correct input device     |
| Speaker silent         | Wrong output selected    | Choose correct output device    |
| Audio too quiet        | Gain/volume too low      | Adjust input/output levels      |
| Echo/feedback          | Mic too close to speaker | Move them apart or lower volume |

### Done Means

Phase 4 is done when you can record your voice and play audio from the speaker reliably.

---

## 10. Phase 5: Text Assistant Prototype

### Goal

Build the assistant logic without voice first.

### Why This Phase Matters

Typed input is much easier to debug than voice. If the assistant cannot answer typed questions, adding voice will only make debugging harder.

### Tasks

- [ ] Create a Python assistant script.
- [ ] Let the user type a question.
- [ ] Send the question to the assistant logic.
- [ ] Print the response in the terminal.
- [ ] Add basic command routing.
- [ ] Add placeholder commands for calendar/weather/Gmail.
- [ ] Add basic error handling.

### Example Commands

| User Input              | Expected Behavior                     |
| ----------------------- | ------------------------------------- |
| “Hello”                 | Assistant greets user                 |
| “What can you do?”      | Assistant lists available features    |
| “What do I have today?” | Placeholder calendar response for now |
| “What is the weather?”  | Placeholder weather response for now  |
| “Exit”                  | Program closes safely                 |

### Deliverables

- Working typed assistant.
- Basic command loop.
- Early project code structure.

### Recommended Simple Code Structure

```text
assistant_robot/
  main.py
  assistant_core.py
  display.py
  audio.py
  integrations/
    calendar_service.py
    weather_service.py
    gmail_service.py
  config/
    settings.example.json
  README.md
```

### Done Means

Phase 5 is done when typed questions produce useful typed responses.

---

## 11. Phase 6: Voice Assistant Loop

### Goal

Turn the typed assistant into a voice assistant.

### Why This Phase Matters

This phase creates the first real “robot assistant” experience.

### Voice Loop

```text
1. User activates assistant.
2. Assistant listens.
3. Speech is converted to text.
4. Text is sent to assistant logic.
5. Assistant creates a response.
6. Response is converted to speech.
7. Speaker plays the response.
8. Screen updates throughout the process.
```

### Activation Options

| Option           |            Difficulty | Notes                                 |
| ---------------- | --------------------: | ------------------------------------- |
| Keyboard press   |                  Easy | Best for first testing                |
| Button press     |                Medium | Good later with Arduino or GPIO       |
| Wake word        |                Harder | Add after basics work                 |
| Always listening | Not recommended first | More privacy and reliability concerns |

### Recommended First Activation

Start with keyboard press or button press. Add wake word later.

### Tasks

- [ ] Add speech-to-text.
- [ ] Add text-to-speech.
- [ ] Connect voice input to assistant logic.
- [ ] Connect assistant response to speaker output.
- [ ] Add screen states: listening, thinking, speaking.
- [ ] Add error message if speech is not understood.
- [ ] Test with short questions.

### Deliverables

- Spoken question becomes text.
- Assistant answers.
- Answer is spoken out loud.
- Screen status updates.

### Done Means

Phase 6 is done when you can ask a simple spoken question and the assistant speaks back.

---

## 12. Phase 7: Local Dashboard and Screen UI

### Goal

Create a simple screen interface for the robot.

### Why This Phase Matters

The screen makes the robot feel alive and helps show information quickly.

### Required UI States

| State     | Purpose                    |
| --------- | -------------------------- |
| Idle      | Shows robot is ready       |
| Listening | Shows it is hearing you    |
| Thinking  | Shows it is processing     |
| Speaking  | Shows it is responding     |
| Calendar  | Shows today’s events       |
| Weather   | Shows weather summary      |
| Error     | Shows something went wrong |

### Possible UI Approaches

| Approach                  | Difficulty | Notes                          |
| ------------------------- | ---------: | ------------------------------ |
| Terminal text             |       Easy | Best for very early testing    |
| Python GUI                |     Medium | Good for a simple local screen |
| Local web app             |     Medium | Flexible and easier to style   |
| Full custom animated face |     Harder | Save for later polish          |

### Recommended First UI

Start simple: large text status and maybe a simple face. Do not overbuild the UI before the assistant works.

### Tasks

- [ ] Pick UI approach.
- [ ] Create idle screen.
- [ ] Create status screens.
- [ ] Create calendar card layout.
- [ ] Create weather card layout.
- [ ] Add error screen.
- [ ] Connect screen updates to assistant state.

### Done Means

Phase 7 is done when the screen changes based on what the assistant is doing.

---

## 13. Phase 8: Google Calendar Integration

### Goal

Allow the assistant to answer calendar questions.

### Why This Phase Matters

Calendar is one of the core personal assistant features.

### Version 1 Calendar Scope

The assistant should be able to answer:

- “What do I have today?”
- “What is my next event?”
- “Am I busy tomorrow?”
- “What time is my first event?”

### Out of Scope for First Calendar Version

- Creating events.
- Deleting events.
- Editing events.
- Inviting people.
- Handling complex scheduling conflicts.

Read-only access is safer for the first version.

### Tasks

- [ ] Create Google Cloud project if needed.
- [ ] Enable Calendar API.
- [ ] Set up OAuth credentials.
- [ ] Store credentials safely.
- [ ] Fetch today’s calendar events.
- [ ] Format events into simple text.
- [ ] Show events on screen.
- [ ] Speak summary out loud.
- [ ] Handle no-events case.

### Example Response

User: “What do I have today?”

Assistant:

```text
You have 3 things today. Your first event is Biology lecture at 10:00 AM. Then you have work at 1:00 PM, and a dentist appointment at 4:30 PM.
```

Screen:

```text
Today
10:00 AM Biology lecture
1:00 PM Work
4:30 PM Dentist
```

### Privacy Notes

- Use read-only permissions first.
- Do not print tokens in logs.
- Do not upload credentials to GitHub.
- Store secrets in local config files that are ignored by Git.

### Done Means

Phase 8 is done when the assistant can read and summarize today’s Google Calendar events.

---

## 14. Phase 9: Weather Integration

### Goal

Allow the assistant to answer weather questions.

### Why This Phase Matters

Weather is useful, relatively simple, and a good first external API integration.

### Version 1 Weather Scope

The assistant should answer:

- “What is the weather today?”
- “Is it going to rain?”
- “What is the temperature outside?”
- “What should I wear today?”

### Tasks

- [ ] Choose weather API.
- [ ] Create API key if needed.
- [ ] Store API key safely.
- [ ] Fetch current weather.
- [ ] Fetch daily forecast if supported.
- [ ] Format the response in plain English.
- [ ] Show weather card on screen.
- [ ] Add error handling if API fails.

### Example Response

```text
It is 78 degrees and partly cloudy. There is a small chance of rain later, so you probably do not need an umbrella unless you will be outside for a long time.
```

### Done Means

Phase 9 is done when the assistant can speak and display a simple weather summary.

---

## 15. Phase 10: Gmail Integration

### Goal

Allow the assistant to summarize or check email in a safe, limited way.

### Why This Phase Matters

Email can be useful, but it is more sensitive than weather or calendar. It should be added carefully.

### Version 1 Gmail Scope

Start with read-only features:

- “Do I have any important emails?”
- “Summarize my unread emails.”
- “Any emails from today?”
- “Do I have emails from [person/company]?”

### Out of Scope for First Gmail Version

- Sending emails automatically.
- Deleting emails.
- Archiving emails.
- Replying without confirmation.
- Reading every email out loud by default.

### Tasks

- [ ] Enable Gmail API.
- [ ] Set up OAuth credentials.
- [ ] Use read-only Gmail scope.
- [ ] Fetch unread email metadata first.
- [ ] Display sender/subject/date.
- [ ] Summarize short snippets.
- [ ] Avoid reading sensitive email content out loud unless requested.
- [ ] Add privacy confirmation step for detailed email reading.

### Safety Rule

The assistant should not send or delete emails in Version 1. If write actions are ever added, require explicit confirmation.

### Done Means

Phase 10 is done when the assistant can safely summarize unread email information using read-only access.

---

## 16. Phase 11: Physical Robot Planning

### Goal

Plan the cute desk robot shell after knowing the real electronics.

### Why This Phase Matters

The body should fit the parts, not the other way around.

### Physical Design Requirements

The robot shell should have space for:

- Main computer.
- Screen.
- Speaker.
- Microphone opening.
- Power cable.
- Ventilation.
- Cable routing.
- Optional Arduino or LED wiring later.

### Design Constraints

- No movement required.
- Stable on a desk.
- Easy to open for repairs.
- No blocked vents.
- No speaker fully sealed inside without openings.
- No microphone buried deep inside plastic.
- Ports should remain reachable or have extension access.

### Tasks

- [ ] Measure all parts.
- [ ] Decide screen placement.
- [ ] Decide speaker placement.
- [ ] Decide microphone placement.
- [ ] Decide power cable exit point.
- [ ] Choose downloaded 3D model or custom design.
- [ ] Create paper/cardboard mockup if helpful.
- [ ] Verify heat/airflow plan.
- [ ] Verify service access plan.

### Done Means

Phase 11 is done when there is a shell plan that fits the actual electronics and can be opened for maintenance.

---

## 17. Phase 12: Integration Build

### Goal

Put the tested electronics into the robot shell.

### Why This Phase Matters

This turns the prototype into a real desk robot.

### Tasks

- [ ] Print or obtain the robot shell.
- [ ] Test-fit all parts before final mounting.
- [ ] Mount screen.
- [ ] Mount speaker.
- [ ] Mount microphone.
- [ ] Mount Raspberry Pi/main computer.
- [ ] Route power cable safely.
- [ ] Secure loose wires.
- [ ] Leave access to ports or create service panel.
- [ ] Test audio after enclosure installation.
- [ ] Test screen after enclosure installation.
- [ ] Test heat after 30–60 minutes of use.

### Integration Risks

| Risk                   | Why It Happens                        | Mitigation                            |
| ---------------------- | ------------------------------------- | ------------------------------------- |
| Mic hears speaker echo | Mic and speaker too close             | Separate placement, reduce volume     |
| Screen cable too short | Shell design not planned around cable | Measure before printing               |
| Device overheats       | Poor airflow                          | Add vents and avoid tight sealed case |
| Hard to repair         | No access panel                       | Design removable back/bottom          |
| Audio muffled          | Speaker blocked by plastic            | Add speaker grille/opening            |

### Done Means

Phase 12 is done when the robot works inside the shell as well as it did on the desk.

---

## 18. Phase 13: Polish and Reliability

### Goal

Make the robot easier to use every day.

### Why This Phase Matters

A prototype that only works when manually started is less useful. This phase makes it feel more like a real product.

### Tasks

- [ ] Add startup script so assistant launches when device boots.
- [ ] Add clear error messages.
- [ ] Add logs for debugging.
- [ ] Add fallback responses when APIs fail.
- [ ] Add offline message if Wi-Fi is down.
- [ ] Add safe shutdown process.
- [ ] Add volume controls.
- [ ] Add settings file.
- [ ] Add README setup instructions.
- [ ] Add backup instructions for configuration.

### Reliability Requirements

| Requirement               | Target                                  |
| ------------------------- | --------------------------------------- |
| Boot to ready state       | Within a reasonable time after power-on |
| Handle Wi-Fi failure      | Show/say understandable error           |
| Handle API failure        | Do not crash                            |
| Handle unclear speech     | Ask user to repeat                      |
| Handle no calendar events | Say there are no events                 |
| Handle no unread emails   | Say there are no unread emails          |

### Done Means

Phase 13 is done when the robot can be restarted and used without manually fixing setup every time.

---

## 19. Phase 14: Future Expansion

### Goal

Add optional features after Version 1 works.

### Possible Future Features

| Feature                    |  Difficulty | Notes                          |
| -------------------------- | ----------: | ------------------------------ |
| LED eyes                   | Easy/Medium | Good Arduino or GPIO add-on    |
| Physical button            | Easy/Medium | Good for activation or mute    |
| Wake word                  | Medium/Hard | Useful but not necessary first |
| Better animated face       |      Medium | Makes robot feel more alive    |
| Touchscreen UI             |      Medium | More interactive               |
| Local memory/preferences   |      Medium | Store user settings            |
| Home Assistant integration |      Medium | Control smart home devices     |
| Servo head movement        | Medium/Hard | First movement feature         |
| Battery power              |      Harder | Requires safety planning       |
| Custom PCB                 |    Advanced | Not needed early               |

### Expansion Rule

Do not add advanced features until the basic assistant is reliable.

---

## 20. Suggested Build Timeline

This is not a strict schedule. It is a suggested order.

| Time Period | Focus           | Expected Result                             |
| ----------- | --------------- | ------------------------------------------- |
| Week 1      | Phase 0 and 1   | Plan parts and learn Arduino basics         |
| Week 2      | Phase 2         | Main computer set up                        |
| Week 3      | Phase 3 and 4   | Screen, mic, and speaker tested             |
| Week 4      | Phase 5         | Typed assistant working                     |
| Week 5      | Phase 6 and 7   | Voice loop and basic screen states working  |
| Week 6      | Phase 8 and 9   | Calendar and weather working                |
| Week 7      | Phase 10        | Gmail read-only support working             |
| Week 8      | Phase 11 and 12 | Robot shell planned and integration started |
| Week 9+     | Phase 13 and 14 | Polish, reliability, future features        |

If school/work is busy, this can easily become a multi-month project. That is okay.

---

## 21. Engineering Task Backlog

### Must Have for Version 1

- [ ] Main computer boots and connects to Wi-Fi.
- [ ] Python assistant program runs.
- [ ] Microphone works.
- [ ] Speaker works.
- [ ] Screen works.
- [ ] Typed assistant works.
- [ ] Voice assistant works.
- [ ] Screen shows assistant status.
- [ ] Google Calendar read-only integration works.
- [ ] Weather integration works.
- [ ] Basic error handling exists.
- [ ] Safe power setup exists.

### Should Have for Version 1

- [ ] Gmail read-only summary.
- [ ] Simple robot face screen.
- [ ] Auto-start on boot.
- [ ] Clear project README.
- [ ] Settings file.
- [ ] Basic logging.
- [ ] Physical shell planned around measured parts.

### Could Have Later

- [ ] LED eyes.
- [ ] Physical button.
- [ ] Wake word.
- [ ] Touchscreen controls.
- [ ] Custom 3D model.
- [ ] Servo movement.
- [ ] Battery power.

### Not Now

- [ ] Walking robot.
- [ ] Wheels.
- [ ] Arms.
- [ ] Sending emails automatically.
- [ ] Deleting emails.
- [ ] Editing calendar events.
- [ ] Complicated PCB design.

---

## 22. Development Workflow

### 22.1 Folder Organization

Recommended repo/folder:

```text
personal-ai-robot/
  README.md
  docs/
    01_PRD.md
    02_Engineering_Roadmap.md
    03_Architecture.md
    04_Budget_BOM.md
    05_API_Privacy_Plan.md
    06_Test_Checklist.md
    07_Decision_Log.md
  src/
    main.py
    assistant_core.py
    audio/
      speech_to_text.py
      text_to_speech.py
    display/
      screen_manager.py
      ui_states.py
    integrations/
      calendar_service.py
      weather_service.py
      gmail_service.py
    config/
      settings.example.json
  tests/
    test_calendar_formatting.py
    test_weather_formatting.py
  hardware/
    wiring_notes.md
    part_measurements.md
  3d_model/
    notes.md
```

### 22.2 Version Control

Use Git if possible. At minimum, save copies often.

Recommended Git habits:

- Commit after each working phase.
- Do not commit API keys.
- Do not commit Google credentials.
- Use `.gitignore` for secrets and tokens.
- Write simple commit messages.

Example commit messages:

```text
Set up project folder
Add typed assistant loop
Add screen status display
Add calendar read-only integration
Add weather summary command
```

---

## 23. Testing Strategy

### 23.1 Test One Thing at a Time

Do not test the full robot every time. Test parts separately:

- Test screen alone.
- Test mic alone.
- Test speaker alone.
- Test assistant text logic alone.
- Test Calendar API alone.
- Test Gmail API alone.

Then combine them.

### 23.2 Test Levels

| Level            | What It Means             | Example                               |
| ---------------- | ------------------------- | ------------------------------------- |
| Component test   | One part works by itself  | Mic records audio                     |
| Integration test | Two systems work together | Voice text goes to assistant          |
| End-to-end test  | Whole user flow works     | Ask calendar question and hear answer |
| Reliability test | Works repeatedly          | Ask 10 questions without crashing     |
| Enclosure test   | Works inside shell        | Audio and heat still okay             |

### 23.3 End-to-End Test Cases

| Test            | User Says                  | Expected Result                     |
| --------------- | -------------------------- | ----------------------------------- |
| Basic assistant | “Hello”                    | Assistant responds naturally        |
| Calendar        | “What do I have today?”    | Speaks and displays events          |
| Calendar empty  | “What do I have today?”    | Says no events if calendar is empty |
| Weather         | “What is the weather?”     | Speaks and displays weather         |
| Gmail           | “Do I have unread emails?” | Summarizes safely                   |
| Unknown request | “Can you teleport?”        | Says it cannot do that              |
| Bad audio       | Mumbled speech             | Asks user to repeat                 |
| Wi-Fi down      | Any API request            | Shows/says network error            |

---

## 24. Risk Register

| Risk                                     | Impact | Likelihood | Mitigation                                           |
| ---------------------------------------- | -----: | ---------: | ---------------------------------------------------- |
| Budget exceeds $150                      | Medium |     Medium | Buy core parts first, delay shell/LEDs               |
| Raspberry Pi supply/prices vary          | Medium |     Medium | Consider alternatives or use existing computer first |
| Audio quality is poor                    |   High |     Medium | Use USB mic/speaker, test before enclosure           |
| Google API setup is confusing            | Medium |       High | Follow one integration at a time                     |
| Credentials accidentally exposed         |   High |     Medium | Use `.gitignore`, do not share keys                  |
| Too many features too early              |   High |       High | Follow roadmap phases                                |
| Screen incompatible or hard to configure | Medium |     Medium | Prefer beginner-friendly display options             |
| Robot shell does not fit parts           | Medium |     Medium | Measure after electronics are chosen                 |
| Heat buildup inside shell                | Medium |     Medium | Add ventilation and test temperature                 |
| Project becomes overwhelming             |   High |     Medium | One phase, one task at a time                        |

---

## 25. Hardware Dependency Map

Some tasks depend on hardware arriving or being chosen first.

```text
Main computer chosen
   ↓
OS setup
   ↓
Python environment
   ↓
Screen/audio testing
   ↓
Assistant software
   ↓
API integrations
   ↓
Physical enclosure planning
```

Do not design the final 3D shell before these are known:

- Screen dimensions.
- Speaker dimensions.
- Microphone placement.
- Main computer dimensions.
- Power cable direction.
- Heat/vent needs.

---

## 26. Software Dependency Map

```text
Python setup
   ↓
Typed assistant core
   ↓
Speech-to-text + text-to-speech
   ↓
Display state manager
   ↓
Calendar integration
   ↓
Weather integration
   ↓
Gmail integration
   ↓
Startup/reliability polish
```

---

## 27. Definition of Done for Version 1

Version 1 is done when:

- The assistant runs on the selected main computer.
- The robot can listen through a microphone.
- The robot can speak through a speaker.
- The screen shows basic status and useful info.
- The assistant can answer normal questions.
- The assistant can read today’s Google Calendar events.
- The assistant can provide weather information.
- Gmail read-only summary works or is clearly deferred.
- The assistant does not crash during basic use.
- API keys and credentials are stored safely.
- The hardware is powered safely.
- The electronics are either ready for the robot shell or already installed in it.
- There is documentation explaining how to start and test the project.

---

## 28. First Three Engineering Steps

If starting from zero, do these first:

1. **Confirm the Version 1 architecture.**  
   Decide that the main assistant brain will be a Raspberry Pi-style device and Arduino will be optional for learning/simple add-ons.

2. **Create the shopping list.**  
   Choose the main computer, storage, power supply, screen, microphone, and speaker while staying as close to $150 as possible.

3. **Do Arduino basics while waiting for parts.**  
   Practice LED, resistor, button, and simple sensor examples so wiring feels less scary later.

---

## 29. Engineering Notes for ChatGPT Project Helper

When using ChatGPT inside the project, ask it to help phase-by-phase.

Good prompts:

```text
Help me complete Phase 0. I need to choose the core parts for Version 1 and stay near $150. Explain what each part does like I am new to electronics.
```

```text
I am on Phase 2. Walk me through setting up the Raspberry Pi from scratch. Do not skip beginner steps.
```

```text
I am on Phase 4. My microphone is plugged in but I do not know how to test if it works. Walk me through it slowly.
```

```text
I am on Phase 8. Help me connect Google Calendar with read-only access. Explain what OAuth means in simple words.
```

Bad prompts:

```text
Build the whole robot.
```

```text
Give me all the code for everything.
```

```text
What should I buy?
```

Those are too broad. Ask for one phase at a time.

---

## 30. Roadmap Maintenance

Update this roadmap when:

- A hardware decision changes.
- A phase is completed.
- A feature is deferred.
- A new risk is discovered.
- The budget changes.
- The project switches to a different main computer.
- The 3D shell design is chosen.

Keep the roadmap realistic. It is better to finish a simple working Version 1 than to plan a perfect robot that never gets built.
