import time

def insertion_sort(arr):
    n = len(arr)
    trocas = 0
    comparacoes = 0

    start_time = time.time()  # Marca o início do tempo de execução

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        comparacoes += 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            trocas += 1

        arr[j + 1] = key

    end_time = time.time()  # Marca o final do tempo de execução
    runtime = end_time - start_time

    return arr, trocas, comparacoes, runtime

lista =  [479, 420, 157, 206, 649, 400, 178, 441, 23, 82, 295, 238, 40, 230, 843, 544, 689, 88, 720, 280, 523, 156, 435, 273, 328, 250, 614, 449, 680, 27, 881, 908, 516, 597, 19, 611, 753, 173, 360, 161, 811, 727, 227, 278, 920, 865, 986, 404, 573, 486, 0, 585, 402, 232, 388, 797, 31, 33, 110, 723, 259, 885, 660, 304, 113, 772, 621, 151, 411, 179, 9, 849, 877, 703, 73, 887, 642, 438, 962, 172, 862, 140, 735, 560, 267, 104, 928, 38, 828, 860, 26, 493, 496, 469, 147, 29, 615, 913, 873, 307, 86, 160, 768, 853, 951, 201, 103, 917, 119, 102, 89, 776, 52, 482, 371, 476, 505, 20, 376, 393, 759, 349, 177, 137, 954, 394, 721, 910, 848, 889, 345, 929, 803, 204, 536, 78, 64, 612, 779, 745, 564, 489, 461, 786, 379, 454, 657, 914, 210, 844, 83, 318, 996, 53, 594, 675, 98, 841, 702, 248, 364, 474, 598, 562, 709, 3, 214, 579, 61, 247, 728, 804, 876, 668, 806, 681, 370, 352, 729, 867, 974, 646, 507, 452, 385, 815, 571, 107, 980, 233, 581, 257, 816, 785, 410, 310, 976, 374, 755, 756, 287, 258, 199, 604, 535, 460, 546, 640, 894, 501, 264, 158, 519, 499, 856, 958, 814, 750, 308, 888, 43, 512, 332, 321, 842, 937, 21, 869, 985, 662, 999, 711, 252, 170, 405, 847, 714, 758, 684, 636, 520, 628, 527, 685, 719, 382, 192, 485, 254, 767, 978, 674, 303, 578, 852, 726, 300, 75, 6, 326, 796, 626, 582, 181, 386, 943, 733, 491, 65, 350, 148, 810, 882, 66, 129, 656, 746, 548, 424, 41, 126, 406, 713, 315, 718, 760, 153, 384, 945, 397, 832, 775, 346, 122, 799, 691, 850, 883, 497, 391, 697, 761, 472, 907, 648, 651, 693, 975, 654, 347, 676, 778, 285, 450, 936, 138, 473, 580, 637, 839, 821, 324, 622, 787, 422, 782, 418, 732, 15, 412, 164, 490, 838, 341, 572, 791, 921, 790, 965, 432, 431, 413, 322, 661, 436, 616, 840, 524, 762, 55, 798, 751, 290, 593, 383, 854, 659, 492, 504, 42, 783, 964, 244, 813, 664, 457, 277, 874, 282, 655, 299, 145, 188, 331, 407, 448, 342, 872, 543, 330, 446, 931, 781, 5, 893, 133, 47, 793, 249, 336, 537, 115, 794, 91, 568, 487, 380, 409, 901, 948, 724, 599, 741, 587, 857, 647, 939, 221, 81, 296, 351, 16, 12, 765, 62, 808, 365, 912, 209, 861, 100, 944, 495, 237, 705, 193, 896, 213, 217, 433, 952, 271, 538, 488, 809, 635, 789, 167, 1, 595, 223, 451, 72, 754, 265, 545, 510, 558, 45, 871, 576, 623, 774, 589, 142, 998, 174, 950, 401, 395, 99, 897, 50, 915, 575, 677, 128, 417, 898, 982, 163, 37, 275, 96, 610, 340, 780, 425, 645, 313, 606, 343, 368, 255, 831, 79, 993, 226, 956, 971, 868, 24, 329, 150, 650, 769, 613, 502, 833, 591, 686, 834, 95, 309, 715, 517, 85, 805, 459, 911, 211, 123, 202, 890, 146, 819, 736, 652, 286, 222, 338, 526, 253, 291, 465, 618, 503, 194, 515, 529, 716, 547, 992, 970, 665, 941, 540, 219, 429, 632, 532, 899, 766, 701, 949, 316, 900, 569, 704, 25, 671, 335, 802, 458, 596, 396, 120, 228, 215, 149, 93, 323, 125, 362, 863, 439, 197, 731, 306, 895, 442, 363, 13, 49, 533, 764, 70, 737, 983, 139, 747, 825, 710, 706, 327, 979, 22, 607, 169, 421, 694, 63, 550, 440, 484, 563, 603, 522, 456, 8, 763, 106, 57, 466, 276, 242, 634, 700, 463, 919, 991, 678, 216, 281, 369, 294, 256, 260, 155, 339, 419, 620, 969, 262, 927, 708, 455, 108, 344, 112, 638, 870, 752, 392, 377, 792, 605, 373, 990, 470, 434, 967, 514, 602, 511, 283, 18, 416, 152, 483, 807, 467, 121, 357, 925, 427, 478, 717, 549, 930, 734, 225, 353, 423, 183, 508, 995, 788, 212, 557, 960, 845, 672, 584, 317, 957, 56, 124, 730, 447, 864, 293, 935, 398, 134, 513, 601, 17, 953, 518, 187, 667, 688, 69, 858, 171, 631, 500, 905, 997, 453, 567, 924, 77, 909, 175, 528, 627, 97, 292, 494, 773, 987, 367, 117, 554, 984, 184, 835, 141, 375, 414, 236, 387, 942, 289, 851, 608, 695, 261, 932, 670, 428, 600, 577, 555, 687, 131, 916, 836, 218, 132, 154, 586, 68, 189, 630, 34, 590, 71, 366, 176, 644, 749, 994, 938, 972, 817, 270, 58, 231, 525, 7, 539, 208, 190, 617, 559, 891, 542, 619, 827, 109, 946, 59, 35, 673, 837, 740, 784, 878, 977, 312, 846, 892, 696, 30, 284, 251, 757, 44, 229, 770, 356, 165, 46, 886, 162, 84, 880, 961, 989, 531, 240, 973, 462, 390, 712, 959, 744, 361, 641, 574, 506, 884, 690, 48, 739, 818, 551, 830, 10, 185, 207, 822, 922, 509, 800, 136, 570, 824, 355, 87, 198, 534, 624, 566, 333, 464, 592, 301, 530, 771, 966, 682, 205, 224, 521, 553, 239, 415, 934, 114, 381, 879, 866, 565, 359, 105, 722, 74, 663, 981, 28, 92, 235, 683, 820, 477, 926, 288, 245, 354, 305, 39, 906, 679, 859, 67, 498, 266, 80, 2, 269, 325, 658, 430, 629, 795, 203, 445, 14, 933, 279, 855, 918, 556, 988, 426, 220, 36, 698, 127, 829, 272, 955, 135, 378, 812, 826, 389, 748, 196, 639, 246, 707, 903, 241, 348, 302, 399, 234, 669, 191, 875, 725, 923, 130, 268, 801, 94, 186, 320, 319, 116, 940, 182, 200, 588, 101, 437, 311, 298, 963, 699, 4, 118, 552, 314, 297, 743, 904, 337, 480, 666, 633, 968, 643, 475, 166, 243, 76, 144, 583, 408, 692, 358, 777, 738, 143, 159, 263, 468, 54, 443, 823, 609, 180, 742, 541, 561, 947, 481, 444, 403, 168, 111, 653, 60, 902, 90, 625, 51, 195, 334, 32, 274, 471, 11, 372]

sorted_list, trocas, comparacoes, tempo_execucao = insertion_sort(lista.copy())

print(f"Quantidade de trocas: {trocas}")
print(f"Quantidade de comparações: {comparacoes}")
print(f"Tempo de execução: {tempo_execucao} segundos")
