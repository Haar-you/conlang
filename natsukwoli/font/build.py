#!/usr/bin/env python2

import fontforge;
import psMat;

nats_consonants = ["p", "p_", "m", "w", "t", "t_", "ts", "ts_", "n", "s", "ch", "ch_", "sh", "k", "k_", "kw", "kw_", "q", "q_", "a", "h", "y", "r", "l", "hl", "tl", "tl_"];

def create_consonants(font):
    cp = 0xe000;

    for c in nats_consonants:
        font.createChar(cp, "Natsukwoli_%s" % c);
        gl = font[cp];
        gl.importOutlines("glyphs/%s.svg" % c);

        cp += 1;


def create_vowels(font):
    font.createChar(0xe020, "Natsukwoli_i");
    font.createChar(0xe021, "Natsukwoli_u");
    font.createChar(0xe022, "Natsukwoli_aa");
    font.createChar(0xe023, "Natsukwoli_ii");
    font.createChar(0xe024, "Natsukwoli_uu");
    font.createChar(0xe025, "Natsukwoli_e");
    font.createChar(0xe026, "Natsukwoli_o");
    font.createChar(0xe027, "Natsukwoli_an");
    font.createChar(0xe028, "Natsukwoli_in");
    font.createChar(0xe029, "Natsukwoli_un");
    font.createChar(0xe02a, "Natsukwoli_en");
    font.createChar(0xe02b, "Natsukwoli_on");
    font.createChar(0xe02c, "Natsukwoli_novowel");


    for v in ["i", "u", "aa", "ii", "uu", "an", "in", "un", "novowel", "alig"]:
        font.createChar(-1, "Natsukwoli_%s_raw" % v)
        gl = font["Natsukwoli_%s_raw" % v];
        gl.importOutlines("glyphs/%s.svg" % v);
    

    #e020-e021 short vowels
    cp = 0xe020;
    for v in ["i", "u"]:
        gl = font[cp];
        gl.addReference("dotted_circle");
        gl.addReference("Natsukwoli_%s_raw" % v, psMat.translate(700,0));
        gl.left_side_bearing = 100;
        gl.right_side_bearing = 100;
        cp += 1;

    #e022-e026 long vowels
    cp = 0xe022;
    for v in ["aa", "ii", "uu"]:
        gl = font[cp];
        gl.addReference("dotted_circle");
        gl.addReference("Natsukwoli_%s_raw" % v, psMat.translate(700,0));
        gl.left_side_bearing = 100;
        gl.right_side_bearing = 100;
        cp += 1;

    gl = font[0xe025];
    gl.addReference("Natsukwoli_alig_raw");
    gl.addReference("dotted_circle", psMat.translate(100,0));
    gl.addReference("Natsukwoli_i_raw", psMat.translate(800,0));
    gl.left_side_bearing = 100;
    gl.right_side_bearing = 100;
    
    gl = font[0xe026];
    gl.addReference("Natsukwoli_alig_raw");
    gl.addReference("dotted_circle", psMat.translate(100,0));
    gl.addReference("Natsukwoli_u_raw", psMat.translate(800,0));
    gl.left_side_bearing = 100;
    gl.right_side_bearing = 100;

    
    

def create_punctuations(font):
    #dottedcircle
    font.createChar(0x25cc, "dotted_circle");
    gl = font[0x25cc];
    gl.importOutlines("glyphs/dottedcircle.svg");


def main():
    font = fontforge.font();

    font.encoding = "UnicodeBmp";

    font.fontname = "Natsukwoli";
    font.fullname = "Natsukwoli";
    font.familyname = "Natsukwoli";

    create_punctuations(font);

    create_consonants(font);
    create_vowels(font);
    


    font.save("Natsukwoli.sfd");
    font.generate("Natsukwoli.ttf");
    font.generate("Natsukwoli.woff");




main();
