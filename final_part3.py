import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
pd.options.mode.chained_assignment = None
pd.options.display.max_columns = None
palette='Set1'
no_pass_palette=[(0.21568627450980393, 0.49411764705882355, 0.7215686274509804), (0.30196078431372547, 0.6862745098039216, 0.2901960784313726), (0.596078431372549, 0.3058823529411765, 0.6392156862745098), (1.0, 0.4980392156862745, 0.0), (1.0, 1.0, 0.2), (0.6509803921568628, 0.33725490196078434, 0.1568627450980392), (0.9686274509803922, 0.5058823529411764, 0.7490196078431373), (0.6, 0.6, 0.6), (0.8941176470588236, 0.10196078431372549, 0.10980392156862745),]

# Introduce the dataset.
df = pd.read_csv('data/eod_2023_burke_county_nc.csv', sep='\t')
relevant_columns = ['order',
                    'family',
                    'genus',
                    'species',
                    'decimalLatitude',
                    'decimalLongitude',
                    'day',
                    'month',
                    'individualCount'
                    ]
df = df[relevant_columns]
cats = df['order'].value_counts().index
df['order'] = pd.Categorical(df['order'], categories=cats, ordered=True)

# Question: Why would a birdwatcher want to come to Burke County? Where and
# when should they go birding to see the most exciting birds?




# Firtly, what are the types of birds present in Burke County?
# Here are the observations by taxonomic order:
ax = sns.countplot(data=df, y='order', palette=palette, order = df['order'].value_counts().index)

labels = df['order'].value_counts(ascending=False).values
ax.bar_label(container=ax.containers[0], labels=labels)
plt.xlim(0, 8300)
plt.xlabel("Count")
plt.ylabel("Order")
plt.title("Bird Observations by Order")

# Passeriformes, the songbirds, dominate. 18 of the 41 orders reportable on
# eBird are represented in Burke County. Unfortunately there are no ostriches,
# parrots, or penguins... those are some of the missing orders.




# Anyway, let's once again remove Passeriformes:
plt.figure()
no_pass_df = df[df['order'] != 'Passeriformes']
ax = sns.countplot(data=no_pass_df, y='order', palette=no_pass_palette, order = no_pass_df['order'].value_counts().iloc[:17].index)

labels = no_pass_df['order'].value_counts(ascending=False).values[:-1]
ax.bar_label(container=ax.containers[0], labels=labels)
plt.xlim(0, 830)
plt.xlabel("Count")
plt.ylabel("Order")
plt.title("Bird Observations by Order (No Passeriformes)")

# I actually have memorized all of the orders now. To answer your previous
# question Dr. Hodges, hummingbirds are in the order Apodiformes.




# We can go even deeper by looking for specific species.
plt.figure(figsize=(10.667, 6))
ax = sns.countplot(data=df, y='species', hue='order', dodge=False, palette=palette, order = df['species'].value_counts().iloc[:20].index)
plt.xlabel("Count")
plt.ylabel("Species")
plt.title("Bird Observations by Species")
ax.legend(fontsize=9.5)

# There are 183 different bird species observed in Burke County, so in the full
# plot there are just a bunch of birds at the bottom with like one or two
# observations making all the labels too small. I pulled out the top 20, which
# are all the birds with more than 150 observations.




# Now that we know what types of birds we'll see in Burke county, we might want
# to know where to go to find the most birds. Here are all the observations by
# latitude and longitude.

plt.figure(figsize=(10, 10))
sns.scatterplot(data=df, x='decimalLongitude', y='decimalLatitude', c="#3b3b3b")
plt.ylim(35.4, 36.1)
plt.xlim(-82.02, -81.32)
plt.title("Bird Observations by Location")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.figure(figsize=(10, 10))
sns.scatterplot(data=df[df['order']=='Passeriformes'], x='decimalLongitude', y='decimalLatitude', c=sns.color_palette('Set1').as_hex()[0])
plt.ylim(35.4, 36.1)
plt.xlim(-82.02, -81.32)
plt.title("Bird Observations by Location (Passeriformes)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.figure(figsize=(10, 10))
sns.scatterplot(data=df[df['order']=='Accipitriformes'], x='decimalLongitude', y='decimalLatitude', c=sns.color_palette('Set1').as_hex()[2])
plt.ylim(35.4, 36.1)
plt.xlim(-82.02, -81.32)
plt.title("Bird Observations by Location (Accipitriformes)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.figure(figsize=(10, 10))
sns.scatterplot(data=df[df['order']=='Anseriformes'], x='decimalLongitude', y='decimalLatitude', c=sns.color_palette('Set1').as_hex()[3])
plt.ylim(35.4, 36.1)
plt.xlim(-82.02, -81.32)
plt.title("Bird Observations by Location (Anseriformes)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")


# It's also important to acknowledge the biases in this dataset. This shows all
# of the recorded bird sightings, not all of the existing birds. So it's not
# like there are zero birds in this part of bird county, there's just no one
# there to see them.




# So, now we know where to go to find our birds, and what types of birds we
# might see. The only question left for our hypothetical bird watcher: when
# sbould he go birdwatching?

plt.figure(figsize=(10.667, 6))
ax = sns.countplot(data=df, x='month', color='#3b3b3b')

labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ax.set_xticklabels(labels)
plt.title("Bird Observations by Month")
plt.xlabel("Month")
plt.ylabel("Count")

#Birds are more common in the spring as
# you'd expect. They are also seen more infall when they are migrating. I
# thought it was interesting that there aren't many bird sightings in summer.
# I did a little Googling, and it's seems to be because it's no longer the
# breeding season, where birds are singing to find mates, and it's now the
# molting season, when birds replace their feathers. They have reduced flight
# ability, and therefore lay low to avoid predators. Finally, natural food
# such as berries are more abundant during summer, which means less birds will
# be visiting human setups such as birdfeeders. Therefore, going back to the
# biases of the data, there would be less human sightings of just people
# watching their birdfeeders.

# These trends follow in the orders as well.
plt.figure(figsize=(10.667, 6))
ax = sns.countplot(data=df[df['order']=='Passeriformes'], x='month', color=sns.color_palette('Set1').as_hex()[0])

labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ax.set_xticklabels(labels)
plt.title("Bird Observations by Month (Passeriformes)")
plt.xlabel("Month")
plt.ylabel("Count")

plt.figure(figsize=(10.667, 6))
ax = sns.countplot(data=df[df['order']=='Anseriformes'], x='month', color=sns.color_palette('Set1').as_hex()[3])

labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ax.set_xticklabels(labels)
plt.title("Bird Observations by Month (Anseriformes)")
plt.xlabel("Month")
plt.ylabel("Count")
# There are way less ducks in the winter... because they fly south.


plt.figure(figsize=(10.667, 6))
ax = sns.countplot(data=df[df['order']=='Charadriiformes'], x='month', color=sns.color_palette('Set1').as_hex()[6])

labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ax.set_xticklabels(labels)
plt.title("Bird Observations by Month (Charadriiformes)")
plt.xlabel("Month")
plt.ylabel("Count")
# In contrast, the Charadriiformes (mostly killdeer) don't, and therefore are
# more present in winter.

# So, to conclude, birdwatchers in Burke County will be seeing mostly songbirds
# throughout all of Burke County, with more waterbirds near bodies of water,
# especially in the spring. What a surprise! But it's nice that the data backs
# our assumptions up.




# And as a bonus graph I found interesting.

plt.figure(figsize=(10.667, 6))
sns.barplot(data=df, x='individualCount', y='order', palette=palette, errorbar=None)
plt.title("Number of Birds per Observation by Order")
plt.xlabel("Count")
plt.ylabel("Order")

plt.figure(figsize=(10.667, 6))
sns.barplot(data=df, x='individualCount', y='species', hue='order', palette=palette, dodge=False, order=df.groupby('species')['individualCount'].mean().sort_values(ascending=False).iloc[:10].index, errorbar=None)
plt.title("Number of Birds per Observation by Species")
plt.xlabel("Count")
plt.ylabel("Species")


# TO-DO
# Set plot and axes labels
# Set colors to be nice
# Google the species and order names