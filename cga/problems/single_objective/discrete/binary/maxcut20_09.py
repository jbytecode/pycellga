from problems.abstract_problem import AbstractProblem

# Maximum Cut of a Graph – MAXCUT
"""
References
    Alba, E. and Dorronsoro B., 2008, Cellular genetic algorithms, Operations research/computer science interfaces series, Springer, US, ISBN: 978-0-387-77609-5.
"""
# Length of chromosomes = 20
# Maximum Fitness Value = 56.740064
# there is a bug that it find sometimes the fitness is bigger than the max, how it can be possible not solved yet


class Maxcut20_09(AbstractProblem):
    def f(self, x: list) -> float:

        problema = [
            [0.000000, 0.130622, 0.694577, 0.922028, 0.335786, 0.359902, 0.279580, 0.880418, 0.201529, 0.313702,
                0.322765, 0.399944, 0.000000, 0.848267, 0.933051, 0.085267, 0.957646, 0.331033, 0.389269, 0.193177],

            [0.130622, 0.000000, 0.946416, 0.388165, 0.000000, 0.232571, 0.605770, 0.065642, 0.114155, 0.737786,
                0.033571, 0.843579, 0.465199, 0.043667, 0.000000, 0.382358, 0.661252, 0.931556, 0.206577, 0.262331],

            [0.694577, 0.946416, 0.000000, 0.989211, 0.000000, 0.152213, 0.000000, 0.084579, 0.610150, 0.131790,
                0.950083, 0.426541, 0.721013, 0.428389, 0.308932, 0.861261, 0.479196, 0.863363, 0.000000, 0.110013],

            [0.922028, 0.388165, 0.989211, 0.000000, 0.785464, 0.227321, 0.469172, 0.032054, 0.574073, 0.736906,
                0.764415, 0.000000, 0.495863, 0.602718, 0.684042, 0.492622, 0.000000, 0.918634, 0.974679, 0.134843],

            [0.335786, 0.000000, 0.000000, 0.785464, 0.000000, 0.478171, 0.684823, 0.594988, 0.000000, 0.043655,
                0.266736, 0.265187, 0.167750, 0.539353, 0.120596, 0.483133, 0.928091, 0.571874, 0.118362, 0.808725],

            [0.359902, 0.232571, 0.152213, 0.227321, 0.478171, 0.000000, 0.969750, 0.948758, 0.527900, 0.652776,
                0.990039, 0.945809, 0.831436, 0.355298, 0.049061, 0.103966, 0.897422, 0.732376, 0.491590, 0.526179],

            [0.279580, 0.605770, 0.000000, 0.469172, 0.684823, 0.969750, 0.000000, 0.652418, 0.123045, 0.368941,
                0.000000, 0.053590, 0.035474, 0.000000, 0.360846, 0.665888, 0.757456, 0.000000, 0.912162, 0.974535],

            [0.880418, 0.065642, 0.084579, 0.032054, 0.594988, 0.948758, 0.652418, 0.000000, 0.656499, 0.879623,
                0.656778, 0.572563, 0.107108, 0.550337, 0.230315, 0.568378, 0.000000, 0.915765, 0.659182, 0.688311],

            [0.201529, 0.114155, 0.610150, 0.574073, 0.000000, 0.527900, 0.123045, 0.656499, 0.000000, 0.995883,
                0.172727, 0.442540, 0.974869, 0.000000, 0.997630, 0.035737, 0.835247, 0.139724, 0.859992, 0.000000],

            [0.313702, 0.737786, 0.131790, 0.736906, 0.043655, 0.652776, 0.368941, 0.879623, 0.995883, 0.000000,
                0.120131, 0.483339, 0.969497, 0.300482, 0.879444, 0.000000, 0.836946, 0.084211, 0.723167, 0.195939],

            [0.322765, 0.033571, 0.950083, 0.764415, 0.266736, 0.990039, 0.000000, 0.656778, 0.172727, 0.120131,
                0.000000, 0.950398, 0.236138, 0.268245, 0.701255, 0.894728, 0.303465, 0.989424, 0.228973, 0.978178],

            [0.399944, 0.843579, 0.426541, 0.000000, 0.265187, 0.945809, 0.053590, 0.572563, 0.442540, 0.483339,
                0.950398, 0.000000, 0.060377, 0.854370, 0.488094, 0.581746, 0.935845, 0.723815, 0.225213, 0.424806],

            [0.000000, 0.465199, 0.721013, 0.495863, 0.167750, 0.831436, 0.035474, 0.107108, 0.974869, 0.969497,
                0.236138, 0.060377, 0.000000, 0.404249, 0.867185, 0.865152, 0.330739, 0.876005, 0.978220, 0.651577],

            [0.848267, 0.043667, 0.428389, 0.602718, 0.539353, 0.355298, 0.000000, 0.550337, 0.000000, 0.300482,
                0.268245, 0.854370, 0.404249, 0.000000, 0.492553, 0.088188, 0.690603, 0.287630, 0.000000, 0.690291],

            [0.933051, 0.000000, 0.308932, 0.684042, 0.120596, 0.049061, 0.360846, 0.230315, 0.997630, 0.879444,
                0.701255, 0.488094, 0.867185, 0.492553, 0.000000, 0.000000, 0.593581, 0.076547, 0.297751, 0.159191],

            [0.085267, 0.382358, 0.861261, 0.492622, 0.483133, 0.103966, 0.665888, 0.568378, 0.035737, 0.000000,
                0.894728, 0.581746, 0.865152, 0.088188, 0.000000, 0.000000, 0.747596, 0.562290, 0.000000, 0.955731],

            [0.957646, 0.661252, 0.479196, 0.000000, 0.928091, 0.897422, 0.757456, 0.000000, 0.835247, 0.836946,
                0.303465, 0.935845, 0.330739, 0.690603, 0.593581, 0.747596, 0.000000, 0.244949, 0.994884, 0.067050],

            [0.331033, 0.931556, 0.863363, 0.918634, 0.571874, 0.732376, 0.000000, 0.915765, 0.139724, 0.084211,
                0.989424, 0.723815, 0.876005, 0.287630, 0.076547, 0.562290, 0.244949, 0.000000, 0.621331, 0.752926],

            [0.389269, 0.206577, 0.000000, 0.974679, 0.118362, 0.491590, 0.912162, 0.659182, 0.859992, 0.723167,
                0.228973, 0.225213, 0.978220, 0.000000, 0.297751, 0.000000, 0.994884, 0.621331, 0.000000, 0.224879],

            [0.193177, 0.262331, 0.110013, 0.134843, 0.808725, 0.526179, 0.974535, 0.688311, 0.000000, 0.195939,
                0.978178, 0.424806, 0.651577, 0.690291, 0.159191, 0.955731, 0.067050, 0.752926, 0.224879, 0.000000]
        ]

        cols = 20
        fitness = 0.0

        for i in range(cols-1):
            j = i
            for j in range(cols):
                if (x[i] ^ x[j]):
                    fitness = fitness + problema[i][j]

        return round(fitness, 6)
