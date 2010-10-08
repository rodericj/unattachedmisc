unicode_doc = u"\xe4\xf6\xfc and some other things"
unicode_query = u'\xe4\xf6\xfc'
unicode_result = u"[[HIGHLIGHT]]\xe4\xf6\xfc[[ENDHIGHLIGHT]] and some other things"

notfound_doc = "hello, this is a thing"
notfound_query = "I don't see this anywhere in the document"
notfound_result = ""

whole_doc = "strawberry docquery"
whole_query = "strawberry docquery"
whole_result = "[[HIGHLIGHT]]strawberry docquery[[ENDHIGHLIGHT]]"

given_doc = "Little star's deep dish pizza sure is fantastic."
given_query = "deep dish pizza"
given_result = "Little star's [[HIGHLIGHT]]deep dish pizza[[ENDHIGHLIGHT]] sure is fantastic."

cheeseburger_result = "Cheeseburger, [[HIGHLIGHT]]sweet potato fries[[ENDHIGHLIGHT]], milkshakes, oh my SO FREAKIN' GOOD."
cheeseburger_query = "sweet potato fries"
cheeseburger_doc = """Gott's got solid cheeseburgers, some of the best tasting sweet potato fries, onion rings, and the cannot miss white pistachio milkshake, this made for a heavy, but tasty lunch.  I was also wondering what all the buzz was about since there always seems to be a long line there.  

I've been told that the fish tacos are also pretty solid there too, so it looks like another tip is in store!

The only thing I can probably fault it on is the price.  I understand that this is supposed to be a step up from your typical in n outs and five guys, but it was hard to gauge whether the taste was also $2-3 better."""

pizzahacker_query = "tomato sauce"
pizzahacker_result = "The standout item that night was the juicy and rich [[HIGHLIGHT]]tomato sauce[[ENDHIGHLIGHT]]." 
pizzahacker = """Looooooong overdue review! But I can probably vouch that Matt and I have eaten more pizzas from Pizza Hacker combined than most Pizza Hacker monsters combined. The exceptions of course are Jeff the inventor himself and his lucky guinea pigs.

Given how much Matt talks trash about the pizzas around the Bay Area, I was curious what he would think about this new street cart movement with the Pizza Hacker. I forwarded Matt some pictures and a few good article writeup on the FrankenWeber. One look at the slight charred, bubbly crusts, and he gave a thumbs up, "This looks promising."

We descended upon Pizza Hacker as one of his last customers during LitQuake. It took us over an hour to figure out that the food carts were in a teenie park - Mission Playground (LitQuake posted no locations), I was battling the SF winds, cold from holding chilled bottled beer all night, starving, and cranky. This better be an awesome pizza. And awesome is what we got from a traditional Margherita pizza with fresh basil, straight from an herb plant, beautifully torn fresh mozzarella, and tasty heirloom tomato sauce. We also got the clam shell pizza which was a knock out. Who knew a FrankenWeber could churn out a Neapolitan pizza and bake seafood, hot enough to kill the germies! The standout item that night was the juicy and rich tomato sauce. I remember pining for more of that sauce!

Fast forward a couple weeks, and we catch him Uptown. The Margherita with regular or buffalo mozzarella has become a staple. The next specialty pizza we try has stinging nettles, some sausage from Bi-Rite (can anything go wrong with Bi-Rite? a resounding now), and stinging nettles. OOOO, another winner.

Another few weeks go by, oh hell, let's just bring the whole operation to  the backyard. That's right, Matt and I had a joint pizza birthday party! We asked Jeff if would an event, and he obliged! When we were planning on the ingredients, we decided on 

SAUCE
Organic Early Girl Tomato Sauce with garlic, basil, oregano, olive oil, and grana padano

CHEESES
fresh cow mozzarella
buffalo mozzarella
parmigiano reggiano stravecchio
raw milk cave aged blue cheese

MEATS
Bi-Rite housemade hot Italian salsiccia
Citterio pancetta
Creston Valley Greek lamb sausage
Palacios Spanish style chorizo 

PRODUCE
Mariquita Farms stinging nettles
organic black Mission figs
caramelized onions
Woodstock Farms organic mixed mushrooms - shiitake, shimeiji, field, abalone
Pasture raised eggs from Lazy 69 Ranch and Soul Food Farm
Tutto Calabria crushed hot chili peppers

I am salivating as I type out these ingredients that the guests could choose from. Or they could go with some suggested pies: marinara, margherita, crowd pleaser (Organic fig, caramelized onion, blue cheese, mozzarella, tomato sauce, rosemary), or the Jeff concocted "Catthew Bday Special" (Marinara pizza with pancetta, nettles, parmesan / mozzarella, egg).

Jeff brought the whole operation and 2 very helpful assistants, Aron and Jon Darsky, former pizza maker/chef from Flour+Water. Aron was always thinking on his feet to resolve any issue at the moment and explain to guests topping recommendations. Some guests went against recommendation and piled all the meats on the pizza, which was so good, none-the-less. Jon meticulously laid the ingredients as if he were plating a pizza! No lopsided portions, nope, nada. And Jeff, the face of FrankenWeber, was busy ensuring that oven was brought up to scorching temps and that the crusts were perrrrrrrrrfect.

My pizza brings all my friends to the yard, that's right, my dough is betta than yours! 

And so this love for Pizza Hacker's pizza continues on today. The best part of this process is that Jeff introduced me to many delectable toppings on a pizza. His signature touch is sprinkling yummy salt on the crust, sometimes it is lavender salt and sometimes it some gourmet salt that I have yet to learn about. Although he has not changed his dough recipe, the pizza dough is getting thinner and crispier, and the crust bubbles with enthusiasm.

As much as Michael Bauer has written up on his favorite pizza places, Gialiana (over and over again on his SFGate blog), Delfina's, Pizzaiolo, Tony's, A16, and many other places, I wish Mr. Bauer would swing by Pizza Hacker and give him a review. I am curious how Jeff's pizza stacks up with the "intuitions" of SF. I promise Mr. Bauer won't be sorry!

Selling the instructions or the actual FrankenWeber is Jeff's ultimate goal. Slinging pies on the streets is great marketing for it!"""

