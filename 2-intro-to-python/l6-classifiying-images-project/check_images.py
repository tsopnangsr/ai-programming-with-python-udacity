#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND/intropylab-classifying-images/check_images.py
#
# TODO: 0. Fill in your information in the programming header below
# PROGRAMMER:Tsopnang Saounde Romaric
# DATE CREATED: 4 November 2019
# REVISED DATE: 8 November 2019            <=(Date Revised - if any)
# REVISED DATE: 05/14/2018 - added import statement that imports the print
#                           functions that can be used to check the lab
# PURPOSE: Check images & report results: read them in, predict their
#          content (classifier), compare prediction to actual value labels
#          and output results
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
import argparse
from time import time, sleep
from os import listdir

# Imports classifier function for using CNN to classify images
from classifier import classifier

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Main program function defined below
def main():
    # TODO: 1. Define start_time to measure total program runtime by
    # collecting start time
    start_time = time()
    #print(start_time)

    # TODO: 2. Define get_input_args() function to create & retrieve command
    # line arguments
    in_arg = get_input_args()

    # Accesses values of Arguments 1, 2 and 3 by printing them
    """
    print("Argument 1:", in_arg.dir, "  Argument 2:", in_arg.arch,
          "  Argument 3:", in_arg.dogfile)
    #in_arg.dir - in_arg.arch - in_arg.dogfile
    """

    # TODO: 3. Define get_pet_labels() function to create pet image labels by
    # creating a dictionary with key=filename and value=file label to be used
    # to check the accuracy of the classifier function
    answers_dic = get_pet_labels(in_arg.dir)
    #Iterating through a dictionary printing all keys & their associated values
    """
    for key in answers_dic:
        #print("Key=", key, " Value=", petlabels_dic[key])
        print("Key= %-35s  Value= %s" % (key, answers_dic[key]))
    """

    # TODO: 4. Define classify_images() function to create the classifier
    # labels with the classifier function using in_arg.arch, comparing the
    # labels, and creating a dictionary of results (result_dic)
    result_dic = classify_images(in_arg.dir, answers_dic, in_arg.arch)
    '''
    #Declaring variables to count Matches and Non-Matches
    n_matches = 0
    n_non_matches = 0
    #Iterating through a dictionary printing matched values
    print("** MATCHES")
    for key in result_dic:
        if result_dic[key][2] == 1:
            n_matches += 1
            print("Label= %-25s  Class= %s " % (result_dic[key][0], result_dic[key][1]))

    #Iterating through a dictionary printing matched values
    print("** NON MATCHES")
    for key in result_dic:
        if result_dic[key][2] == 0:
            n_non_matches += 1
            print("Label= %-25s  Class= %s " % (result_dic[key][0], result_dic[key][1]))
    print("** The total amount of images is ", n_matches+n_non_matches, "** MATCHES", n_matches, "** NON MATCHES", n_non_matches)
    '''
    # TODO: 5. Define adjust_results4_isadog() function to adjust the results
    # dictionary(result_dic) to determine if classifier correctly classified
    # images as 'a dog' or 'not a dog'. This demonstrates if the model can
    # correctly classify dog images as dogs (regardless of breed)
    adjust_results4_isadog(result_dic, in_arg.dogfile)
    """
    n_matches = 0
    n_non_matches = 0
    #Iterating through a dictionary printing matched values
    print("** MATCHES")
    for key in result_dic:
        if result_dic[key][2] == 1:
            n_matches += 1
            print("Label= %-25s  Class= %s %s %s " % (result_dic[key][0], result_dic[key][1], str(result_dic[key][3]), str(result_dic[key][4])))

    #Iterating through a dictionary printing matched values
    print("** NON MATCHES")
    for key in result_dic:
        if result_dic[key][2] == 0:
            n_non_matches += 1
            print("Label= %-25s  Class= %s %s %s " % (result_dic[key][0], result_dic[key][1], str(result_dic[key][3]), str(result_dic[key][4])))
    print("** The total amount of images is ", n_matches+n_non_matches, "** MATCHES", n_matches, "** NON MATCHES", n_non_matches)
    """

    # TODO: 6. Define calculates_results_stats() function to calculate
    # results of run and puts statistics in a results statistics
    # dictionary (results_stats_dic)
    results_stats_dic = calculates_results_stats(result_dic)
    """
    print(results_stats_dic)
    """

    # TODO: 7. Define print_results() function to print summary results,
    # incorrect classifications of dogs and breeds if requested.
    #print_results()
    print_results(result_dic, results_stats_dic, in_arg.arch, True, True)

    # TODO: 1. Define end_time to measure total program runtime
    # by collecting end time
    #sleep(5)
    end_time = time()

    # TODO: 1. Define tot_time to computes overall runtime in
    # seconds & prints it in hh:mm:ss format
    tot_time = int(end_time - start_time)
    #tot_time = 86465
    hh = tot_time // 3600
    mm = (tot_time - 3600*hh) // 60
    ss = (tot_time - 3600*hh - 60*mm)
    print("\n** Total Elapsed Runtime in seconds :", tot_time)
    print("\n** Total Elapsed Runtime in hh:mm:ss : {}:{}:{}".format(hh, mm, ss))



# TODO: 2.-to-7. Define all the function below. Notice that the input
# parameters and return values have been left in the function's docstrings.
# This is to provide guidance for achieving a solution similar to the
# instructor provided solution. Feel free to ignore this guidance as long as
# you are able to achieve the desired outcomes with this lab.

def get_input_args():
    """
    Retrieves and parses the command line arguments created and defined using
    the argparse module. This function returns these arguments as an
    ArgumentParser object.
     3 command line arguments are created:
       dir - Path to the pet image files(default- 'pet_images/')
       arch - CNN model architecture to use for image classification(default-
              pick any of the following vgg, alexnet, resnet)
       dogfile - Text file that contains all labels associated to dogs(default-
                'dognames.txt'
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object
    dir = 'pet_images/', arch, dogfile = 'dognames.txt'
    """
    #Creates Argument Parser object named Parser
    parser = argparse.ArgumentParser()
    #Argument 1: That's the path to the pet image files (default- "pet_images/")
    parser.add_argument('--dir', type = str, default = 'pet_images/', help = 'Path to the pet image files')

    #Argument 2: That's the CNN model achitecture to use for image classification
    parser.add_argument('--arch', type = str, default = 'vgg', help = 'CNN model for image classification: vgg, alexnet, resnet')

    #Argument 3: That's Text file that contains dog names
    parser.add_argument('--dogfile', type = str, default = 'dognames.txt')

    #Returning variable parse_args()
    return parser.parse_args()
    #pass


def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels based upon the filenames of the image
    files. Reads in pet filenames and extracts the pet image labels from the
    filenames and returns these labels as petlabel_dic. This is used to check
    the accuracy of the image classifier model.
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by pretrained CNN models (string)
    Returns:
     petlabels_dic - Dictionary storing image filename (as key) and Pet Image
                     Labels (as value)
    """
    #Retrive the filenames form forlder image_dir
    filename_list = listdir(image_dir)
    #Creates empty dictionary named petlabels_dic
    petlabels_dic = dict()
    #Print 10 of the filenames form folder image_dir
    """
    print("\nPrints 10 filenames from folder image_dir")
    for idx in range(0, 10, 1):
        print("%2d file: %-25s" % (idx + 1,filename_list[idx]))
    """
    for idx in range(0, len(filename_list), 1):
        if filename_list[idx] not in petlabels_dic:
            petlabels_dic[filename_list[idx]] = " ".join(filename_list[idx].split("_")[0:-1]).lower()
        else:
            print("** Warning: Key =", filename_list[idx],
                  "already exists in petlabel_dic with value =", petlabels_dic[filename_list[idx]])

    return petlabels_dic
    #pass


def classify_images(images_dir, petlabel_dic, model):
    """
    Creates classifier labels with classifier function, compares labels, and
    creates a dictionary containing both labels and comparison of them to be
    returned.
     PLEASE NOTE: This function uses the classifier() function defined in
     classifier.py within this function. The proper use of this function is
     in test_classifier.py Please refer to this program prior to using the
     classifier() function to classify images in this function.
     Parameters:
      images_dir - The (full) path to the folder of images that are to be
                   classified by pretrained CNN models (string)
      petlabel_dic - Dictionary that contains the pet image(true) labels
                     that classify what's in the image, where its key is the
                     pet image filename & its value is pet image label where
                     label is lowercase with space between each word in label
      model - pretrained CNN whose architecture is indicated by this parameter,
              values must be: resnet alexnet vgg (string)
     Returns:
      results_dic - Dictionary with key as image filename and value as a List
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)   where 1 = match between pet image and
                    classifer labels and 0 = no match between labels
    """
    #Creates empty dictionary to store the values to return
    result_dic = dict()
    for img_path in petlabel_dic:
        full_path = images_dir + img_path
        classifier_label = classifier(full_path, model).lower().strip()
        pet_label = petlabel_dic[img_path]
        found_idx = classifier_label.find(pet_label)
        #if(petlabel_dic[img_path] in image_classification):
        if(found_idx == 0 and len(pet_label) == len(classifier_label)):
            #True Match with single term.
            comparision = 1
        elif(( (found_idx == 0) or (classifier_label[found_idx - 1] == " ")) and
            ((found_idx + len(pet_label) == len(classifier_label) ) or
            (classifier_label[found_idx + len(pet_label) :found_idx + len(pet_label) +1] in  (" ",",")))):
            #True Match with multiple terms
            comparision = 1
        else:
            comparision = 0
        result_dic[img_path] = [pet_label, classifier_label, comparision]
    return result_dic
    #pass


def adjust_results4_isadog(result_dic, dogsfile):
    """
    Adjusts the results dictionary to determine if classifier correctly
    classified images 'as a dog' or 'not a dog' especially when not a match.
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and
                            classifer labels and 0 = no match between labels
                    --- where idx 3 & idx 4 are added by this function ---
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and
                            0 = pet Image 'is-NOT-a' dog.
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image
                            'as-a' dog and 0 = Classifier classifies image
                            'as-NOT-a' dog.
     dogsfile - A text file that contains names of all dogs from ImageNet
                1000 labels (used by classifier model) and dog names from
                the pet image files. This file has one dog name per line.
                Dog names are all in lowercase with spaces separating the
                distinct words of the dogname. This file should have been
                passed in as a command line argument. (string - indicates
                text file's name)
    Returns:
           None - results_dic is mutable data type so no return needed.
    """
    dognames_dic = dict()
    for dogname in open(dogsfile, "r"):
        dogname = dogname.rstrip()
        if dogname not in dognames_dic:
            dognames_dic[dogname] = 1
        else:
            print("** Warning, the item ", dogname, " Already exists")
    label_is_a_dog = 0
    class_is_a_dog = 0
    for result in result_dic:
        if dognames_dic.get(result_dic[result][0], 0) == 1:
            label_is_a_dog = 1
        else:
            label_is_a_dog = 0
        if dognames_dic.get(result_dic[result][1], 0) == 1:
            class_is_a_dog = 1
        else:
            class_is_a_dog = 0
        result_dic[result].extend([label_is_a_dog, class_is_a_dog])
    #pass


def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the run using classifier's model
    architecture on classifying images. Then puts the results statistics in a
    dictionary (results_stats) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and
                            0 = pet Image 'is-NOT-a' dog.
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image
                            'as-a' dog and 0 = Classifier classifies image
                            'as-NOT-a' dog.
    Returns:
     results_stats - Dictionary that contains the results statistics (either a
                     percentage or a count) where the key is the statistic's
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value
    """
    results_stats = dict()

    n_images = len(results_dic) #Z

    n_correct_dogs = 0 #A
    n_correct_not_dogs = 0 #C
    n_correct_breed = 0 #E

    pct_correct_dogs = 0
    pct_correct_not_dogs = 0
    pct_correct_breed = 0

    n_dog_images = 0 #B
    n_not_dog_images = 0 #D
    n_label_matches = 0 #Y

    pct_label_matches = 0
    #Iterating through results_dic to update my counters
    for result in results_dic:
        if results_dic[result][3] == 1 and results_dic[result][4] == 1:
            n_correct_dogs += 1 #A

        if results_dic[result][3] == 1:
            n_dog_images += 1 #B

        if results_dic[result][3] == 0 and results_dic[result][4] == 0:
            n_correct_not_dogs += 1 #C

        if results_dic[result][3] == 0:
            n_not_dog_images += 1 #D

        if results_dic[result][3] == 1 and results_dic[result][2] == 1:
            n_correct_breed += 1 #E

        if results_dic[result][2] == 1:
            n_label_matches += 1 #Y
    pct_correct_dogs = (n_correct_dogs/n_dog_images) * 100 #A/B * 100
    if n_correct_not_dogs > 0:
        pct_correct_not_dogs = (n_correct_not_dogs/n_not_dog_images) * 100 #C/D *100
    else:
        pct_correct_not_dogs = 0
    pct_correct_breed = (n_correct_breed/n_dog_images) * 100 #E/B * 100
    pct_label_matches = (n_label_matches/n_images) * 100 #Y/Z * 100

    #Updating results_stats dictionnary using computed variables
    results_stats["n_images"] = n_images #Z
    results_stats["n_correct_dogs"] = n_correct_dogs #A
    results_stats["n_dog_images"] = n_dog_images #B
    results_stats["n_correct_not_dogs"] = n_correct_not_dogs #C
    results_stats["n_not_dog_images"] = n_not_dog_images #D
    results_stats["n_correct_breed"] = n_correct_breed #E
    results_stats["n_label_matches"] = n_label_matches #Y

    results_stats["pct_correct_dogs"] = pct_correct_dogs
    results_stats["pct_correct_not_dogs"] = pct_correct_not_dogs
    results_stats["pct_correct_breed"] = pct_correct_breed
    results_stats["pct_label_matches"] = pct_label_matches
    return results_stats
    #pass


def print_results(results_dic, results_stats, model, print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly
    classified dogs and incorrectly classified dog breeds if user indicates
    they want those printouts (use non-default values)
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and
                            0 = pet Image 'is-NOT-a' dog.
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image
                            'as-a' dog and 0 = Classifier classifies image
                            'as-NOT-a' dog.
      results_stats - Dictionary that contains the results statistics (either a
                     percentage or a count) where the key is the statistic's
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value
      model - pretrained CNN whose architecture is indicated by this parameter,
              values must be: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and
                             False doesn't print anything(default) (bool)
      print_incorrect_breed - True prints incorrectly classified dog breeds and
                              False doesn't print anything(default) (bool)
    Returns:
           None - simply printing results.
    """
    print("\n** Here are the final results of the classification: \n")
    print(" The model used here is: ", model)
    print("%26s: %3d" % ("N images", results_stats["n_images"]))
    print("%26s: %3d" % ("N Dog Images", results_stats["n_dog_images"]))
    print("%26s: %3d" % ("N Not-Dog Images", results_stats["n_not_dog_images"]))
    print("\n")
    print("%26s: %3d" % ("Percentage Correct Dogs", results_stats["pct_correct_dogs"]))
    print("%26s: %3d" % ("Percentage Correct Breed", results_stats["pct_correct_breed"]))
    print("%26s: %3d" % ("Percentage Correct Not-Dog", results_stats["pct_correct_not_dogs"]))
    print("%26s: %3d" % ("Percentage of Match", results_stats["pct_label_matches"]))
    if print_incorrect_dogs == True:
        print(" \nPrinting dogs Misclassifications: ")
        if results_stats["n_correct_dogs"] + results_stats["n_correct_not_dogs"] != results_stats["n_images"]:
            print(" They are some dogs Misclassifications: ")
            for result in results_dic:
                if sum(results_dic[result][3:]) == 1:
                    print(" Pet image: %-30s Classified label: %-30s"% (result, results_dic[result][1]))
        else:
            print(" They are no dog Misclassification")

    #Printing Misclassified Breed's of Dogs
    if print_incorrect_breed == True:
        print(" \nPrinting Misclassified Breeds of Dog: ")
        if results_stats["n_correct_dogs"] != results_stats["n_correct_breed"]:
            print(" They are some Misclassified Breeds of dog")
            for result in results_dic:
                if sum(results_dic[result][3:]) == 2 and results_dic[result][2] == 0:
                    print(" Pet image: %-30s Classified label: %-30s"% (result, results_dic[result][1]))
        else:
            print(" They are NO Misclassified Breeds of dog")
    print("\nImages Classification DONE !!!")
    #pass



# Call to main function to run the program
if __name__ == "__main__":
    main()
