# Design Rationales

## Lo-Fi Prototype V1

For our first prototype we wanted to build features around the main functionalities of our app: The Timer/Stopwatch and the Stats View. Here are the main concepts we tackled at this stage:

- Calendar/Statistics Separation: The app has two main views: the calendar and the statistical overview. To emphasize their functional separation, we decided to present them on distinct screens. Navigating between both modes is made seamless with the navigation buttons at the bottom. We did not choose alternative solutions such as integrating the statistical overview as a pop-up or within the settings to maintain fast navigation between both components.

- Customization Settings: Users are initially presented with the default interface and settings. For those seeking a more personalized experience, accessing the Settings page via the cog icon (top right corner) allows them to explore customization options. One notable feature is the "collapsible hours" toggle, enabling users to hide unused hours at the start of their day. Even with hours hidden, users are notified of events within that timeframe via a dot indicator. This reduces the amount of vertical space occupied by commonly unused times of day.

- Statistics View: By default, the statistical overview uses pie and bar charts to offer a visual representation of a specified timeframe for selected activities. Graphical over numerical data is preferred for ease of understanding and accessibility.

- Timer/Stopwatch: Users can access the stopwatch functionality by tapping the play button in the calendar view. Additionally, they have the option to switch to a timer mode to set a specific duration and receive notifications upon completion. This flexibility caters to varying user needs, whether it's adhering to time limits or simply tracking activity duration.

- Bookmarks: The bookmarks icon offers quick access to recently timed activities to minimize repeating entries for timed tasks.

- Icon Usage: Instead of using textual labels to navigate the interface, we use icons to reduce cognitive load and facilitate fast user recognition.

## Lo-Fi Prototype V2

The main goal of the pilot study was initially to improve the general UI’s usability by comparing v1 and v2 of the lo-fi prototypes, and more specifically, to clarify the difference between setting a timer and a stopwatch. This goal emerged from confusion we ourselves faced when implementing the timer and stopwatch features in the first version of the lo-fi prototype.

After inspecting our prototype to find something UI-related worth conducting the user study on, we identified the lack of clarity that the separation between both timed events had. With this in mind, we started brainstorming a new prototype (lo-fi v2) that had a clearer separation. This led us to pose the following question: how do different configurations of the timer/stopwatch interface affect how intuitive it is to use, measured by the total task completion time and the total clicks used?

The main thing we understood from pilot study was that the toggle function was clearly superior both in terms of speed and clarity. This way there was a much clearer distinction between the two modes while keeping them on the same modal popup. Keeping them on the same page allows us to streamline the process of doing both actions but it is not without its flaws. There are considerations to make when choosing this implementation style. The main drawbacks of this design choice is potentially cluttering the timer/stopwatch UI element. Having the toggle sit at the bottom of the model requires a balance between size, color and contrast for both the toggle and its text. This is why weve chosen to make the time slider appear only when the toggle is set to timer. This way we add minimal clutter and improve functionality massively.

## Hi-Fi Prototype V1

Our hi-fi prototype has been designed to provide a basis for our user experiment. Thus, not all functionality and screens presented in our lo-fi design are supported. For example, the settings page and event adding, modification, and deletion have not been implemented in this hi-fi prototype. Nevertheless, the addition of these features may be useful for future experiments.

The results of the pilot study on our lo-fi prototype v1 and v2 guided several changes to the design choices in our hi-fi prototype. The following highlights the main design choices:

- Timer/Stopwatch Toggle: The pilot study aimed to clarify the difference between setting a timer and a stopwatch. From the experimental results we gathered, it was clear that our initial design was flawed - participants had trouble distinguishing between both types of timed events. Nevertheless, the alternative UI that we tested received positive feedback. Thus, we chose to use v2 of the lo-fi prototype as a starting point for an improved hi-fi UI. From the verbal feedback received from participants, we mad slight adjustments to the positioning and scale of the toggle. It should be noted that, though the Timer/Stopwatch functionality's appearance is implemented, it is not "responsive"; the calendar and statistical overview do not dynamically update upon saving a timed event - this is not needed, it supports enough functionality for us to reasonably perform our user study.

- Bookmarks/Presets: From the feedback received during the pilot study, we learned that the Bookmarks feature was unclear. Participants reported that the Bookmarks icon was misleading and the general functionality was ambiguous. To address these concerns in our updated hi-fi design, we had to remind ourselves of the purpose of the Bookmarks feature: to help users initialize commonly reused timed events more quickly, without needing to enter all fields manually. From this reflection, we recognized that the naming of this feature could be enhanced to add clarity. Instead of "Bookmarks", we chose to change the naming to "Presets". Additionally, we decided to change the icon to a star, as recommended by one of the participants of the user study. To further enhance the clarity of this "Presets" functionality, we aim to add a short description at the top of the Presets window that is triggered by clicking the star icon. Due to time constraints, the Presets functionality is not yet implemented fully, the only visible change has been the icon change. Nevertheless, we intend for the general appearance to remain similar to our previous prototype (see Figure 2 in Appendix), with changes from the name "Bookmarks" to "Presets" and with the addition of a short description at the top of the window (see Section iii in Appendix).

- Statistical Overview Data Visualization: One participant of the pilot study mentioned that aside from the visual indication of time distribution in the pie chart, there should be numerical labels for more precise time estimates. Therefore, to enhance the clarity of the pie chart proportions, our hi-fi prototype incorporates two numbers per slice: an absolute measure of the number of hours a certain activity took and its relative proportion of the total tracked time. Additionally, to give precise time measures of each bar in the bar chart, we added the additional feature of clicking a specified bar to reveal precise hours. This added user interaction on the bar chart enhances user experience by providing easy access to these numerical features. The UI of the Statistical Overview closely resembles that presented in the low-fi prototypes with the inclusion of explicit data labeling in the pie chart and bar chart.

Overall, the hi-fi prototype proved capable of our needs related to our user study, enabling us to make a deeper analysis of our concept.
