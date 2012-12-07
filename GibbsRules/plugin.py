# coding=utf8
###
# Copyright (c) 2012, Terje Hoås
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import random
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
from supybot.i18n import PluginInternationalization, internationalizeDocstring

_ = PluginInternationalization('GibbsRules')

@internationalizeDocstring
class GibbsRules(callbacks.Plugin):
    """Add the help for "@plugin help GibbsRules" here
    This should describe *how* to use this plugin."""
    pass

    def gibbs(self, irc, msg, args, gibbs):
        """[number | search term]

        Returns a Gibbs Rule (rules, guidelines and principles that
        Special Agent Leroy ethro Gibbs requires his team to learn).

        No arguments return a random gibbs. A search term with several hits
        return a random one of those."""
        hits = None # List to store hits in, in case of search
        if gibbs:
            # If no argument, pick something at random.
            try:
                # If there is input, check if the string is digit.
                if gibbs.isdigit():
                    gibbs = str(gibbs)
                else:
                    # If input is text, raise exception
                    raise
            except:
                # Incase string input that is not digit.
                # This is a bit dirty. makes us have to loop through it twice.
                hits = []
                for r in gibbss:
                    if gibbs.lower() in r[1].lower():
                        hits.append(r)
                if len(hits) > 0:
                    gibbs = hits[random.randint(0, len(hits)-1)][0]
        else: # if not gibbs
            gibbs = gibbss[random.randint(0, len(gibbss)-1)][0]
        #extrahits = ""
        #if hits and len(hits) > 1:
        #    extrahits = " (" + str(len(hits)-1) + " additional hits.)"
        for r in gibbss:
            if str(r[0]) == str(gibbs):
                if str(r[0]).isdigit(): #Ohgod, the horror
                    irc.reply("Rule #{0}: {1}".format(r[0], r[1])) # + " (" + r[2] + ")")
                else:
                    irc.reply("Rule #??: {0}".format(r[1]))
                return
        irc.reply("404 - Rule not found.")
    gibbs = wrap(gibbs, [optional('text')])

gibbss = [
    [1, 'Never let suspects stay together.'],
    [2, 'Always wear gloves at a crime scene.'],
    [3, "Don't believe what you're told, Double check."],
    [4, 'If you have a secret, the best thing is to keep it to yourself. The second-best is to tell one other person if you must. There is no third best.'],
    [5, "You don't waste good."],
    [6, "Never say you're sorry. It's a sign of weakness."],
    [7, 'Always be specific when you lie.'],
    [8, 'Never take anything for granted.'],
    [9, 'Never go anywhere without a knife.'],
    [10, 'Never get personally involved in a case.'],
    [11, 'When the job is done, walk away.'],
    [12, 'Never date a coworker.'],
    [13, "Never, ever involve lawyers."],
    [14, 'Never screw (over) your partner.'],
    [15, 'Always work as a team.'],
    [16, 'If someone thinks they have the upper hand, break it.'],
    [18, "It's better to ask forgiveness than ask permission."],
    [22, 'Never, ever interrupt Gibbs in interrogation.'],
    [23, "Never mess with a Marine's coffee if you want to live."],
    [27, 'There are two ways to follow someone. 1st way - they never notice you. 2nd way - they only notice you.'],
    [35, 'Always watch the watchers.'],
    [36, "If it feels like you're being played, you probably are."],
    [38, 'Your case, your lead.'],
    [39, 'There is no such thing as coincidence.'],
    [40, "If it seems like someone's out to get you, they are."],
    [42, "Don't ever accept an apology from someone that just sucker-punched you."],
    [44, 'First things first, hide the women and children'],
    [45, 'Clean up your messes.'],
    [51, "Sometimes - you're wrong"],
    [69, "Never trust a woman who doesn't trust her man."],
    ]

Class = GibbsRules


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
