import java.util.*;
import java.awt.Desktop;
import java.net.URI;

public class MoodMusicMenuApp {
    static Scanner scanner = new Scanner(System.in);
    static Map<String, Map<String, String[]>> playlistData = new LinkedHashMap<>();

    public static void main(String[] args) {
        initializePlaylists();

        System.out.println("\n🎶 Welcome to Mood Music Recommender 🎶");

        while (true) {
            System.out.println("\n🌍 Select your preferred language:");
            System.out.println("1. Hindi");
            System.out.println("2. Telugu");
            System.out.println("3. English");
            System.out.println("4. Exit");
            System.out.print("Enter your choice (1–4): ");

            int langChoice;
            try {
                langChoice = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("❌ Please enter a valid number (1–4).");
                continue;
            }

            if (langChoice == 4) {
                System.out.println("\n👋 Thanks for using Mood Music Recommender! Keep vibing! 🎧");
                break;
            }

            String language = switch (langChoice) {
                case 1 -> "hindi";
                case 2 -> "telugu";
                case 3 -> "english";
                default -> {
                    System.out.println("❌ Invalid choice. Please try again.");
                    yield null;
                }
            };

            if (language == null) continue;

            Map<String, String[]> moodMap = playlistData.get(language);
            List<String> moods = new ArrayList<>(moodMap.keySet());

            System.out.println("\n🎵 Available moods in " + capitalize(language) + ":");
            for (int i = 0; i < moods.size(); i++) {
                System.out.println((i + 1) + ". " + moods.get(i));
            }
            System.out.println((moods.size() + 1) + ". Go Back");

            System.out.print("\nEnter your mood number: ");
            int moodChoice;
            try {
                moodChoice = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("❌ Please enter a valid number.");
                continue;
            }

            if (moodChoice == moods.size() + 1) {
                System.out.println("↩️ Returning to language menu...");
                continue;
            }

            if (moodChoice < 1 || moodChoice > moods.size()) {
                System.out.println("❌ Invalid mood number. Try again.");
                continue;
            }

            String selectedMood = moods.get(moodChoice - 1);
            String[] data = moodMap.get(selectedMood);

            System.out.println("\n🎧 Mood: " + selectedMood);
            System.out.println("💬 Quote: " + data[1]);
            System.out.println("🎵 Opening " + capitalize(language) + " music...");

            try {
                Desktop.getDesktop().browse(new URI(data[0]));
            } catch (Exception e) {
                System.out.println("⚠️ Unable to open link. Please copy manually: " + data[0]);
            }

            System.out.print("\nWould you like to try another mood or language? (yes/no): ");
            String again = scanner.nextLine().trim().toLowerCase();
            if (!again.equals("yes") && !again.equals("y")) {
                System.out.println("\n👋 Thanks for using Mood Music Recommender! Have a musical day! 🎶");
                break;
            }
        }
    }

    static void initializePlaylists() {
        playlistData.put("hindi", new LinkedHashMap<>());
        playlistData.put("telugu", new LinkedHashMap<>());
        playlistData.put("english", new LinkedHashMap<>());

        // ✅ HINDI (YouTube Search Links)
        playlistData.get("hindi").put("Violence", new String[]{
            "https://www.youtube.com/results?search_query=hindi+action+songs",
            "Channel your fire into focus."
        });
        playlistData.get("hindi").put("Motivational", new String[]{
            "https://www.youtube.com/results?search_query=hindi+motivational+songs",
            "Push yourself — because no one else will."
        });
        playlistData.get("hindi").put("Spiritual", new String[]{
            "https://www.youtube.com/results?search_query=hindi+bhajan+songs",
            "Peace comes from within. Do not seek it without."
        });
        playlistData.get("hindi").put("Love", new String[]{
            "https://www.youtube.com/results?search_query=hindi+romantic+songs",
            "Love is composed of a single soul inhabiting two bodies."
        });
        playlistData.get("hindi").put("Chill", new String[]{
            "https://www.youtube.com/results?search_query=hindi+chill+songs",
            "Relax. Recharge. Refocus."
        });
        playlistData.get("hindi").put("Heartbroken", new String[]{
            "https://www.youtube.com/results?search_query=hindi+sad+songs",
            "The heart will heal, even if it takes time."
        });

        // ✅ TELUGU (YouTube Search Links)
        playlistData.get("telugu").put("Violence", new String[]{
            "https://www.youtube.com/results?search_query=telugu+mass+songs",
            "Let your rage become your rhythm."
        });
        playlistData.get("telugu").put("Motivational", new String[]{
            "https://www.youtube.com/results?search_query=telugu+motivational+songs",
            "Greatness begins with a single step."
        });
        playlistData.get("telugu").put("Spiritual", new String[]{
            "https://www.youtube.com/results?search_query=telugu+devotional+songs",
            "In silence, the soul speaks."
        });
        playlistData.get("telugu").put("Love", new String[]{
            "https://www.youtube.com/results?search_query=telugu+love+songs",
            "To love and be loved is everything."
        });
        playlistData.get("telugu").put("Chill", new String[]{
            "https://www.youtube.com/results?search_query=telugu+chill+songs",
            "Let the music melt your stress."
        });
        playlistData.get("telugu").put("Heartbroken", new String[]{
            "https://www.youtube.com/results?search_query=telugu+sad+songs",
            "Even broken hearts beat with beauty."
        });

        // ✅ ENGLISH (YouTube Search Links)
        playlistData.get("english").put("Violence", new String[]{
            "https://www.youtube.com/results?search_query=english+rock+workout+songs",
            "Turn your fury into fuel."
        });
        playlistData.get("english").put("Motivational", new String[]{
            "https://www.youtube.com/results?search_query=english+motivational+songs",
            "Discipline is the bridge between goals and accomplishment."
        });
        playlistData.get("english").put("Spiritual", new String[]{
            "https://www.youtube.com/results?search_query=english+spiritual+music",
            "Let your soul catch up with your body."
        });
        playlistData.get("english").put("Love", new String[]{
            "https://www.youtube.com/results?search_query=english+love+songs",
            "Love is the closest thing we have to magic."
        });
        playlistData.get("english").put("Chill", new String[]{
            "https://www.youtube.com/results?search_query=english+chill+music",
            "Breathe in calm. Breathe out chaos."
        });
        playlistData.get("english").put("Heartbroken", new String[]{
            "https://www.youtube.com/results?search_query=english+sad+songs",
            "Scars remind us where we've been, not where we're going."
        });
    }

    static String capitalize(String word) {
        return word.substring(0, 1).toUpperCase() + word.substring(1);
    }
}