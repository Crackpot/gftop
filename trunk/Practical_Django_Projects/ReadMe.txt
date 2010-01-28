Apress.Practical Django Projects

Contents
    About the Author _________________________________________________________________xiii
    About the Technical Reviewer_______________________________________________________xv
    Introduction _____________________________________________________________________xvii

    CHAPTER 1
        Welcome to Django __________________________________________1
        What’s a Web Framework and Why Should I Want One? _______________1
        Say Hello to Django _______________________________________________2
        Say Hello to Python _______________________________________________3
        Installing Django _________________________________________________4
        Your First Steps with Django _______________________________________5
        Exploring Your Django Project ______________________________________7
        Looking Ahead ___________________________________________________8

    CHAPTER 2
        Your First Django Site: A Simple CMS ______________________9
        Configuring Your First Django Project _______________________________9
        Putting Together the CMS ________________________________________12
        A Quick Introduction to the Django Template System_________________18
        Looking Ahead __________________________________________________21

    CHAPTER 3
        Customizing the Simple CMS______________________________23
        Adding Rich-Text Editing _________________________________________23
        Adding a Search System to the CMS _______________________________26
        Improving the Search View _______________________________________31
        Improving the Search Function with Keywords ______________________33
        Looking Ahead __________________________________________________40

    CHAPTER 4
        A Django-Powered Weblog _________________________________43
        Feature Checklist ________________________________________________43
        Writing a Django Application ______________________________________44
        Projects vs_Applications _____________________________________44
        Standalone and Coupled Applications _________________________45
        Creating the Weblog Application ___________________________________45
        Designing the Models ____________________________________________47
        The Entry Model _________________________________________________52
        Basic Fields ________________________________________________53
        Slugs, Useful Defaults, and Uniqueness Constraints _____________54
        Authors, Comments, and Featured Entries _____________________55
        Different Types of Entries ____________________________________56
        Categorizing and Tagging Entries _____________________________58
        Writing Entries Without Writing HTML _________________________59
        Finishing Touches __________________________________________61
        The Weblog Models So Far _______________________________________62
        Writing the First Views ___________________________________________65
        Using Django's Generic Views _____________________________________69
        How Did Django Do That? ___________________________________70
        Decoupling the URLs _____________________________________________72
        Looking Ahead __________________________________________________75

    CHAPTER 5
        Expanding the Weblog ______________________________________77
        Writing the Link Model ___________________________________________77
        Views for the Link Model _________________________________________83
        Setting Up Views for Categories ___________________________________84
        Using Generic Views (Again) ______________________________________86
        Views for Tags __________________________________________________87
        Cleaning Up the URLConf _________________________________________89
        Handling Live Entries ____________________________________________93
        Looking Ahead __________________________________________________95

    CHAPTER 6
        Templates for the Weblog __________________________________97
        Dealing with Repetitive Elements: The Power of Inheritance___________97
        How Template Inheritance Works _____________________________99
        Limits of Template Inheritance ______________________________100
        Defining the Base Template for the Blog ___________________________100
        Section Templates ______________________________________________103
        Archives of Entries______________________________________________104
        Entry Index _______________________________________________104
        Yearly Archive _____________________________________________105
        Monthly and Daily Archives _________________________________106
        Entry Detail _______________________________________________107
        Templates for Other Types of Content _____________________________110
        Extending the Template System with Custom Tags _________________111
        How a Django Template Works ______________________________112
        A Simple Custom Tag ______________________________________113
        Writing a More Flexible Tag with Arguments __________________116
        Writing the Compilation Function ____________________________116
        Writing the LatestContentNode ______________________________119
        Registering and Using the New Tag __________________________120
        Looking Ahead _________________________________________________122

    CHAPTER 7
        Finishing the Weblog ______________________________________123
        Comments and django.contrib.comments _________________________123
        Installing the Comments Application _________________________123
        Basic Setup _______________________________________________124
        Retrieving Lists of Comments for Display _____________________128
        Comment Moderation ___________________________________________129
        Signals and the Django Dispatcher___________________________130
        Building the Automatic Comment Moderator __________________131
        Adding Akismet Support ____________________________________132
        E-mail Notification of Comments ____________________________135
        Dealing with Moderated Comments in Public-Facing
        Templates _____________________________________________137
        Adding Feeds __________________________________________________138
        LatestEntriesFeed _________________________________________139
        Entries by Category: A More Complex Feed Example ___________142
        Looking Ahead ________________________________________________146

    CHAPTER 8
        A Social Code-Sharing Site ________________________________147
        Feature Checklist _______________________________________________147
        Setting Up the Application _______________________________________148
        Building the Initial Models _______________________________________148
        The Language Model _______________________________________149
        The Snippet Model _________________________________________151
        Testing the Snippets Application __________________________________154
        Initial Views for Snippets and Languages __________________________155
        CSS for pygments Syntax Highlighting________________________156
        Views for Languages _______________________________________157
        An Advanced View: Top Authors _____________________________158
        Improving the View of Top Authors ___________________________159
        Adding a top_languages View _______________________________162
        Looking Ahead _________________________________________________163

    CHAPTER 9
        Form Processing in the Code-Sharing Application ______165
        A Brief Tour of Django’s Form System_____________________________165
        A Simple Example _________________________________________166
        Validating the Username____________________________________168
        Validating the Password ____________________________________169
        Creating the New User _____________________________________169
        How Form Validation Works _________________________________171
        Processing the Form _______________________________________173
        A Form for Adding Code Snippets_________________________________175
        Writing a View to Process the Form __________________________178
        Automatically Generating a Form for Adding Snippets _______________180
        Simplifying Templates That Display Forms _________________________183
        Editing Snippets ________________________________________________184
        Looking Ahead _________________________________________________186

    CHAPTER 10 Finishing the Code-Sharing Application __________________187
        Bookmarking Snippets __________________________________________187
        Basic Bookmark Views __________________________________________188
        A New Template Tag: {% if_bookmarked %} _______________________192
        Parsing Ahead in a Django Template _________________________193
        Resolving Variables Inside a Template Node __________________194
        Using RequestContext to Automatically Populate Template
        Variables ___________________________________________________196
        Adding the User Rating System __________________________________198
        Rating Snippets ___________________________________________201
        Adding an {% if_rated %} Template Tag ______________________202
        Retrieving a User’s Rating __________________________________203
        Looking Ahead _________________________________________________204

    CHAPTER 11 Writing Reusable Django Applications ___________________205
        One Thing at a Time ____________________________________________206
        Staying Focused ___________________________________________206
        Advantages of Tightly Focused Applications ___________________207
        Developing Multiple Applications _________________________________208
        Drawing the Lines Between Applications _____________________209
        Splitting Up the Snippets Application _________________________210
        Building for Flexibility ___________________________________________210
        Flexible Form Handling _____________________________________211
        Flexible Template Handling _________________________________212
        Flexible Post-Form Processing ______________________________213
        Flexible URL Handling ______________________________________214
        Taking Advantage of Django’s APIs __________________________215
        Staying Generic ___________________________________________215
        Distributing Django Applications __________________________________217
        Python Packaging Tools ____________________________________217
        Writing a setup.py Script with distutils________________________218
        Standard Files to Include in a Package _______________________219
        Documenting an Application ________________________________220
        Looking Ahead _________________________________________________224
